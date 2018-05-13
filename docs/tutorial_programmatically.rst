Using s2protocol Programmatically
=================================

If you're looking to do more than just look at a single replay's output once,
you'll want to explore the programmatic API. 

SC2Replay files are MPQ archives which are used by blizzard. These archives contain several files with replay information. With the mpyq package you can open and decode these archives and look inside:

	>>> import mpyq
	>>> archive = mpyq.MPQArchive('~/Desktop/my_pvp_replay.SC2Replay')
	
With an attached debugger you can now explore the archive or print out a list of all files inside the archive:
	
	>>> print archive.files
	
which returns: 
	
	* ``replay.attributes.events``
	* ``replay.details``
	* ``replay.details.backup``
	* ``replay.game.events``
	* ``replay.gamemetadata.json``
	* ``replay.initData``
	* ``replay.initData.backup``
	* ``replay.load.info``
	* ``replay.message.events``
	* ``replay.resumable.events``
	* ``replay.server.battlelobby``
	* ``replay.smartcam.events``
	* ``replay.sync.events``
	* ``replay.sync.history``
	* ``replay.tracker.events``

To decode any further information you need to determine the build version with which the replay was recorded. You can do this by accessing the header information and extract the build version from it:

	>>> from s2protocol import versions
	>>> header = versions.latest().decode_replay_header(contents)
	>>> baseBuild = header['m_version']['m_baseBuild']
	>>> protocol = versions.build(baseBuild)
	
	
The variable ``protocol`` now contains a decoder for the replay specific game version. Now you can decode the files inside the archive correctly. For example to decode the gameevents you can do:

	>>> contents = archive.read_file('replay.game.events')
	>>> gameEvents = protocol.decode_replay_game_events(contents)

To decode the ingame messages you can do:

	>>> contents = archive.read_file('replay.message.events')
	>>> messageEvents = protocol.decode_replay_message_events(contents)