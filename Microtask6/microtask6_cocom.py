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
import pprint
import sys
from graal.backends.core.cocom import CoCom, CoComCommand

cc_parser = CoComCommand.setup_cmd_parser()
parsed_args = cc_parser.parse(*sys.argv[1:])

cc = CoCom(uri=parsed_args.uri, git_path=parsed_args.git_path, details=parsed_args.details)

for analysis in cc.fetch(from_date=parsed_args.from_date, to_date=parsed_args.to_date):
    pprint.pprint(analysis)
