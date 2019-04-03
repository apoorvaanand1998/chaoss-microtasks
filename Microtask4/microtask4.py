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
import ast
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(
    description = "Simple parser for SoftwareHeritage API"
    )
parser.add_argument("-r", "--repo",
                    help = "GitHub repository, as 'owner/repo'")
args = parser.parse_args()

# use origin end point
ro_get1 = requests.get('https://archive.softwareheritage.org/api/1/origin/git/url/https://github.com/{}/'.format(args.repo))
#convert to dict
origin_dict = ast.literal_eval(ro_get1.text)
# check for status code
if ro_get1.status_code == 404:
    print("The repository is not available on SoftwareHeritage")
else:
    #use visit end point
    visits_url = origin_dict["origin_visits_url"]
    ro_get2 = requests.get('https://archive.softwareheritage.org/{}'.format(visits_url))
    #do this so literal eval works
    visits_str = ro_get2.text.replace("null", "'null'")
    visits_list = ast.literal_eval(visits_str)
    print("The repository is available on SoftwareHeritage and the date of last visit is", visits_list[0]["date"], "and the status is", visits_list[0]["status"])

