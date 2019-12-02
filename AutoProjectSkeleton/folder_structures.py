import os

sphinx_instructions = (

    '# Sphinx Instructions',

    "If sphinx is not installed run:",

    "\n\n\t```pip install sphinx```\n",

    "\nOnce installed run `sphinx-quickstart`",

    "\nDont forget to fix the path in `conf.py` change it to something like `../<module >` or `..`"
)


def python(repo_name, desc):
    '''
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
    |   |-- __init__.py
    |   |-- main.py
    |   |-- test/
    |   |   |-- __init__.py
    |   |   |-- test_main.py
    |
    |-- setup.py
    |-- README
    |-- TODO
    '''
    # Change dir to newly created dir for the rest of file inits
    os.chdir(f'{os.getcwd()}/{repo_name}')
    with open('README.md', 'w') as f:
        f.write(f'# {repo_name.capitalize()}')
        if desc is not None:
            f.write(f'\n## {desc}')
    with open('TODO.md', 'w') as f:
        f.write(f'# TODO')
    with open('requirements.txt', 'w') as f:
        os.utime(os.getcwd(), None)

    # create package
    os.mkdir(repo_name)
    os.chdir(f'{os.getcwd()}/{repo_name}')
    with open('__init__.py', 'w') as f:
        os.utime(os.getcwd(), None)

    with open(f'{repo_name}.py', 'w') as f:
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
        f.write(''.join(sphinx_instructions))

    os.chdir('..')


def cpp(repo_name):
    """
    taken from: https://medium.com/heuristics/c-application-development-part-1-project-structure-454b00f9eddc
    creates the following file structure:

    Project_name
    |
    |---- CMakeLists.txt
    |
    |---- include
    |       |
    |       |---- Project_name
    |                 |
    |                 |---- public_header(s).h
    |
    ---- src
    |     |
    |     |---- private_header(s).h
    |     |
    |     |---- code(s).cpp
    |
    |
    |---- libs
    |       |
    |       |---- A
    |       |
    |       |---- B
    |
    |
    |---- tests
    """
    os.chdir(f'{os.getcwd()}/{repo_name}')

    # Make dirs
    os.mkdir('tests')
    os.mkdir('libs')
    os.mkdir('src')
    os.mkdir('include')

    # base dir files
    with open('README.md', 'w') as f:
        f.write(f'# {repo_name.capitalize()}')
    with open('TODO.md', 'w') as f:
        f.write(f'# TODO')
    with open('CMakeLists.txt', 'w') as f:
        os.utime(os.getcwd(), None)

    os.chdir(f'{os.getcwd()}/include')
    os.mkdir(f'{repo_name}')
    os.chdir('..')

    os.chdir((f'{os.getcwd()}/src'))
    with open('main.cpp', 'w') as f:
        os.utime(os.getcwd(), None)
    os.chdir('..')
