# scattering_trapping
Element of code to complete Eike Muller work, to build trapping geometries


If you are reading this, you must have access to Eike Muller work on BEMPP. This repository only add new functions on the code, it does not work on its own.
First, you will have to build BEMPP from scratch. You will then have somewhere the repository bempp/api/shapes. There, you can change the file __init__.py by the file with the same name that you will find on this github. To the file shapes.py, you will need to add the functions cube_rotated, cube_shifted that you will find on the file with the same name on this github.

Then, you will have to build a virtual environement where you can 
