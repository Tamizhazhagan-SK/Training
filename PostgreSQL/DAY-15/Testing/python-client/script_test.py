import subprocess
import time

import pytest
import requests

BASE_URL = "http://localhost:8081"


@pytest.fixture(scope="function", autouse=True)
def docker_compose_service():
    """Starts the sample API container before each test and stops it after."""
    subprocess.run(["docker", "compose", "up", "-d", "--build"], check=True)

    timeout = 60
    start_time = time.time()
    api_ready = False

    while time.time() - start_time < timeout:
        try:
            response = requests.get(f"{BASE_URL}/api/products", timeout=2)
            if response.status_code < 500:
                api_ready = True
                break
        except requests.exceptions.RequestException:
            pass
        time.sleep(1)

    if not api_ready:
        subprocess.run(["docker", "compose", "down", "-v"], check=True)
        pytest.fail("Docker service failed to start or respond within timeout.")

    yield

    subprocess.run(["docker", "compose", "down", "-v"], check=True)


@pytest.fixture
def valid_product_payload():
    """Fixture providing a valid product payload."""
    return {
        "name": "Apple Macbook M2",
        "description": "Apple Bionic Chip M2 with ARM Processor",
        "price": 150000,
        "quantity": 20,
    }


def _create_product(payload):
    response = requests.post(
        f"{BASE_URL}/api/products",
        json=payload,
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code in (200, 201), (
        f"Unexpected status code: {response.status_code}"
    )
    return response


def _extract_product_id(response_json):
    if "id" in response_json:
        return response_json["id"]
    if "productId" in response_json:
        return response_json["productId"]
    raise AssertionError("Response should include a product identifier")


def test_create_product_success(valid_product_payload):
    """Test successful creation of a product (HTTP 201/200)."""
    response = _create_product(valid_product_payload)
    data = response.json()

    assert _extract_product_id(data) is not None
    assert data["name"] == valid_product_payload["name"]
    assert data["price"] == valid_product_payload["price"]
    assert data["quantity"] == valid_product_payload["quantity"]


def test_create_product_missing_required_fields():
    """Test creating a product with missing required fields (HTTP 400 Bad Request)."""
    incomplete_payload = {
        "name": "Incomplete Product"
        # Missing price and quantity
    }

    response = requests.post(
        f"{BASE_URL}/api/products",
        json=incomplete_payload,
    )

    assert response.status_code == 400


def test_create_product_invalid_data_types():
    """Test payload validation for invalid data types (e.g., negative price or non-numeric quantity)."""
    invalid_payload = {
        "name": "Invalid Price Product",
        "description": "Test",
        "price": -500,
        "quantity": "twenty",
    }

    response = requests.post(
        f"{BASE_URL}/api/products",
        json=invalid_payload,
    )

    assert response.status_code in (400, 422, 500)


def test_get_all_products():
    """Test fetching the full product list."""
    response = requests.get(f"{BASE_URL}/api/products")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_product_by_id_success(valid_product_payload):
    """Test fetching a product by its identifier."""
    created_response = _create_product(valid_product_payload)
    product_id = _extract_product_id(created_response.json())

    response = requests.get(f"{BASE_URL}/api/products/{product_id}")

    assert response.status_code == 200
    data = response.json()
    assert _extract_product_id(data) == product_id
    assert data["name"] == valid_product_payload["name"]


def test_update_product_success(valid_product_payload):
    """Test updating an existing product."""
    created_response = _create_product(valid_product_payload)
    product_id = _extract_product_id(created_response.json())

    updated_payload = {
        **valid_product_payload,
        "name": "Updated Macbook Pro",
        "price": 180000,
        "quantity": 12,
    }

    response = requests.put(
        f"{BASE_URL}/api/products/{product_id}",
        json=updated_payload,
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Macbook Pro"
    assert data["price"] == 180000
    assert data["quantity"] == 12


def test_delete_product_by_id_success(valid_product_payload):
    """Test deleting a product by its identifier."""
    created_response = _create_product(valid_product_payload)
    product_id = _extract_product_id(created_response.json())

    response = requests.delete(f"{BASE_URL}/api/products/{product_id}")

    assert response.status_code == 204


def test_delete_all_products():
    """Test bulk delete behaviour for the product collection."""
    response = requests.delete(f"{BASE_URL}/api/products")

    assert response.status_code in (200, 204, 404, 405)