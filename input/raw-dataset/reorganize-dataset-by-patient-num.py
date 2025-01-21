import os
import shutil

# Define the root directory containing the folders
root_dir = 'C:\\Users\\User\\utm\\postgrad\\testing_heart\\stl2nii\\input\\raw-dataset'

# Define the folders to process (excluding 'fullheart')
folders = ['heart', 'heartatriumleft', 'heartatriumright', 'heartmyocardium', 'hearttissue', 'heartventricleleft', 'heartventricleright']

# Define the output directory
output_dir = os.path.join(root_dir, 'organized-by-patient-num')

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Iterate through each folder and organize files by patient number
for folder in folders:
    folder_path = os.path.join(root_dir, folder)
    
    # Iterate through each file in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.stl'):
            # Extract the patient number from the file name
            patient_number = file_name.split('_')[0]
            
            # Create a patient folder in the output directory if it doesn't exist
            patient_folder = os.path.join(output_dir, patient_number)
            os.makedirs(patient_folder, exist_ok=True)
            
            # Copy the file to the patient folder
            src_file = os.path.join(folder_path, file_name)
            dst_file = os.path.join(patient_folder, file_name)
            shutil.copy(src_file, dst_file)
            print(f"Copied {src_file} to {dst_file}")

print("Organization complete!")