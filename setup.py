
from setuptools import setup, find_packages

setup(
    name= azazel-sem ,
    version= 0.1 ,
    packages=find_packages(),
    entry_points={
         console_scripts : [
             display_trimix_image = azazelSEm:display_trimix_image 
        ]
    }
)
