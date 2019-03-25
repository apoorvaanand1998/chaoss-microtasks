#! /usr/bin/env python3

import argparse
import datetime
from pprint import pprint

from perceval.backends.core.git import Git
from perceval.backends.core.github import GitHub

# Parse command line arguments
parser = argparse.ArgumentParser(
    description = "Simple parser for Git and Github"
    )
parser.add_argument("-t", "--token",
                    help = "GitHub token")
parser.add_argument("-r", "--repo",
                    help = "GitHub repository, as 'owner/repo'")
parser.add_argument("-fr", "--fromdate",
                    help = "Date that you want to fetch information from in format YYYYMMDD")
parser.add_argument("-to", "--todate",
                    help = "Date that you want to fetch information till in format YYYYMMDD")
args = parser.parse_args()

# Owner and repository names
(owner, repo) = args.repo.split('/')
repo_git_uri = "http://github.com/{}/{}.git".format(owner, repo)
repo_dir = 'tmp/perceval'

# Convert from and to date to datetime object
fr_dt_tuple = map(int, (args.fromdate[:4], args.fromdate[4:6], args.fromdate[6:]))
fr_dt = datetime.datetime(*fr_dt_tuple)
to_dt_tuple = map(int, (args.todate[:4], args.todate[4:6], args.todate[6:]))
to_dt = datetime.datetime(*to_dt_tuple)

git_obj = Git(uri=repo_git_uri, gitpath=repo_dir)
github_obj = GitHub(owner=owner, repository=repo, api_token=args.token)

# Big dicts printed, can be pretty printed for convenience
for commit in git_obj.fetch():
    print(commit, '\n')

for item in github_obj.fetch(from_date=fr_dt, to_date=to_dt):
    print(item, '\n')