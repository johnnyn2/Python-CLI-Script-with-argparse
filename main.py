import math
import argparse

# accept args
parser = argparse.ArgumentParser(description="Calculate volume of a Cylinder")
parser.add_argument('-r', '--radius', type=int, metavar='', required=True, help='Radius of cylinder')
parser.add_argument('-H', '--height', type=int, metavar='', required=True, help='Height of cylinder')
# only one of the arguments in the group can be specified
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='print quiet')
group.add_argument('-v', '--verbose', action='store_true', help='print verbose')
# parse args from CLI
args=parser.parse_args()

def cylinder_volume(radius, height):
    vol = math.pi * math.sqrt(radius) * height
    return vol

if __name__ == '__main__':
    volume = cylinder_volume(args.radius, args.height)
    if args.quiet:
        print(volume)
    elif args.verbose:
        print("Volume of a Cylinder with radius %s and height %s is %s" % (args.radius, args.height, volume))
    else:
        print( "The volume is %s" % volume)