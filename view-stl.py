import pyvista as pv

# Load the STL file
stl_file_path = "C:\\Users\\User\\utm\\postgrad\\testing_heart\\stl2nii\\input\\raw-dataset\\organized-by-patient-num\\003164\\003164_heartfull.stl"  # Replace with the path to your STL file

# Read the STL file using PyVista
mesh = pv.read(stl_file_path)

# Create a PyVista plotter
plotter = pv.Plotter()

# Add the mesh to the plotter
plotter.add_mesh(mesh, color="lightblue", show_edges=True)

# Set labels for the axes
plotter.add_axes()
plotter.show_grid()

# Set the title of the plot
plotter.add_title("3D Visualization of STL File")

# Display the plot
plotter.show()