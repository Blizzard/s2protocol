import logging
import os
import re
import importlib
import sys

PROTOCOLS=[]
def _import_protocol(base_path, protocol_module_name):
    """
    Import a module from a base path, used to import protocol modules.

    This implementation is derived from the import_module example here:
        https://docs.python.org/3/library/importlib.html#approximating-importlib-import-module
    """

    requested_protocol = protocol_module_name
    if protocol_module_name not in PROTOCOLS:
        fallback_module_name = max(
            PROTOCOLS,
            key=protocol_version
        )
        logger = logging.getLogger(__name__)
        logger.warning(
            "Protocol %s not supported, using %s",
            requested_protocol,
            fallback_module_name,
        )
        protocol_module_name = fallback_module_name.split('.')[0]


    # Try to return the module if it's been loaded already
    try:
        return sys.modules[protocol_module_name]
    except KeyError:
        pass

    # Otherwise try to load the module
    spec = importlib.util.spec_from_file_location(
        protocol_module_name,
        os.path.join(base_path, protocol_module_name+'.py')
    )
    if spec is None or spec.loader is None:
        raise ImportError(
            f"Unable to load protocol module '{protocol_module_name}'"
        )
    module = importlib.util.module_from_spec(spec)

    # If the module does not exist, raise an exception and let the
    # caller handle it
    if( not os.path.exists(spec.origin) ):
        raise ImportError("No module named '{}'".format(protocol_module_name))

    sys.modules[protocol_module_name] = module
    spec.loader.exec_module(module)
    return module

def protocol_version(name):
    m = re.search(r'(\d+)', name)
    if not m:
        raise ValueError(f"Invalid protocol name: {name}")
    return int(m.group(1))

def list_all(base_path=None):
    """
    Returns a list of the current protocol version file names in the versions module sorted by name.
    """
    global PROTOCOLS
    if base_path is None:
        base_path = os.path.dirname(__file__)
    pattern = re.compile('.*protocol[0-9]+.py$')
    PROTOCOLS = [ f for f in os.listdir(base_path) \
        if pattern.match(f) ]

    """
    sort string containing integers is problematic.
    """
    PROTOCOLS.sort(key=protocol_version)
    return PROTOCOLS


def latest():
    """
    Import the latest protocol version in the versions module (directory)
    """
    # Find matchng protocol version files
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

