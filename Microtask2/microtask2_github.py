# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Apoorva Anand
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, 51 Franklin Street, Fifth Floor, Boston, MA 02110-1335, USA.
#
# Authors:
#     Apoorva Anand <mitul.apoorva@gmail.com>
#
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

