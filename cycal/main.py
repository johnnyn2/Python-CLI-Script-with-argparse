import math

def output(func, val, args):
    quiet = args.quiet
    verbose = args.verbose
    radius = args.radius
    height = args.height
    if quiet:
        print(val)
    elif verbose:
        print(f"{func} of a Cylinder with radius {radius} and height {height} is {val}")
    else:
        print(f"The volume is {val}")

def volume(args):
    radius = args.radius
    height = args.height
    vol = math.pi * math.pow(radius, 2) * height
    output(func='Volume', val=vol, args=args)

def surface(args):
    radius = args.radius
    height = args.height
    surface = 2 * math.pi * radius * height + 2 * math.pi * math.pow(radius, 2)
    output(func='Surface', val=surface, args=args)