#!/usr/bin/env python
#
# Somewhat generic, but then also hacked specifically to compare protocol 38215 to 38749.
#
# Usage: python ./protocol-diff.py 38215 38749
#

import sys
import argparse
import pprint

def diff_things(typeinfo_index, thing_a, thing_b):
    if type(thing_a) == dict:
        thing_a = thing_a.items()
        thing_b = thing_b.items()
        
    if type(thing_a) == list or type(thing_a) == tuple:
        if len(thing_a) != len(thing_b):
            print >> sys.stdout, "typeinfo {} diff len: {} {}".format(index, len(thing_a), len(thing_b))
        else:
            for ix in range(len(thing_a)):
                diff_things(typeinfo_index, thing_a[ix], thing_b[ix])
    elif thing_a != thing_b:
        if type(thing_a) == int:
            if (thing_a < 55 or thing_a - 1 != thing_b):
                print >> sys.stdout, "typeinfo {} diff number: {} {}".format(index, thing_a, thing_b)
        else:
            print >> sys.stdout, "typeinfo {} diff string: {} {}".format(index, thing_a, thing_b)
            

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('protocol_a', help='first protocol to compare')
    parser.add_argument('protocol_b', help='second protocol to compare')
    args = parser.parse_args()

    print >> sys.stdout, "Comparing {} to {}".format(args.protocol_a, args.protocol_b)

    protocol_a = __import__('protocol%s' % (args.protocol_a,))
    protocol_b = __import__('protocol%s' % (args.protocol_b,))

    print >> sys.stdout, "# typeinfos: {} {}".format(len(protocol_a.typeinfos), len(protocol_b.typeinfos))

    del protocol_a.typeinfos[55]
    for index in range(202):
        a = protocol_a.typeinfos[index]
        b = protocol_b.typeinfos[index]
        diff_things(index, a, b)
