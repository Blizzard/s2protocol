#!/usr/bin/python

import sys
import unittest
import os
import inspect
import re

from optparse import OptionParser

#
# Fix up import path if running directly
#
if __name__ == '__main__':
    filename = os.path.abspath(inspect.getfile(inspect.currentframe()))
    thispath = os.path.dirname(filename)
    normpath = os.path.normpath(os.path.join(thispath, os.pardir))
    sys.path.insert(0, normpath)

import s2protocol
import test_versions
import test_files


def run():
    parser = OptionParser()
    parser.add_option('-l', '--list', dest='list', action='store_true',
        help='List all test cases')
    parser.add_option('-r', '--requests', dest='requests', action='store_true',
        help='Enable logging of requests')
    parser.add_option('-v', '--verbose', dest='verbose', action='store_true',
        help='Enable verbose logging')
    parser.add_option('-f', '--filter', dest='filter', type='string', action='store',
        help='Filter test cases with a regular expression')
    options, args = parser.parse_args()

    all_tests = [
        test_versions.suite(),
        test_files.suite()
    ]

    if options.list:
        for suite in all_tests:
            for t in suite:
                print(t.id())
        return

    if options.filter:
        pattern = re.compile(options.filter)
        def expand_tests():
            for suite in all_tests:
                for t in suite:
                    yield t

        def pattern_match(test):
            name = test.id()
            return pattern.match(name) is not None
        all_tests = unittest.TestSuite(filter(pattern_match, expand_tests()))
    else:
        all_tests = unittest.TestSuite(all_tests)

    test_verbosity = 1
    if options.verbose:
        test_verbosity = 3

    unittest.TextTestRunner(verbosity=test_verbosity, failfast=True).run(all_tests)

if __name__ == '__main__':
    run()

