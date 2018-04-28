import setuptools


setuptools.setup(
    name="DataLake",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        "click"
    ],
    entry_points={
        "console_scripts": ["test = datalake.cli:main"]
    },
)
