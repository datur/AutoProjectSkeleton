import os
import sys
import json
import requests
from requests.exceptions import HTTPError
import argparse


'''
TODO:
    - Get github username url from the request response 


'''
GITHUB_CREATE_URL = "https://api.github.com/user/repos"
GITHUB_PUSH_URL = "https://github.com/"

def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--projectname', type=str,
                        help='Name of the project', required=True)
    parser.add_argument('-g', '--usegit', help='Flag whether git repo is created and initialised. Please ensure github \
     access token is defined in environment variables the default env variable for this flag is "GITHUB_TOKEN" if this \
     is different to you use the token name flag', action='store_true')
    parser.add_argument('-t', '--tokenvariable', help='Optional flag for specifying a custom env variable name',
                        action='store_true')
    parser.add_argument(
        '-p', '--path', help="specify path if not current working directory")
    parser.add_argument('-l', '--license',
                        help="Specify the programming language")
    parser.add_argument('-d', '--description',
                        help="Description of this project")

    return parser.parse_args()

def create_filesystem(repo_name: str):
    """
    uses Jean-Paul Calderone's Filesystem structure of a Python project from:
    http://as.ynchrono.us/2007/12/filesystem-structure-of-python-project_21.html
    Project/
    |-- bin/
    |   |-- project
    |
    |-- docs/
    |   |-- Instructions.md
    |
    |-- project/
    |   |-- test/
    |   |   |-- __init__.py
    |   |   |-- test_main.py
    |   |
    |   |-- __init__.py
    |   |-- main.py
    |
    |-- setup.py
    |-- README
    |-- TODO

    :return: Nothing
    """
    # Create porject base dir
    os.mkdir(repo_name)

    # Change dir to newly created dir for the rest of file inits
    os.chdir(f'{os.getcwd()}/{repo_name}')
    with open('README.md', 'w') as f:
        f.write(f'# {repo_name.capitalize()}')
    with open('TODO.md', 'w') as f:
        f.write(f'# TODO')
    with open('requirements.txt', 'w') as f:
        os.utime(os.getcwd(), None)

    # create package
    os.mkdir(repo_name)
    os.chdir(f'{os.getcwd()}/{repo_name}')
    with open('__init__.py', 'w') as f:
        os.utime(os.getcwd(), None)

    with open('main.py', 'w') as f:
        os.utime(os.getcwd(), None)

    os.mkdir('test')
    os.chdir(f'{os.getcwd()}/test')
    with open('__init__.py', 'w') as f:
        os.utime(os.getcwd(), None)
    with open('test_main.py', 'w') as f:
        os.utime(os.getcwd(), None)

    os.chdir("../..")

    os.mkdir('docs')
    os.chdir(f'{os.getcwd()}/docs')
    with open('Instructions.md', 'w') as f:
        text = '''
# Sphinx Instructions

If sphinx is not installed run:

    ```pip install sphinx```

Once installed run `sphinx-quickstart`

Dont forget to fix the path in `conf.py` change it to something like `../<module>` or `..`
        '''
        f.write(text)

    os.chdir('..')


def create_repo(repo_name, language=None, licence=None, desc=None):
    print(os.getcwd())
    header = {"Authorization": f"token {os.environ['GITHUB_TOKEN']}"}
    data = {"name": repo_name, "auto_init": False}
    if language is not None:
        data["gitignore_template"] = language.capitalize()
    if licence is not None:
        data["license_template"] = licence
    if desc is not None:
        data['description'] = desc
    try:
        response = requests.post(
            GITHUB_CREATE_URL, headers=header, data=json.dumps(data))

        repo_suffix = json.loads(response.content)
        repo_suffix = repo_suffix['full_name'] 
        response.raise_for_status()
    except HTTPError as http_err:
        if http_err.response.status_code == 422:
            print(
                f'HTTP error occurred: 422 This repository already exists on your account')
        else:
            print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Created new Repository')

    repo_url = GITHUB_PUSH_URL+repo_suffix+'.git'
    os.popen("git init")
    os.popen(f"git remote add origin {repo_url}") 
    os.popen(f'git add .')
    os.popen(f"git commit -m 'initial commit'")
    os.popen(f'git push -u origin master')
    

if __name__ == '__main__':
    args = parse_args()
    create_filesystem(args.projectname)
    if args.usegit:
        create_repo(args.projectname, language='python',
                    licence="mit", desc='Test Repository')
