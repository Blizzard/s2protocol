import os
import re
import importlib.util
import sys


def _import_protocol(base_path, protocol_module_name):
    """
    Import a module from a base path, used to import protocol modules.

    This implementation is derived from the __import__ example here:
        https://docs.python.org/2/library/imp.html
    """

    # Try to return the module if it's been loaded already
    try:
        return sys.modules[protocol_module_name]
    except KeyError:
        pass

    # If any of the following calls raises an exception,
    # there's a problem we can't handle -- let the caller handle it.
    #
    spec = importlib.util.find_spec(protocol_module_name, [base_path])
    if spec is not None:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    else:
        raise ImportError(f"Can't find {protocol_module_name}")


def list_all(base_path=None):
    """
    Returns a list of the current protocol version file names in the versions module sorted by name.
    """
    if base_path is None:
        base_path = os.path.dirname(__file__)
    pattern = re.compile('.*protocol[0-9]+.py$')
    files = [f for f in os.listdir(base_path) if pattern.match(f)]
    files.sort()
    return files


def latest():
    """
    Import the latest protocol version in the versions module (directory)
    """
    # Find matching protocol version files
    base_path = os.path.dirname(__file__)
    files = list_all(base_path)

    # Sort using version number, take latest
    latest_version = files[-1]

    # Convert file to module name
    module_name = latest_version.split('.')[0]

    # Perform the import
    return _import_protocol(base_path, module_name)


def build(build_version):
    """
    Get the module for a specific build version
    """
    base_path = os.path.dirname(__file__)
    return _import_protocol(base_path, 'protocol{0:05d}'.format(build_version))
