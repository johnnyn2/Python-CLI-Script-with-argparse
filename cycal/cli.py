import argparse
from .main import volume, surface

# accept args
parser = argparse.ArgumentParser(description="Cylinder Calculator")
subparsers = parser.add_subparsers(title='subcommands', description='available functions')

subcommands = [
    surface, volume
]
for cmd in subcommands:
    # add subcommands
    subparser = subparsers.add_parser(cmd.__name__)
    subparser.add_argument('-r', '--radius', type=int, metavar='', required=True, help='Radius of cylinder')
    subparser.add_argument('-H', '--height', type=int, metavar='', required=True, help='Height of cylinder')
    subparser.set_defaults(func=cmd)
    # only one of the arguments in the group can be specified
    subgroup = subparser.add_mutually_exclusive_group()
    subgroup.add_argument('-q', '--quiet', action='store_true', help='print quiet')
    subgroup.add_argument('--verbose', action='store_true', help='print verbose')

# parse args from CLI
args=parser.parse_args()

def main():
    try:
        args.func(args)
    except:
        parser.print_help()
