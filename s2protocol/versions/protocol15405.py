# Copyright (c) 2015-2017 Blizzard Entertainment
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

from s2protocol.decoders import *



# Decoding instructions for each protocol type.
typeinfos = [
    ('_int',[(0,7)]),  #0
    ('_int',[(0,4)]),  #1
    ('_int',[(0,6)]),  #2
    ('_int',[(0,14)]),  #3
    ('_int',[(0,22)]),  #4
    ('_int',[(0,32)]),  #5
    ('_choice',[(0,2),{0:('m_uint6',2),1:('m_uint14',3),2:('m_uint22',4),3:('m_uint32',5)}]),  #6
    ('_blob',[(0,8)]),  #7
    ('_int',[(0,8)]),  #8
    ('_struct',[[('m_flags',8,0),('m_major',8,1),('m_minor',8,2),('m_revision',8,3),('m_build',5,4),('m_baseBuild',5,5)]]),  #9
    ('_int',[(0,3)]),  #10
    ('_struct',[[('m_signature',7,0),('m_version',9,1),('m_type',10,2),('m_elapsedGameLoops',5,3)]]),  #11
    ('_fourcc',[]),  #12
    ('_blob',[(0,7)]),  #13
    ('_struct',[[('m_region',8,0),('m_programId',12,1),('m_realm',5,2),('m_name',13,3)]]),  #14
    ('_struct',[[('m_a',8,0),('m_r',8,1),('m_g',8,2),('m_b',8,3)]]),  #15
    ('_int',[(0,2)]),  #16
    ('_struct',[[('m_name',7,0),('m_toon',14,1),('m_race',7,2),('m_color',15,3),('m_control',8,4),('m_teamId',1,5),('m_handicap',0,6),('m_observe',16,7),('m_result',16,8)]]),  #17
    ('_array',[(0,5),17]),  #18
    ('_optional',[18]),  #19
    ('_blob',[(0,10)]),  #20
    ('_blob',[(0,11)]),  #21
    ('_struct',[[('m_file',21,0)]]),  #22
    ('_bool',[]),  #23
    ('_int',[(-9223372036854775808,64)]),  #24
    ('_blob',[(0,12)]),  #25
    ('_blob',[(40,0)]),  #26
    ('_array',[(0,4),26]),  #27
    ('_optional',[27]),  #28
    ('_struct',[[('m_playerList',19,0),('m_title',20,1),('m_difficulty',7,2),('m_thumbnail',22,3),('m_isBlizzardMap',23,4),('m_timeUTC',24,5),('m_timeLocalOffset',24,6),('m_description',25,7),('m_imageFilePath',20,8),('m_mapFileName',20,9),('m_cacheHandles',28,10),('m_miniSave',23,11),('m_gameSpeed',10,12),('m_defaultDifficulty',2,13)]]),  #29
    ('_optional',[8]),  #30
    ('_struct',[[('m_race',30,-1)]]),  #31
    ('_struct',[[('m_name',7,-6),('m_randomSeed',5,-5),('m_racePreference',31,-4),('m_testMap',23,-3),('m_testAuto',23,-2),('m_observe',16,-1)]]),  #32
    ('_array',[(0,5),32]),  #33
    ('_struct',[[('m_lockTeams',23,-11),('m_teamsTogether',23,-10),('m_advancedSharedControl',23,-9),('m_randomRaces',23,-8),('m_battleNet',23,-7),('m_amm',23,-6),('m_ranked',23,-5),('m_noVictoryOrDefeat',23,-4),('m_fog',16,-3),('m_observers',16,-2),('m_userDifficulty',16,-1)]]),  #34
    ('_int',[(0,5)]),  #35
    ('_int',[(1,4)]),  #36
    ('_int',[(1,5)]),  #37
    ('_int',[(1,8)]),  #38
    ('_bitarray',[(0,6)]),  #39
    ('_bitarray',[(0,8)]),  #40
    ('_bitarray',[(0,2)]),  #41
    ('_struct',[[('m_allowedColors',39,-5),('m_allowedRaces',40,-4),('m_allowedDifficulty',39,-3),('m_allowedControls',40,-2),('m_allowedObserveTypes',41,-1)]]),  #42
    ('_array',[(0,5),42]),  #43
    ('_struct',[[('m_randomValue',5,-21),('m_gameCacheName',20,-20),('m_gameOptions',34,-19),('m_gameSpeed',10,-18),('m_gameType',10,-17),('m_maxUsers',35,-16),('m_maxObservers',35,-15),('m_maxPlayers',1,-14),('m_maxTeams',36,-13),('m_maxColors',37,-12),('m_maxRaces',38,-11),('m_maxControls',38,-10),('m_mapSizeX',8,-9),('m_mapSizeY',8,-8),('m_mapFileSyncChecksum',5,-7),('m_mapFileName',20,-6),('m_modFileSyncChecksum',5,-5),('m_slotDescriptions',43,-4),('m_defaultDifficulty',2,-3),('m_cacheHandles',27,-2),('m_isBlizzardMap',23,-1)]]),  #44
    ('_optional',[1]),  #45
    ('_optional',[35]),  #46
    ('_struct',[[('m_color',46,-1)]]),  #47
    ('_int',[(0,16)]),  #48
    ('_array',[(0,5),48]),  #49
    ('_struct',[[('m_control',8,-9),('m_userId',45,-8),('m_teamId',1,-7),('m_colorPref',47,-6),('m_racePref',31,-5),('m_difficulty',2,-4),('m_handicap',0,-3),('m_observe',16,-2),('m_rewards',49,-1)]]),  #50
    ('_array',[(0,5),50]),  #51
    ('_struct',[[('m_phase',10,-9),('m_maxUsers',35,-8),('m_maxObservers',35,-7),('m_slots',51,-6),('m_randomSeed',5,-5),('m_hostUserId',45,-4),('m_isSinglePlayer',23,-3),('m_gameDuration',5,-2),('m_defaultDifficulty',2,-1)]]),  #52
    ('_struct',[[('m_userInitialData',33,-3),('m_gameDescription',44,-2),('m_lobbyState',52,-1)]]),  #53
    ('_struct',[[('m_syncLobbyState',53,-1)]]),  #54
    ('_struct',[[('m_name',13,-5)]]),  #55
    ('_blob',[(0,6)]),  #56
    ('_struct',[[('m_name',56,-5)]]),  #57
    ('_struct',[[('m_name',56,-7),('m_type',5,-6),('m_data',13,-5)]]),  #58
    ('_struct',[[('m_type',5,-7),('m_name',56,-6),('m_data',25,-5)]]),  #59
    ('_struct',[[('m_developmentCheatsEnabled',23,-8),('m_multiplayerCheatsEnabled',23,-7),('m_syncChecksummingEnabled',23,-6),('m_isMapToMapTransition',23,-5)]]),  #60
    ('_struct',[[]]),  #61
    ('_struct',[[('m_fileName',20,-9),('m_automatic',23,-8),('m_overwrite',23,-7),('m_name',7,-6),('m_description',20,-5)]]),  #62
    ('_int',[(-2147483648,32)]),  #63
    ('_struct',[[('x',63,-2),('y',63,-1)]]),  #64
    ('_struct',[[('m_point',64,-4),('m_time',63,-3),('m_verb',20,-2),('m_arguments',20,-1)]]),  #65
    ('_struct',[[('m_data',65,-5)]]),  #66
    ('_struct',[[('x',63,-3),('y',63,-2),('z',63,-1)]]),  #67
    ('_struct',[[('m_cmdFlags',5,-15),('m_abilLink',48,-14),('m_abilCmdIndex',8,-13),('m_abilCmdData',8,-12),('m_targetUnitFlags',8,-11),('m_targetUnitTimer',8,-10),('m_otherUnit',5,-9),('m_targetUnitTag',5,-8),('m_targetUnitSnapshotUnitLink',48,-7),('m_targetUnitSnapshotPlayerId',45,-6),('m_targetPoint',67,-5)]]),  #68
    ('_struct',[[('__parent',40,-1)]]),  #69
    ('_struct',[[('m_unitLink',48,-3),('m_intraSubgroupPriority',8,-2),('m_count',8,-1)]]),  #70
    ('_array',[(0,8),70]),  #71
    ('_array',[(0,8),5]),  #72
    ('_struct',[[('m_subgroupIndex',8,-4),('m_removeMask',69,-3),('m_addSubgroups',71,-2),('m_addUnitTags',72,-1)]]),  #73
    ('_struct',[[('m_controlGroupId',1,-6),('m_delta',73,-5)]]),  #74
    ('_struct',[[('m_controlGroupIndex',1,-7),('m_controlGroupUpdate',16,-6),('m_mask',69,-5)]]),  #75
    ('_struct',[[('m_count',8,-6),('m_subgroupCount',8,-5),('m_activeSubgroupIndex',8,-4),('m_unitTagsChecksum',5,-3),('m_subgroupIndicesChecksum',5,-2),('m_subgroupsChecksum',5,-1)]]),  #76
    ('_struct',[[('m_controlGroupId',1,-6),('m_selectionSyncData',76,-5)]]),  #77
    ('_array',[(0,3),63]),  #78
    ('_struct',[[('m_recipientId',1,-6),('m_resources',78,-5)]]),  #79
    ('_struct',[[('m_chatMessage',20,-5)]]),  #80
    ('_int',[(-128,8)]),  #81
    ('_struct',[[('m_beacon',81,-11),('m_ally',81,-10),('m_autocast',81,-9),('m_targetUnitTag',5,-8),('m_targetUnitSnapshotUnitLink',48,-7),('m_targetUnitSnapshotPlayerId',45,-6),('m_targetPoint',67,-5)]]),  #82
    ('_struct',[[('m_speed',10,-5)]]),  #83
    ('_struct',[[('m_delta',81,-5)]]),  #84
    ('_struct',[[('m_verb',20,-6),('m_arguments',20,-5)]]),  #85
    ('_struct',[[('m_alliance',5,-6),('m_control',5,-5)]]),  #86
    ('_struct',[[('m_unitTag',5,-5)]]),  #87
    ('_struct',[[('m_unitTag',5,-6),('m_flags',8,-5)]]),  #88
    ('_struct',[[('m_conversationId',63,-6),('m_replyId',63,-5)]]),  #89
    ('_struct',[[('m_purchaseItemId',63,-5)]]),  #90
    ('_struct',[[('m_difficultyLevel',63,-5)]]),  #91
    ('_null',[]),  #92
    ('_choice',[(0,3),{0:('None',92),1:('Checked',23),2:('ValueChanged',5),3:('SelectionChanged',63),4:('TextChanged',21)}]),  #93
    ('_struct',[[('m_controlId',63,-7),('m_eventType',63,-6),('m_eventData',93,-5)]]),  #94
    ('_struct',[[('m_soundHash',5,-6),('m_length',5,-5)]]),  #95
    ('_struct',[[('m_soundHash',72,-2),('m_length',72,-1)]]),  #96
    ('_struct',[[('m_syncInfo',96,-5)]]),  #97
    ('_struct',[[('m_sound',5,-5)]]),  #98
    ('_struct',[[('m_transmissionId',63,-5)]]),  #99
    ('_struct',[[('m_target',64,-8),('m_distance',63,-7),('m_pitch',63,-6),('m_yaw',63,-5)]]),  #100
    ('_int',[(0,1)]),  #101
    ('_struct',[[('m_skipType',101,-5)]]),  #102
    ('_struct',[[('m_button',5,-11),('m_down',23,-10),('m_posXUI',5,-9),('m_posYUI',5,-8),('m_posXWorld',63,-7),('m_posYWorld',63,-6),('m_posZWorld',63,-5)]]),  #103
    ('_struct',[[('m_soundtrack',5,-5)]]),  #104
    ('_struct',[[('m_planetId',63,-5)]]),  #105
    ('_struct',[[('m_key',81,-6),('m_flags',81,-5)]]),  #106
    ('_struct',[[('m_resources',78,-5)]]),  #107
    ('_struct',[[('m_fulfillRequestId',63,-5)]]),  #108
    ('_struct',[[('m_cancelRequestId',63,-5)]]),  #109
    ('_struct',[[('m_researchItemId',63,-5)]]),  #110
    ('_struct',[[('m_laggingPlayerId',1,-5)]]),  #111
    ('_struct',[[('m_mercenaryId',63,-5)]]),  #112
    ('_struct',[[('m_battleReportId',63,-6),('m_difficultyLevel',63,-5)]]),  #113
    ('_struct',[[('m_battleReportId',63,-5)]]),  #114
    ('_struct',[[('m_decrementMs',5,-5)]]),  #115
    ('_struct',[[('m_portraitId',63,-5)]]),  #116
    ('_struct',[[('m_functionName',13,-5)]]),  #117
    ('_struct',[[('m_result',63,-5)]]),  #118
    ('_struct',[[('m_gameMenuItemIndex',63,-5)]]),  #119
    ('_struct',[[('m_reason',81,-5)]]),  #120
    ('_struct',[[('m_purchaseCategoryId',63,-5)]]),  #121
    ('_struct',[[('m_button',48,-5)]]),  #122
    ('_struct',[[('m_recipient',16,-3),('m_string',21,-2)]]),  #123
    ('_struct',[[('m_recipient',16,-3),('m_point',64,-2)]]),  #124
    ('_struct',[[('m_progress',63,-2)]]),  #125
]

# Map from protocol NNet.Game.*Event eventid to (typeid, name)
game_event_types = {
    5: (61, 'NNet.Game.SUserFinishedLoadingSyncEvent'),
    7: (55, 'NNet.Game.SBankFileEvent'),
    8: (57, 'NNet.Game.SBankSectionEvent'),
    9: (58, 'NNet.Game.SBankKeyEvent'),
    10: (59, 'NNet.Game.SBankValueEvent'),
    11: (60, 'NNet.Game.SUserOptionsEvent'),
    22: (62, 'NNet.Game.SSaveGameEvent'),
    23: (61, 'NNet.Game.SSaveGameDoneEvent'),
    25: (61, 'NNet.Game.SPlayerLeaveEvent'),
    26: (66, 'NNet.Game.SGameCheatEvent'),
    27: (68, 'NNet.Game.SCmdEvent'),
    28: (74, 'NNet.Game.SSelectionDeltaEvent'),
    29: (75, 'NNet.Game.SControlGroupUpdateEvent'),
    30: (77, 'NNet.Game.SSelectionSyncCheckEvent'),
    31: (79, 'NNet.Game.SResourceTradeEvent'),
    32: (80, 'NNet.Game.STriggerChatMessageEvent'),
    33: (82, 'NNet.Game.SAICommunicateEvent'),
    34: (83, 'NNet.Game.SSetAbsoluteGameSpeedEvent'),
    35: (84, 'NNet.Game.SAddAbsoluteGameSpeedEvent'),
    37: (85, 'NNet.Game.SBroadcastCheatEvent'),
    38: (86, 'NNet.Game.SAllianceEvent'),
    39: (87, 'NNet.Game.SUnitClickEvent'),
    40: (88, 'NNet.Game.SUnitHighlightEvent'),
    41: (89, 'NNet.Game.STriggerReplySelectedEvent'),
    44: (61, 'NNet.Game.STriggerSkippedEvent'),
    45: (95, 'NNet.Game.STriggerSoundLengthQueryEvent'),
    46: (98, 'NNet.Game.STriggerSoundOffsetEvent'),
    47: (99, 'NNet.Game.STriggerTransmissionOffsetEvent'),
    48: (99, 'NNet.Game.STriggerTransmissionCompleteEvent'),
    49: (100, 'NNet.Game.SCameraUpdateEvent'),
    50: (61, 'NNet.Game.STriggerAbortMissionEvent'),
    51: (90, 'NNet.Game.STriggerPurchaseMadeEvent'),
    52: (61, 'NNet.Game.STriggerPurchaseExitEvent'),
    53: (91, 'NNet.Game.STriggerPlanetMissionLaunchedEvent'),
    54: (61, 'NNet.Game.STriggerPlanetPanelCanceledEvent'),
    55: (94, 'NNet.Game.STriggerDialogControlEvent'),
    56: (97, 'NNet.Game.STriggerSoundLengthSyncEvent'),
    57: (102, 'NNet.Game.STriggerConversationSkippedEvent'),
    58: (103, 'NNet.Game.STriggerMouseClickedEvent'),
    63: (61, 'NNet.Game.STriggerPlanetPanelReplayEvent'),
    64: (104, 'NNet.Game.STriggerSoundtrackDoneEvent'),
    65: (105, 'NNet.Game.STriggerPlanetMissionSelectedEvent'),
    66: (106, 'NNet.Game.STriggerKeyPressedEvent'),
    67: (117, 'NNet.Game.STriggerMovieFunctionEvent'),
    68: (61, 'NNet.Game.STriggerPlanetPanelBirthCompleteEvent'),
    69: (61, 'NNet.Game.STriggerPlanetPanelDeathCompleteEvent'),
    70: (107, 'NNet.Game.SResourceRequestEvent'),
    71: (108, 'NNet.Game.SResourceRequestFulfillEvent'),
    72: (109, 'NNet.Game.SResourceRequestCancelEvent'),
    73: (61, 'NNet.Game.STriggerResearchPanelExitEvent'),
    74: (61, 'NNet.Game.STriggerResearchPanelPurchaseEvent'),
    75: (110, 'NNet.Game.STriggerResearchPanelSelectionChangedEvent'),
    76: (111, 'NNet.Game.SLagMessageEvent'),
    77: (61, 'NNet.Game.STriggerMercenaryPanelExitEvent'),
    78: (61, 'NNet.Game.STriggerMercenaryPanelPurchaseEvent'),
    79: (112, 'NNet.Game.STriggerMercenaryPanelSelectionChangedEvent'),
    80: (61, 'NNet.Game.STriggerVictoryPanelExitEvent'),
    81: (61, 'NNet.Game.STriggerBattleReportPanelExitEvent'),
    82: (113, 'NNet.Game.STriggerBattleReportPanelPlayMissionEvent'),
    83: (114, 'NNet.Game.STriggerBattleReportPanelPlaySceneEvent'),
    84: (114, 'NNet.Game.STriggerBattleReportPanelSelectionChangedEvent'),
    85: (91, 'NNet.Game.STriggerVictoryPanelPlayMissionAgainEvent'),
    86: (61, 'NNet.Game.STriggerMovieStartedEvent'),
    87: (61, 'NNet.Game.STriggerMovieFinishedEvent'),
    88: (115, 'NNet.Game.SDecrementGameTimeRemainingEvent'),
    89: (116, 'NNet.Game.STriggerPortraitLoadedEvent'),
    90: (118, 'NNet.Game.STriggerCustomDialogDismissedEvent'),
    91: (119, 'NNet.Game.STriggerGameMenuItemSelectedEvent'),
    92: (120, 'NNet.Game.STriggerCameraMoveEvent'),
    93: (90, 'NNet.Game.STriggerPurchasePanelSelectedPurchaseItemChangedEvent'),
    94: (121, 'NNet.Game.STriggerPurchasePanelSelectedPurchaseCategoryChangedEvent'),
    95: (122, 'NNet.Game.STriggerButtonPressedEvent'),
    96: (61, 'NNet.Game.STriggerGameCreditsFinishedEvent'),
}

# The typeid of the NNet.Game.EEventId enum.
game_eventid_typeid = 0

# Map from protocol NNet.Game.*Message eventid to (typeid, name)
message_event_types = {
    0: (123, 'NNet.Game.SChatMessage'),
    1: (124, 'NNet.Game.SPingMessage'),
    2: (125, 'NNet.Game.SLoadingProgressMessage'),
}

# The typeid of the NNet.Game.EMessageId enum.
message_eventid_typeid = 1

# Map from protocol NNet.Replay.Tracker.*Event eventid to (typeid, name)
tracker_event_types = {
}

# NOTE: older builds may not support some types and the generated methods
# may fail to function properly, if specific backwards compatibility is 
# needed these values should be tested against for None

# The typeid of the NNet.Replay.Tracker.EEventId enum.
tracker_eventid_typeid = None

# The typeid of NNet.SVarUint32 (the type used to encode gameloop deltas).
svaruint32_typeid = 6

# The typeid of NNet.Replay.SGameUserId (the type used to encode player ids).
replay_userid_typeid = None

# The typeid of NNet.Replay.SHeader (the type used to store replay game version and length).
replay_header_typeid = 11

# The typeid of NNet.Game.SDetails (the type used to store overall replay details).
game_details_typeid = 29

# The typeid of NNet.Replay.SInitData (the type used to store the inital lobby).
replay_initdata_typeid = 54


def _varuint32_value(value):
    # Returns the numeric value from a SVarUint32 instance.
    for v in value.values():
        return v
    return 0


def _decode_event_stream(decoder, eventid_typeid, event_types, decode_user_id):
    # Decodes events prefixed with a gameloop and possibly userid
    gameloop = 0
    while not decoder.done():
        start_bits = decoder.used_bits()

        # decode the gameloop delta before each event
        delta = _varuint32_value(decoder.instance(svaruint32_typeid))
        gameloop += delta

        # decode the userid before each event
        if decode_user_id:
            userid = decoder.instance(replay_userid_typeid)

        # decode the event id
        eventid = decoder.instance(eventid_typeid)
        typeid, typename = event_types.get(eventid, (None, None))
        if typeid is None:
            raise CorruptedError('eventid({}) at {}'.format(eventid, decoder))

        # decode the event struct instance
        event = decoder.instance(typeid)
        event['_event'] = typename
        event['_eventid'] = eventid

        #  insert gameloop and userid
        event['_gameloop'] = gameloop
        if decode_user_id:
            event['_userid'] = userid

        # the next event is byte aligned
        decoder.byte_align()

        # insert bits used in stream
        event['_bits'] = decoder.used_bits() - start_bits

        yield event


def decode_replay_game_events(contents):
    """Decodes and yields each game event from the contents byte string."""
    decoder = BitPackedDecoder(contents, typeinfos)
    for event in _decode_event_stream(decoder,
                                      game_eventid_typeid,
                                      game_event_types,
                                      decode_user_id=True):
        yield event


def decode_replay_message_events(contents):
    """Decodes and yields each message event from the contents byte string."""
    decoder = BitPackedDecoder(contents, typeinfos)
    for event in _decode_event_stream(decoder,
                                      message_eventid_typeid,
                                      message_event_types,
                                      decode_user_id=True):
        yield event


def decode_replay_tracker_events(contents):
    """Decodes and yields each tracker event from the contents byte string."""
    decoder = VersionedDecoder(contents, typeinfos)
    for event in _decode_event_stream(decoder,
                                      tracker_eventid_typeid,
                                      tracker_event_types,
                                      decode_user_id=False):
        yield event


def decode_replay_header(contents):
    """Decodes and return the replay header from the contents byte string."""
    decoder = VersionedDecoder(contents, typeinfos)
    return decoder.instance(replay_header_typeid)


def decode_replay_details(contents):
    """Decodes and returns the game details from the contents byte string."""
    decoder = VersionedDecoder(contents, typeinfos)
    return decoder.instance(game_details_typeid)


def decode_replay_initdata(contents):
    """Decodes and return the replay init data from the contents byte string."""
    decoder = BitPackedDecoder(contents, typeinfos)
    return decoder.instance(replay_initdata_typeid)


def decode_replay_attributes_events(contents):
    """Decodes and yields each attribute from the contents byte string."""
    buffer = BitPackedBuffer(contents, 'little')
    attributes = {}
    if not buffer.done():
        attributes['source'] = buffer.read_bits(8)
        attributes['mapNamespace'] = buffer.read_bits(32)
        count = buffer.read_bits(32)
        attributes['scopes'] = {}
        while not buffer.done():
            value = {}
            value['namespace'] = buffer.read_bits(32)
            value['attrid'] = attrid = buffer.read_bits(32)
            scope = buffer.read_bits(8)
            value['value'] = buffer.read_aligned_bytes(4)[::-1].strip(b'\x00')
            if not scope in attributes['scopes']:
                attributes['scopes'][scope] = {}
            if not attrid in attributes['scopes'][scope]:
                attributes['scopes'][scope][attrid] = []
            attributes['scopes'][scope][attrid].append(value)
    return attributes


def unit_tag(unitTagIndex, unitTagRecycle):
    return (unitTagIndex << 18) + unitTagRecycle


def unit_tag_index(unitTag):
    return (unitTag >> 18) & 0x00003fff


def unit_tag_recycle(unitTag):
    return (unitTag) & 0x0003ffff
