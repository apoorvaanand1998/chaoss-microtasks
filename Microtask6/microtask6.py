#! /usr/bin/env python3
import pprint
from graal.backends.core.colic import CoLic
from graal.backends.core.cocom import CoCom

# URL for the git repo to analyze
repo_uri = 'http://github.com/chaoss/grimoirelab-perceval'

# Colic and Cocom object initialization
cc = CoCom(uri=repo_uri, git_path='/tmp/graal-cocom')
cl = CoLic(uri=repo_uri, git_path='/tmp/graal-colic', exec_path='/home/spirit/Desktop/fossology/src/nomos/agent/nomossa')

# print analysis of cocom and colic alternatively, indefinitely, keyboard interrupt to end
while True:
    pprint.pprint(next(cc.fetch()))
    pprint.pprint(next(cl.fetch()))



