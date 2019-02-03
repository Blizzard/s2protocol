Events
======

There are a lot of different event types used in SC2Replays. This list will cover some events but won´t claim any sort of completness. If you stumble across a game event not mentioned here please feel free to contribute.

Every event is a python dictionary. Each event contains the following keys:

	* ``_eventid``
	* ``_event`` 
	* ``_gameloop`` 
	* ``_userid``
	* ``_bits``


NNet.Game.SChatMessage
----------------------
	* ``m_string'`` - contains the chat message
	
	
NNet.Game.SCameraUpdateEvent
----------------------------
	* ``m_target`` - contains x and y coordinates
	* ``m_reason`` 
	* ``m_distance`` 
	* ``m_pitch`` 
	* ``m_follow`` 
	* ``m_yaw`` 
	
NNet.Game.SControlGroupUpdateEvent
----------------------------------
tbc

	
NNet.Game.SSelectionDeltaEvent
------------------------------
tbc


NNet.Game.SCmdEvent
-------------------
tbc