import setuptools


setuptools.setup(
    name="pkg",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
)