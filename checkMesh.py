import meshio
import numpy as np

# Replace "my_mesh.msh" with the path to your mesh file
mesh = meshio.read("scenes/brain/brain.msh")

# Ensure the mesh has tetrahedral cells
if "tetra" not in mesh.cells_dict:
    raise ValueError("Mesh does not contain tetrahedral elements.")

# Extract tetrahedral connectivity and point coordinates
tets = mesh.cells_dict["tetra"]
points = mesh.points

# Print the number of tetrahedra and points
print(f"Number of tetrahedra: {len(tets)}")
print(f"Number of points: {len(points)}")

# Prepare lists to store minimum and maximum edge lengths of each tetrahedron
min_length = 0
max_length = 0

# Define the six edges of a tetrahedron by vertex index pairs
edge_indices = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

# Compute min and max edge lengths for each tetrahedron
for tet in tets:
    verts = points[tet]  # Coordinates of the 4 vertices of the current tetrahedron
    # Compute lengths for each of the six edges
    edge_lengths = [np.linalg.norm(verts[i] - verts[j]) for i, j in edge_indices]
    min_length = min(edge_lengths)
    max_length = max(edge_lengths)



# Print the results
print(f"Minimum edge length: {min_length:.6f}")
print(f"Maximum edge length: {max_length:.6f}")
