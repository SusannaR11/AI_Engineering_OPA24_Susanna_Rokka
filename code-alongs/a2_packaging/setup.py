from setuptools import setup, find_packages

setup(
    name= "taxipred",
    version="0.0.1",
    description="This package contains taxipred app that predicts taxi prices",
    author="Susanna",
    author_email="author@email.com",
    install_requires=["streamlit", "pandas", "fastapi", "scikit-learn", "uvicorn"],
    package_dir={"": "src"},
    package_data={"taxipred": ["data/*.csv"]},
    packages=find_packages(),

)


# 'tree .' to see folder/file structure in terminal
# 'uv pip install -e .' for building editable updates of project based on 
# 'setup.py' file

