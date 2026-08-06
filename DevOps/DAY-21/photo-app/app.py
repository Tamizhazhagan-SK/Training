import os
import shutil

# We will point our storage to a directory inside the container 
# that is mapped to a Docker volume.
STORAGE_DIR = "/app/images"

def ensure_storage():
    if not os.path.exists(STORAGE_DIR):
        os.makedirs(STORAGE_DIR)

def list_images():
    ensure_storage()
    images = os.listdir(STORAGE_DIR)
    print("\n--- Photos in Volume ---")
    if not images:
        print("No photos found.")
    else:
        for img in images:
            print(f"- {img}")
    print("------------------------\n")

def import_photo(file_path):
    ensure_storage()
    if os.path.exists(file_path):
        file_name = os.path.basename(file_path)
        dest_path = os.path.join(STORAGE_DIR, file_name)
        shutil.copy(file_path, dest_path)
        print(f"\nSuccess: '{file_name}' imported into the volume!\n")
    else:
        print(f"\nError: File '{file_path}' does not exist.\n")

if __name__ == "__main__":
    ensure_storage()
    while True:
        print("=== Photo Manager App ===")
        print("1. List stored photos")
        print("2. Import a photo")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            list_images()
        elif choice == "2":
            path = input("Enter the path to the photo on your host/container: ").strip()
            import_photo(path)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.\n")