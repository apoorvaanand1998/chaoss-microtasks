import sys
import pprint
from perceval.backends.core.github import GitHubCommand, GitHub

# GitHub cmd parser
gh_parser = GitHubCommand.setup_cmd_parser()
# parse all commandline arguments
parsed_args = gh_parser.parse(*sys.argv[1:])

github_obj = GitHub(owner=parsed_args.owner, repository=parsed_args.repository, api_token=parsed_args.api_token)

# the whole big dict is pretty printed
for commit in github_obj.fetch(from_date=parsed_args.from_date, to_date=parsed_args.to_date):
    pprint.pprint(commit)

