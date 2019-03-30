import pprint
import sys
from graal.backends.core.colic import CoLic, CoLicCommand

cl_parser = CoLicCommand.setup_cmd_parser()
parsed_args = cl_parser.parse(*sys.argv[1:])

cl = CoLic(uri=parsed_args.uri, git_path=parsed_args.git_path, exec_path=parsed_args.exec_path)

for analysis in cl.fetch(from_date=parsed_args.from_date, to_date=parsed_args.to_date):
    pprint.pprint(analysis)