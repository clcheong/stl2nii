import os
from stl import mesh
import numpy as np

# Define the base directory and the folders
base_dir = 'C:\\Users\\User\\utm\\postgrad\\testing_heart\\stl2nii\\input\\raw-dataset'
folders = ['heart', 'heartatriumleft', 'heartatriumright', 'heartmyocardium', 'hearttissue', 'heartventricleleft', 'heartventricleright']
fullheart_dir = os.path.join(base_dir, 'fullheart')

# Ensure the fullheart directory exists
os.makedirs(fullheart_dir, exist_ok=True)

# Get a list of all patient numbers
patient_numbers = set()
for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    for file in os.listdir(folder_path):
        if file.endswith('.stl'):
            patient_number = file.split('_')[0]
            patient_numbers.add(patient_number)

# Iterate through each patient number and combine their .stl files
for patient_number in patient_numbers:
    combined_vertices = []
    combined_faces = []
    face_offset = 0

    for folder in folders:
        folder_path = os.path.join(base_dir, folder)
        file_name = f"{patient_number}_{folder}.stl"
        file_path = os.path.join(folder_path, file_name)

        if os.path.exists(file_path):
            # Load the STL file
            stl_mesh = mesh.Mesh.from_file(file_path)
            
            # Combine vertices and faces
            combined_vertices.append(stl_mesh.vectors)
            combined_faces.append(stl_mesh.vectors.shape[0])
            
            # Update face offset
            face_offset += stl_mesh.vectors.shape[0]

    if combined_vertices:
        # Combine all vertices into a single array
        combined_vertices = np.concatenate(combined_vertices)
        
        # Create a new mesh object
        combined_mesh = mesh.Mesh(np.zeros(combined_vertices.shape[0], dtype=mesh.Mesh.dtype))
        combined_mesh.vectors = combined_vertices
        
        # Save the combined mesh as a new STL file
        output_file = os.path.join(fullheart_dir, f"{patient_number}_fullheart.stl")
        combined_mesh.save(output_file)
        print(f"Saved {output_file}")
    else:
        print(f"No files found for patient {patient_number}")