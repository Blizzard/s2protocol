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
    ('_array',[(0,6),27]),  #28
    ('_optional',[28]),  #29
    ('_array',[(0,6),22]),  #30
    ('_optional',[30]),  #31
    ('_struct',[[('m_playerList',20,0),('m_title',21,1),('m_difficulty',7,2),('m_thumbnail',23,3),('m_isBlizzardMap',24,4),('m_timeUTC',25,5),('m_timeLocalOffset',25,6),('m_description',26,7),('m_imageFilePath',22,8),('m_mapFileName',22,9),('m_cacheHandles',29,10),('m_miniSave',24,11),('m_gameSpeed',10,12),('m_defaultDifficulty',2,13),('m_modPaths',31,14)]]),  #32
    ('_optional',[8]),  #33
    ('_struct',[[('m_race',33,-1)]]),  #34
    ('_struct',[[('m_team',33,-1)]]),  #35
    ('_struct',[[('m_name',7,-8),('m_randomSeed',5,-7),('m_racePreference',34,-6),('m_teamPreference',35,-5),('m_testMap',24,-4),('m_testAuto',24,-3),('m_examine',24,-2),('m_observe',17,-1)]]),  #36
    ('_array',[(0,5),36]),  #37
    ('_struct',[[('m_lockTeams',24,-12),('m_teamsTogether',24,-11),('m_advancedSharedControl',24,-10),('m_randomRaces',24,-9),('m_battleNet',24,-8),('m_amm',24,-7),('m_ranked',24,-6),('m_noVictoryOrDefeat',24,-5),('m_fog',17,-4),('m_observers',17,-3),('m_userDifficulty',17,-2),('m_clientDebugFlags',14,-1)]]),  #38
    ('_int',[(0,5)]),  #39
    ('_int',[(1,4)]),  #40
    ('_int',[(1,8)]),  #41
    ('_bitarray',[(0,6)]),  #42
    ('_bitarray',[(0,8)]),  #43
    ('_bitarray',[(0,2)]),  #44
    ('_struct',[[('m_allowedColors',42,-5),('m_allowedRaces',43,-4),('m_allowedDifficulty',42,-3),('m_allowedControls',43,-2),('m_allowedObserveTypes',44,-1)]]),  #45
    ('_array',[(0,5),45]),  #46
    ('_struct',[[('m_randomValue',5,-23),('m_gameCacheName',21,-22),('m_gameOptions',38,-21),('m_gameSpeed',10,-20),('m_gameType',10,-19),('m_maxUsers',39,-18),('m_maxObservers',39,-17),('m_maxPlayers',39,-16),('m_maxTeams',40,-15),('m_maxColors',2,-14),('m_maxRaces',41,-13),('m_maxControls',41,-12),('m_mapSizeX',8,-11),('m_mapSizeY',8,-10),('m_mapFileSyncChecksum',5,-9),('m_mapFileName',22,-8),('m_mapAuthorName',7,-7),('m_modFileSyncChecksum',5,-6),('m_slotDescriptions',46,-5),('m_defaultDifficulty',2,-4),('m_cacheHandles',28,-3),('m_isBlizzardMap',24,-2),('m_isPremadeFFA',24,-1)]]),  #47
    ('_optional',[1]),  #48
    ('_optional',[39]),  #49
    ('_struct',[[('m_color',49,-1)]]),  #50
    ('_array',[(0,5),5]),  #51
    ('_array',[(0,9),5]),  #52
    ('_struct',[[('m_control',8,-11),('m_userId',48,-10),('m_teamId',1,-9),('m_colorPref',50,-8),('m_racePref',34,-7),('m_difficulty',2,-6),('m_handicap',0,-5),('m_observe',17,-4),('m_rewards',51,-3),('m_toonHandle',13,-2),('m_licenses',52,-1)]]),  #53
    ('_array',[(0,5),53]),  #54
    ('_struct',[[('m_phase',10,-9),('m_maxUsers',39,-8),('m_maxObservers',39,-7),('m_slots',54,-6),('m_randomSeed',5,-5),('m_hostUserId',48,-4),('m_isSinglePlayer',24,-3),('m_gameDuration',5,-2),('m_defaultDifficulty',2,-1)]]),  #55
    ('_struct',[[('m_userInitialData',37,-3),('m_gameDescription',47,-2),('m_lobbyState',55,-1)]]),  #56
    ('_struct',[[('m_syncLobbyState',56,-1)]]),  #57
    ('_struct',[[('m_name',13,-5)]]),  #58
    ('_blob',[(0,6)]),  #59
    ('_struct',[[('m_name',59,-5)]]),  #60
    ('_struct',[[('m_name',59,-7),('m_type',5,-6),('m_data',13,-5)]]),  #61
    ('_struct',[[('m_type',5,-7),('m_name',59,-6),('m_data',26,-5)]]),  #62
    ('_array',[(0,5),8]),  #63
    ('_struct',[[('m_signature',63,-5)]]),  #64
    ('_struct',[[('m_gameFullyDownloaded',24,-10),('m_developmentCheatsEnabled',24,-9),('m_multiplayerCheatsEnabled',24,-8),('m_syncChecksummingEnabled',24,-7),('m_isMapToMapTransition',24,-6),('m_useAIBeacons',24,-5)]]),  #65
    ('_struct',[[]]),  #66
    ('_struct',[[('m_fileName',22,-9),('m_automatic',24,-8),('m_overwrite',24,-7),('m_name',7,-6),('m_description',21,-5)]]),  #67
    ('_int',[(-2147483648,32)]),  #68
    ('_struct',[[('x',68,-2),('y',68,-1)]]),  #69
    ('_struct',[[('m_point',69,-4),('m_time',68,-3),('m_verb',21,-2),('m_arguments',21,-1)]]),  #70
    ('_struct',[[('m_data',70,-5)]]),  #71
    ('_int',[(0,20)]),  #72
    ('_int',[(0,16)]),  #73
    ('_struct',[[('m_abilLink',73,-3),('m_abilCmdIndex',39,-2),('m_abilCmdData',33,-1)]]),  #74
    ('_optional',[74]),  #75
    ('_null',[]),  #76
    ('_struct',[[('x',72,-3),('y',72,-2),('z',68,-1)]]),  #77
    ('_struct',[[('m_targetUnitFlags',8,-7),('m_timer',8,-6),('m_tag',5,-5),('m_snapshotUnitLink',73,-4),('m_snapshotControlPlayerId',48,-3),('m_snapshotUpkeepPlayerId',48,-2),('m_snapshotPoint',77,-1)]]),  #78
    ('_choice',[(0,2),{0:('None',76),1:('TargetPoint',77),2:('TargetUnit',78),3:('Data',5)}]),  #79
    ('_optional',[5]),  #80
    ('_struct',[[('m_cmdFlags',72,-8),('m_abil',75,-7),('m_data',79,-6),('m_otherUnit',80,-5)]]),  #81
    ('_int',[(0,9)]),  #82
    ('_bitarray',[(0,9)]),  #83
    ('_array',[(0,9),82]),  #84
    ('_choice',[(0,2),{0:('None',76),1:('Mask',83),2:('OneIndices',84),3:('ZeroIndices',84)}]),  #85
    ('_struct',[[('m_unitLink',73,-3),('m_intraSubgroupPriority',8,-2),('m_count',82,-1)]]),  #86
    ('_array',[(0,9),86]),  #87
    ('_struct',[[('m_subgroupIndex',82,-4),('m_removeMask',85,-3),('m_addSubgroups',87,-2),('m_addUnitTags',52,-1)]]),  #88
    ('_struct',[[('m_controlGroupId',1,-6),('m_delta',88,-5)]]),  #89
    ('_struct',[[('m_controlGroupIndex',1,-7),('m_controlGroupUpdate',17,-6),('m_mask',85,-5)]]),  #90
    ('_struct',[[('m_count',82,-6),('m_subgroupCount',82,-5),('m_activeSubgroupIndex',82,-4),('m_unitTagsChecksum',5,-3),('m_subgroupIndicesChecksum',5,-2),('m_subgroupsChecksum',5,-1)]]),  #91
    ('_struct',[[('m_controlGroupId',1,-6),('m_selectionSyncData',91,-5)]]),  #92
    ('_array',[(0,3),68]),  #93
    ('_struct',[[('m_recipientId',1,-6),('m_resources',93,-5)]]),  #94
    ('_struct',[[('m_chatMessage',21,-5)]]),  #95
    ('_int',[(-128,8)]),  #96
    ('_struct',[[('x',68,-3),('y',68,-2),('z',68,-1)]]),  #97
    ('_struct',[[('m_beacon',96,-13),('m_ally',96,-12),('m_flags',96,-11),('m_build',96,-10),('m_targetUnitTag',5,-9),('m_targetUnitSnapshotUnitLink',73,-8),('m_targetUnitSnapshotUpkeepPlayerId',96,-7),('m_targetUnitSnapshotControlPlayerId',96,-6),('m_targetPoint',97,-5)]]),  #98
    ('_struct',[[('m_speed',10,-5)]]),  #99
    ('_struct',[[('m_delta',96,-5)]]),  #100
    ('_struct',[[('m_point',69,-7),('m_unit',5,-6),('m_pingedMinimap',24,-5)]]),  #101
    ('_struct',[[('m_verb',21,-6),('m_arguments',21,-5)]]),  #102
    ('_struct',[[('m_alliance',5,-6),('m_control',5,-5)]]),  #103
    ('_struct',[[('m_unitTag',5,-5)]]),  #104
    ('_struct',[[('m_unitTag',5,-6),('m_flags',8,-5)]]),  #105
    ('_struct',[[('m_conversationId',68,-6),('m_replyId',68,-5)]]),  #106
    ('_struct',[[('m_purchaseItemId',68,-5)]]),  #107
    ('_struct',[[('m_difficultyLevel',68,-5)]]),  #108
    ('_choice',[(0,3),{0:('None',76),1:('Checked',24),2:('ValueChanged',5),3:('SelectionChanged',68),4:('TextChanged',22)}]),  #109
    ('_struct',[[('m_controlId',68,-7),('m_eventType',68,-6),('m_eventData',109,-5)]]),  #110
    ('_struct',[[('m_soundHash',5,-6),('m_length',5,-5)]]),  #111
    ('_array',[(0,8),5]),  #112
    ('_struct',[[('m_soundHash',112,-2),('m_length',112,-1)]]),  #113
    ('_struct',[[('m_syncInfo',113,-5)]]),  #114
    ('_struct',[[('m_sound',5,-5)]]),  #115
    ('_struct',[[('m_transmissionId',68,-6),('m_thread',5,-5)]]),  #116
    ('_struct',[[('m_transmissionId',68,-5)]]),  #117
    ('_struct',[[('x',73,-2),('y',73,-1)]]),  #118
    ('_optional',[73]),  #119
    ('_struct',[[('m_target',118,-8),('m_distance',119,-7),('m_pitch',119,-6),('m_yaw',119,-5)]]),  #120
    ('_int',[(0,1)]),  #121
    ('_struct',[[('m_skipType',121,-5)]]),  #122
    ('_int',[(0,11)]),  #123
    ('_struct',[[('x',123,-2),('y',123,-1)]]),  #124
    ('_struct',[[('m_button',5,-8),('m_down',24,-7),('m_posUI',124,-6),('m_posWorld',77,-5)]]),  #125
    ('_struct',[[('m_posUI',124,-6),('m_posWorld',77,-5)]]),  #126
    ('_struct',[[('m_achievementLink',73,-5)]]),  #127
    ('_struct',[[('m_soundtrack',5,-5)]]),  #128
    ('_struct',[[('m_planetId',68,-5)]]),  #129
    ('_struct',[[('m_key',96,-6),('m_flags',96,-5)]]),  #130
    ('_struct',[[('m_resources',93,-5)]]),  #131
    ('_struct',[[('m_fulfillRequestId',68,-5)]]),  #132
    ('_struct',[[('m_cancelRequestId',68,-5)]]),  #133
    ('_struct',[[('m_researchItemId',68,-5)]]),  #134
    ('_struct',[[('m_laggingPlayerId',1,-5)]]),  #135
    ('_struct',[[('m_mercenaryId',68,-5)]]),  #136
    ('_struct',[[('m_battleReportId',68,-6),('m_difficultyLevel',68,-5)]]),  #137
    ('_struct',[[('m_battleReportId',68,-5)]]),  #138
    ('_int',[(0,19)]),  #139
    ('_struct',[[('m_decrementMs',139,-5)]]),  #140
    ('_struct',[[('m_portraitId',68,-5)]]),  #141
    ('_struct',[[('m_functionName',13,-5)]]),  #142
    ('_struct',[[('m_result',68,-5)]]),  #143
    ('_struct',[[('m_gameMenuItemIndex',68,-5)]]),  #144
    ('_struct',[[('m_reason',96,-5)]]),  #145
    ('_struct',[[('m_purchaseCategoryId',68,-5)]]),  #146
    ('_struct',[[('m_button',73,-5)]]),  #147
    ('_struct',[[('m_cutsceneId',68,-6),('m_bookmarkName',13,-5)]]),  #148
    ('_struct',[[('m_cutsceneId',68,-5)]]),  #149
    ('_struct',[[('m_cutsceneId',68,-7),('m_conversationLine',13,-6),('m_altConversationLine',13,-5)]]),  #150
    ('_struct',[[('m_cutsceneId',68,-6),('m_conversationLine',13,-5)]]),  #151
    ('_struct',[[('m_recipient',10,-3),('m_string',22,-2)]]),  #152
    ('_struct',[[('m_recipient',10,-3),('m_point',69,-2)]]),  #153
    ('_struct',[[('m_progress',68,-2)]]),  #154
]

# Map from protocol NNet.Game.*Event eventid to (typeid, name)
game_event_types = {
    5: (66, 'NNet.Game.SUserFinishedLoadingSyncEvent'),
    7: (58, 'NNet.Game.SBankFileEvent'),
    8: (60, 'NNet.Game.SBankSectionEvent'),
    9: (61, 'NNet.Game.SBankKeyEvent'),
    10: (62, 'NNet.Game.SBankValueEvent'),
    11: (64, 'NNet.Game.SBankSignatureEvent'),
    12: (65, 'NNet.Game.SUserOptionsEvent'),
    22: (67, 'NNet.Game.SSaveGameEvent'),
    23: (66, 'NNet.Game.SSaveGameDoneEvent'),
    25: (66, 'NNet.Game.SPlayerLeaveEvent'),
    26: (71, 'NNet.Game.SGameCheatEvent'),
    27: (81, 'NNet.Game.SCmdEvent'),
    28: (89, 'NNet.Game.SSelectionDeltaEvent'),
    29: (90, 'NNet.Game.SControlGroupUpdateEvent'),
    30: (92, 'NNet.Game.SSelectionSyncCheckEvent'),
    31: (94, 'NNet.Game.SResourceTradeEvent'),
    32: (95, 'NNet.Game.STriggerChatMessageEvent'),
    33: (98, 'NNet.Game.SAICommunicateEvent'),
    34: (99, 'NNet.Game.SSetAbsoluteGameSpeedEvent'),
    35: (100, 'NNet.Game.SAddAbsoluteGameSpeedEvent'),
    36: (101, 'NNet.Game.STriggerPingEvent'),
    37: (102, 'NNet.Game.SBroadcastCheatEvent'),
    38: (103, 'NNet.Game.SAllianceEvent'),
    39: (104, 'NNet.Game.SUnitClickEvent'),
    40: (105, 'NNet.Game.SUnitHighlightEvent'),
    41: (106, 'NNet.Game.STriggerReplySelectedEvent'),
    44: (66, 'NNet.Game.STriggerSkippedEvent'),
    45: (111, 'NNet.Game.STriggerSoundLengthQueryEvent'),
    46: (115, 'NNet.Game.STriggerSoundOffsetEvent'),
    47: (116, 'NNet.Game.STriggerTransmissionOffsetEvent'),
    48: (117, 'NNet.Game.STriggerTransmissionCompleteEvent'),
    49: (120, 'NNet.Game.SCameraUpdateEvent'),
    50: (66, 'NNet.Game.STriggerAbortMissionEvent'),
    51: (107, 'NNet.Game.STriggerPurchaseMadeEvent'),
    52: (66, 'NNet.Game.STriggerPurchaseExitEvent'),
    53: (108, 'NNet.Game.STriggerPlanetMissionLaunchedEvent'),
    54: (66, 'NNet.Game.STriggerPlanetPanelCanceledEvent'),
    55: (110, 'NNet.Game.STriggerDialogControlEvent'),
    56: (114, 'NNet.Game.STriggerSoundLengthSyncEvent'),
    57: (122, 'NNet.Game.STriggerConversationSkippedEvent'),
    58: (125, 'NNet.Game.STriggerMouseClickedEvent'),
    59: (126, 'NNet.Game.STriggerMouseMovedEvent'),
    60: (127, 'NNet.Game.SAchievementAwardedEvent'),
    63: (66, 'NNet.Game.STriggerPlanetPanelReplayEvent'),
    64: (128, 'NNet.Game.STriggerSoundtrackDoneEvent'),
    65: (129, 'NNet.Game.STriggerPlanetMissionSelectedEvent'),
    66: (130, 'NNet.Game.STriggerKeyPressedEvent'),
    67: (142, 'NNet.Game.STriggerMovieFunctionEvent'),
    68: (66, 'NNet.Game.STriggerPlanetPanelBirthCompleteEvent'),
    69: (66, 'NNet.Game.STriggerPlanetPanelDeathCompleteEvent'),
    70: (131, 'NNet.Game.SResourceRequestEvent'),
    71: (132, 'NNet.Game.SResourceRequestFulfillEvent'),
    72: (133, 'NNet.Game.SResourceRequestCancelEvent'),
    73: (66, 'NNet.Game.STriggerResearchPanelExitEvent'),
    74: (66, 'NNet.Game.STriggerResearchPanelPurchaseEvent'),
    75: (134, 'NNet.Game.STriggerResearchPanelSelectionChangedEvent'),
    76: (135, 'NNet.Game.SLagMessageEvent'),
    77: (66, 'NNet.Game.STriggerMercenaryPanelExitEvent'),
    78: (66, 'NNet.Game.STriggerMercenaryPanelPurchaseEvent'),
    79: (136, 'NNet.Game.STriggerMercenaryPanelSelectionChangedEvent'),
    80: (66, 'NNet.Game.STriggerVictoryPanelExitEvent'),
    81: (66, 'NNet.Game.STriggerBattleReportPanelExitEvent'),
    82: (137, 'NNet.Game.STriggerBattleReportPanelPlayMissionEvent'),
    83: (138, 'NNet.Game.STriggerBattleReportPanelPlaySceneEvent'),
    84: (138, 'NNet.Game.STriggerBattleReportPanelSelectionChangedEvent'),
    85: (108, 'NNet.Game.STriggerVictoryPanelPlayMissionAgainEvent'),
    86: (66, 'NNet.Game.STriggerMovieStartedEvent'),
    87: (66, 'NNet.Game.STriggerMovieFinishedEvent'),
    88: (140, 'NNet.Game.SDecrementGameTimeRemainingEvent'),
    89: (141, 'NNet.Game.STriggerPortraitLoadedEvent'),
    90: (143, 'NNet.Game.STriggerCustomDialogDismissedEvent'),
    91: (144, 'NNet.Game.STriggerGameMenuItemSelectedEvent'),
    92: (145, 'NNet.Game.STriggerCameraMoveEvent'),
    93: (107, 'NNet.Game.STriggerPurchasePanelSelectedPurchaseItemChangedEvent'),
    94: (146, 'NNet.Game.STriggerPurchasePanelSelectedPurchaseCategoryChangedEvent'),
    95: (147, 'NNet.Game.STriggerButtonPressedEvent'),
    96: (66, 'NNet.Game.STriggerGameCreditsFinishedEvent'),
    97: (148, 'NNet.Game.STriggerCutsceneBookmarkFiredEvent'),
    98: (149, 'NNet.Game.STriggerCutsceneEndSceneFiredEvent'),
    99: (150, 'NNet.Game.STriggerCutsceneConversationLineEvent'),
    100: (151, 'NNet.Game.STriggerCutsceneConversationLineMissingEvent'),
}

# The typeid of the NNet.Game.EEventId enum.
game_eventid_typeid = 0

# Map from protocol NNet.Game.*Message eventid to (typeid, name)
message_event_types = {
    0: (152, 'NNet.Game.SChatMessage'),
    1: (153, 'NNet.Game.SPingMessage'),
    2: (154, 'NNet.Game.SLoadingProgressMessage'),
    3: (66, 'NNet.Game.SServerPingMessage'),
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
game_details_typeid = 32

# The typeid of NNet.Replay.SInitData (the type used to store the inital lobby).
replay_initdata_typeid = 57


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
