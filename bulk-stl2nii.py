import os
import trimesh
import numpy as np
import SimpleITK as sitk
import nibabel as nib

# Define the root directories
source_dir = "C:\\Users\\User\\utm\\postgrad\\testing_heart\\stl2nii\\input\\raw-dataset"
output_dir = "C:\\Users\\User\\utm\\postgrad\\testing_heart\\stl2nii\\input\\nii-dataset"

# Define the voxel grid resolution
grid_shape = (100, 100, 100)  # Adjust the resolution as needed

# Walk through the source directory and process all STL files
for root, dirs, files in os.walk(source_dir):
    for file in files:
        if file.endswith(".stl"):
            # Construct the full path to the STL file
            stl_file_path = os.path.join(root, file)
            
            # Construct the corresponding output path in the nii-dataset directory
            relative_path = os.path.relpath(root, source_dir)
            output_subdir = os.path.join(output_dir, relative_path)
            os.makedirs(output_subdir, exist_ok=True)
            
            # Define the output NIfTI file path
            output_filename = os.path.join(output_subdir, file.replace(".stl", ".nii.gz"))
            
            # Load the STL file using Trimesh
            try:
                mesh = trimesh.load(stl_file_path)
                
                # Check if the mesh is loaded correctly
                if not isinstance(mesh, trimesh.Trimesh):
                    print(f"Skipping invalid mesh: {stl_file_path}")
                    continue
                
                # Optional: Visualize the mesh (for debugging purposes)
                # mesh.show()
                
                # Automatically determine voxel size
                voxel_size = np.max(mesh.extents) / np.max(grid_shape)
                
                # Voxelize the mesh
                voxel_grid = mesh.voxelized(pitch=voxel_size)
                
                # Get the voxel grid as a 3D numpy array
                volume = voxel_grid.matrix.astype(np.uint8)
                
                # Save the volume as a NIfTI file using SimpleITK
                sitk_image = sitk.GetImageFromArray(volume)
                sitk_image.SetSpacing((voxel_size, voxel_size, voxel_size))  # Set voxel spacing
                sitk.WriteImage(sitk_image, output_filename)
                
                # Optionally, save the NIfTI file using NiBabel for further processing
                nii_image = nib.Nifti1Image(volume, np.eye(4))
                nii_image.header.set_zooms((voxel_size, voxel_size, voxel_size))  # Set voxel spacing
                nib.save(nii_image, output_filename)
                
                print(f"Conversion complete! Saved: {output_filename}")
            
            except Exception as e:
                print(f"Error processing {stl_file_path}: {e}")

print("Bulk STL to NIfTI conversion complete!")