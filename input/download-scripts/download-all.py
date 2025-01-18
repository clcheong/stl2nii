import os
import requests
from glob import glob

# Define the input folder (where the .txt files are located) and output base directory
input_folder = "."  # Current directory (or specify the path to the folder containing .txt files)
output_base_dir = "../raw-dataset"

# Create the output base directory if it doesn't exist
os.makedirs(output_base_dir, exist_ok=True)

# Find all .txt files in the input folder
txt_files = glob(os.path.join(input_folder, "*.txt"))

# Process each .txt file
for txt_file in txt_files:
    # Extract the organ name from the filename (e.g., "heart.txt" -> "heart")
    organ_name = os.path.basename(txt_file).replace(".txt", "")

    # Define the output directory for this organ
    output_dir = os.path.join(output_base_dir, organ_name)

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Read URLs from the .txt file
    with open(txt_file, "r") as file:
        urls = file.readlines()

    # Download each URL and rename the file
    for url in urls:
        url = url.strip()  # Remove any leading/trailing whitespace
        if not url:
            continue  # Skip empty lines

        # Extract the filename from the URL
        filename = url.split("files=")[1].split("&")[0]

        # Define the output path
        output_path = os.path.join(output_dir, filename)

        # Download the file
        print(f"Downloading {organ_name}: {filename}")
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(output_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"Downloaded and saved: {filename}")
        else:
            print(f"Failed to download {organ_name}: {filename} (Status Code: {response.status_code})")