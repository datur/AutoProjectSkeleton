import parser
import AutoProjectSkeleton as aps
import unittest


args = parser.parse_args()
filepath = args.path if args.path else '.'
git_data = {}
git_data['desc'] = args.description if args.description else None
git_data['lang'] = args.programminglanguage if args.programminglanguage else None
git_data['license'] = args.license if args.license else None
aps.create_filesystem(args.projectname, filepath,
                      use_git=args.usegit, git_data=git_data)
