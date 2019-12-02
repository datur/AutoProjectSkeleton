import os
import sys
import json
import requests
from requests.exceptions import HTTPError
import folder_structures
import utils


GITHUB_CREATE_URL = "https://api.github.com/user/repos"
GITHUB_PUSH_URL = "https://github.com/"


def create_filesystem(repo_name: str, filepath: str, use_git=False, git_data=None):
    """
    Creates the filesystem

    :return: Nothing
    """
    git_data = utils.dotdict(git_data)
    if use_git:
        # Creates a repo with github api and clones it into user specified path
        create_repo(repo_name, filepath, language=git_data['lang'],
                    license=git_data['license'], desc=git_data['desc'])

    else:
        os.chdir(filepath)
        # Create porject base dir
        os.mkdir(repo_name)

    if git_data.lang == 'python':
        folder_structures.python(repo_name=repo_name, desc=git_data.desc)

    if git_data.lang.lower() == 'c++' or 'cpp':
        folder_structures.cpp(repo_name=repo_name)

    if use_git:
        utils.create_process(f'git add .')
        utils.create_process(f"git commit -m 'initial commit'")
        utils.create_process(f'git push -u origin master')


def create_repo(repo_name: str, filepath: str, language=None, license=None, desc=None):
    header = {"Authorization": f"token {os.environ['GITHUB_TOKEN']}"}
    data = {"name": repo_name, "auto_init": False}
    if language is not None:
        data["gitignore_template"] = language.capitalize()
    if license is not None:
        data["license_template"] = license
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
        os.chdir(filepath)

        utils.create_process(
            f'git clone {GITHUB_PUSH_URL+repo_suffix+".git"}')
