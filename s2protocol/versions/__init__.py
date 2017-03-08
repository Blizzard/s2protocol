import os
import re
import imp
import sys


def import_protocol(base_path, module_name):

    # Try to return the module if it's been loaded already
    try:
        return sys.modules[module_name]
    except KeyError:
        pass

    # print 'importing', module_name, 'from', base_path
    # If any of the following calls raises an exception,
    # there's a problem we can't handle -- let the caller handle it.
    fp, pathname, description = imp.find_module(module_name, [base_path])
    try:
        return imp.load_module(module_name, fp, pathname, description)
    finally:
        # Since we may exit via an exception, close fp explicitly.
        if fp:
            fp.close()


def list_all(base_path=None):
    if base_path is None:
        base_path = os.path.dirname(__file__)
    pattern = re.compile('.*protocol[0-9]+.py$')
    files = [ f for f in os.listdir(base_path) \
        if pattern.match(f) ]
    files.sort()
    return files


def latest():
    """
    Import the latest protocol version in the versions module (directory)

    This implementation is derived from the __import__ example here:
        https://docs.python.org/2/library/imp.html
    """
    # Find matchng protocol version files
    base_path = os.path.dirname(__file__)
    files = list_all(base_path)

    # Sort using version number, take latest
    latest_version = files[-1]
    
    # Convert file to module name
    module_name = latest_version.split('.')[0]
    
    # Perform the import
    return import_protocol(base_path, module_name)



def build(build_version):
    """
    Get the module for a specific build version
    """
    base_path = os.path.dirname(__file__)
    return import_protocol(base_path, 'protocol{0}'.format(build_version))

