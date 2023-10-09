from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="logger",
    version="0.0.1",
    author="Wesley Marques",
    description="display of logs in project development",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["app/logger"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[],
    dependency_links=['https://github.com/wesleymr59/logger']
)