import pyvista as pv
import os

# Define the path to the patient folder
patient_folder = "./input/000442/"  # Replace with your folder path

# List all STL files in the folder
stl_files = [f for f in os.listdir(patient_folder) if f.endswith(".stl")]

# Check if there are any STL files in the folder
if not stl_files:
    raise FileNotFoundError("No STL files found in the specified folder.")

# Create an empty PyVista mesh to hold the combined result
combined_mesh = pv.PolyData()

# Load and combine each STL file
for stl_file in stl_files:
    # Load the STL file
    mesh = pv.read(os.path.join(patient_folder, stl_file))
    
    # Combine the mesh with the existing combined mesh
    combined_mesh += mesh

# Visualize the combined mesh
print("Displaying the combined 3D model...")
combined_mesh.plot()

# Save the combined mesh as "heartfull.stl" in the same folder
output_file = os.path.join(patient_folder, "heart-ground-truth.stl")
combined_mesh.save(output_file)
print(f"Combined mesh saved as {output_file}")