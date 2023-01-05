from setuptools import setup, find_packages
from typing import List

#Declaring variables for setup functions 
PROJECT_NAME ="housing-predictor"
VERSION="0.0.2"
AUTHOR="karthik"
DESCRIPTION="This is an ml project"
REQUIREMENTS_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Desciption :This function is going to return the list of requirements mentioned in requirements.txt file
    
    return: the list of requirements(libraries) as text

    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")
    pass


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires= get_requirements_list()
)

