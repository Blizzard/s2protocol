#!/usr/bin/env python
from __future__ import print_function

import argparse
import binascii
import cProfile
import json
import pprint
import pstats
import re
import sys

from mpyq import MPQArchive

from s2protocol.versions import build, list_all, latest
from s2protocol.diff import diff
from s2protocol.compat import get_stream
import s2protocol.attributes as _attr

__all__ = (
    'EventFilter', 'JSONOutputFilter', 'NDJSONOutputFilter',
    'PrettyPrintFilter', 'StatCollectionFilter', 'TypeDumpFilter',
    'cache_handle_uri', 'convert_fourcc', 'json_dump', 'main',
    'process_details_data', 'process_init_data', 'process_scope_attributes',
    'read_contents',
)


def json_dump(obj, indent=None):
    def dispatch(o):
        # Find all bytes(str in Python2) to decode with ISO-8850-1
        if isinstance(o, dict):
            return {k: dispatch(v) for k, v in o.items()}
        elif isinstance(o, list):
            return [dispatch(v) for v in o]
        elif isinstance(o, bytes):
            return o.decode('ISO-8859-1')
        else:
            return o

    return json.dumps(dispatch(obj), indent=indent)


class EventFilter(object):
    def process(self, event):
        """ Called for each event in the replay stream """
        return event

    def finish(self):
        """ Called when the stream has finished """
        pass


class JSONOutputFilter(EventFilter):
    """ Added as a filter will format the event into JSON """
    def __init__(self, output):
        self._output = output

    def process(self, event):
        print(json_dump(event, indent=4), file=self._output)
        return event


class NDJSONOutputFilter(EventFilter):
    """ Added as a filter will format the event into NDJSON """
    def __init__(self, output):
        self._output = output

    def process(self, event):
        print(json_dump(event), file=self._output)
        return event


class PrettyPrintFilter(EventFilter):
    """ Add as a filter will send objects to stdout """
    def __init__(self, output):
        self._output = output

    def process(self, event):
        pprint.pprint(event, stream=self._output)
        return event


class TypeDumpFilter(EventFilter):
    """ Add as a filter to convert events into type information """
    def process(self, event):
        def recurse_into(value):
            if type(value) is list:
                decoded = []
                for item in value:
                    decoded.append(recurse_into(item))
                return decoded
            elif type(value) is dict:
                decoded = {}
                for key, inner_value in value.items():
                    decoded[key] = recurse_into(inner_value)
                return decoded
            return (type(value).__name__, value)
        return recurse_into(event)
    

class StatCollectionFilter(EventFilter):
    """ Add as a filter to collect stats on events """
    def __init__(self):
        self._event_stats = {}

    def process(self, event):
        # update stats
        if '_event' in event and '_bits' in event:
            stat = self._event_stats.get(event['_event'], [0, 0])
            stat[0] += 1  # count of events
            stat[1] += event['_bits']  # count of bits
            self._event_stats[event['_event']] = stat
        return event

    def finish(self):
        print('Name, Count, Bits')
        for name, stat in sorted(self._event_stats.items(), key=lambda x: x[1][1]):
            print('"{:s}", {:d}, {:d}'.format(name, stat[0], stat[1] / 8))


def convert_fourcc(fourcc_hex):
    """
    Convert a hexidecimal [fourcc](https://en.wikipedia.org/wiki/FourCC) 
    represpentation to a string.
    """
    s = []
    for i in range(0, 7, 2):
        n = int(fourcc_hex[i:i+2], 16)
        if n is not 0:
            s.append(chr(n))
    return ''.join(s)


def cache_handle_uri(handle):
    """
    Convert a 'cache handle' from a binary string to a string URI
    """
    handle_hex = binascii.b2a_hex(handle).decode()
    purpose = convert_fourcc(handle_hex[0:8]) # first 4 bytes
    region = convert_fourcc(handle_hex[8:16]) # next 4 bytes
    content_hash = handle_hex[16:]
  
    uri = ''.join([
        'http://',
        region.lower(),
        '.depot.battle.net:1119/',
        content_hash.lower(), '.',
        purpose.lower()
      ])
    return uri


def process_details_data(details):
    """
    Take details and convert cache handles to HTTP references.
    """
    translated_handles = []
    for handle in details['m_cacheHandles']:
        translated_handles.append(cache_handle_uri(handle))
    details['m_cacheHandles'] = translated_handles
    return details


def process_init_data(initdata):
    """
    Take replay init data and convert cache handles to HTTP references.
    """
    translated_handles = []
    for handle in initdata['m_syncLobbyState']['m_gameDescription']['m_cacheHandles']:
        translated_handles.append(cache_handle_uri(handle))
    initdata['m_syncLobbyState']['m_gameDescription']['m_cacheHandles'] = translated_handles
    return initdata


def process_scope_attributes(all_scopes, event_fn):
    # Build up the reverse attribute mapping
    attr_id_to_name = {}
    for sym in _attr.__dict__:
        if sym.startswith('_'):
            continue
        attr_id_to_name[_attr.__dict__.get(sym)] = sym.lower()

    # Each scope represents a slot in the lobby
    for scope, scope_dict in all_scopes.items():
        scope_doc = { 'scope': scope }
        # Convert all other attributes to symbolic representation
        for attr_id, val_dict in scope_dict.items():
            val = val_dict[0]['value'] 
            attr_name = attr_id_to_name.get(attr_id, None)
            if attr_name is not None:
                scope_doc[attr_name] = val
            else:
                scope_doc['unknown_{}'.format(attr_id)] = val

        # Pass the scope doc as a new event 
        event_fn(scope_doc)


def read_contents(archive, content):
    contents = archive.read_file(content)
    if not contents:
        print('Error: Archive missing {}'.format(content))
        sys.exit(1)
    return contents


def main():
    """
    Get command line arguments and invoke the command line functionality.
    """
    filters = []
    parser = argparse.ArgumentParser()
    parser.add_argument('replay_file', help='.SC2Replay file to load',
                        nargs='?')
    parser.add_argument("--gameevents", help="print game events",
                        action="store_true")
    parser.add_argument("--messageevents", help="print message events",
                        action="store_true")
    parser.add_argument("--trackerevents", help="print tracker events",
                        action="store_true")
    parser.add_argument("--attributeevents", help="print attributes events",
                        action="store_true")
    parser.add_argument("--attributeparse", help="parse attributes events",
                        action="store_true")
    parser.add_argument("--header", help="print protocol header",
                        action="store_true")
    parser.add_argument("--metadata", help="print game metadata",
                        action="store_true")
    parser.add_argument("--details", help="print protocol details",
                        action="store_true")
    parser.add_argument("--details_backup", help="print protocol anoynmized details",
                        action="store_true")
    parser.add_argument("--initdata", help="print protocol initdata",
                        action="store_true")
    parser.add_argument("--all", help="print all data",
                        action="store_true")
    parser.add_argument("--quiet", help="disable printing",
                        action="store_true")
    parser.add_argument("--stats", help="print stats",
                        action="store_true")
    parser.add_argument("--diff", help="diff two protocols",
                        default=None,
                        action="store")
    parser.add_argument("--versions", help="show all protocol versions",
                        action="store_true")
    parser.add_argument("--types", help="show type information in event output",
                        action="store_true")
    parser.add_argument("--json", help="print output as json",
                        action="store_true")
    parser.add_argument("--ndjson", help="print output as ndjson (newline delimited)",
                        action="store_true")
    parser.add_argument("--profile", help="Whether to profile or not",
                        action="store_true")
    args = parser.parse_args()

    if args.profile:
        pr = cProfile.Profile()
        pr.enable()

    # TODO: clean up the command line arguments to allow cleaner sub-command
    # style commands

    # List all protocol versions
    if args.versions:
        files = list_all()
        pattern = re.compile('^protocol([0-9]+).py$')
        captured = []
        for f in files:
            captured.append(pattern.match(f).group(1))
            if len(captured) == 8:
                print(captured[0:8])
                captured = []
        print(captured)
        return

    # Diff two protocols
    if args.diff and args.diff is not None:
        version_list = args.diff.split(',')
        if len(version_list) < 2:
            print("--diff requires two versions separated by comma e.g. --diff=1,2",
                  file=sys.stderr)
            sys.exit(1)
        diff(version_list[0], version_list[1])
        return

    # Check/test the replay file
    if args.replay_file is None:
        print(".S2Replay file not specified", file=sys.stderr)
        sys.exit(1)

    archive = MPQArchive(args.replay_file)
    
    filters = []

    if args.json:
        filters.insert(0, JSONOutputFilter(sys.stdout))
    elif args.ndjson:
        filters.insert(0, NDJSONOutputFilter(sys.stdout))
    elif not args.quiet:
        filters.insert(0, PrettyPrintFilter(sys.stdout))

    if args.types:
        filters.insert(0, TypeDumpFilter())

    if args.stats:
        filters.insert(0, StatCollectionFilter())

    def process_event(event):
        for f in filters:
            event = f.process(event)
        
    # Read the protocol header, this can be read with any protocol
    contents = archive.header['user_data_header']['content']
    header = latest().decode_replay_header(contents)
    if args.header:
        process_event(header)

    # The header's baseBuild determines which protocol to use
    baseBuild = header['m_version']['m_baseBuild']
    try:
        protocol = build(baseBuild)
    except Exception as e:
        print('Unsupported base build: {0} ({1!s})'.format(baseBuild, e),
              file=sys.stderr)
        sys.exit(1)

    # Process game metadata
    if args.all or args.metadata:
        contents = read_contents(archive, 'replay.gamemetadata.json')
        process_event(json.loads(contents))

    # Print protocol details
    if args.all or args.details:
        contents = read_contents(archive, 'replay.details')
        details = protocol.decode_replay_details(contents)
        details = process_details_data(details)
        process_event(details)

    # Print protocol details
    if args.all or args.details_backup:
        contents = read_contents(archive, 'replay.details.backup')
        details_backup = protocol.decode_replay_details(contents)
        details_backup = process_details_data(details_backup)
        process_event(details_backup)

    # Print protocol init data
    if args.all or args.initdata:
        contents = read_contents(archive, 'replay.initData')
        initdata = protocol.decode_replay_initdata(contents)
        initdata = process_init_data(initdata)
        process_event(initdata)

    # Print game events and/or game events stats
    if args.all or args.gameevents:
        contents = read_contents(archive, 'replay.game.events')
        map(process_event, protocol.decode_replay_game_events(contents))

    # Print message events
    if args.all or args.messageevents:
        contents = read_contents(archive, 'replay.message.events')
        map(process_event, protocol.decode_replay_message_events(contents))

    # Print tracker events
    if args.all or args.trackerevents:
        if hasattr(protocol, 'decode_replay_tracker_events'):
            contents = read_contents(archive, 'replay.tracker.events')
            map(process_event, protocol.decode_replay_tracker_events(contents))

    # Print attributes events
    if args.all or args.attributeevents or args.attributeparse:
        contents = read_contents(archive, 'replay.attributes.events')
        attributes = protocol.decode_replay_attributes_events(contents)

        # Process raw attribute events structure
        if args.attributeevents:
            process_event(attributes)
        
        # Convert attributes to higher level requested data, will
        # call prcess_event for each new event that it creates
        if args.attributeparse:
            process_scope_attributes(attributes['scopes'], process_event)
            
        
    for f in filters:
        f.finish()

    if args.profile:
        pr.disable()
        print("Profiler Results")
        print("----------------")
        s = get_stream()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())

if __name__ == '__main__':
    main()
