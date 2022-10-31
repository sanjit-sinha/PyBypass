from setuptools import setup
import setuptools
import sys
import os

#==========================================================================================

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 7)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write(
        """
==========================
Unsupported Python version
==========================
This version of Requests requires at least Python {}.{}, but
you're trying to install it on Python {}.{}. To resolve this,
consider upgrading to a supported Python version.

If you can't upgrade your Python version, you'll need to
pin to an older version of Requests (<2.28).
""".format(
            *(REQUIRED_PYTHON + CURRENT_PYTHON)
        )
    )
    sys.exit(1)
    
#============================================================================================

about = {}
location = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(location, "PyBypass", "__version__.py"), "r") as f:
    exec(f.read(), about)


with open("README.md", "r") as file:
    readme = file.read()
    
#============================================================================================


requires = ["beautifulsoup4>=4.11.1", "requests>=2.28.1"]

#============================================================================================

setup(
    name=about["__title__"],  
    version=about["__version__"],                       
    author=about["__author__"],
    author_email=about["__author_email__"],            
    description=about["__description__"],
    long_description=readme, 
    long_description_content_type="text/markdown",
    project_source="https://github.com/sanjit-sinha/PyBypass",
    license=about["__license__"],
    
    packages=setuptools.find_packages(),
    keywords=['bypasser', 'ads', 'shortners', 'filehosters', 'gdtot', 'appdrive', 'shortners'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                               
    python_requires='>=3.7, <4',     
    package_dir={"PyBypass":"PyBypass"},    
    install_requires=requires,
    zip_safe=True
)
