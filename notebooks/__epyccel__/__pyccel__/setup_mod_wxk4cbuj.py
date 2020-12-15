from setuptools import Extension, setup
import numpy

extension_mod = Extension("mod_wxk4cbuj",
		[ r'mod_wxk4cbuj_wrapper.c' ],
		extra_objects = [r'/home/abdelbasset/Desktop/HPCgit/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__/bind_c_mod_wxk4cbuj.o',
				r'/home/abdelbasset/Desktop/HPCgit/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__/mod_wxk4cbuj.o'],
		include_dirs = [r'/home/abdelbasset/Desktop/HPCgit/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__', numpy.get_include()],
		libraries = [r'gfortran'],
		library_dirs = [r'/usr/lib/gcc/x86_64-linux-gnu/9'],
		extra_link_args = [r'-O3',
				r'-fPIC',
				r'-I"/home/abdelbasset/Desktop/HPCgit/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__"'])

setup(name = "mod_wxk4cbuj", ext_modules=[extension_mod])