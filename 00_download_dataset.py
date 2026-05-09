import os
import zipfile
import subprocess

DATASET = "olistbr/brazilian-ecommerce"
RAW_DIR = "data/raw"
ZIP_FILE = os.path.join(RAW_DIR, "brazilian-ecommerce.zip")

def create_directories():
    os.makedirs(RAW_DIR, exist_ok=True)

def download_dataset():
    print("Downloading dataset from Kaggle...")
    command = [
        "kaggle", "datasets", "download",
        "-d", DATASET,
        "-p", RAW_DIR
    ]
    subprocess.run(command, check=True)
    print("Download completed.")

def extract_dataset():
    print("Extracting dataset files...")
    with zipfile.ZipFile(ZIP_FILE, "r") as zip_ref:
        zip_ref.extractall(RAW_DIR)
    print("Extraction completed.")

def main():
    create_directories()
    download_dataset()
    extract_dataset()

if __name__ == "__main__":
    main()