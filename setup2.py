from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

# Define the extension module
extensions = [
    Extension(
        name="math_functions",               # Module name
        sources=["src/math_functions.pyx"],  # Cython source file
    )
]

setup(
    name="math_functions",
    version="0.1",
    ext_modules=cythonize(extensions),
    include_dirs=[np.get_include()],
    package_dir={"": "src"},  # Source files are in the "src" directory
    packages=[""],            # Automatically include packages from "src"
)
