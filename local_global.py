def local_global():
    b = 5
    c = 10
    print(locals())  # resultat {'b': 5, 'c': 10}
    print(a)

a = 3
local_global()
print( globals()) #resultat   {'__name__': '__main__', '__doc__': None, '__package__': None, 
                #'__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f41fe8834c0>, 
                #'__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 
                #'__file__': '/mnt/nfs/homes/dzybin/Documents/PYTHON/local_global.py', '__cached__': None, 'local_global': <function local_global at 0x7f41fe840280>, 'a': 3}
