# S2 Protocol

[![Documentation Status](https://readthedocs.org/projects/s2protocol/badge/?version=latest)](http://s2protocol.readthedocs.io/en/latest/?badge=latest)

[![Build Status](https://travis-ci.org/Blizzard/s2protocol.svg?branch=master)](https://travis-ci.org/Blizzard/s2protocol)

s2protocol is a reference Python library and standalone tool to decode StarCraft II replay files into Python data structures.

Currently s2protocol can decode these structures and events:
* replay header
* game details
* replay init data
* game events
* message events
* tracker events

s2protocol can be used as a base-build-specific library to decode binary blobs, or it can be run as a standalone tool to pretty print information from supported replay files.

Note that s2protocol does not expose game balance information or provide any kind of high level analysis of replays; it's meant
to be just the first tool in the chain for your data mining application.

# Supported Versions

s2protocol supports all StarCraft II replay files that were written with retail versions of the game. The current plan is to support all future publicly released versions, including public betas.

# Tracker Events

Some notes on tracker events:
* Tracker events are new in version 2.0.8, they do not exist in replays recorded with older versions of the game.
* Convert unit tag index, recycle pairs into unit tags (as seen in game events) with protocol.unit_tag(index, recycle)
* Interpret the NNet.Replay.Tracker.SUnitPositionsEvent events like this:

```python
    unitIndex = event['m_firstUnitIndex']
    for i in range(0, len(event['m_items']), 3):
        unitIndex += event['m_items'][i + 0]
        x = event['m_items'][i + 1] * 4
        y = event['m_items'][i + 2] * 4
        # unit identified by unitIndex at the current event['_gameloop'] time is at approximate position (x, y)
```
* Only units that have inflicted or taken damage are mentioned in unit position events, and they occur periodically with a limit of 256 units mentioned per event.
* NNet.Replay.Tracker.SUnitInitEvent events appear for units under construction. When complete you'll see a NNet.Replay.Tracker.SUnitDoneEvent with the same unit tag.
* NNet.Replay.Tracker.SUnitBornEvent events appear for units that are created fully constructed.
* You may receive a NNet.Replay.Tracker.SUnitDiedEvent after either a UnitInit or UnitBorn event for the corresponding unit tag.
* In NNet.Replay.Tracker.SPlayerStatsEvent, m_scoreValueFoodUsed and m_scoreValueFoodMade are in fixed point (divide by 4096 for integer values). All other values are in integers.
* There's a known issue where revived units are not tracked, and placeholder units track death but not birth.

# License

Copyright (c) 2013 Blizzard Entertainment

Open sourced under the MIT license. See the included LICENSE file for more information.

# Acknowledgements

The standalone tool uses [mpyq](https://github.com/eagleflo/mpyq/) to read mopaq files.

Thanks to David Joerg and Graylin Kim of [GGTracker](http://www.ggtracker.com) for design feedback and beta-testing.

# Ports and Related Projects

There are unofficial ports of s2protocol (and the required MPQ parser) available in other languages:

### Go

This Go implementation is a standalone project for both the MPQ parser and the s2protocol implementation (also provide some higher level API):

**Go MPQ parser:** https://github.com/icza/mpq

**Go s2protocol:** https://github.com/icza/s2prot

### Java

This Java implementation is part of the open source [Scelight](https://github.com/icza/scelight) project (which is much more than just a replay parser, it also gives a high-level API):

**Java MPQ parser:** https://github.com/icza/scelight/tree/master/src-app-libs/hu/belicza/andras/mpq

**Java s2protocol:** https://github.com/icza/scelight/tree/master/src-app/hu/scelight/sc2/rep/s2prot
