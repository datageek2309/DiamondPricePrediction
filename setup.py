from setuptools import find_packages,setup
from typing import List

HYPEN_E="-e ."

def get_requirements(file_path:str)->List[str]:
    """
    This function reads the packages from the requirements.txt
    file and returns all of them in a list
    """
    try:
        with open(file_path,'r') as packages_file:
            packages=packages_file.readlines()
            packages=[package.replace("\n","") for package in packages]
            if HYPEN_E in packages:
                packages.remove(HYPEN_E)
        return packages
    except Exception as e:
        raise e

setup(
    name="DiamondPricePrediction",
    version="0.0.1",
    author="Venkat Prashanth Moram",
    author_email="moramvenkatprashanth@gmail.com",
    intall_requires=get_requirements("requirements.txt"),
    packages=find_packages(),

)