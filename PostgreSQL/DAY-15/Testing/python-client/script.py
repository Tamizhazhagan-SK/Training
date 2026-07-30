import http.client
import json

BASE_URL = "localhost"
PORT = 8081


def make_request(method, path, payload=None, headers=None):
    connection = http.client.HTTPConnection(BASE_URL, PORT)
    if headers is None:
        headers = {}
    body = None if payload is None else json.dumps(payload)
    connection.request(method, path, body=body, headers=headers)
    response = connection.getresponse()
    data = response.read().decode("utf-8")
    connection.close()
    return response.status, data


def create_product(payload):
    status, data = make_request(
        "POST",
        "/api/products",
        payload=payload,
        headers={"Content-Type": "application/json"},
    )
    print("Create product:", status, data)
    return status, json.loads(data) if data else None


def get_all_products():
    status, data = make_request("GET", "/api/products")
    print("Get all products:", status, data)
    return status, json.loads(data) if data else None


def get_product_by_id(product_id):
    status, data = make_request(f"GET", f"/api/products/{product_id}")
    print("Get product by id:", status, data)
    return status, json.loads(data) if data else None


def update_product(product_id, payload):
    status, data = make_request(
        "PUT",
        f"/api/products/{product_id}",
        payload=payload,
        headers={"Content-Type": "application/json"},
    )
    print("Update product:", status, data)
    return status, json.loads(data) if data else None


def delete_product_by_id(product_id):
    status, data = make_request("DELETE", f"/api/products/{product_id}")
    print("Delete product by id:", status, data)
    return status, data


def delete_all_products():
    status, data = make_request("DELETE", "/api/products")
    print("Delete all products:", status, data)
    return status, data


if __name__ == "__main__":
    product_payload = {
        "name": "Apple Macbook M2",
        "description": "Apple Bionic Chip M2 with ARM Processor",
        "price": 150000,
        "quantity": 20,
    }

    create_product(product_payload)
    get_all_products()
    get_product_by_id(1)
    update_product(1, {**product_payload, "name": "Updated Macbook Pro", "price": 180000, "quantity": 12})
    delete_product_by_id(1)
    delete_all_products()