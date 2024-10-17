# setup.py

from setuptools import setup, find_packages

setup(
    name="nwos",
    version="0.3",
    description="A library for working with prime and composite numbers",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Nlolik1111",
    author_email="nikolay9047670014@gmail.com",
    url="https://github.com/yourusername/nwos",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
