import argparse


def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--projectname', type=str,
                        help='Name of the project', required=True)
    parser.add_argument('-g', '--usegit', help='Flag whether git repo is created and initialised. Please ensure github \
     access token is defined in environment variables the default env variable for this flag is "GITHUB_TOKEN" if this \
     is different to you use the token name flag', action='store_true')
    parser.add_argument(
        '-p', '--path', help="specify path if not current working directory")
    parser.add_argument('-l', '--license',
                        help="Specify the opensource licence to use if any")
    parser.add_argument('-c', '--programminglanguage',
                        help='Programming language to use if any')
    parser.add_argument('-d', '--description',
                        help="Description of this project")

    return parser.parse_args()
