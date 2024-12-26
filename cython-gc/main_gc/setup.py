from setuptools import setup
from Cython.Build import cythonize

setup(
    name="GC",
    ext_modules=cythonize("cvthon_gc.pyx")
)
