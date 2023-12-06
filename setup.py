import os
import setuptools

__version__ = '0.0.1'
repo_name = "CNN-Project-structure"
author_git_url = "https://github.com/Srinubabuvelugu"

setuptools.,setup(
    name = "CNN Project Structure",
    version = '0.0.1',
    author = "Velugu Srinu Babu",
    author_email = "srinubabu1119@gmail.com",
    description = "This is the Deep Learning Classification Project",
    long_description = long_description,
    long_description_content = "text/markdown",
    url= f"{author_git_url}/{repo_name}",
    project_urls = {
        "Bug Tracker": f"{author_git_url}/{repo_name}/issues",
    },
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where="src")
)