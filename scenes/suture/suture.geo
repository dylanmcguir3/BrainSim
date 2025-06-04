L   = 1.0;
R   = 0.005;
lc  = 0.02;


// Create 8 points around a circle in the y-z plane (center at (0,0,0))
Point(1) = {0,    R,    0, lc};
Point(2) = {0,  0.707*R, 0.707*R, lc};
Point(3) = {0,  0,     R, lc};
Point(4) = {0, -0.707*R, 0.707*R, lc};
Point(5) = {0, -R,    0, lc};
Point(6) = {0, -0.707*R, -0.707*R, lc};
Point(7) = {0,  0,    -R, lc};
Point(8) = {0,  0.707*R, -0.707*R, lc};
Point(9) = {0,  0,      0, lc};   

Circle(1) = {1, 9, 2};
Circle(2) = {2, 9, 3};
Circle(3) = {3, 9, 4};
Circle(4) = {4, 9, 5};
Circle(5) = {5, 9, 6};
Circle(6) = {6, 9, 7};
Circle(7) = {7, 9, 8};
Circle(8) = {8, 9, 1};

Line Loop(10) = {1, 2, 3, 4, 5, 6, 7, 8};

Plane Surface(11) = {10};

Extrude {L, 0, 0} { Surface{11};}

// The Extrude command creates new volumes (entity dim = 3). Identify it:
Physical Volume("ThreadCylinder") = {1}; 
Physical Surface("BottomCircle") = {11}; 


// (Optionally) force 3D mesh:
Mesh 3;


