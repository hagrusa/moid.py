#this may need to be modified based on whatever machine you are using
f2py3 -c -m moidpy moid.f 
ln -s moidpy.cpython-311-darwin.so moidpy.so