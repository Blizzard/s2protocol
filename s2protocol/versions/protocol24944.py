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
    ('_int',[(0,5)]),  #7
    ('_struct',[[('m_userId',7,-1)]]),  #8
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
    ('_optional',[10]),  #20
    ('_struct',[[('m_name',9,0),('m_toon',17,1),('m_race',9,2),('m_color',18,3),('m_control',10,4),('m_teamId',1,5),('m_handicap',0,6),('m_observe',19,7),('m_result',19,8),('m_workingSetSlotId',20,9)]]),  #21
    ('_array',[(0,5),21]),  #22
    ('_optional',[22]),  #23
    ('_blob',[(0,10)]),  #24
    ('_blob',[(0,11)]),  #25
    ('_struct',[[('m_file',25,0)]]),  #26
    ('_bool',[]),  #27
    ('_int',[(-9223372036854775808,64)]),  #28
    ('_blob',[(0,12)]),  #29
    ('_blob',[(40,0)]),  #30
    ('_array',[(0,6),30]),  #31
    ('_optional',[31]),  #32
    ('_array',[(0,6),25]),  #33
    ('_optional',[33]),  #34
    ('_struct',[[('m_playerList',23,0),('m_title',24,1),('m_difficulty',9,2),('m_thumbnail',26,3),('m_isBlizzardMap',27,4),('m_timeUTC',28,5),('m_timeLocalOffset',28,6),('m_description',29,7),('m_imageFilePath',25,8),('m_campaignIndex',10,15),('m_mapFileName',25,9),('m_cacheHandles',32,10),('m_miniSave',27,11),('m_gameSpeed',12,12),('m_defaultDifficulty',2,13),('m_modPaths',34,14)]]),  #35
    ('_optional',[9]),  #36
    ('_optional',[5]),  #37
    ('_struct',[[('m_race',20,-1)]]),  #38
    ('_struct',[[('m_team',20,-1)]]),  #39
    ('_struct',[[('m_name',9,-12),('m_clanTag',36,-11),('m_highestLeague',20,-10),('m_combinedRaceLevels',37,-9),('m_randomSeed',5,-8),('m_racePreference',38,-7),('m_teamPreference',39,-6),('m_testMap',27,-5),('m_testAuto',27,-4),('m_examine',27,-3),('m_customInterface',27,-2),('m_observe',19,-1)]]),  #40
    ('_array',[(0,5),40]),  #41
    ('_struct',[[('m_lockTeams',27,-12),('m_teamsTogether',27,-11),('m_advancedSharedControl',27,-10),('m_randomRaces',27,-9),('m_battleNet',27,-8),('m_amm',27,-7),('m_competitive',27,-6),('m_noVictoryOrDefeat',27,-5),('m_fog',19,-4),('m_observers',19,-3),('m_userDifficulty',19,-2),('m_clientDebugFlags',16,-1)]]),  #42
    ('_int',[(1,4)]),  #43
    ('_int',[(1,8)]),  #44
    ('_bitarray',[(0,6)]),  #45
    ('_bitarray',[(0,8)]),  #46
    ('_bitarray',[(0,2)]),  #47
    ('_bitarray',[(0,7)]),  #48
    ('_struct',[[('m_allowedColors',45,-6),('m_allowedRaces',46,-5),('m_allowedDifficulty',45,-4),('m_allowedControls',46,-3),('m_allowedObserveTypes',47,-2),('m_allowedAIBuilds',48,-1)]]),  #49
    ('_array',[(0,5),49]),  #50
    ('_struct',[[('m_randomValue',5,-25),('m_gameCacheName',24,-24),('m_gameOptions',42,-23),('m_gameSpeed',12,-22),('m_gameType',12,-21),('m_maxUsers',7,-20),('m_maxObservers',7,-19),('m_maxPlayers',7,-18),('m_maxTeams',43,-17),('m_maxColors',2,-16),('m_maxRaces',44,-15),('m_maxControls',44,-14),('m_mapSizeX',10,-13),('m_mapSizeY',10,-12),('m_mapFileSyncChecksum',5,-11),('m_mapFileName',25,-10),('m_mapAuthorName',9,-9),('m_modFileSyncChecksum',5,-8),('m_slotDescriptions',50,-7),('m_defaultDifficulty',2,-6),('m_defaultAIBuild',0,-5),('m_cacheHandles',31,-4),('m_isBlizzardMap',27,-3),('m_isPremadeFFA',27,-2),('m_isCoopMode',27,-1)]]),  #51
    ('_optional',[1]),  #52
    ('_optional',[7]),  #53
    ('_struct',[[('m_color',53,-1)]]),  #54
    ('_array',[(0,6),5]),  #55
    ('_array',[(0,9),5]),  #56
    ('_struct',[[('m_control',10,-13),('m_userId',52,-12),('m_teamId',1,-11),('m_colorPref',54,-10),('m_racePref',38,-9),('m_difficulty',2,-8),('m_aiBuild',0,-7),('m_handicap',0,-6),('m_observe',19,-5),('m_workingSetSlotId',20,-4),('m_rewards',55,-3),('m_toonHandle',15,-2),('m_licenses',56,-1)]]),  #57
    ('_array',[(0,5),57]),  #58
    ('_struct',[[('m_phase',12,-10),('m_maxUsers',7,-9),('m_maxObservers',7,-8),('m_slots',58,-7),('m_randomSeed',5,-6),('m_hostUserId',52,-5),('m_isSinglePlayer',27,-4),('m_gameDuration',5,-3),('m_defaultDifficulty',2,-2),('m_defaultAIBuild',0,-1)]]),  #59
    ('_struct',[[('m_userInitialData',41,-3),('m_gameDescription',51,-2),('m_lobbyState',59,-1)]]),  #60
    ('_struct',[[('m_syncLobbyState',60,-1)]]),  #61
    ('_struct',[[('m_name',15,-6)]]),  #62
    ('_blob',[(0,6)]),  #63
    ('_struct',[[('m_name',63,-6)]]),  #64
    ('_struct',[[('m_name',63,-8),('m_type',5,-7),('m_data',15,-6)]]),  #65
    ('_struct',[[('m_type',5,-8),('m_name',63,-7),('m_data',29,-6)]]),  #66
    ('_array',[(0,5),10]),  #67
    ('_struct',[[('m_signature',67,-7),('m_toonHandle',15,-6)]]),  #68
    ('_struct',[[('m_gameFullyDownloaded',27,-12),('m_developmentCheatsEnabled',27,-11),('m_multiplayerCheatsEnabled',27,-10),('m_syncChecksummingEnabled',27,-9),('m_isMapToMapTransition',27,-8),('m_startingRally',27,-7),('m_baseBuildNum',5,-6)]]),  #69
    ('_struct',[[]]),  #70
    ('_struct',[[('m_fileName',25,-10),('m_automatic',27,-9),('m_overwrite',27,-8),('m_name',9,-7),('m_description',24,-6)]]),  #71
    ('_int',[(-2147483648,32)]),  #72
    ('_struct',[[('x',72,-2),('y',72,-1)]]),  #73
    ('_struct',[[('m_point',73,-4),('m_time',72,-3),('m_verb',24,-2),('m_arguments',24,-1)]]),  #74
    ('_struct',[[('m_data',74,-6)]]),  #75
    ('_int',[(0,20)]),  #76
    ('_int',[(0,16)]),  #77
    ('_struct',[[('m_abilLink',77,-3),('m_abilCmdIndex',7,-2),('m_abilCmdData',20,-1)]]),  #78
    ('_optional',[78]),  #79
    ('_null',[]),  #80
    ('_struct',[[('x',76,-3),('y',76,-2),('z',72,-1)]]),  #81
    ('_struct',[[('m_targetUnitFlags',10,-7),('m_timer',10,-6),('m_tag',5,-5),('m_snapshotUnitLink',77,-4),('m_snapshotControlPlayerId',52,-3),('m_snapshotUpkeepPlayerId',52,-2),('m_snapshotPoint',81,-1)]]),  #82
    ('_choice',[(0,2),{0:('None',80),1:('TargetPoint',81),2:('TargetUnit',82),3:('Data',5)}]),  #83
    ('_struct',[[('m_cmdFlags',76,-9),('m_abil',79,-8),('m_data',83,-7),('m_otherUnit',37,-6)]]),  #84
    ('_int',[(0,9)]),  #85
    ('_bitarray',[(0,9)]),  #86
    ('_array',[(0,9),85]),  #87
    ('_choice',[(0,2),{0:('None',80),1:('Mask',86),2:('OneIndices',87),3:('ZeroIndices',87)}]),  #88
    ('_struct',[[('m_unitLink',77,-4),('m_subgroupPriority',10,-3),('m_intraSubgroupPriority',10,-2),('m_count',85,-1)]]),  #89
    ('_array',[(0,9),89]),  #90
    ('_struct',[[('m_subgroupIndex',85,-4),('m_removeMask',88,-3),('m_addSubgroups',90,-2),('m_addUnitTags',56,-1)]]),  #91
    ('_struct',[[('m_controlGroupId',1,-7),('m_delta',91,-6)]]),  #92
    ('_struct',[[('m_controlGroupIndex',1,-8),('m_controlGroupUpdate',19,-7),('m_mask',88,-6)]]),  #93
    ('_struct',[[('m_count',85,-6),('m_subgroupCount',85,-5),('m_activeSubgroupIndex',85,-4),('m_unitTagsChecksum',5,-3),('m_subgroupIndicesChecksum',5,-2),('m_subgroupsChecksum',5,-1)]]),  #94
    ('_struct',[[('m_controlGroupId',1,-7),('m_selectionSyncData',94,-6)]]),  #95
    ('_array',[(0,3),72]),  #96
    ('_struct',[[('m_recipientId',1,-7),('m_resources',96,-6)]]),  #97
    ('_struct',[[('m_chatMessage',24,-6)]]),  #98
    ('_int',[(-128,8)]),  #99
    ('_struct',[[('x',72,-3),('y',72,-2),('z',72,-1)]]),  #100
    ('_struct',[[('m_beacon',99,-14),('m_ally',99,-13),('m_flags',99,-12),('m_build',99,-11),('m_targetUnitTag',5,-10),('m_targetUnitSnapshotUnitLink',77,-9),('m_targetUnitSnapshotUpkeepPlayerId',99,-8),('m_targetUnitSnapshotControlPlayerId',99,-7),('m_targetPoint',100,-6)]]),  #101
    ('_struct',[[('m_speed',12,-6)]]),  #102
    ('_struct',[[('m_delta',99,-6)]]),  #103
    ('_struct',[[('m_point',73,-8),('m_unit',5,-7),('m_pingedMinimap',27,-6)]]),  #104
    ('_struct',[[('m_verb',24,-7),('m_arguments',24,-6)]]),  #105
    ('_struct',[[('m_alliance',5,-7),('m_control',5,-6)]]),  #106
    ('_struct',[[('m_unitTag',5,-6)]]),  #107
    ('_struct',[[('m_unitTag',5,-7),('m_flags',10,-6)]]),  #108
    ('_struct',[[('m_conversationId',72,-7),('m_replyId',72,-6)]]),  #109
    ('_optional',[15]),  #110
    ('_struct',[[('m_gameUserId',1,-5),('m_observe',19,-4),('m_name',9,-3),('m_toonHandle',110,-2),('m_clanTag',36,-1)]]),  #111
    ('_array',[(0,5),111]),  #112
    ('_int',[(0,1)]),  #113
    ('_struct',[[('m_userInfos',112,-7),('m_method',113,-6)]]),  #114
    ('_struct',[[('m_purchaseItemId',72,-6)]]),  #115
    ('_struct',[[('m_difficultyLevel',72,-6)]]),  #116
    ('_choice',[(0,3),{0:('None',80),1:('Checked',27),2:('ValueChanged',5),3:('SelectionChanged',72),4:('TextChanged',25),5:('MouseButton',5)}]),  #117
    ('_struct',[[('m_controlId',72,-8),('m_eventType',72,-7),('m_eventData',117,-6)]]),  #118
    ('_struct',[[('m_soundHash',5,-7),('m_length',5,-6)]]),  #119
    ('_array',[(0,7),5]),  #120
    ('_struct',[[('m_soundHash',120,-2),('m_length',120,-1)]]),  #121
    ('_struct',[[('m_syncInfo',121,-6)]]),  #122
    ('_struct',[[('m_sound',5,-6)]]),  #123
    ('_struct',[[('m_transmissionId',72,-7),('m_thread',5,-6)]]),  #124
    ('_struct',[[('m_transmissionId',72,-6)]]),  #125
    ('_struct',[[('x',77,-2),('y',77,-1)]]),  #126
    ('_optional',[126]),  #127
    ('_optional',[77]),  #128
    ('_struct',[[('m_target',127,-9),('m_distance',128,-8),('m_pitch',128,-7),('m_yaw',128,-6)]]),  #129
    ('_struct',[[('m_skipType',113,-6)]]),  #130
    ('_int',[(0,11)]),  #131
    ('_struct',[[('x',131,-2),('y',131,-1)]]),  #132
    ('_struct',[[('m_button',5,-9),('m_down',27,-8),('m_posUI',132,-7),('m_posWorld',81,-6)]]),  #133
    ('_struct',[[('m_posUI',132,-7),('m_posWorld',81,-6)]]),  #134
    ('_struct',[[('m_achievementLink',77,-6)]]),  #135
    ('_struct',[[('m_abilLink',77,-8),('m_abilCmdIndex',7,-7),('m_state',99,-6)]]),  #136
    ('_struct',[[('m_soundtrack',5,-6)]]),  #137
    ('_struct',[[('m_planetId',72,-6)]]),  #138
    ('_struct',[[('m_key',99,-7),('m_flags',99,-6)]]),  #139
    ('_struct',[[('m_resources',96,-6)]]),  #140
    ('_struct',[[('m_fulfillRequestId',72,-6)]]),  #141
    ('_struct',[[('m_cancelRequestId',72,-6)]]),  #142
    ('_struct',[[('m_researchItemId',72,-6)]]),  #143
    ('_struct',[[('m_mercenaryId',72,-6)]]),  #144
    ('_struct',[[('m_battleReportId',72,-7),('m_difficultyLevel',72,-6)]]),  #145
    ('_struct',[[('m_battleReportId',72,-6)]]),  #146
    ('_int',[(0,19)]),  #147
    ('_struct',[[('m_decrementMs',147,-6)]]),  #148
    ('_struct',[[('m_portraitId',72,-6)]]),  #149
    ('_struct',[[('m_functionName',15,-6)]]),  #150
    ('_struct',[[('m_result',72,-6)]]),  #151
    ('_struct',[[('m_gameMenuItemIndex',72,-6)]]),  #152
    ('_struct',[[('m_reason',99,-6)]]),  #153
    ('_struct',[[('m_purchaseCategoryId',72,-6)]]),  #154
    ('_struct',[[('m_button',77,-6)]]),  #155
    ('_struct',[[('m_cutsceneId',72,-7),('m_bookmarkName',15,-6)]]),  #156
    ('_struct',[[('m_cutsceneId',72,-6)]]),  #157
    ('_struct',[[('m_cutsceneId',72,-8),('m_conversationLine',15,-7),('m_altConversationLine',15,-6)]]),  #158
    ('_struct',[[('m_cutsceneId',72,-7),('m_conversationLine',15,-6)]]),  #159
    ('_struct',[[('m_observe',19,-9),('m_name',9,-8),('m_toonHandle',110,-7),('m_clanTag',36,-6)]]),  #160
    ('_struct',[[('m_recipient',12,-3),('m_string',25,-2)]]),  #161
    ('_struct',[[('m_recipient',12,-3),('m_point',73,-2)]]),  #162
    ('_struct',[[('m_progress',72,-2)]]),  #163
]

# Map from protocol NNet.Game.*Event eventid to (typeid, name)
game_event_types = {
    5: (70, 'NNet.Game.SUserFinishedLoadingSyncEvent'),
    7: (69, 'NNet.Game.SUserOptionsEvent'),
    9: (62, 'NNet.Game.SBankFileEvent'),
    10: (64, 'NNet.Game.SBankSectionEvent'),
    11: (65, 'NNet.Game.SBankKeyEvent'),
    12: (66, 'NNet.Game.SBankValueEvent'),
    13: (68, 'NNet.Game.SBankSignatureEvent'),
    21: (71, 'NNet.Game.SSaveGameEvent'),
    22: (70, 'NNet.Game.SSaveGameDoneEvent'),
    23: (70, 'NNet.Game.SLoadGameDoneEvent'),
    26: (75, 'NNet.Game.SGameCheatEvent'),
    27: (84, 'NNet.Game.SCmdEvent'),
    28: (92, 'NNet.Game.SSelectionDeltaEvent'),
    29: (93, 'NNet.Game.SControlGroupUpdateEvent'),
    30: (95, 'NNet.Game.SSelectionSyncCheckEvent'),
    31: (97, 'NNet.Game.SResourceTradeEvent'),
    32: (98, 'NNet.Game.STriggerChatMessageEvent'),
    33: (101, 'NNet.Game.SAICommunicateEvent'),
    34: (102, 'NNet.Game.SSetAbsoluteGameSpeedEvent'),
    35: (103, 'NNet.Game.SAddAbsoluteGameSpeedEvent'),
    36: (104, 'NNet.Game.STriggerPingEvent'),
    37: (105, 'NNet.Game.SBroadcastCheatEvent'),
    38: (106, 'NNet.Game.SAllianceEvent'),
    39: (107, 'NNet.Game.SUnitClickEvent'),
    40: (108, 'NNet.Game.SUnitHighlightEvent'),
    41: (109, 'NNet.Game.STriggerReplySelectedEvent'),
    43: (114, 'NNet.Game.SHijackReplayGameEvent'),
    44: (70, 'NNet.Game.STriggerSkippedEvent'),
    45: (119, 'NNet.Game.STriggerSoundLengthQueryEvent'),
    46: (123, 'NNet.Game.STriggerSoundOffsetEvent'),
    47: (124, 'NNet.Game.STriggerTransmissionOffsetEvent'),
    48: (125, 'NNet.Game.STriggerTransmissionCompleteEvent'),
    49: (129, 'NNet.Game.SCameraUpdateEvent'),
    50: (70, 'NNet.Game.STriggerAbortMissionEvent'),
    51: (115, 'NNet.Game.STriggerPurchaseMadeEvent'),
    52: (70, 'NNet.Game.STriggerPurchaseExitEvent'),
    53: (116, 'NNet.Game.STriggerPlanetMissionLaunchedEvent'),
    54: (70, 'NNet.Game.STriggerPlanetPanelCanceledEvent'),
    55: (118, 'NNet.Game.STriggerDialogControlEvent'),
    56: (122, 'NNet.Game.STriggerSoundLengthSyncEvent'),
    57: (130, 'NNet.Game.STriggerConversationSkippedEvent'),
    58: (133, 'NNet.Game.STriggerMouseClickedEvent'),
    59: (134, 'NNet.Game.STriggerMouseMovedEvent'),
    60: (135, 'NNet.Game.SAchievementAwardedEvent'),
    62: (136, 'NNet.Game.STriggerTargetModeUpdateEvent'),
    63: (70, 'NNet.Game.STriggerPlanetPanelReplayEvent'),
    64: (137, 'NNet.Game.STriggerSoundtrackDoneEvent'),
    65: (138, 'NNet.Game.STriggerPlanetMissionSelectedEvent'),
    66: (139, 'NNet.Game.STriggerKeyPressedEvent'),
    67: (150, 'NNet.Game.STriggerMovieFunctionEvent'),
    68: (70, 'NNet.Game.STriggerPlanetPanelBirthCompleteEvent'),
    69: (70, 'NNet.Game.STriggerPlanetPanelDeathCompleteEvent'),
    70: (140, 'NNet.Game.SResourceRequestEvent'),
    71: (141, 'NNet.Game.SResourceRequestFulfillEvent'),
    72: (142, 'NNet.Game.SResourceRequestCancelEvent'),
    73: (70, 'NNet.Game.STriggerResearchPanelExitEvent'),
    74: (70, 'NNet.Game.STriggerResearchPanelPurchaseEvent'),
    75: (143, 'NNet.Game.STriggerResearchPanelSelectionChangedEvent'),
    77: (70, 'NNet.Game.STriggerMercenaryPanelExitEvent'),
    78: (70, 'NNet.Game.STriggerMercenaryPanelPurchaseEvent'),
    79: (144, 'NNet.Game.STriggerMercenaryPanelSelectionChangedEvent'),
    80: (70, 'NNet.Game.STriggerVictoryPanelExitEvent'),
    81: (70, 'NNet.Game.STriggerBattleReportPanelExitEvent'),
    82: (145, 'NNet.Game.STriggerBattleReportPanelPlayMissionEvent'),
    83: (146, 'NNet.Game.STriggerBattleReportPanelPlaySceneEvent'),
    84: (146, 'NNet.Game.STriggerBattleReportPanelSelectionChangedEvent'),
    85: (116, 'NNet.Game.STriggerVictoryPanelPlayMissionAgainEvent'),
    86: (70, 'NNet.Game.STriggerMovieStartedEvent'),
    87: (70, 'NNet.Game.STriggerMovieFinishedEvent'),
    88: (148, 'NNet.Game.SDecrementGameTimeRemainingEvent'),
    89: (149, 'NNet.Game.STriggerPortraitLoadedEvent'),
    90: (151, 'NNet.Game.STriggerCustomDialogDismissedEvent'),
    91: (152, 'NNet.Game.STriggerGameMenuItemSelectedEvent'),
    92: (153, 'NNet.Game.STriggerCameraMoveEvent'),
    93: (115, 'NNet.Game.STriggerPurchasePanelSelectedPurchaseItemChangedEvent'),
    94: (154, 'NNet.Game.STriggerPurchasePanelSelectedPurchaseCategoryChangedEvent'),
    95: (155, 'NNet.Game.STriggerButtonPressedEvent'),
    96: (70, 'NNet.Game.STriggerGameCreditsFinishedEvent'),
    97: (156, 'NNet.Game.STriggerCutsceneBookmarkFiredEvent'),
    98: (157, 'NNet.Game.STriggerCutsceneEndSceneFiredEvent'),
    99: (158, 'NNet.Game.STriggerCutsceneConversationLineEvent'),
    100: (159, 'NNet.Game.STriggerCutsceneConversationLineMissingEvent'),
    101: (70, 'NNet.Game.SGameUserLeaveEvent'),
    102: (160, 'NNet.Game.SGameUserJoinEvent'),
}

# The typeid of the NNet.Game.EEventId enum.
game_eventid_typeid = 0

# Map from protocol NNet.Game.*Message eventid to (typeid, name)
message_event_types = {
    0: (161, 'NNet.Game.SChatMessage'),
    1: (162, 'NNet.Game.SPingMessage'),
    2: (163, 'NNet.Game.SLoadingProgressMessage'),
    3: (70, 'NNet.Game.SServerPingMessage'),
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
replay_userid_typeid = 8

# The typeid of NNet.Replay.SHeader (the type used to store replay game version and length).
replay_header_typeid = 13

# The typeid of NNet.Game.SDetails (the type used to store overall replay details).
game_details_typeid = 35

# The typeid of NNet.Replay.SInitData (the type used to store the inital lobby).
replay_initdata_typeid = 61


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
