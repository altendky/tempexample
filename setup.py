import setuptools


setuptools.setup(
    name="pkg",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'gui_scripts': [
            (
                'main = pkg.main:main',
            ),
        ],
    },
    install_requires=[
        'pyqt5',
        'pyopengl',
    ],
)