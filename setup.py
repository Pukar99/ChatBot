# setup.py

from setuptools import setup, find_packages

setup(
    name="ChatbotProject",
    version="0.1.0",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    ,
)
