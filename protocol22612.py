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
    ('_array',[(0,6),29]),  #30
    ('_optional',[30]),  #31
    ('_array',[(0,6),24]),  #32
    ('_optional',[32]),  #33
    ('_struct',[[('m_playerList',22,0),('m_title',23,1),('m_difficulty',9,2),('m_thumbnail',25,3),('m_isBlizzardMap',26,4),('m_timeUTC',27,5),('m_timeLocalOffset',27,6),('m_description',28,7),('m_imageFilePath',24,8),('m_mapFileName',24,9),('m_cacheHandles',31,10),('m_miniSave',26,11),('m_gameSpeed',12,12),('m_defaultDifficulty',2,13),('m_modPaths',33,14)]]),  #34
    ('_optional',[10]),  #35
    ('_struct',[[('m_race',35,-1)]]),  #36
    ('_struct',[[('m_team',35,-1)]]),  #37
    ('_struct',[[('m_name',9,-8),('m_randomSeed',5,-7),('m_racePreference',36,-6),('m_teamPreference',37,-5),('m_testMap',26,-4),('m_testAuto',26,-3),('m_examine',26,-2),('m_observe',19,-1)]]),  #38
    ('_array',[(0,5),38]),  #39
    ('_struct',[[('m_lockTeams',26,-12),('m_teamsTogether',26,-11),('m_advancedSharedControl',26,-10),('m_randomRaces',26,-9),('m_battleNet',26,-8),('m_amm',26,-7),('m_ranked',26,-6),('m_noVictoryOrDefeat',26,-5),('m_fog',19,-4),('m_observers',19,-3),('m_userDifficulty',19,-2),('m_clientDebugFlags',16,-1)]]),  #40
    ('_int',[(1,4)]),  #41
    ('_int',[(1,8)]),  #42
    ('_bitarray',[(0,6)]),  #43
    ('_bitarray',[(0,8)]),  #44
    ('_bitarray',[(0,2)]),  #45
    ('_struct',[[('m_allowedColors',43,-5),('m_allowedRaces',44,-4),('m_allowedDifficulty',43,-3),('m_allowedControls',44,-2),('m_allowedObserveTypes',45,-1)]]),  #46
    ('_array',[(0,5),46]),  #47
    ('_struct',[[('m_randomValue',5,-23),('m_gameCacheName',23,-22),('m_gameOptions',40,-21),('m_gameSpeed',12,-20),('m_gameType',12,-19),('m_maxUsers',7,-18),('m_maxObservers',7,-17),('m_maxPlayers',7,-16),('m_maxTeams',41,-15),('m_maxColors',2,-14),('m_maxRaces',42,-13),('m_maxControls',42,-12),('m_mapSizeX',10,-11),('m_mapSizeY',10,-10),('m_mapFileSyncChecksum',5,-9),('m_mapFileName',24,-8),('m_mapAuthorName',9,-7),('m_modFileSyncChecksum',5,-6),('m_slotDescriptions',47,-5),('m_defaultDifficulty',2,-4),('m_cacheHandles',30,-3),('m_isBlizzardMap',26,-2),('m_isPremadeFFA',26,-1)]]),  #48
    ('_optional',[1]),  #49
    ('_optional',[7]),  #50
    ('_struct',[[('m_color',50,-1)]]),  #51
    ('_array',[(0,5),5]),  #52
    ('_array',[(0,9),5]),  #53
    ('_struct',[[('m_control',10,-11),('m_userId',49,-10),('m_teamId',1,-9),('m_colorPref',51,-8),('m_racePref',36,-7),('m_difficulty',2,-6),('m_handicap',0,-5),('m_observe',19,-4),('m_rewards',52,-3),('m_toonHandle',15,-2),('m_licenses',53,-1)]]),  #54
    ('_array',[(0,5),54]),  #55
    ('_struct',[[('m_phase',12,-9),('m_maxUsers',7,-8),('m_maxObservers',7,-7),('m_slots',55,-6),('m_randomSeed',5,-5),('m_hostUserId',49,-4),('m_isSinglePlayer',26,-3),('m_gameDuration',5,-2),('m_defaultDifficulty',2,-1)]]),  #56
    ('_struct',[[('m_userInitialData',39,-3),('m_gameDescription',48,-2),('m_lobbyState',56,-1)]]),  #57
    ('_struct',[[('m_syncLobbyState',57,-1)]]),  #58
    ('_struct',[[('m_name',15,-1)]]),  #59
    ('_blob',[(0,6)]),  #60
    ('_struct',[[('m_name',60,-1)]]),  #61
    ('_struct',[[('m_name',60,-3),('m_type',5,-2),('m_data',15,-1)]]),  #62
    ('_struct',[[('m_type',5,-3),('m_name',60,-2),('m_data',28,-1)]]),  #63
    ('_array',[(0,5),10]),  #64
    ('_struct',[[('m_signature',64,-1)]]),  #65
    ('_struct',[[('m_gameFullyDownloaded',26,-6),('m_developmentCheatsEnabled',26,-5),('m_multiplayerCheatsEnabled',26,-4),('m_syncChecksummingEnabled',26,-3),('m_isMapToMapTransition',26,-2),('m_useAIBeacons',26,-1)]]),  #66
    ('_struct',[[]]),  #67
    ('_struct',[[('m_fileName',24,-5),('m_automatic',26,-4),('m_overwrite',26,-3),('m_name',9,-2),('m_description',23,-1)]]),  #68
    ('_int',[(-2147483648,32)]),  #69
    ('_struct',[[('x',69,-2),('y',69,-1)]]),  #70
    ('_struct',[[('m_point',70,-4),('m_time',69,-3),('m_verb',23,-2),('m_arguments',23,-1)]]),  #71
    ('_struct',[[('m_data',71,-1)]]),  #72
    ('_int',[(0,20)]),  #73
    ('_int',[(0,16)]),  #74
    ('_struct',[[('m_abilLink',74,-3),('m_abilCmdIndex',7,-2),('m_abilCmdData',35,-1)]]),  #75
    ('_optional',[75]),  #76
    ('_null',[]),  #77
    ('_struct',[[('x',73,-3),('y',73,-2),('z',69,-1)]]),  #78
    ('_struct',[[('m_targetUnitFlags',10,-7),('m_timer',10,-6),('m_tag',5,-5),('m_snapshotUnitLink',74,-4),('m_snapshotControlPlayerId',49,-3),('m_snapshotUpkeepPlayerId',49,-2),('m_snapshotPoint',78,-1)]]),  #79
    ('_choice',[(0,2),{0:('None',77),1:('TargetPoint',78),2:('TargetUnit',79),3:('Data',5)}]),  #80
    ('_optional',[5]),  #81
    ('_struct',[[('m_cmdFlags',73,-4),('m_abil',76,-3),('m_data',80,-2),('m_otherUnit',81,-1)]]),  #82
    ('_int',[(0,9)]),  #83
    ('_bitarray',[(0,9)]),  #84
    ('_array',[(0,9),83]),  #85
    ('_choice',[(0,2),{0:('None',77),1:('Mask',84),2:('OneIndices',85),3:('ZeroIndices',85)}]),  #86
    ('_struct',[[('m_unitLink',74,-3),('m_intraSubgroupPriority',10,-2),('m_count',83,-1)]]),  #87
    ('_array',[(0,9),87]),  #88
    ('_struct',[[('m_subgroupIndex',83,-4),('m_removeMask',86,-3),('m_addSubgroups',88,-2),('m_addUnitTags',53,-1)]]),  #89
    ('_struct',[[('m_controlGroupId',1,-2),('m_delta',89,-1)]]),  #90
    ('_struct',[[('m_controlGroupIndex',1,-3),('m_controlGroupUpdate',19,-2),('m_mask',86,-1)]]),  #91
    ('_struct',[[('m_count',83,-6),('m_subgroupCount',83,-5),('m_activeSubgroupIndex',83,-4),('m_unitTagsChecksum',5,-3),('m_subgroupIndicesChecksum',5,-2),('m_subgroupsChecksum',5,-1)]]),  #92
    ('_struct',[[('m_controlGroupId',1,-2),('m_selectionSyncData',92,-1)]]),  #93
    ('_array',[(0,3),69]),  #94
    ('_struct',[[('m_recipientId',1,-2),('m_resources',94,-1)]]),  #95
    ('_struct',[[('m_chatMessage',23,-1)]]),  #96
    ('_int',[(-128,8)]),  #97
    ('_struct',[[('x',69,-3),('y',69,-2),('z',69,-1)]]),  #98
    ('_struct',[[('m_beacon',97,-9),('m_ally',97,-8),('m_flags',97,-7),('m_build',97,-6),('m_targetUnitTag',5,-5),('m_targetUnitSnapshotUnitLink',74,-4),('m_targetUnitSnapshotUpkeepPlayerId',97,-3),('m_targetUnitSnapshotControlPlayerId',97,-2),('m_targetPoint',98,-1)]]),  #99
    ('_struct',[[('m_speed',12,-1)]]),  #100
    ('_struct',[[('m_delta',97,-1)]]),  #101
    ('_struct',[[('m_point',70,-3),('m_unit',5,-2),('m_pingedMinimap',26,-1)]]),  #102
    ('_struct',[[('m_verb',23,-2),('m_arguments',23,-1)]]),  #103
    ('_struct',[[('m_alliance',5,-2),('m_control',5,-1)]]),  #104
    ('_struct',[[('m_unitTag',5,-1)]]),  #105
    ('_struct',[[('m_unitTag',5,-2),('m_flags',10,-1)]]),  #106
    ('_struct',[[('m_conversationId',69,-2),('m_replyId',69,-1)]]),  #107
    ('_struct',[[('m_purchaseItemId',69,-1)]]),  #108
    ('_struct',[[('m_difficultyLevel',69,-1)]]),  #109
    ('_choice',[(0,3),{0:('None',77),1:('Checked',26),2:('ValueChanged',5),3:('SelectionChanged',69),4:('TextChanged',24)}]),  #110
    ('_struct',[[('m_controlId',69,-3),('m_eventType',69,-2),('m_eventData',110,-1)]]),  #111
    ('_struct',[[('m_soundHash',5,-2),('m_length',5,-1)]]),  #112
    ('_array',[(0,8),5]),  #113
    ('_struct',[[('m_soundHash',113,-2),('m_length',113,-1)]]),  #114
    ('_struct',[[('m_syncInfo',114,-1)]]),  #115
    ('_struct',[[('m_sound',5,-1)]]),  #116
    ('_struct',[[('m_transmissionId',69,-2),('m_thread',5,-1)]]),  #117
    ('_struct',[[('m_transmissionId',69,-1)]]),  #118
    ('_struct',[[('x',74,-2),('y',74,-1)]]),  #119
    ('_optional',[74]),  #120
    ('_struct',[[('m_target',119,-4),('m_distance',120,-3),('m_pitch',120,-2),('m_yaw',120,-1)]]),  #121
    ('_int',[(0,1)]),  #122
    ('_struct',[[('m_skipType',122,-1)]]),  #123
    ('_int',[(0,11)]),  #124
    ('_struct',[[('x',124,-2),('y',124,-1)]]),  #125
    ('_struct',[[('m_button',5,-4),('m_down',26,-3),('m_posUI',125,-2),('m_posWorld',78,-1)]]),  #126
    ('_struct',[[('m_posUI',125,-2),('m_posWorld',78,-1)]]),  #127
    ('_struct',[[('m_achievementLink',74,-1)]]),  #128
    ('_struct',[[('m_soundtrack',5,-1)]]),  #129
    ('_struct',[[('m_planetId',69,-1)]]),  #130
    ('_struct',[[('m_key',97,-2),('m_flags',97,-1)]]),  #131
    ('_struct',[[('m_resources',94,-1)]]),  #132
    ('_struct',[[('m_fulfillRequestId',69,-1)]]),  #133
    ('_struct',[[('m_cancelRequestId',69,-1)]]),  #134
    ('_struct',[[('m_researchItemId',69,-1)]]),  #135
    ('_struct',[[('m_laggingPlayerId',1,-1)]]),  #136
    ('_struct',[[('m_mercenaryId',69,-1)]]),  #137
    ('_struct',[[('m_battleReportId',69,-2),('m_difficultyLevel',69,-1)]]),  #138
    ('_struct',[[('m_battleReportId',69,-1)]]),  #139
    ('_int',[(0,19)]),  #140
    ('_struct',[[('m_decrementMs',140,-1)]]),  #141
    ('_struct',[[('m_portraitId',69,-1)]]),  #142
    ('_struct',[[('m_functionName',15,-1)]]),  #143
    ('_struct',[[('m_result',69,-1)]]),  #144
    ('_struct',[[('m_gameMenuItemIndex',69,-1)]]),  #145
    ('_struct',[[('m_reason',97,-1)]]),  #146
    ('_struct',[[('m_purchaseCategoryId',69,-1)]]),  #147
    ('_struct',[[('m_button',74,-1)]]),  #148
    ('_struct',[[('m_cutsceneId',69,-2),('m_bookmarkName',15,-1)]]),  #149
    ('_struct',[[('m_cutsceneId',69,-1)]]),  #150
    ('_struct',[[('m_cutsceneId',69,-3),('m_conversationLine',15,-2),('m_altConversationLine',15,-1)]]),  #151
    ('_struct',[[('m_cutsceneId',69,-2),('m_conversationLine',15,-1)]]),  #152
    ('_struct',[[('m_recipient',12,-2),('m_string',24,-1)]]),  #153
    ('_struct',[[('m_recipient',12,-2),('m_point',70,-1)]]),  #154
    ('_struct',[[('m_progress',69,-1)]]),  #155
]

# Map from protocol NNet.Game.*Event eventid to (typeid, name)
game_event_types = {
    5: (67, 'NNet.Game.SUserFinishedLoadingSyncEvent'),
    7: (59, 'NNet.Game.SBankFileEvent'),
    8: (61, 'NNet.Game.SBankSectionEvent'),
    9: (62, 'NNet.Game.SBankKeyEvent'),
    10: (63, 'NNet.Game.SBankValueEvent'),
    11: (65, 'NNet.Game.SBankSignatureEvent'),
    12: (66, 'NNet.Game.SUserOptionsEvent'),
    22: (68, 'NNet.Game.SSaveGameEvent'),
    23: (67, 'NNet.Game.SSaveGameDoneEvent'),
    25: (67, 'NNet.Game.SPlayerLeaveEvent'),
    26: (72, 'NNet.Game.SGameCheatEvent'),
    27: (82, 'NNet.Game.SCmdEvent'),
    28: (90, 'NNet.Game.SSelectionDeltaEvent'),
    29: (91, 'NNet.Game.SControlGroupUpdateEvent'),
    30: (93, 'NNet.Game.SSelectionSyncCheckEvent'),
    31: (95, 'NNet.Game.SResourceTradeEvent'),
    32: (96, 'NNet.Game.STriggerChatMessageEvent'),
    33: (99, 'NNet.Game.SAICommunicateEvent'),
    34: (100, 'NNet.Game.SSetAbsoluteGameSpeedEvent'),
    35: (101, 'NNet.Game.SAddAbsoluteGameSpeedEvent'),
    36: (102, 'NNet.Game.STriggerPingEvent'),
    37: (103, 'NNet.Game.SBroadcastCheatEvent'),
    38: (104, 'NNet.Game.SAllianceEvent'),
    39: (105, 'NNet.Game.SUnitClickEvent'),
    40: (106, 'NNet.Game.SUnitHighlightEvent'),
    41: (107, 'NNet.Game.STriggerReplySelectedEvent'),
    44: (67, 'NNet.Game.STriggerSkippedEvent'),
    45: (112, 'NNet.Game.STriggerSoundLengthQueryEvent'),
    46: (116, 'NNet.Game.STriggerSoundOffsetEvent'),
    47: (117, 'NNet.Game.STriggerTransmissionOffsetEvent'),
    48: (118, 'NNet.Game.STriggerTransmissionCompleteEvent'),
    49: (121, 'NNet.Game.SCameraUpdateEvent'),
    50: (67, 'NNet.Game.STriggerAbortMissionEvent'),
    51: (108, 'NNet.Game.STriggerPurchaseMadeEvent'),
    52: (67, 'NNet.Game.STriggerPurchaseExitEvent'),
    53: (109, 'NNet.Game.STriggerPlanetMissionLaunchedEvent'),
    54: (67, 'NNet.Game.STriggerPlanetPanelCanceledEvent'),
    55: (111, 'NNet.Game.STriggerDialogControlEvent'),
    56: (115, 'NNet.Game.STriggerSoundLengthSyncEvent'),
    57: (123, 'NNet.Game.STriggerConversationSkippedEvent'),
    58: (126, 'NNet.Game.STriggerMouseClickedEvent'),
    59: (127, 'NNet.Game.STriggerMouseMovedEvent'),
    60: (128, 'NNet.Game.SAchievementAwardedEvent'),
    63: (67, 'NNet.Game.STriggerPlanetPanelReplayEvent'),
    64: (129, 'NNet.Game.STriggerSoundtrackDoneEvent'),
    65: (130, 'NNet.Game.STriggerPlanetMissionSelectedEvent'),
    66: (131, 'NNet.Game.STriggerKeyPressedEvent'),
    67: (143, 'NNet.Game.STriggerMovieFunctionEvent'),
    68: (67, 'NNet.Game.STriggerPlanetPanelBirthCompleteEvent'),
    69: (67, 'NNet.Game.STriggerPlanetPanelDeathCompleteEvent'),
    70: (132, 'NNet.Game.SResourceRequestEvent'),
    71: (133, 'NNet.Game.SResourceRequestFulfillEvent'),
    72: (134, 'NNet.Game.SResourceRequestCancelEvent'),
    73: (67, 'NNet.Game.STriggerResearchPanelExitEvent'),
    74: (67, 'NNet.Game.STriggerResearchPanelPurchaseEvent'),
    75: (135, 'NNet.Game.STriggerResearchPanelSelectionChangedEvent'),
    76: (136, 'NNet.Game.SLagMessageEvent'),
    77: (67, 'NNet.Game.STriggerMercenaryPanelExitEvent'),
    78: (67, 'NNet.Game.STriggerMercenaryPanelPurchaseEvent'),
    79: (137, 'NNet.Game.STriggerMercenaryPanelSelectionChangedEvent'),
    80: (67, 'NNet.Game.STriggerVictoryPanelExitEvent'),
    81: (67, 'NNet.Game.STriggerBattleReportPanelExitEvent'),
    82: (138, 'NNet.Game.STriggerBattleReportPanelPlayMissionEvent'),
    83: (139, 'NNet.Game.STriggerBattleReportPanelPlaySceneEvent'),
    84: (139, 'NNet.Game.STriggerBattleReportPanelSelectionChangedEvent'),
    85: (109, 'NNet.Game.STriggerVictoryPanelPlayMissionAgainEvent'),
    86: (67, 'NNet.Game.STriggerMovieStartedEvent'),
    87: (67, 'NNet.Game.STriggerMovieFinishedEvent'),
    88: (141, 'NNet.Game.SDecrementGameTimeRemainingEvent'),
    89: (142, 'NNet.Game.STriggerPortraitLoadedEvent'),
    90: (144, 'NNet.Game.STriggerCustomDialogDismissedEvent'),
    91: (145, 'NNet.Game.STriggerGameMenuItemSelectedEvent'),
    92: (146, 'NNet.Game.STriggerCameraMoveEvent'),
    93: (108, 'NNet.Game.STriggerPurchasePanelSelectedPurchaseItemChangedEvent'),
    94: (147, 'NNet.Game.STriggerPurchasePanelSelectedPurchaseCategoryChangedEvent'),
    95: (148, 'NNet.Game.STriggerButtonPressedEvent'),
    96: (67, 'NNet.Game.STriggerGameCreditsFinishedEvent'),
    97: (149, 'NNet.Game.STriggerCutsceneBookmarkFiredEvent'),
    98: (150, 'NNet.Game.STriggerCutsceneEndSceneFiredEvent'),
    99: (151, 'NNet.Game.STriggerCutsceneConversationLineEvent'),
    100: (152, 'NNet.Game.STriggerCutsceneConversationLineMissingEvent'),
}

# The typeid of the NNet.Game.EEventId enum.
game_eventid_typeid = 0

# Map from protocol NNet.Game.*Message eventid to (typeid, name)
message_event_types = {
    0: (153, 'NNet.Game.SChatMessage'),
    1: (154, 'NNet.Game.SPingMessage'),
    2: (155, 'NNet.Game.SLoadingProgressMessage'),
    3: (67, 'NNet.Game.SServerPingMessage'),
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
game_details_typeid = 34

# The typeid of NNet.Replay.SInitData (the type used to store the inital lobby).
replay_initdata_typeid = 58


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
        attributes['source'] = buffer.read_bits(8)
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
