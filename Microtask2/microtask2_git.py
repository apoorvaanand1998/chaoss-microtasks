import sys
import pprint
from perceval.backends.core.git import GitCommand, Git

# Git cmd parser
g_parser = GitCommand.setup_cmd_parser()
# parse all commandline arguments
parsed_args = g_parser.parse(*sys.argv[1:])

git_obj = Git(uri=parsed_args.uri, gitpath=parsed_args.git_path)

for commit in git_obj.fetch(from_date=parsed_args.from_date, to_date=parsed_args.to_date):
    pprint.pprint(commit)