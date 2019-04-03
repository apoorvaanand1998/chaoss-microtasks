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
import requests
import pprint
import ast
import json

# General statistics of the content of archive
counters = requests.get('https://archive.softwareheritage.org/api/1/stat/counters/')
print("Here's some general info from the SoftwareHeritage API:")
pprint.pprint(ast.literal_eval(counters.text))

# Info through the repo and timestamp
repo = "chaoss/grimoirelab"  # assuming only git repos
timestamp = "2018-01-01T00:00:00+00:00"  # timestamp in ISO date or UNIX time format

# to get origin id
origin = requests.get('https://archive.softwareheritage.org/api/1/origin/git/url/https://github.com/{}/'.format(repo))
origin_dict= ast.literal_eval(origin.text)
id = origin_dict["id"]

# Revision info based on origin id and timestamp
rev = requests.get('https://archive.softwareheritage.org/api/1/revision/origin/{}/ts/{}/'.format(id, timestamp))
print("\nHere's the revision info based on origin id and timestamp\n", json.dumps(json.loads(rev.text), indent=4), "\n")

# log info
rev_log = requests.get('https://archive.softwareheritage.org/api/1/revision/origin/{}/ts/{}/log'.format(id, timestamp))
print("\nHere's the log for above revision\n", json.dumps(json.loads(rev_log.text), indent=4), "\n")

# Info through git commit id
commit_id = "96c10381fd4019ee763df534741a7e1e679d382f"

# Revision info based on commit id
rev_id = requests.get('https://archive.softwareheritage.org/api/1/revision/{}/'.format(commit_id))
print("\nHere's the revision info based on commit id\n", json.dumps(json.loads(rev_id.text), indent=4), "\n")

# Revision log based on commit id
rev_id_log = requests.get('https://archive.softwareheritage.org/api/1/revision/{}/log'.format(commit_id))
print("\nHere's the log based on commit id\n", json.dumps(json.loads(rev_id_log.text), indent=4), "\n")

# The json.dumps can be outputted to data.json file if needed, and also careful about the number of attempts at API

