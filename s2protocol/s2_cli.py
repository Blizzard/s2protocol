#!/usr/bin/env python
#
# Copyright (c) 2013 Blizzard Entertainment
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import sys
import argparse
import pprint
import re

import mpyq

import versions
import diff


class EventLogger:
    def __init__(self):
        self._event_stats = {}

    def log(self, output, event):
        # update stats
        if '_event' in event and '_bits' in event:
            stat = self._event_stats.get(event['_event'], [0, 0])
            stat[0] += 1  # count of events
            stat[1] += event['_bits']  # count of bits
            self._event_stats[event['_event']] = stat
        # write structure
        pprint.pprint(event, stream=output)

    def log_stats(self, output):
        for name, stat in sorted(self._event_stats.iteritems(), key=lambda x: x[1][1]):
            print >> output, '"%s", %d, %d,' % (name, stat[0], stat[1] / 8)


def main():
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
    parser.add_argument("--header", help="print protocol header",
                        action="store_true")
    parser.add_argument("--details", help="print protocol details",
                        action="store_true")
    parser.add_argument("--initdata", help="print protocol initdata",
                        action="store_true")
    parser.add_argument("--stats", help="print stats",
                        action="store_true")
    parser.add_argument("--diff", help="diff two protocols",
                        default=None,
                        action="store")
    parser.add_argument("--versions", help="show all protocol versions",
                        action="store_true")
    args = parser.parse_args()

    # TODO: clean up the command line arguments to allow cleaner sub-command
    # style commands

    # List all protocol versions
    if args.versions:
        files = versions.list_all()
        pattern = re.compile('^protocol([0-9]+).py$')
        captured = []
        for f in files:
            captured.append(pattern.match(f).group(1))
            if len(captured) == 8:
                print >> sys.stdout, captured[0:8]
                captured = []
        print >> sys.stdout, captured
        return

    # Diff two protocols
    if args.diff and args.diff is not None:
        version_list = args.diff.split(',')
        if len(version_list) < 2:
            print >> sys.stderr, "--diff requires two versions separated by comma e.g. --diff=1,2"
            sys.exit(1)
        diff.diff(version_list[0], version_list[1])
        return

    # Check/test the replay file
    if args.replay_file is None:
        print >> sys.stderr, ".S2Replay file not specified"
        sys.exit(1)

    archive = mpyq.MPQArchive(args.replay_file)

    logger = EventLogger()

    # Read the protocol header, this can be read with any protocol
    contents = archive.header['user_data_header']['content']
    header = versions.latest().decode_replay_header(contents)
    if args.header:
        logger.log(sys.stdout, header)

    # The header's baseBuild determines which protocol to use
    baseBuild = header['m_version']['m_baseBuild']
    try:
        protocol = versions.build(baseBuild)
    except:
        print >> sys.stderr, 'Unsupported base build: %d' % baseBuild
        sys.exit(1)

    # Print protocol details
    if args.details:
        contents = archive.read_file('replay.details')
        details = protocol.decode_replay_details(contents)
        logger.log(sys.stdout, details)

    # Print protocol init data
    if args.initdata:
        contents = archive.read_file('replay.initData')
        initdata = protocol.decode_replay_initdata(contents)
        logger.log(sys.stdout, initdata['m_syncLobbyState']['m_gameDescription']['m_cacheHandles'])
        logger.log(sys.stdout, initdata)

    # Print game events and/or game events stats
    if args.gameevents:
        contents = archive.read_file('replay.game.events')
        for event in protocol.decode_replay_game_events(contents):
            logger.log(sys.stdout, event)

    # Print message events
    if args.messageevents:
        contents = archive.read_file('replay.message.events')
        for event in protocol.decode_replay_message_events(contents):
            logger.log(sys.stdout, event)

    # Print tracker events
    if args.trackerevents:
        if hasattr(protocol, 'decode_replay_tracker_events'):
            contents = archive.read_file('replay.tracker.events')
            for event in protocol.decode_replay_tracker_events(contents):
                logger.log(sys.stdout, event)

    # Print attributes events
    if args.attributeevents:
        contents = archive.read_file('replay.attributes.events')
        attributes = protocol.decode_replay_attributes_events(contents)
        logger.log(sys.stdout, attributes)

    # Print stats
    if args.stats:
        logger.log_stats(sys.stderr)


if __name__ == '__main__':
    main()
