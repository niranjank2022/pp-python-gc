from setuptools import setup, Extension
from Cython.Build import cythonize

# Define the extension module
extensions = [
    Extension(
        name="cython_gc",               # Module name
        sources=["src/cython_gc.pyx"],  # Cython source file
    )
]

setup(
    name="cython_gc_project",
    version="0.1",
    ext_modules=cythonize(extensions),
    package_dir={"": "src"},  # Source files are in the "src" directory
    packages=[""],            # Automatically include packages from "src"
)
