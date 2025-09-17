from setuptools import setup, find_packages # finds folders with __init__.py files

#print(find_packages())

setup(
    name="cool_package",
    version="0.0.1",
    description="this package is a template for fullstack app",
    author="Susanna Rokka",
    author_email="author@email.com",
    packages=find_packages(),

)

# to install setup.py locally
# uv pip install -e .