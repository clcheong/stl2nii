import os
import random
import pyvista as pv
from itertools import combinations

# Define the root directory containing the organized patient folders
organized_dir = "C:\\Users\\User\\utm\\postgrad\\testing_heart\\stl2nii\\input\\raw-dataset\\organized-by-patient-num"

# Iterate through each patient folder in the organized directory
for patient_folder_name in os.listdir(organized_dir):
    patient_folder = os.path.join(organized_dir, patient_folder_name)
    
    # Ensure it's a directory
    if os.path.isdir(patient_folder):
        print(f"Processing patient folder: {patient_folder_name}")
        
        # List all STL files in the folder (excluding heartfull.stl)
        stl_files = [f for f in os.listdir(patient_folder) if f.endswith(".stl") and not f.endswith("heartfull.stl")]
        
        # Check if there are enough STL files to create combinations
        if len(stl_files) < 1:
            print(f"Not enough STL files in {patient_folder_name}. Skipping...")
            continue
        
        # Create the "input-combination" folder if it doesn't exist
        input_combination_dir = os.path.join(patient_folder, "input-combination")
        os.makedirs(input_combination_dir, exist_ok=True)
        
        # Generate 10 different combinations of the STL files
        for i in range(1, 11):
            # Randomly choose the number of components to include (1 to 6)
            num_components = random.randint(1, 6)
            
            # Randomly select the components
            selected_components = random.sample(stl_files, num_components)
            
            # Create an empty PyVista mesh to hold the combined result
            combined_mesh = pv.PolyData()
            
            # Load and combine the selected STL files
            for component in selected_components:
                mesh = pv.read(os.path.join(patient_folder, component))
                combined_mesh += mesh
            
            # Save the combined mesh as "input-combination-{i}.stl"
            output_file = os.path.join(input_combination_dir, f"input-combination-{i}.stl")
            combined_mesh.save(output_file)
            print(f"Saved combination {i} for patient {patient_folder_name} at {output_file}")

print("Combination generation complete!")