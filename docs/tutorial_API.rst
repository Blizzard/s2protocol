Using the s2protocol API
=================================

If you're looking to do more than just look at a single replay's output once,
you'll want to explore the programmatic API. 

SC2Replay files are MPQ archives. MPQ archives are used by blizzard in several contexts. The SC2Replay archives contain mostly header/meta information and multiple files. The replay data itself is grouped and encoded in different files. With the mpyq package you can open and decode these archives and look inside:

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

	>>> contents = archive.header['user_data_header']['content']
	>>> from s2protocol import versions
	>>> header = versions.latest().decode_replay_header(contents)
	>>> baseBuild = header['m_version']['m_baseBuild']
	>>> protocol = versions.build(baseBuild)
	
	
The variable ``protocol`` now contains a decoder for the replay specific game version. You can now decode the files inside the archive correctly. For example to decode the game events you can do:

	>>> contents = archive.read_file('replay.game.events')
	>>> gameEvents = protocol.decode_replay_game_events(contents)

Or to get the ingame messages you can do:

	>>> contents = archive.read_file('replay.message.events')
	>>> messageEvents = protocol.decode_replay_message_events(contents)
	
	
Now you can perfom any operation you like on these objects. For example if you are just interested in ``NNet.Game.SCmdEvent`` you can filter the game events like this:

	>>> cmdEventList = []
	>>> for event in gameEvents:
	>>> 	if event['_event'] == 'NNet.Game.SCmdEvent':
	>>> 		cmdEventList.append(event)
	
Of course you always have the option to export your current selection as JSON to a textfile and use other environments or tools for your exploratory data analysis. To export your data to a JSON file you can do:

	>>> import json
	>>> json_data = json.dumps(cmdEventList, indent=4)
	>>> output_file = open("someJSONFile.json", "w")
	>>> output_file.write(json_data)
	>>> output_file.close()
