# scattering_trapping
Element of code to complete Eike Muller work, to build trapping geometries


If you are reading this, you must have access to Eike Muller work on BEMPP. This repository only add new functions on the code, it does not work on its own.
First, you will have to build BEMPP from scratch. You will then have somewhere the repository bempp/api/shapes. There, you can change the file __init__.py by the file with the same name that you will find on this github. To the file shapes.py, you will need to add the functions cube_rotated, cube_shifted that you will find on the file with the same name on this github.

Then, you will have to build a virtual environement. I did not did that part, but I used the file source_bempp to activate it, and I use it again in the file scattering.py in scattering/src/

Moreover, for the file scattering.py, you can replace the function run and the whole main by what you will find in this Github. You need to pay attention to the file scattering.py, because in the MAIN, the wavenumber k changes by k+=0.5 instead of k*=2 in Eike's code. Also, the parameter "l" (which is the length trap) does not exist in Eike code, so it is better to start with a slurm_script in this Github, and make the change necessary. In the file scattering.py, you will find all of the geometries I build. The names can be confusing, so read well how there are built. The origin of the cube is the left down vertice. About cube_rotated and cube_shifted, you can find in shapes.py how there are built.


