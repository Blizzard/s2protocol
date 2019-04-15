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
    ('_int',[(0,5)]),  #2
    ('_int',[(0,6)]),  #3
    ('_int',[(0,14)]),  #4
    ('_int',[(0,22)]),  #5
    ('_int',[(0,32)]),  #6
    ('_choice',[(0,2),{0:('m_uint6',3),1:('m_uint14',4),2:('m_uint22',5),3:('m_uint32',6)}]),  #7
    ('_struct',[[('m_userId',2,-1)]]),  #8
    ('_blob',[(0,8)]),  #9
    ('_int',[(0,8)]),  #10
    ('_struct',[[('m_flags',10,0),('m_major',10,1),('m_minor',10,2),('m_revision',10,3),('m_build',6,4),('m_baseBuild',6,5)]]),  #11
    ('_int',[(0,3)]),  #12
    ('_bool',[]),  #13
    ('_struct',[[('m_signature',9,0),('m_version',11,1),('m_type',12,2),('m_elapsedGameLoops',6,3),('m_useScaledTime',13,4)]]),  #14
    ('_fourcc',[]),  #15
    ('_blob',[(0,7)]),  #16
    ('_int',[(0,64)]),  #17
    ('_struct',[[('m_region',10,0),('m_programId',15,1),('m_realm',6,2),('m_name',16,3),('m_id',17,4)]]),  #18
    ('_struct',[[('m_a',10,0),('m_r',10,1),('m_g',10,2),('m_b',10,3)]]),  #19
    ('_int',[(0,2)]),  #20
    ('_optional',[10]),  #21
    ('_struct',[[('m_name',9,0),('m_toon',18,1),('m_race',9,2),('m_color',19,3),('m_control',10,4),('m_teamId',1,5),('m_handicap',0,6),('m_observe',20,7),('m_result',20,8),('m_workingSetSlotId',21,9)]]),  #22
    ('_array',[(0,5),22]),  #23
    ('_optional',[23]),  #24
    ('_blob',[(0,10)]),  #25
    ('_blob',[(0,11)]),  #26
    ('_struct',[[('m_file',26,0)]]),  #27
    ('_optional',[13]),  #28
    ('_int',[(-9223372036854775808,64)]),  #29
    ('_blob',[(0,12)]),  #30
    ('_blob',[(40,0)]),  #31
    ('_array',[(0,6),31]),  #32
    ('_optional',[32]),  #33
    ('_array',[(0,6),26]),  #34
    ('_optional',[34]),  #35
    ('_struct',[[('m_playerList',24,0),('m_title',25,1),('m_difficulty',9,2),('m_thumbnail',27,3),('m_isBlizzardMap',13,4),('m_restartAsTransitionMap',28,16),('m_timeUTC',29,5),('m_timeLocalOffset',29,6),('m_description',30,7),('m_imageFilePath',26,8),('m_campaignIndex',10,15),('m_mapFileName',26,9),('m_cacheHandles',33,10),('m_miniSave',13,11),('m_gameSpeed',12,12),('m_defaultDifficulty',3,13),('m_modPaths',35,14)]]),  #36
    ('_optional',[9]),  #37
    ('_optional',[6]),  #38
    ('_struct',[[('m_race',21,-1)]]),  #39
    ('_struct',[[('m_team',21,-1)]]),  #40
    ('_struct',[[('m_name',9,-12),('m_clanTag',37,-11),('m_highestLeague',21,-10),('m_combinedRaceLevels',38,-9),('m_randomSeed',6,-8),('m_racePreference',39,-7),('m_teamPreference',40,-6),('m_testMap',13,-5),('m_testAuto',13,-4),('m_examine',13,-3),('m_customInterface',13,-2),('m_observe',20,-1)]]),  #41
    ('_array',[(0,5),41]),  #42
    ('_struct',[[('m_lockTeams',13,-12),('m_teamsTogether',13,-11),('m_advancedSharedControl',13,-10),('m_randomRaces',13,-9),('m_battleNet',13,-8),('m_amm',13,-7),('m_competitive',13,-6),('m_noVictoryOrDefeat',13,-5),('m_fog',20,-4),('m_observers',20,-3),('m_userDifficulty',20,-2),('m_clientDebugFlags',17,-1)]]),  #43
    ('_int',[(1,4)]),  #44
    ('_int',[(1,8)]),  #45
    ('_bitarray',[(0,6)]),  #46
    ('_bitarray',[(0,8)]),  #47
    ('_bitarray',[(0,2)]),  #48
    ('_bitarray',[(0,7)]),  #49
    ('_struct',[[('m_allowedColors',46,-6),('m_allowedRaces',47,-5),('m_allowedDifficulty',46,-4),('m_allowedControls',47,-3),('m_allowedObserveTypes',48,-2),('m_allowedAIBuilds',49,-1)]]),  #50
    ('_array',[(0,5),50]),  #51
    ('_struct',[[('m_randomValue',6,-25),('m_gameCacheName',25,-24),('m_gameOptions',43,-23),('m_gameSpeed',12,-22),('m_gameType',12,-21),('m_maxUsers',2,-20),('m_maxObservers',2,-19),('m_maxPlayers',2,-18),('m_maxTeams',44,-17),('m_maxColors',3,-16),('m_maxRaces',45,-15),('m_maxControls',10,-14),('m_mapSizeX',10,-13),('m_mapSizeY',10,-12),('m_mapFileSyncChecksum',6,-11),('m_mapFileName',26,-10),('m_mapAuthorName',9,-9),('m_modFileSyncChecksum',6,-8),('m_slotDescriptions',51,-7),('m_defaultDifficulty',3,-6),('m_defaultAIBuild',0,-5),('m_cacheHandles',32,-4),('m_isBlizzardMap',13,-3),('m_isPremadeFFA',13,-2),('m_isCoopMode',13,-1)]]),  #52
    ('_optional',[1]),  #53
    ('_optional',[2]),  #54
    ('_struct',[[('m_color',54,-1)]]),  #55
    ('_array',[(0,6),6]),  #56
    ('_array',[(0,9),6]),  #57
    ('_struct',[[('m_control',10,-13),('m_userId',53,-12),('m_teamId',1,-11),('m_colorPref',55,-10),('m_racePref',39,-9),('m_difficulty',3,-8),('m_aiBuild',0,-7),('m_handicap',0,-6),('m_observe',20,-5),('m_workingSetSlotId',21,-4),('m_rewards',56,-3),('m_toonHandle',16,-2),('m_licenses',57,-1)]]),  #58
    ('_array',[(0,5),58]),  #59
    ('_struct',[[('m_phase',12,-10),('m_maxUsers',2,-9),('m_maxObservers',2,-8),('m_slots',59,-7),('m_randomSeed',6,-6),('m_hostUserId',53,-5),('m_isSinglePlayer',13,-4),('m_gameDuration',6,-3),('m_defaultDifficulty',3,-2),('m_defaultAIBuild',0,-1)]]),  #60
    ('_struct',[[('m_userInitialData',42,-3),('m_gameDescription',52,-2),('m_lobbyState',60,-1)]]),  #61
    ('_struct',[[('m_syncLobbyState',61,-1)]]),  #62
    ('_struct',[[('m_name',16,-6)]]),  #63
    ('_blob',[(0,6)]),  #64
    ('_struct',[[('m_name',64,-6)]]),  #65
    ('_struct',[[('m_name',64,-8),('m_type',6,-7),('m_data',16,-6)]]),  #66
    ('_struct',[[('m_type',6,-8),('m_name',64,-7),('m_data',30,-6)]]),  #67
    ('_array',[(0,5),10]),  #68
    ('_struct',[[('m_signature',68,-7),('m_toonHandle',16,-6)]]),  #69
    ('_struct',[[('m_gameFullyDownloaded',13,-13),('m_developmentCheatsEnabled',13,-12),('m_multiplayerCheatsEnabled',13,-11),('m_syncChecksummingEnabled',13,-10),('m_isMapToMapTransition',13,-9),('m_startingRally',13,-8),('m_debugPauseEnabled',13,-7),('m_baseBuildNum',6,-6)]]),  #70
    ('_struct',[[]]),  #71
    ('_int',[(0,16)]),  #72
    ('_struct',[[('x',72,-2),('y',72,-1)]]),  #73
    ('_struct',[[('m_which',12,-7),('m_target',73,-6)]]),  #74
    ('_struct',[[('m_fileName',26,-10),('m_automatic',13,-9),('m_overwrite',13,-8),('m_name',9,-7),('m_description',25,-6)]]),  #75
    ('_int',[(-2147483648,32)]),  #76
    ('_struct',[[('x',76,-2),('y',76,-1)]]),  #77
    ('_struct',[[('m_point',77,-4),('m_time',76,-3),('m_verb',25,-2),('m_arguments',25,-1)]]),  #78
    ('_struct',[[('m_data',78,-6)]]),  #79
    ('_int',[(0,20)]),  #80
    ('_struct',[[('m_abilLink',72,-3),('m_abilCmdIndex',2,-2),('m_abilCmdData',21,-1)]]),  #81
    ('_optional',[81]),  #82
    ('_null',[]),  #83
    ('_struct',[[('x',80,-3),('y',80,-2),('z',76,-1)]]),  #84
    ('_struct',[[('m_targetUnitFlags',10,-7),('m_timer',10,-6),('m_tag',6,-5),('m_snapshotUnitLink',72,-4),('m_snapshotControlPlayerId',53,-3),('m_snapshotUpkeepPlayerId',53,-2),('m_snapshotPoint',84,-1)]]),  #85
    ('_choice',[(0,2),{0:('None',83),1:('TargetPoint',84),2:('TargetUnit',85),3:('Data',6)}]),  #86
    ('_struct',[[('m_cmdFlags',80,-9),('m_abil',82,-8),('m_data',86,-7),('m_otherUnit',38,-6)]]),  #87
    ('_int',[(0,9)]),  #88
    ('_bitarray',[(0,9)]),  #89
    ('_array',[(0,9),88]),  #90
    ('_choice',[(0,2),{0:('None',83),1:('Mask',89),2:('OneIndices',90),3:('ZeroIndices',90)}]),  #91
    ('_struct',[[('m_unitLink',72,-4),('m_subgroupPriority',10,-3),('m_intraSubgroupPriority',10,-2),('m_count',88,-1)]]),  #92
    ('_array',[(0,9),92]),  #93
    ('_struct',[[('m_subgroupIndex',88,-4),('m_removeMask',91,-3),('m_addSubgroups',93,-2),('m_addUnitTags',57,-1)]]),  #94
    ('_struct',[[('m_controlGroupId',1,-7),('m_delta',94,-6)]]),  #95
    ('_struct',[[('m_controlGroupIndex',1,-8),('m_controlGroupUpdate',20,-7),('m_mask',91,-6)]]),  #96
    ('_struct',[[('m_count',88,-6),('m_subgroupCount',88,-5),('m_activeSubgroupIndex',88,-4),('m_unitTagsChecksum',6,-3),('m_subgroupIndicesChecksum',6,-2),('m_subgroupsChecksum',6,-1)]]),  #97
    ('_struct',[[('m_controlGroupId',1,-7),('m_selectionSyncData',97,-6)]]),  #98
    ('_array',[(0,3),76]),  #99
    ('_struct',[[('m_recipientId',1,-7),('m_resources',99,-6)]]),  #100
    ('_struct',[[('m_chatMessage',25,-6)]]),  #101
    ('_int',[(-128,8)]),  #102
    ('_struct',[[('x',76,-3),('y',76,-2),('z',76,-1)]]),  #103
    ('_struct',[[('m_beacon',102,-14),('m_ally',102,-13),('m_flags',102,-12),('m_build',102,-11),('m_targetUnitTag',6,-10),('m_targetUnitSnapshotUnitLink',72,-9),('m_targetUnitSnapshotUpkeepPlayerId',102,-8),('m_targetUnitSnapshotControlPlayerId',102,-7),('m_targetPoint',103,-6)]]),  #104
    ('_struct',[[('m_speed',12,-6)]]),  #105
    ('_struct',[[('m_delta',102,-6)]]),  #106
    ('_struct',[[('m_point',77,-8),('m_unit',6,-7),('m_pingedMinimap',13,-6)]]),  #107
    ('_struct',[[('m_verb',25,-7),('m_arguments',25,-6)]]),  #108
    ('_struct',[[('m_alliance',6,-7),('m_control',6,-6)]]),  #109
    ('_struct',[[('m_unitTag',6,-6)]]),  #110
    ('_struct',[[('m_unitTag',6,-7),('m_flags',10,-6)]]),  #111
    ('_struct',[[('m_conversationId',76,-7),('m_replyId',76,-6)]]),  #112
    ('_optional',[16]),  #113
    ('_struct',[[('m_gameUserId',1,-5),('m_observe',20,-4),('m_name',9,-3),('m_toonHandle',113,-2),('m_clanTag',37,-1)]]),  #114
    ('_array',[(0,5),114]),  #115
    ('_int',[(0,1)]),  #116
    ('_struct',[[('m_userInfos',115,-7),('m_method',116,-6)]]),  #117
    ('_struct',[[('m_purchaseItemId',76,-6)]]),  #118
    ('_struct',[[('m_difficultyLevel',76,-6)]]),  #119
    ('_choice',[(0,3),{0:('None',83),1:('Checked',13),2:('ValueChanged',6),3:('SelectionChanged',76),4:('TextChanged',26),5:('MouseButton',6)}]),  #120
    ('_struct',[[('m_controlId',76,-8),('m_eventType',76,-7),('m_eventData',120,-6)]]),  #121
    ('_struct',[[('m_soundHash',6,-7),('m_length',6,-6)]]),  #122
    ('_array',[(0,7),6]),  #123
    ('_struct',[[('m_soundHash',123,-2),('m_length',123,-1)]]),  #124
    ('_struct',[[('m_syncInfo',124,-6)]]),  #125
    ('_struct',[[('m_sound',6,-6)]]),  #126
    ('_struct',[[('m_transmissionId',76,-7),('m_thread',6,-6)]]),  #127
    ('_struct',[[('m_transmissionId',76,-6)]]),  #128
    ('_optional',[73]),  #129
    ('_optional',[72]),  #130
    ('_struct',[[('m_target',129,-9),('m_distance',130,-8),('m_pitch',130,-7),('m_yaw',130,-6)]]),  #131
    ('_struct',[[('m_skipType',116,-6)]]),  #132
    ('_int',[(0,11)]),  #133
    ('_struct',[[('x',133,-2),('y',133,-1)]]),  #134
    ('_struct',[[('m_button',6,-10),('m_down',13,-9),('m_posUI',134,-8),('m_posWorld',84,-7),('m_flags',102,-6)]]),  #135
    ('_struct',[[('m_posUI',134,-8),('m_posWorld',84,-7),('m_flags',102,-6)]]),  #136
    ('_struct',[[('m_achievementLink',72,-6)]]),  #137
    ('_struct',[[('m_abilLink',72,-8),('m_abilCmdIndex',2,-7),('m_state',102,-6)]]),  #138
    ('_struct',[[('m_soundtrack',6,-6)]]),  #139
    ('_struct',[[('m_planetId',76,-6)]]),  #140
    ('_struct',[[('m_key',102,-7),('m_flags',102,-6)]]),  #141
    ('_struct',[[('m_resources',99,-6)]]),  #142
    ('_struct',[[('m_fulfillRequestId',76,-6)]]),  #143
    ('_struct',[[('m_cancelRequestId',76,-6)]]),  #144
    ('_struct',[[('m_researchItemId',76,-6)]]),  #145
    ('_struct',[[('m_mercenaryId',76,-6)]]),  #146
    ('_struct',[[('m_battleReportId',76,-7),('m_difficultyLevel',76,-6)]]),  #147
    ('_struct',[[('m_battleReportId',76,-6)]]),  #148
    ('_int',[(0,19)]),  #149
    ('_struct',[[('m_decrementMs',149,-6)]]),  #150
    ('_struct',[[('m_portraitId',76,-6)]]),  #151
    ('_struct',[[('m_functionName',16,-6)]]),  #152
    ('_struct',[[('m_result',76,-6)]]),  #153
    ('_struct',[[('m_gameMenuItemIndex',76,-6)]]),  #154
    ('_struct',[[('m_reason',102,-6)]]),  #155
    ('_struct',[[('m_purchaseCategoryId',76,-6)]]),  #156
    ('_struct',[[('m_button',72,-6)]]),  #157
    ('_struct',[[('m_cutsceneId',76,-7),('m_bookmarkName',16,-6)]]),  #158
    ('_struct',[[('m_cutsceneId',76,-6)]]),  #159
    ('_struct',[[('m_cutsceneId',76,-8),('m_conversationLine',16,-7),('m_altConversationLine',16,-6)]]),  #160
    ('_struct',[[('m_cutsceneId',76,-7),('m_conversationLine',16,-6)]]),  #161
    ('_struct',[[('m_observe',20,-9),('m_name',9,-8),('m_toonHandle',113,-7),('m_clanTag',37,-6)]]),  #162
    ('_struct',[[('m_recipient',12,-3),('m_string',26,-2)]]),  #163
    ('_struct',[[('m_recipient',12,-3),('m_point',77,-2)]]),  #164
    ('_struct',[[('m_progress',76,-2)]]),  #165
    ('_struct',[[('m_scoreValueMineralsCurrent',76,0),('m_scoreValueVespeneCurrent',76,1),('m_scoreValueMineralsCollectionRate',76,2),('m_scoreValueVespeneCollectionRate',76,3),('m_scoreValueWorkersActiveCount',76,4),('m_scoreValueMineralsUsedInProgressArmy',76,5),('m_scoreValueMineralsUsedInProgressEconomy',76,6),('m_scoreValueMineralsUsedInProgressTechnology',76,7),('m_scoreValueVespeneUsedInProgressArmy',76,8),('m_scoreValueVespeneUsedInProgressEconomy',76,9),('m_scoreValueVespeneUsedInProgressTechnology',76,10),('m_scoreValueMineralsUsedCurrentArmy',76,11),('m_scoreValueMineralsUsedCurrentEconomy',76,12),('m_scoreValueMineralsUsedCurrentTechnology',76,13),('m_scoreValueVespeneUsedCurrentArmy',76,14),('m_scoreValueVespeneUsedCurrentEconomy',76,15),('m_scoreValueVespeneUsedCurrentTechnology',76,16),('m_scoreValueMineralsLostArmy',76,17),('m_scoreValueMineralsLostEconomy',76,18),('m_scoreValueMineralsLostTechnology',76,19),('m_scoreValueVespeneLostArmy',76,20),('m_scoreValueVespeneLostEconomy',76,21),('m_scoreValueVespeneLostTechnology',76,22),('m_scoreValueMineralsKilledArmy',76,23),('m_scoreValueMineralsKilledEconomy',76,24),('m_scoreValueMineralsKilledTechnology',76,25),('m_scoreValueVespeneKilledArmy',76,26),('m_scoreValueVespeneKilledEconomy',76,27),('m_scoreValueVespeneKilledTechnology',76,28),('m_scoreValueFoodUsed',76,29),('m_scoreValueFoodMade',76,30),('m_scoreValueMineralsUsedActiveForces',76,31),('m_scoreValueVespeneUsedActiveForces',76,32),('m_scoreValueMineralsFriendlyFireArmy',76,33),('m_scoreValueMineralsFriendlyFireEconomy',76,34),('m_scoreValueMineralsFriendlyFireTechnology',76,35),('m_scoreValueVespeneFriendlyFireArmy',76,36),('m_scoreValueVespeneFriendlyFireEconomy',76,37),('m_scoreValueVespeneFriendlyFireTechnology',76,38)]]),  #166
    ('_struct',[[('m_playerId',1,0),('m_stats',166,1)]]),  #167
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_unitTypeName',25,2),('m_controlPlayerId',1,3),('m_upkeepPlayerId',1,4),('m_x',10,5),('m_y',10,6)]]),  #168
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_killerPlayerId',53,2),('m_x',10,3),('m_y',10,4)]]),  #169
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_controlPlayerId',1,2),('m_upkeepPlayerId',1,3)]]),  #170
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_unitTypeName',25,2)]]),  #171
    ('_struct',[[('m_playerId',1,0),('m_upgradeTypeName',25,1),('m_count',76,2)]]),  #172
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1)]]),  #173
    ('_array',[(0,10),76]),  #174
    ('_struct',[[('m_firstUnitIndex',6,0),('m_items',174,1)]]),  #175
]

# Map from protocol NNet.Game.*Event eventid to (typeid, name)
game_event_types = {
    5: (71, 'NNet.Game.SUserFinishedLoadingSyncEvent'),
    7: (70, 'NNet.Game.SUserOptionsEvent'),
    9: (63, 'NNet.Game.SBankFileEvent'),
    10: (65, 'NNet.Game.SBankSectionEvent'),
    11: (66, 'NNet.Game.SBankKeyEvent'),
    12: (67, 'NNet.Game.SBankValueEvent'),
    13: (69, 'NNet.Game.SBankSignatureEvent'),
    14: (74, 'NNet.Game.SCameraSaveEvent'),
    21: (75, 'NNet.Game.SSaveGameEvent'),
    22: (71, 'NNet.Game.SSaveGameDoneEvent'),
    23: (71, 'NNet.Game.SLoadGameDoneEvent'),
    26: (79, 'NNet.Game.SGameCheatEvent'),
    27: (87, 'NNet.Game.SCmdEvent'),
    28: (95, 'NNet.Game.SSelectionDeltaEvent'),
    29: (96, 'NNet.Game.SControlGroupUpdateEvent'),
    30: (98, 'NNet.Game.SSelectionSyncCheckEvent'),
    31: (100, 'NNet.Game.SResourceTradeEvent'),
    32: (101, 'NNet.Game.STriggerChatMessageEvent'),
    33: (104, 'NNet.Game.SAICommunicateEvent'),
    34: (105, 'NNet.Game.SSetAbsoluteGameSpeedEvent'),
    35: (106, 'NNet.Game.SAddAbsoluteGameSpeedEvent'),
    36: (107, 'NNet.Game.STriggerPingEvent'),
    37: (108, 'NNet.Game.SBroadcastCheatEvent'),
    38: (109, 'NNet.Game.SAllianceEvent'),
    39: (110, 'NNet.Game.SUnitClickEvent'),
    40: (111, 'NNet.Game.SUnitHighlightEvent'),
    41: (112, 'NNet.Game.STriggerReplySelectedEvent'),
    43: (117, 'NNet.Game.SHijackReplayGameEvent'),
    44: (71, 'NNet.Game.STriggerSkippedEvent'),
    45: (122, 'NNet.Game.STriggerSoundLengthQueryEvent'),
    46: (126, 'NNet.Game.STriggerSoundOffsetEvent'),
    47: (127, 'NNet.Game.STriggerTransmissionOffsetEvent'),
    48: (128, 'NNet.Game.STriggerTransmissionCompleteEvent'),
    49: (131, 'NNet.Game.SCameraUpdateEvent'),
    50: (71, 'NNet.Game.STriggerAbortMissionEvent'),
    51: (118, 'NNet.Game.STriggerPurchaseMadeEvent'),
    52: (71, 'NNet.Game.STriggerPurchaseExitEvent'),
    53: (119, 'NNet.Game.STriggerPlanetMissionLaunchedEvent'),
    54: (71, 'NNet.Game.STriggerPlanetPanelCanceledEvent'),
    55: (121, 'NNet.Game.STriggerDialogControlEvent'),
    56: (125, 'NNet.Game.STriggerSoundLengthSyncEvent'),
    57: (132, 'NNet.Game.STriggerConversationSkippedEvent'),
    58: (135, 'NNet.Game.STriggerMouseClickedEvent'),
    59: (136, 'NNet.Game.STriggerMouseMovedEvent'),
    60: (137, 'NNet.Game.SAchievementAwardedEvent'),
    62: (138, 'NNet.Game.STriggerTargetModeUpdateEvent'),
    63: (71, 'NNet.Game.STriggerPlanetPanelReplayEvent'),
    64: (139, 'NNet.Game.STriggerSoundtrackDoneEvent'),
    65: (140, 'NNet.Game.STriggerPlanetMissionSelectedEvent'),
    66: (141, 'NNet.Game.STriggerKeyPressedEvent'),
    67: (152, 'NNet.Game.STriggerMovieFunctionEvent'),
    68: (71, 'NNet.Game.STriggerPlanetPanelBirthCompleteEvent'),
    69: (71, 'NNet.Game.STriggerPlanetPanelDeathCompleteEvent'),
    70: (142, 'NNet.Game.SResourceRequestEvent'),
    71: (143, 'NNet.Game.SResourceRequestFulfillEvent'),
    72: (144, 'NNet.Game.SResourceRequestCancelEvent'),
    73: (71, 'NNet.Game.STriggerResearchPanelExitEvent'),
    74: (71, 'NNet.Game.STriggerResearchPanelPurchaseEvent'),
    75: (145, 'NNet.Game.STriggerResearchPanelSelectionChangedEvent'),
    77: (71, 'NNet.Game.STriggerMercenaryPanelExitEvent'),
    78: (71, 'NNet.Game.STriggerMercenaryPanelPurchaseEvent'),
    79: (146, 'NNet.Game.STriggerMercenaryPanelSelectionChangedEvent'),
    80: (71, 'NNet.Game.STriggerVictoryPanelExitEvent'),
    81: (71, 'NNet.Game.STriggerBattleReportPanelExitEvent'),
    82: (147, 'NNet.Game.STriggerBattleReportPanelPlayMissionEvent'),
    83: (148, 'NNet.Game.STriggerBattleReportPanelPlaySceneEvent'),
    84: (148, 'NNet.Game.STriggerBattleReportPanelSelectionChangedEvent'),
    85: (119, 'NNet.Game.STriggerVictoryPanelPlayMissionAgainEvent'),
    86: (71, 'NNet.Game.STriggerMovieStartedEvent'),
    87: (71, 'NNet.Game.STriggerMovieFinishedEvent'),
    88: (150, 'NNet.Game.SDecrementGameTimeRemainingEvent'),
    89: (151, 'NNet.Game.STriggerPortraitLoadedEvent'),
    90: (153, 'NNet.Game.STriggerCustomDialogDismissedEvent'),
    91: (154, 'NNet.Game.STriggerGameMenuItemSelectedEvent'),
    92: (155, 'NNet.Game.STriggerCameraMoveEvent'),
    93: (118, 'NNet.Game.STriggerPurchasePanelSelectedPurchaseItemChangedEvent'),
    94: (156, 'NNet.Game.STriggerPurchasePanelSelectedPurchaseCategoryChangedEvent'),
    95: (157, 'NNet.Game.STriggerButtonPressedEvent'),
    96: (71, 'NNet.Game.STriggerGameCreditsFinishedEvent'),
    97: (158, 'NNet.Game.STriggerCutsceneBookmarkFiredEvent'),
    98: (159, 'NNet.Game.STriggerCutsceneEndSceneFiredEvent'),
    99: (160, 'NNet.Game.STriggerCutsceneConversationLineEvent'),
    100: (161, 'NNet.Game.STriggerCutsceneConversationLineMissingEvent'),
    101: (71, 'NNet.Game.SGameUserLeaveEvent'),
    102: (162, 'NNet.Game.SGameUserJoinEvent'),
}

# The typeid of the NNet.Game.EEventId enum.
game_eventid_typeid = 0

# Map from protocol NNet.Game.*Message eventid to (typeid, name)
message_event_types = {
    0: (163, 'NNet.Game.SChatMessage'),
    1: (164, 'NNet.Game.SPingMessage'),
    2: (165, 'NNet.Game.SLoadingProgressMessage'),
    3: (71, 'NNet.Game.SServerPingMessage'),
}

# The typeid of the NNet.Game.EMessageId enum.
message_eventid_typeid = 1

# Map from protocol NNet.Replay.Tracker.*Event eventid to (typeid, name)
tracker_event_types = {
    0: (167, 'NNet.Replay.Tracker.SPlayerStatsEvent'),
    1: (168, 'NNet.Replay.Tracker.SUnitBornEvent'),
    2: (169, 'NNet.Replay.Tracker.SUnitDiedEvent'),
    3: (170, 'NNet.Replay.Tracker.SUnitOwnerChangeEvent'),
    4: (171, 'NNet.Replay.Tracker.SUnitTypeChangeEvent'),
    5: (172, 'NNet.Replay.Tracker.SUpgradeEvent'),
    6: (168, 'NNet.Replay.Tracker.SUnitInitEvent'),
    7: (173, 'NNet.Replay.Tracker.SUnitDoneEvent'),
    8: (175, 'NNet.Replay.Tracker.SUnitPositionsEvent'),
}

# NOTE: older builds may not support some types and the generated methods
# may fail to function properly, if specific backwards compatibility is 
# needed these values should be tested against for None

# The typeid of the NNet.Replay.Tracker.EEventId enum.
tracker_eventid_typeid = 2

# The typeid of NNet.SVarUint32 (the type used to encode gameloop deltas).
svaruint32_typeid = 7

# The typeid of NNet.Replay.SGameUserId (the type used to encode player ids).
replay_userid_typeid = 8

# The typeid of NNet.Replay.SHeader (the type used to store replay game version and length).
replay_header_typeid = 14

# The typeid of NNet.Game.SDetails (the type used to store overall replay details).
game_details_typeid = 36

# The typeid of NNet.Replay.SInitData (the type used to store the inital lobby).
replay_initdata_typeid = 62


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
