from setuptools import setup, find_packages

setup(
    #this will be the package name you will see, e.g. the output of 'conda list' in anaconda prompt
    name = 'python_ds_algo', 
    #some version number you may wish to add - increment this after every update
    version='1.0', 
  
    # Use one of the below approach to define package and/or module names:
  
    #if there are only handful of modules placed in root directory, and no packages/directories exist then can use below syntax
#     packages=[''], #have to import modules directly in code after installing this wheel, like import mod2 (respective file name in this case is mod2.py) - no direct use of distribution name while importing
  
    #can list down each package names - no need to keep __init__.py under packages / directories
#     packages=['<list of name of packages>'], #importing is like: from package1 import mod2, or import package1.mod2 as m2
  
    #this approach automatically finds out all directories (packages) - those must contain a file named __init__.py (can be empty)
    packages=find_packages(), #include/exclude arguments take * as wildcard, . for any sub-package names
        install_requires=[
        "Django>=2.0",
        "libsass~=0.19",
    ],
    extras_require={
        "dev": [
            "flake8~=3.8",
            "flake8-annotations~=2.0",
            "flake8-bugbear~=20.1",
            "flake8-docstrings~=1.4",
            "flake8-import-order~=0.18",
            "flake8-tidy-imports~=4.0",
            "flake8-todo~=0.7",
            "flake8-string-format~=0.3",
            "pdoc~=0.3",
            "pep8-naming~=0.9",
            "pre-commit~=2.1",
            "PyGithub~=1.43",
            "wheel~=0.33",
        ]
    },
    include_package_data=True,
)
