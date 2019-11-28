# Auto Project Skeleton

A simple command line project skeleton generator with git integration.

usage: main.py [-h] -n PROJECTNAME [-g] [-p PATH] [-l LICENSE] [-c PROGRAMMINGLANGUAGE] [-d DESCRIPTION]

optional arguments:
  -h, --help            show this help message and exit
  -n PROJECTNAME, --projectname PROJECTNAME
                        Name of the project
  -g, --usegit          Flag whether git repo is created and initialised. Please ensure github access token is defined in environment
                        variables the default env variable for this flag is "GITHUB_TOKEN" if this is different to you use the token
                        name flag
  -p PATH, --path PATH  specify path if not current working directory
  -l LICENSE, --license LICENSE
                        Specify the opensource licence to use if any
  -c PROGRAMMINGLANGUAGE, --programminglanguage PROGRAMMINGLANGUAGE
                        Programming language to use if any
  -d DESCRIPTION, --description DESCRIPTION
                        Description of this project
