import pyvista as pv
import os

# Define the root directory containing the organized patient folders
organized_dir = 'C:\\Users\\User\\utm\\postgrad\\testing_heart\\stl2nii\\input\\raw-dataset\\organized-by-patient-num'

# Iterate through each patient folder in the organized directory
for patient_folder_name in os.listdir(organized_dir):
    patient_folder = os.path.join(organized_dir, patient_folder_name)
    
    # Ensure it's a directory
    if os.path.isdir(patient_folder):
        print(f"Processing patient folder: {patient_folder_name}")
        
        # List all STL files in the folder
        stl_files = [f for f in os.listdir(patient_folder) if f.endswith(".stl")]
        
        # Check if there are any STL files in the folder
        if not stl_files:
            print(f"No STL files found in {patient_folder_name}. Skipping...")
            continue
        
        # Create an empty PyVista mesh to hold the combined result
        combined_mesh = pv.PolyData()
        
        # Load and combine each STL file
        for stl_file in stl_files:
            # Load the STL file
            mesh = pv.read(os.path.join(patient_folder, stl_file))
            
            # Combine the mesh with the existing combined mesh
            combined_mesh += mesh
        
        # Save the combined mesh as "{patient_number}_heartfull.stl" in the patient folder
        output_file = os.path.join(patient_folder, f"{patient_folder_name}_heartfull.stl")
        combined_mesh.save(output_file)
        print(f"Combined mesh saved as {output_file}")

print("Full heart generation complete!")