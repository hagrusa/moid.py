# moidpy
Compute the minimum orbit intersection distance (MOID) with python.

This is an extremely crude python wrapper of the original fortran code written by Wiśniowski & Rickman. I simply modified to make it a function instead of having hard-coded inputs. Then you can compile it as a shared object using f2py3, and then import it into your python code.

A peak at compile.sh and example.py should make installation relatively straightforward. Once you compile moid.f, the shared object simply needs to be in your PYTHONPATH to import it.

