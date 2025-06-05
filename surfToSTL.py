import os
import numpy as np
import nibabel as nib

# Path to your FreeSurfer .surf file (update this to your actual path)
surf_path = 'subject01/bem/inner_skull.surf'
stl_output_path = 'inner_skull.stl'

if not os.path.exists(surf_path):
    print(f"Surf file '{surf_path}' not found. Please place your .surf file in the working directory or update `surf_path`.")
else:
    # Read vertices and faces from the .surf file
    coords, faces = nib.freesurfer.read_geometry(surf_path)

    # Write an ASCII STL
    with open(stl_output_path, 'w') as f:
        f.write(f"solid {os.path.splitext(os.path.basename(stl_output_path))[0]}\n")
        for tri in faces:
            v1, v2, v3 = coords[tri[0]], coords[tri[1]], coords[tri[2]]
            normal = np.cross(v2 - v1, v3 - v1)
            norm = np.linalg.norm(normal)
            normal = normal / norm if norm > 1e-6 else np.array([0.0, 0.0, 0.0])
            f.write(f"  facet normal {normal[0]} {normal[1]} {normal[2]}\n")
            f.write("    outer loop\n")
            f.write(f"      vertex {v1[0]} {v1[1]} {v1[2]}\n")
            f.write(f"      vertex {v2[0]} {v2[1]} {v2[2]}\n")
            f.write(f"      vertex {v3[0]} {v3[1]} {v3[2]}\n")
            f.write("    endloop\n")
            f.write("  endfacet\n")
        f.write(f"endsolid {os.path.splitext(os.path.basename(stl_output_path))[0]}\n")

    print(f"STL successfully written to '{stl_output_path}'. You can download it using the following link:")
    print(f"[Download the STL](sandbox:/mnt/data/{stl_output_path})")
