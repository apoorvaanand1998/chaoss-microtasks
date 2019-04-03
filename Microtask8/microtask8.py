import sys
import os
import shutil
import pprint
from graal.graal import GraalCommand, GraalCommandArgumentParser, GraalRepository
from graal.backends.core.analyzers.flake8 import Flake8

class XGraalCommand(GraalCommand):

    @staticmethod
    def setup_cmd_parser(exec_path=False):
        """Returns the XGraal argument parser."""

        parser = XGraalCommandArgumentParser(from_date=True, to_date=True, exec_path=exec_path)

        # Required arguments
        parser.parser.add_argument('uri',
                                   help="URI of the Git log repository")
        parser.parser.add_argument('--git-path', dest='git_path',
                                   help="Path where the Git repository will be cloned")
        parser.parser.add_argument('--sha', dest='sha',
                                   help="Commit SHA")

        return parser


class XGraalCommandArgumentParser(GraalCommandArgumentParser):

    def parse(self, *args):
        """Parse a list of arguments.

        Parse argument strings needed to run a backend command. The result
        will be a `argparse.Namespace` object populated with the values
        obtained after the validation of the parameters.

        :param args: argument strings

        :result: an object with the parsed values
        """
        parsed_args = self.parser.parse_args(*args)

        return parsed_args


def main():
    parser = XGraalCommand.setup_cmd_parser()
    args = parser.parse(sys.argv[1:])

    if not GraalRepository.exists(args.git_path):
        repo = GraalRepository.clone(args.uri, args.git_path)
    if os.path.isdir(args.git_path):
        repo = GraalRepository(args.uri, args.git_path)

    # delete tree if it already exists
    if GraalRepository.exists('/tmp/worktrees'):
        shutil.rmtree('/tmp/worktrees')

    if not os.path.exists('/tmp/worktrees'):
        os.mkdir('/tmp/worktrees')

    # create new tree
    repo.worktree('/tmp/worktrees')
    repo.checkout(args.sha)

    flake8_obj = Flake8()
    result = flake8_obj.analyze(module_path='/tmp/worktrees', details=True, worktree_path='/tmp/worktrees')
    pprint.pprint(result)

if __name__ == '__main__':
    main()