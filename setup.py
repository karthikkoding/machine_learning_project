from setuptools import setup
from typing import List

#Declaring variables for setup functions 
PROJECT_NAME ="housing-predictor"
VERSION="0.0"
AUTHOR="karthik"
DESCRIPTION="This is an ml project"
PACKAGES= ["housing"]
REQUIREMENTS_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Desciption :This function is going to return the list of requirements mentioned in requirements.txt file
    
    return: the list of requirements(libraries) as text

    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()
    pass


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires= get_requirements_list()
)


if __name__=="__main__":
    print(get_requirements_list())