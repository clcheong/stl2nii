import trimesh
import numpy as np
import SimpleITK as sitk
import nibabel as nib

# Load the STL file using Trimesh
stl_file = "./input/000442/000442_heartventricleleft.stl"
mesh = trimesh.load(stl_file)

# Check if the mesh is loaded correctly
if not isinstance(mesh, trimesh.Trimesh):
    raise ValueError("The input file is not a valid mesh.")

# Optional: Visualize the mesh (for debugging purposes)
mesh.show()

# Define the voxel grid resolution and size
grid_shape = (100, 100, 100)  # Adjust the resolution as needed
voxel_size = np.max(mesh.extents) / np.max(grid_shape)  # Automatically determine voxel size

# Voxelize the mesh
voxel_grid = mesh.voxelized(pitch=voxel_size)

# Get the voxel grid as a 3D numpy array
volume = voxel_grid.matrix.astype(np.uint8)

# Save the volume as a NIfTI file using SimpleITK
output_filename = "./output/000442_heartventricleleft.nii.gz"
sitk_image = sitk.GetImageFromArray(volume)
sitk_image.SetSpacing((voxel_size, voxel_size, voxel_size))  # Set voxel spacing
sitk.WriteImage(sitk_image, output_filename)

print(f"Conversion complete! The NIfTI file is saved as {output_filename}")

# Optionally, save the NIfTI file using NiBabel for further processing
nii_image = nib.Nifti1Image(volume, np.eye(4))
nii_image.header.set_zooms((voxel_size, voxel_size, voxel_size))  # Set voxel spacing
nib.save(nii_image, output_filename)