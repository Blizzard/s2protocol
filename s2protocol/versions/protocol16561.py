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

from decoders import *


# Decoding instructions for each protocol type.
typeinfos = [
    ('_int',[(0,7)]),  #0
    ('_int',[(0,4)]),  #1
    ('_int',[(0,6)]),  #2
    ('_int',[(0,14)]),  #3
    ('_int',[(0,22)]),  #4
    ('_int',[(0,32)]),  #5
    ('_choice',[(0,2),{0:('m_uint6',2),1:('m_uint14',3),2:('m_uint22',4),3:('m_uint32',5)}]),  #6
    ('_int',[(0,5)]),  #7
    ('_struct',[[('m_playerId',7,-1)]]),  #8
    ('_blob',[(0,8)]),  #9
    ('_int',[(0,8)]),  #10
    ('_struct',[[('m_flags',10,0),('m_major',10,1),('m_minor',10,2),('m_revision',10,3),('m_build',5,4),('m_baseBuild',5,5)]]),  #11
    ('_int',[(0,3)]),  #12
    ('_struct',[[('m_signature',9,0),('m_version',11,1),('m_type',12,2),('m_elapsedGameLoops',5,3)]]),  #13
    ('_fourcc',[]),  #14
    ('_blob',[(0,7)]),  #15
    ('_int',[(0,64)]),  #16
    ('_struct',[[('m_region',10,0),('m_programId',14,1),('m_realm',5,2),('m_name',15,3),('m_id',16,4)]]),  #17
    ('_struct',[[('m_a',10,0),('m_r',10,1),('m_g',10,2),('m_b',10,3)]]),  #18
    ('_int',[(0,2)]),  #19
    ('_struct',[[('m_name',9,0),('m_toon',17,1),('m_race',9,2),('m_color',18,3),('m_control',10,4),('m_teamId',1,5),('m_handicap',0,6),('m_observe',19,7),('m_result',19,8)]]),  #20
    ('_array',[(0,5),20]),  #21
    ('_optional',[21]),  #22
    ('_blob',[(0,10)]),  #23
    ('_blob',[(0,11)]),  #24
    ('_struct',[[('m_file',24,0)]]),  #25
    ('_bool',[]),  #26
    ('_int',[(-9223372036854775808,64)]),  #27
    ('_blob',[(0,12)]),  #28
    ('_blob',[(40,0)]),  #29
    ('_array',[(0,4),29]),  #30
    ('_optional',[30]),  #31
    ('_struct',[[('m_playerList',22,0),('m_title',23,1),('m_difficulty',9,2),('m_thumbnail',25,3),('m_isBlizzardMap',26,4),('m_timeUTC',27,5),('m_timeLocalOffset',27,6),('m_description',28,7),('m_imageFilePath',24,8),('m_mapFileName',24,9),('m_cacheHandles',31,10),('m_miniSave',26,11),('m_gameSpeed',12,12),('m_defaultDifficulty',2,13)]]),  #32
    ('_optional',[10]),  #33
    ('_struct',[[('m_race',33,-1)]]),  #34
    ('_struct',[[('m_team',33,-1)]]),  #35
    ('_struct',[[('m_name',9,-7),('m_randomSeed',5,-6),('m_racePreference',34,-5),('m_teamPreference',35,-4),('m_testMap',26,-3),('m_testAuto',26,-2),('m_observe',19,-1)]]),  #36
    ('_array',[(0,5),36]),  #37
    ('_struct',[[('m_lockTeams',26,-11),('m_teamsTogether',26,-10),('m_advancedSharedControl',26,-9),('m_randomRaces',26,-8),('m_battleNet',26,-7),('m_amm',26,-6),('m_ranked',26,-5),('m_noVictoryOrDefeat',26,-4),('m_fog',19,-3),('m_observers',19,-2),('m_userDifficulty',19,-1)]]),  #38
    ('_int',[(1,4)]),  #39
    ('_int',[(1,5)]),  #40
    ('_int',[(1,8)]),  #41
    ('_bitarray',[(0,6)]),  #42
    ('_bitarray',[(0,8)]),  #43
    ('_bitarray',[(0,2)]),  #44
    ('_struct',[[('m_allowedColors',42,-5),('m_allowedRaces',43,-4),('m_allowedDifficulty',42,-3),('m_allowedControls',43,-2),('m_allowedObserveTypes',44,-1)]]),  #45
    ('_array',[(0,5),45]),  #46
    ('_struct',[[('m_randomValue',5,-23),('m_gameCacheName',23,-22),('m_gameOptions',38,-21),('m_gameSpeed',12,-20),('m_gameType',12,-19),('m_maxUsers',7,-18),('m_maxObservers',7,-17),('m_maxPlayers',7,-16),('m_maxTeams',39,-15),('m_maxColors',40,-14),('m_maxRaces',41,-13),('m_maxControls',41,-12),('m_mapSizeX',10,-11),('m_mapSizeY',10,-10),('m_mapFileSyncChecksum',5,-9),('m_mapFileName',24,-8),('m_mapAuthorName',9,-7),('m_modFileSyncChecksum',5,-6),('m_slotDescriptions',46,-5),('m_defaultDifficulty',2,-4),('m_cacheHandles',30,-3),('m_isBlizzardMap',26,-2),('m_isPremadeFFA',26,-1)]]),  #47
    ('_optional',[1]),  #48
    ('_optional',[7]),  #49
    ('_struct',[[('m_color',49,-1)]]),  #50
    ('_array',[(0,5),5]),  #51
    ('_struct',[[('m_control',10,-9),('m_userId',48,-8),('m_teamId',1,-7),('m_colorPref',50,-6),('m_racePref',34,-5),('m_difficulty',2,-4),('m_handicap',0,-3),('m_observe',19,-2),('m_rewards',51,-1)]]),  #52
    ('_array',[(0,5),52]),  #53
    ('_struct',[[('m_phase',12,-9),('m_maxUsers',7,-8),('m_maxObservers',7,-7),('m_slots',53,-6),('m_randomSeed',5,-5),('m_hostUserId',48,-4),('m_isSinglePlayer',26,-3),('m_gameDuration',5,-2),('m_defaultDifficulty',2,-1)]]),  #54
    ('_struct',[[('m_userInitialData',37,-3),('m_gameDescription',47,-2),('m_lobbyState',54,-1)]]),  #55
    ('_struct',[[('m_syncLobbyState',55,-1)]]),  #56
    ('_struct',[[('m_name',15,-1)]]),  #57
    ('_blob',[(0,6)]),  #58
    ('_struct',[[('m_name',58,-1)]]),  #59
    ('_struct',[[('m_name',58,-3),('m_type',5,-2),('m_data',15,-1)]]),  #60
    ('_struct',[[('m_type',5,-3),('m_name',58,-2),('m_data',28,-1)]]),  #61
    ('_struct',[[('m_developmentCheatsEnabled',26,-4),('m_multiplayerCheatsEnabled',26,-3),('m_syncChecksummingEnabled',26,-2),('m_isMapToMapTransition',26,-1)]]),  #62
    ('_struct',[[]]),  #63
    ('_struct',[[('m_fileName',24,-5),('m_automatic',26,-4),('m_overwrite',26,-3),('m_name',9,-2),('m_description',23,-1)]]),  #64
    ('_int',[(-2147483648,32)]),  #65
    ('_struct',[[('x',65,-2),('y',65,-1)]]),  #66
    ('_struct',[[('m_point',66,-4),('m_time',65,-3),('m_verb',23,-2),('m_arguments',23,-1)]]),  #67
    ('_struct',[[('m_data',67,-1)]]),  #68
    ('_int',[(0,17)]),  #69
    ('_int',[(0,16)]),  #70
    ('_struct',[[('m_abilLink',70,-3),('m_abilCmdIndex',7,-2),('m_abilCmdData',33,-1)]]),  #71
    ('_optional',[71]),  #72
    ('_null',[]),  #73
    ('_int',[(0,20)]),  #74
    ('_struct',[[('x',74,-3),('y',74,-2),('z',65,-1)]]),  #75
    ('_struct',[[('m_targetUnitFlags',10,-6),('m_timer',10,-5),('m_tag',5,-4),('m_snapshotUnitLink',70,-3),('m_snapshotPlayerId',48,-2),('m_snapshotPoint',75,-1)]]),  #76
    ('_choice',[(0,2),{0:('None',73),1:('TargetPoint',75),2:('TargetUnit',76),3:('Data',5)}]),  #77
    ('_optional',[5]),  #78
    ('_struct',[[('m_cmdFlags',69,-4),('m_abil',72,-3),('m_data',77,-2),('m_otherUnit',78,-1)]]),  #79
    ('_array',[(0,8),10]),  #80
    ('_choice',[(0,2),{0:('None',73),1:('Mask',43),2:('OneIndices',80),3:('ZeroIndices',80)}]),  #81
    ('_struct',[[('m_unitLink',70,-3),('m_intraSubgroupPriority',10,-2),('m_count',10,-1)]]),  #82
    ('_array',[(0,8),82]),  #83
    ('_array',[(0,8),5]),  #84
    ('_struct',[[('m_subgroupIndex',10,-4),('m_removeMask',81,-3),('m_addSubgroups',83,-2),('m_addUnitTags',84,-1)]]),  #85
    ('_struct',[[('m_controlGroupId',1,-2),('m_delta',85,-1)]]),  #86
    ('_struct',[[('m_controlGroupIndex',1,-3),('m_controlGroupUpdate',19,-2),('m_mask',81,-1)]]),  #87
    ('_struct',[[('m_count',10,-6),('m_subgroupCount',10,-5),('m_activeSubgroupIndex',10,-4),('m_unitTagsChecksum',5,-3),('m_subgroupIndicesChecksum',5,-2),('m_subgroupsChecksum',5,-1)]]),  #88
    ('_struct',[[('m_controlGroupId',1,-2),('m_selectionSyncData',88,-1)]]),  #89
    ('_array',[(0,3),65]),  #90
    ('_struct',[[('m_recipientId',1,-2),('m_resources',90,-1)]]),  #91
    ('_struct',[[('m_chatMessage',23,-1)]]),  #92
    ('_int',[(-128,8)]),  #93
    ('_struct',[[('x',65,-3),('y',65,-2),('z',65,-1)]]),  #94
    ('_struct',[[('m_beacon',93,-7),('m_ally',93,-6),('m_autocast',93,-5),('m_targetUnitTag',5,-4),('m_targetUnitSnapshotUnitLink',70,-3),('m_targetUnitSnapshotPlayerId',48,-2),('m_targetPoint',94,-1)]]),  #95
    ('_struct',[[('m_speed',12,-1)]]),  #96
    ('_struct',[[('m_delta',93,-1)]]),  #97
    ('_struct',[[('m_verb',23,-2),('m_arguments',23,-1)]]),  #98
    ('_struct',[[('m_alliance',5,-2),('m_control',5,-1)]]),  #99
    ('_struct',[[('m_unitTag',5,-1)]]),  #100
    ('_struct',[[('m_unitTag',5,-2),('m_flags',10,-1)]]),  #101
    ('_struct',[[('m_conversationId',65,-2),('m_replyId',65,-1)]]),  #102
    ('_struct',[[('m_purchaseItemId',65,-1)]]),  #103
    ('_struct',[[('m_difficultyLevel',65,-1)]]),  #104
    ('_choice',[(0,3),{0:('None',73),1:('Checked',26),2:('ValueChanged',5),3:('SelectionChanged',65),4:('TextChanged',24)}]),  #105
    ('_struct',[[('m_controlId',65,-3),('m_eventType',65,-2),('m_eventData',105,-1)]]),  #106
    ('_struct',[[('m_soundHash',5,-2),('m_length',5,-1)]]),  #107
    ('_struct',[[('m_soundHash',84,-2),('m_length',84,-1)]]),  #108
    ('_struct',[[('m_syncInfo',108,-1)]]),  #109
    ('_struct',[[('m_sound',5,-1)]]),  #110
    ('_struct',[[('m_transmissionId',65,-1)]]),  #111
    ('_struct',[[('x',70,-2),('y',70,-1)]]),  #112
    ('_optional',[70]),  #113
    ('_struct',[[('m_target',112,-4),('m_distance',113,-3),('m_pitch',113,-2),('m_yaw',113,-1)]]),  #114
    ('_int',[(0,1)]),  #115
    ('_struct',[[('m_skipType',115,-1)]]),  #116
    ('_struct',[[('m_button',5,-7),('m_down',26,-6),('m_posXUI',5,-5),('m_posYUI',5,-4),('m_posXWorld',65,-3),('m_posYWorld',65,-2),('m_posZWorld',65,-1)]]),  #117
    ('_struct',[[('m_soundtrack',5,-1)]]),  #118
    ('_struct',[[('m_planetId',65,-1)]]),  #119
    ('_struct',[[('m_key',93,-2),('m_flags',93,-1)]]),  #120
    ('_struct',[[('m_resources',90,-1)]]),  #121
    ('_struct',[[('m_fulfillRequestId',65,-1)]]),  #122
    ('_struct',[[('m_cancelRequestId',65,-1)]]),  #123
    ('_struct',[[('m_researchItemId',65,-1)]]),  #124
    ('_struct',[[('m_laggingPlayerId',1,-1)]]),  #125
    ('_struct',[[('m_mercenaryId',65,-1)]]),  #126
    ('_struct',[[('m_battleReportId',65,-2),('m_difficultyLevel',65,-1)]]),  #127
    ('_struct',[[('m_battleReportId',65,-1)]]),  #128
    ('_int',[(0,19)]),  #129
    ('_struct',[[('m_decrementMs',129,-1)]]),  #130
    ('_struct',[[('m_portraitId',65,-1)]]),  #131
    ('_struct',[[('m_functionName',15,-1)]]),  #132
    ('_struct',[[('m_result',65,-1)]]),  #133
    ('_struct',[[('m_gameMenuItemIndex',65,-1)]]),  #134
    ('_struct',[[('m_reason',93,-1)]]),  #135
    ('_struct',[[('m_purchaseCategoryId',65,-1)]]),  #136
    ('_struct',[[('m_button',70,-1)]]),  #137
    ('_struct',[[('m_recipient',19,-2),('m_string',24,-1)]]),  #138
    ('_struct',[[('m_recipient',19,-2),('m_point',66,-1)]]),  #139
    ('_struct',[[('m_progress',65,-1)]]),  #140
]

# Map from protocol NNet.Game.*Event eventid to (typeid, name)
game_event_types = {
    5: (63, 'NNet.Game.SUserFinishedLoadingSyncEvent'),
    7: (57, 'NNet.Game.SBankFileEvent'),
    8: (59, 'NNet.Game.SBankSectionEvent'),
    9: (60, 'NNet.Game.SBankKeyEvent'),
    10: (61, 'NNet.Game.SBankValueEvent'),
    11: (62, 'NNet.Game.SUserOptionsEvent'),
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
    58: (117, 'NNet.Game.STriggerMouseClickedEvent'),
    63: (63, 'NNet.Game.STriggerPlanetPanelReplayEvent'),
    64: (118, 'NNet.Game.STriggerSoundtrackDoneEvent'),
    65: (119, 'NNet.Game.STriggerPlanetMissionSelectedEvent'),
    66: (120, 'NNet.Game.STriggerKeyPressedEvent'),
    67: (132, 'NNet.Game.STriggerMovieFunctionEvent'),
    68: (63, 'NNet.Game.STriggerPlanetPanelBirthCompleteEvent'),
    69: (63, 'NNet.Game.STriggerPlanetPanelDeathCompleteEvent'),
    70: (121, 'NNet.Game.SResourceRequestEvent'),
    71: (122, 'NNet.Game.SResourceRequestFulfillEvent'),
    72: (123, 'NNet.Game.SResourceRequestCancelEvent'),
    73: (63, 'NNet.Game.STriggerResearchPanelExitEvent'),
    74: (63, 'NNet.Game.STriggerResearchPanelPurchaseEvent'),
    75: (124, 'NNet.Game.STriggerResearchPanelSelectionChangedEvent'),
    76: (125, 'NNet.Game.SLagMessageEvent'),
    77: (63, 'NNet.Game.STriggerMercenaryPanelExitEvent'),
    78: (63, 'NNet.Game.STriggerMercenaryPanelPurchaseEvent'),
    79: (126, 'NNet.Game.STriggerMercenaryPanelSelectionChangedEvent'),
    80: (63, 'NNet.Game.STriggerVictoryPanelExitEvent'),
    81: (63, 'NNet.Game.STriggerBattleReportPanelExitEvent'),
    82: (127, 'NNet.Game.STriggerBattleReportPanelPlayMissionEvent'),
    83: (128, 'NNet.Game.STriggerBattleReportPanelPlaySceneEvent'),
    84: (128, 'NNet.Game.STriggerBattleReportPanelSelectionChangedEvent'),
    85: (104, 'NNet.Game.STriggerVictoryPanelPlayMissionAgainEvent'),
    86: (63, 'NNet.Game.STriggerMovieStartedEvent'),
    87: (63, 'NNet.Game.STriggerMovieFinishedEvent'),
    88: (130, 'NNet.Game.SDecrementGameTimeRemainingEvent'),
    89: (131, 'NNet.Game.STriggerPortraitLoadedEvent'),
    90: (133, 'NNet.Game.STriggerCustomDialogDismissedEvent'),
    91: (134, 'NNet.Game.STriggerGameMenuItemSelectedEvent'),
    92: (135, 'NNet.Game.STriggerCameraMoveEvent'),
    93: (103, 'NNet.Game.STriggerPurchasePanelSelectedPurchaseItemChangedEvent'),
    94: (136, 'NNet.Game.STriggerPurchasePanelSelectedPurchaseCategoryChangedEvent'),
    95: (137, 'NNet.Game.STriggerButtonPressedEvent'),
    96: (63, 'NNet.Game.STriggerGameCreditsFinishedEvent'),
}

# The typeid of the NNet.Game.EEventId enum.
game_eventid_typeid = 0

# Map from protocol NNet.Game.*Message eventid to (typeid, name)
message_event_types = {
    0: (138, 'NNet.Game.SChatMessage'),
    1: (139, 'NNet.Game.SPingMessage'),
    2: (140, 'NNet.Game.SLoadingProgressMessage'),
    3: (63, 'NNet.Game.SServerPingMessage'),
}

# The typeid of the NNet.Game.EMessageId enum.
message_eventid_typeid = 1

# The typeid of NNet.SVarUint32 (the type used to encode gameloop deltas).
svaruint32_typeid = 6

# The typeid of NNet.Replay.SPlayerId (the type used to encode player ids).
replay_playerid_typeid = 8

# The typeid of NNet.Replay.SHeader (the type used to store replay game version and length).
replay_header_typeid = 13

# The typeid of NNet.Game.SDetails (the type used to store overall replay details).
game_details_typeid = 32

# The typeid of NNet.Replay.SInitData (the type used to store the inital lobby).
replay_initdata_typeid = 56


def _varuint32_value(value):
    # Returns the numeric value from a SVarUint32 instance.
    for k,v in value.iteritems():
        return v
    return 0


def _decode_event_stream(decoder, eventid_typeid, event_types, decode_player_id):
    # Decodes events prefixed with a gameloop and possibly userid
    gameloop = 0
    while not decoder.done():
        start_bits = decoder.used_bits()

        # decode the gameloop delta before each event
        delta = _varuint32_value(decoder.instance(svaruint32_typeid))
        gameloop += delta

        # decode the userid before each event
        if decode_player_id:
            playerid = decoder.instance(replay_playerid_typeid)

        # decode the event id
        eventid = decoder.instance(eventid_typeid)
        typeid, typename = event_types.get(eventid, (None, None))
        if typeid is None:
            raise CorruptedError('eventid(%d) at %s' % (eventid, decoder))

        # decode the event struct instance
        event = decoder.instance(typeid)
        event['_event'] = typename
        event['_eventid'] = eventid

        #  insert gameloop and userid
        event['_gameloop'] = gameloop
        if decode_player_id:
            event['_playerid'] = playerid

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
                                      decode_player_id=True):
        yield event


def decode_replay_message_events(contents):
    """Decodes and yields each message event from the contents byte string."""
    decoder = BitPackedDecoder(contents, typeinfos)
    for event in _decode_event_stream(decoder,
                                      message_eventid_typeid,
                                      message_event_types,
                                      decode_player_id=True):
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
        attributes['source'] = None
        attributes['mapNamespace'] = buffer.read_bits(32)
        count = buffer.read_bits(32)
        attributes['scopes'] = {}
        while not buffer.done():
            value = {}
            value['namespace'] = buffer.read_bits(32)
            value['attrid'] = attrid = buffer.read_bits(32)
            scope = buffer.read_bits(8)
            value['value'] = buffer.read_aligned_bytes(4)[::-1].strip('\x00')
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
