from setuptools import setup, Extension
from Cython.Build import cythonize

# Define the extension module
extensions = [
    Extension(
        "primes_cython",  # Name of the compiled module
        ["primes_cython.pyx"],  # Source file
        extra_compile_args=["-std=c++14"],  # Compiler arguments
        language="c++",  # Specify C++ as the language
    )
]

# Setup configuration
setup(
    name="primes_cython",
    ext_modules=cythonize(extensions),
)
