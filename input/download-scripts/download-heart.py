import os
import requests

# Input file and output directory
input_file = "heart.txt"
output_dir = "../raw-dataset/heart"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Read URLs from the input file
with open(input_file, "r") as file:
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
    print(f"Downloading: {filename}")
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded and saved: {filename}")
    else:
        print(f"Failed to download: {filename} (Status Code: {response.status_code})")