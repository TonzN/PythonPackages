from setuptools import setup, find_packages

setup(
    name='DevelopmentPackages',
    version='0.0.2.5',
    packages=["PythonPackages"],
    install_requires=[
          'numpy',
          "pygame",
          "matplotlib",
      ],
    zip_safe = False
)
