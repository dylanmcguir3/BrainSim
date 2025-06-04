SetFactory("OpenCASCADE");
r  = 1.0;
lc = 0.05;
Sphere(1) = {0, 0, 0, r};
Field[1] = MathEval;
Field[1].F = lc;
Background Field = 1;
Physical Surface("surface") = {1};
Physical Volume("volume")   = {1};
