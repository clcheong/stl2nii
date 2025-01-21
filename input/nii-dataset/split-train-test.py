import os
import random
import shutil

# Define the root directory of the nii-dataset
nii_dataset_dir = "C:\\Users\\User\\utm\\postgrad\\testing_heart\\stl2nii\\input\\nii-dataset"

# Define the paths for train and test folders
train_dir = os.path.join(nii_dataset_dir, "train")
test_dir = os.path.join(nii_dataset_dir, "test")

# Create train and test directories if they don't exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# List all patient folders in the organized-by-patient-num directory
organized_dir = os.path.join(nii_dataset_dir, "organized-by-patient-num")
patient_folders = [f for f in os.listdir(organized_dir) if os.path.isdir(os.path.join(organized_dir, f))]

# Shuffle the patient folders to ensure randomness
random.shuffle(patient_folders)

# Split patients into 18 for training and 27 for testing
train_patients = patient_folders[:18]
test_patients = patient_folders[18:45]

# Function to organize patient data into train/test folders
def organize_patients(patients, target_dir):
    for patient in patients:
        # Define source and target paths
        source_patient_dir = os.path.join(organized_dir, patient)
        target_complete_dir = os.path.join(target_dir, "complete")
        target_incomplete_dir = os.path.join(target_dir, "incomplete", patient)
        
        # Create complete and incomplete directories
        os.makedirs(target_complete_dir, exist_ok=True)
        os.makedirs(target_incomplete_dir, exist_ok=True)
        
        # Copy the fullheart.nii.gz file to the complete folder
        fullheart_file = os.path.join(source_patient_dir, f"{patient}_heartfull.nii.gz")
        if os.path.exists(fullheart_file):
            shutil.copy(fullheart_file, os.path.join(target_complete_dir, f"{patient}_heartfull.nii.gz"))
        
        # Copy the input-combination files to the incomplete folder
        input_combination_dir = os.path.join(source_patient_dir, "input-combination")
        if os.path.exists(input_combination_dir):
            for combination_file in os.listdir(input_combination_dir):
                if combination_file.endswith(".nii.gz"):
                    shutil.copy(
                        os.path.join(input_combination_dir, combination_file),
                        os.path.join(target_incomplete_dir, combination_file)
                    )

# Organize training patients
organize_patients(train_patients, train_dir)

# Organize testing patients
organize_patients(test_patients, test_dir)

print("Organization complete!")