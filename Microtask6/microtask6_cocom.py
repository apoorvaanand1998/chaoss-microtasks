import pprint
import sys
from graal.backends.core.cocom import CoCom, CoComCommand

cc_parser = CoComCommand.setup_cmd_parser()
parsed_args = cc_parser.parse(*sys.argv[1:])

cc = CoCom(uri=parsed_args.uri, git_path=parsed_args.git_path, details=parsed_args.details)

for analysis in cc.fetch(from_date=parsed_args.from_date, to_date=parsed_args.to_date):
    pprint.pprint(analysis)