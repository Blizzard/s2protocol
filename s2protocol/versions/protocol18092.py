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
    ('_int',[(0,64)]),  #14
    ('_struct',[[('m_region',8,0),('m_programId',12,1),('m_realm',5,2),('m_name',13,3),('m_id',14,4)]]),  #15
    ('_struct',[[('m_a',8,0),('m_r',8,1),('m_g',8,2),('m_b',8,3)]]),  #16
    ('_int',[(0,2)]),  #17
    ('_struct',[[('m_name',7,0),('m_toon',15,1),('m_race',7,2),('m_color',16,3),('m_control',8,4),('m_teamId',1,5),('m_handicap',0,6),('m_observe',17,7),('m_result',17,8)]]),  #18
    ('_array',[(0,5),18]),  #19
    ('_optional',[19]),  #20
    ('_blob',[(0,10)]),  #21
    ('_blob',[(0,11)]),  #22
    ('_struct',[[('m_file',22,0)]]),  #23
    ('_bool',[]),  #24
    ('_int',[(-9223372036854775808,64)]),  #25
    ('_blob',[(0,12)]),  #26
    ('_blob',[(40,0)]),  #27
    ('_array',[(0,4),27]),  #28
    ('_optional',[28]),  #29
    ('_struct',[[('m_playerList',20,0),('m_title',21,1),('m_difficulty',7,2),('m_thumbnail',23,3),('m_isBlizzardMap',24,4),('m_timeUTC',25,5),('m_timeLocalOffset',25,6),('m_description',26,7),('m_imageFilePath',22,8),('m_mapFileName',22,9),('m_cacheHandles',29,10),('m_miniSave',24,11),('m_gameSpeed',10,12),('m_defaultDifficulty',2,13)]]),  #30
    ('_optional',[8]),  #31
    ('_struct',[[('m_race',31,-1)]]),  #32
    ('_struct',[[('m_team',31,-1)]]),  #33
    ('_struct',[[('m_name',7,-7),('m_randomSeed',5,-6),('m_racePreference',32,-5),('m_teamPreference',33,-4),('m_testMap',24,-3),('m_testAuto',24,-2),('m_observe',17,-1)]]),  #34
    ('_array',[(0,5),34]),  #35
    ('_struct',[[('m_lockTeams',24,-11),('m_teamsTogether',24,-10),('m_advancedSharedControl',24,-9),('m_randomRaces',24,-8),('m_battleNet',24,-7),('m_amm',24,-6),('m_ranked',24,-5),('m_noVictoryOrDefeat',24,-4),('m_fog',17,-3),('m_observers',17,-2),('m_userDifficulty',17,-1)]]),  #36
    ('_int',[(0,5)]),  #37
    ('_int',[(1,4)]),  #38
    ('_int',[(1,8)]),  #39
    ('_bitarray',[(0,6)]),  #40
    ('_bitarray',[(0,8)]),  #41
    ('_bitarray',[(0,2)]),  #42
    ('_struct',[[('m_allowedColors',40,-5),('m_allowedRaces',41,-4),('m_allowedDifficulty',40,-3),('m_allowedControls',41,-2),('m_allowedObserveTypes',42,-1)]]),  #43
    ('_array',[(0,5),43]),  #44
    ('_struct',[[('m_randomValue',5,-23),('m_gameCacheName',21,-22),('m_gameOptions',36,-21),('m_gameSpeed',10,-20),('m_gameType',10,-19),('m_maxUsers',37,-18),('m_maxObservers',37,-17),('m_maxPlayers',37,-16),('m_maxTeams',38,-15),('m_maxColors',2,-14),('m_maxRaces',39,-13),('m_maxControls',39,-12),('m_mapSizeX',8,-11),('m_mapSizeY',8,-10),('m_mapFileSyncChecksum',5,-9),('m_mapFileName',22,-8),('m_mapAuthorName',7,-7),('m_modFileSyncChecksum',5,-6),('m_slotDescriptions',44,-5),('m_defaultDifficulty',2,-4),('m_cacheHandles',28,-3),('m_isBlizzardMap',24,-2),('m_isPremadeFFA',24,-1)]]),  #45
    ('_optional',[1]),  #46
    ('_optional',[37]),  #47
    ('_struct',[[('m_color',47,-1)]]),  #48
    ('_array',[(0,5),5]),  #49
    ('_struct',[[('m_control',8,-10),('m_userId',46,-9),('m_teamId',1,-8),('m_colorPref',48,-7),('m_racePref',32,-6),('m_difficulty',2,-5),('m_handicap',0,-4),('m_observe',17,-3),('m_rewards',49,-2),('m_toonHandle',13,-1)]]),  #50
    ('_array',[(0,5),50]),  #51
    ('_struct',[[('m_phase',10,-9),('m_maxUsers',37,-8),('m_maxObservers',37,-7),('m_slots',51,-6),('m_randomSeed',5,-5),('m_hostUserId',46,-4),('m_isSinglePlayer',24,-3),('m_gameDuration',5,-2),('m_defaultDifficulty',2,-1)]]),  #52
    ('_struct',[[('m_userInitialData',35,-3),('m_gameDescription',45,-2),('m_lobbyState',52,-1)]]),  #53
    ('_struct',[[('m_syncLobbyState',53,-1)]]),  #54
    ('_struct',[[('m_name',13,-5)]]),  #55
    ('_blob',[(0,6)]),  #56
    ('_struct',[[('m_name',56,-5)]]),  #57
    ('_struct',[[('m_name',56,-7),('m_type',5,-6),('m_data',13,-5)]]),  #58
    ('_struct',[[('m_type',5,-7),('m_name',56,-6),('m_data',26,-5)]]),  #59
    ('_array',[(0,5),8]),  #60
    ('_struct',[[('m_signature',60,-5)]]),  #61
    ('_struct',[[('m_developmentCheatsEnabled',24,-8),('m_multiplayerCheatsEnabled',24,-7),('m_syncChecksummingEnabled',24,-6),('m_isMapToMapTransition',24,-5)]]),  #62
    ('_struct',[[]]),  #63
    ('_struct',[[('m_fileName',22,-9),('m_automatic',24,-8),('m_overwrite',24,-7),('m_name',7,-6),('m_description',21,-5)]]),  #64
    ('_int',[(-2147483648,32)]),  #65
    ('_struct',[[('x',65,-2),('y',65,-1)]]),  #66
    ('_struct',[[('m_point',66,-4),('m_time',65,-3),('m_verb',21,-2),('m_arguments',21,-1)]]),  #67
    ('_struct',[[('m_data',67,-5)]]),  #68
    ('_int',[(0,17)]),  #69
    ('_int',[(0,16)]),  #70
    ('_struct',[[('m_abilLink',70,-3),('m_abilCmdIndex',37,-2),('m_abilCmdData',31,-1)]]),  #71
    ('_optional',[71]),  #72
    ('_null',[]),  #73
    ('_int',[(0,20)]),  #74
    ('_struct',[[('x',74,-3),('y',74,-2),('z',65,-1)]]),  #75
    ('_struct',[[('m_targetUnitFlags',8,-6),('m_timer',8,-5),('m_tag',5,-4),('m_snapshotUnitLink',70,-3),('m_snapshotPlayerId',46,-2),('m_snapshotPoint',75,-1)]]),  #76
    ('_choice',[(0,2),{0:('None',73),1:('TargetPoint',75),2:('TargetUnit',76),3:('Data',5)}]),  #77
    ('_optional',[5]),  #78
    ('_struct',[[('m_cmdFlags',69,-8),('m_abil',72,-7),('m_data',77,-6),('m_otherUnit',78,-5)]]),  #79
    ('_array',[(0,8),8]),  #80
    ('_choice',[(0,2),{0:('None',73),1:('Mask',41),2:('OneIndices',80),3:('ZeroIndices',80)}]),  #81
    ('_struct',[[('m_unitLink',70,-3),('m_intraSubgroupPriority',8,-2),('m_count',8,-1)]]),  #82
    ('_array',[(0,8),82]),  #83
    ('_array',[(0,8),5]),  #84
    ('_struct',[[('m_subgroupIndex',8,-4),('m_removeMask',81,-3),('m_addSubgroups',83,-2),('m_addUnitTags',84,-1)]]),  #85
    ('_struct',[[('m_controlGroupId',1,-6),('m_delta',85,-5)]]),  #86
    ('_struct',[[('m_controlGroupIndex',1,-7),('m_controlGroupUpdate',17,-6),('m_mask',81,-5)]]),  #87
    ('_struct',[[('m_count',8,-6),('m_subgroupCount',8,-5),('m_activeSubgroupIndex',8,-4),('m_unitTagsChecksum',5,-3),('m_subgroupIndicesChecksum',5,-2),('m_subgroupsChecksum',5,-1)]]),  #88
    ('_struct',[[('m_controlGroupId',1,-6),('m_selectionSyncData',88,-5)]]),  #89
    ('_array',[(0,3),65]),  #90
    ('_struct',[[('m_recipientId',1,-6),('m_resources',90,-5)]]),  #91
    ('_struct',[[('m_chatMessage',21,-5)]]),  #92
    ('_int',[(-128,8)]),  #93
    ('_struct',[[('x',65,-3),('y',65,-2),('z',65,-1)]]),  #94
    ('_struct',[[('m_beacon',93,-11),('m_ally',93,-10),('m_autocast',93,-9),('m_targetUnitTag',5,-8),('m_targetUnitSnapshotUnitLink',70,-7),('m_targetUnitSnapshotPlayerId',46,-6),('m_targetPoint',94,-5)]]),  #95
    ('_struct',[[('m_speed',10,-5)]]),  #96
    ('_struct',[[('m_delta',93,-5)]]),  #97
    ('_struct',[[('m_verb',21,-6),('m_arguments',21,-5)]]),  #98
    ('_struct',[[('m_alliance',5,-6),('m_control',5,-5)]]),  #99
    ('_struct',[[('m_unitTag',5,-5)]]),  #100
    ('_struct',[[('m_unitTag',5,-6),('m_flags',8,-5)]]),  #101
    ('_struct',[[('m_conversationId',65,-6),('m_replyId',65,-5)]]),  #102
    ('_struct',[[('m_purchaseItemId',65,-5)]]),  #103
    ('_struct',[[('m_difficultyLevel',65,-5)]]),  #104
    ('_choice',[(0,3),{0:('None',73),1:('Checked',24),2:('ValueChanged',5),3:('SelectionChanged',65),4:('TextChanged',22)}]),  #105
    ('_struct',[[('m_controlId',65,-7),('m_eventType',65,-6),('m_eventData',105,-5)]]),  #106
    ('_struct',[[('m_soundHash',5,-6),('m_length',5,-5)]]),  #107
    ('_struct',[[('m_soundHash',84,-2),('m_length',84,-1)]]),  #108
    ('_struct',[[('m_syncInfo',108,-5)]]),  #109
    ('_struct',[[('m_sound',5,-5)]]),  #110
    ('_struct',[[('m_transmissionId',65,-5)]]),  #111
    ('_struct',[[('x',70,-2),('y',70,-1)]]),  #112
    ('_optional',[70]),  #113
    ('_struct',[[('m_target',112,-8),('m_distance',113,-7),('m_pitch',113,-6),('m_yaw',113,-5)]]),  #114
    ('_int',[(0,1)]),  #115
    ('_struct',[[('m_skipType',115,-5)]]),  #116
    ('_int',[(0,11)]),  #117
    ('_struct',[[('x',117,-2),('y',117,-1)]]),  #118
    ('_struct',[[('m_button',5,-8),('m_down',24,-7),('m_posUI',118,-6),('m_posWorld',75,-5)]]),  #119
    ('_struct',[[('m_posUI',118,-6),('m_posWorld',75,-5)]]),  #120
    ('_struct',[[('m_soundtrack',5,-5)]]),  #121
    ('_struct',[[('m_planetId',65,-5)]]),  #122
    ('_struct',[[('m_key',93,-6),('m_flags',93,-5)]]),  #123
    ('_struct',[[('m_resources',90,-5)]]),  #124
    ('_struct',[[('m_fulfillRequestId',65,-5)]]),  #125
    ('_struct',[[('m_cancelRequestId',65,-5)]]),  #126
    ('_struct',[[('m_researchItemId',65,-5)]]),  #127
    ('_struct',[[('m_laggingPlayerId',1,-5)]]),  #128
    ('_struct',[[('m_mercenaryId',65,-5)]]),  #129
    ('_struct',[[('m_battleReportId',65,-6),('m_difficultyLevel',65,-5)]]),  #130
    ('_struct',[[('m_battleReportId',65,-5)]]),  #131
    ('_int',[(0,19)]),  #132
    ('_struct',[[('m_decrementMs',132,-5)]]),  #133
    ('_struct',[[('m_portraitId',65,-5)]]),  #134
    ('_struct',[[('m_functionName',13,-5)]]),  #135
    ('_struct',[[('m_result',65,-5)]]),  #136
    ('_struct',[[('m_gameMenuItemIndex',65,-5)]]),  #137
    ('_struct',[[('m_reason',93,-5)]]),  #138
    ('_struct',[[('m_purchaseCategoryId',65,-5)]]),  #139
    ('_struct',[[('m_button',70,-5)]]),  #140
    ('_struct',[[('m_recipient',17,-3),('m_string',22,-2)]]),  #141
    ('_struct',[[('m_recipient',17,-3),('m_point',66,-2)]]),  #142
    ('_struct',[[('m_progress',65,-2)]]),  #143
]

# Map from protocol NNet.Game.*Event eventid to (typeid, name)
game_event_types = {
    5: (63, 'NNet.Game.SUserFinishedLoadingSyncEvent'),
    7: (55, 'NNet.Game.SBankFileEvent'),
    8: (57, 'NNet.Game.SBankSectionEvent'),
    9: (58, 'NNet.Game.SBankKeyEvent'),
    10: (59, 'NNet.Game.SBankValueEvent'),
    11: (61, 'NNet.Game.SBankSignatureEvent'),
    12: (62, 'NNet.Game.SUserOptionsEvent'),
    22: (64, 'NNet.Game.SSaveGameEvent'),
    23: (63, 'NNet.Game.SSaveGameDoneEvent'),
    25: (63, 'NNet.Game.SPlayerLeaveEvent'),
    26: (68, 'NNet.Game.SGameCheatEvent'),
    27: (79, 'NNet.Game.SCmdEvent'),
    28: (86, 'NNet.Game.SSelectionDeltaEvent'),
    29: (87, 'NNet.Game.SControlGroupUpdateEvent'),
    30: (89, 'NNet.Game.SSelectionSyncCheckEvent'),
    31: (91, 'NNet.Game.SResourceTradeEvent'),
    32: (92, 'NNet.Game.STriggerChatMessageEvent'),
    33: (95, 'NNet.Game.SAICommunicateEvent'),
    34: (96, 'NNet.Game.SSetAbsoluteGameSpeedEvent'),
    35: (97, 'NNet.Game.SAddAbsoluteGameSpeedEvent'),
    37: (98, 'NNet.Game.SBroadcastCheatEvent'),
    38: (99, 'NNet.Game.SAllianceEvent'),
    39: (100, 'NNet.Game.SUnitClickEvent'),
    40: (101, 'NNet.Game.SUnitHighlightEvent'),
    41: (102, 'NNet.Game.STriggerReplySelectedEvent'),
    44: (63, 'NNet.Game.STriggerSkippedEvent'),
    45: (107, 'NNet.Game.STriggerSoundLengthQueryEvent'),
    46: (110, 'NNet.Game.STriggerSoundOffsetEvent'),
    47: (111, 'NNet.Game.STriggerTransmissionOffsetEvent'),
    48: (111, 'NNet.Game.STriggerTransmissionCompleteEvent'),
    49: (114, 'NNet.Game.SCameraUpdateEvent'),
    50: (63, 'NNet.Game.STriggerAbortMissionEvent'),
    51: (103, 'NNet.Game.STriggerPurchaseMadeEvent'),
    52: (63, 'NNet.Game.STriggerPurchaseExitEvent'),
    53: (104, 'NNet.Game.STriggerPlanetMissionLaunchedEvent'),
    54: (63, 'NNet.Game.STriggerPlanetPanelCanceledEvent'),
    55: (106, 'NNet.Game.STriggerDialogControlEvent'),
    56: (109, 'NNet.Game.STriggerSoundLengthSyncEvent'),
    57: (116, 'NNet.Game.STriggerConversationSkippedEvent'),
    58: (119, 'NNet.Game.STriggerMouseClickedEvent'),
    59: (120, 'NNet.Game.STriggerMouseMovedEvent'),
    63: (63, 'NNet.Game.STriggerPlanetPanelReplayEvent'),
    64: (121, 'NNet.Game.STriggerSoundtrackDoneEvent'),
    65: (122, 'NNet.Game.STriggerPlanetMissionSelectedEvent'),
    66: (123, 'NNet.Game.STriggerKeyPressedEvent'),
    67: (135, 'NNet.Game.STriggerMovieFunctionEvent'),
    68: (63, 'NNet.Game.STriggerPlanetPanelBirthCompleteEvent'),
    69: (63, 'NNet.Game.STriggerPlanetPanelDeathCompleteEvent'),
    70: (124, 'NNet.Game.SResourceRequestEvent'),
    71: (125, 'NNet.Game.SResourceRequestFulfillEvent'),
    72: (126, 'NNet.Game.SResourceRequestCancelEvent'),
    73: (63, 'NNet.Game.STriggerResearchPanelExitEvent'),
    74: (63, 'NNet.Game.STriggerResearchPanelPurchaseEvent'),
    75: (127, 'NNet.Game.STriggerResearchPanelSelectionChangedEvent'),
    76: (128, 'NNet.Game.SLagMessageEvent'),
    77: (63, 'NNet.Game.STriggerMercenaryPanelExitEvent'),
    78: (63, 'NNet.Game.STriggerMercenaryPanelPurchaseEvent'),
    79: (129, 'NNet.Game.STriggerMercenaryPanelSelectionChangedEvent'),
    80: (63, 'NNet.Game.STriggerVictoryPanelExitEvent'),
    81: (63, 'NNet.Game.STriggerBattleReportPanelExitEvent'),
    82: (130, 'NNet.Game.STriggerBattleReportPanelPlayMissionEvent'),
    83: (131, 'NNet.Game.STriggerBattleReportPanelPlaySceneEvent'),
    84: (131, 'NNet.Game.STriggerBattleReportPanelSelectionChangedEvent'),
    85: (104, 'NNet.Game.STriggerVictoryPanelPlayMissionAgainEvent'),
    86: (63, 'NNet.Game.STriggerMovieStartedEvent'),
    87: (63, 'NNet.Game.STriggerMovieFinishedEvent'),
    88: (133, 'NNet.Game.SDecrementGameTimeRemainingEvent'),
    89: (134, 'NNet.Game.STriggerPortraitLoadedEvent'),
    90: (136, 'NNet.Game.STriggerCustomDialogDismissedEvent'),
    91: (137, 'NNet.Game.STriggerGameMenuItemSelectedEvent'),
    92: (138, 'NNet.Game.STriggerCameraMoveEvent'),
    93: (103, 'NNet.Game.STriggerPurchasePanelSelectedPurchaseItemChangedEvent'),
    94: (139, 'NNet.Game.STriggerPurchasePanelSelectedPurchaseCategoryChangedEvent'),
    95: (140, 'NNet.Game.STriggerButtonPressedEvent'),
    96: (63, 'NNet.Game.STriggerGameCreditsFinishedEvent'),
}

# The typeid of the NNet.Game.EEventId enum.
game_eventid_typeid = 0

# Map from protocol NNet.Game.*Message eventid to (typeid, name)
message_event_types = {
    0: (141, 'NNet.Game.SChatMessage'),
    1: (142, 'NNet.Game.SPingMessage'),
    2: (143, 'NNet.Game.SLoadingProgressMessage'),
    3: (63, 'NNet.Game.SServerPingMessage'),
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
game_details_typeid = 30

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
