'''
The setup.py file is an esential part of package distribution in Python.
 It contains metadata about the package and instructions on how to install it.
 This file is used by tools like pip to install the package and its dependencies.
 '''
from setuptools import setup, find_packages
from typing import List


def get_requirements()-> List[str]:
    """
    This function reads the requirements.txt file and returns a list of dependencies.
    """
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt','r') as file:
            # read line from the file
            lines = file.readlines()
            #process each line
            for line in lines:
                requirement = line.strip()
                ## ignore empty lines and -e .
                if requirement and not requirement.startswith('-e'):
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the project directory.")
    return requirement_lst


setup(
    name='NetworkSecurity',
    version='0.1.0',
    author='Vishal Shelke',
    author_email='vishalshelke2229@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)