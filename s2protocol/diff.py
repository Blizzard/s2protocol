#
# Protocol diffing tool from http://github.com/dsjoerg/s2protocol
#
# Usage: s2_cli.py --diff 38215,38749
#

import sys
import argparse
import pprint

from s2protocol.versions import build

def diff_things(typeinfo_index, thing_a, thing_b):
    if type(thing_a) != type(thing_b):
        print(
            "typeinfo {} diff types: {} {}".format(
                typeinfo_index, type(thing_a), type(thing_b)
            )
        )
        return

    if type(thing_a) == dict:
        thing_a = thing_a.items()
        thing_b = thing_b.items()
         
    if type(thing_a) == list or type(thing_a) == tuple:
        if len(thing_a) != len(thing_b):
            print(
                "typeinfo {} diff len: {} {}".format(
                    typeinfo_index, len(thing_a), len(thing_b)
                )
            )
        else:
            for ix in range(len(thing_a)):
                diff_things(typeinfo_index, thing_a[ix], thing_b[ix])
    elif thing_a != thing_b:
        if type(thing_a) == int:
            if (thing_a < 55 or thing_a - 1 != thing_b):
                print(
                    "typeinfo {} diff number: {} {}".format(
                        typeinfo_index, thing_a, thing_b
                    )
                )
        else:
            print(
                "typeinfo {} diff string: {} {}".format(
                    typeinfo_index, thing_a, thing_b
                )
            )
            

def diff(protocol_a_ver, protocol_b_ver):
    print(
        "Comparing {} to {}".format(
            protocol_a_ver, protocol_b_ver
        )
    )

    protocol_a = build(protocol_a_ver)
    protocol_b = build(protocol_b_ver)
    count_a = len(protocol_a.typeinfos)
    count_b = len(protocol_b.typeinfos)
    print("Count of typeinfos: {} {}".format(count_a, count_b))
    for index in range(max(count_a, count_b)):
        if index >= count_a:
            print("Protocol {} missing typeinfo {}".format(protocol_a_ver, index))
            continue
        if index >= count_b:
            print("Protocol {} missing typeinfo {}".format(protocol_b_ver, index))
            continue
        a = protocol_a.typeinfos[index]
        b = protocol_b.typeinfos[index]
        diff_things(index, a, b)
