// Define the geometry
Point(1) = {0, 0, 0, 1.0};   // bottom-left
Point(2) = {1, 0, 0, 1.0};   // bottom-right
Point(3) = {1, 1, 0, 1.0};   // top-right
Point(4) = {0, 1, 0, 1.0};   // top-left

// Create lines between the points
Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 1};

// Create a closed curve loop and a plane surface
Line Loop(1) = {1, 2, 3, 4};
Plane Surface(1) = {1};

// Define mesh element size explicitly
Mesh.MeshSizeMin = 0.01;
Mesh.MeshSizeMax = 0.01;
