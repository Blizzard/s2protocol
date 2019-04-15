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
    ('_optional',[31]),  #38
    ('_optional',[6]),  #39
    ('_struct',[[('m_race',21,-1)]]),  #40
    ('_struct',[[('m_team',21,-1)]]),  #41
    ('_struct',[[('m_name',9,-13),('m_clanTag',37,-12),('m_clanLogo',38,-11),('m_highestLeague',21,-10),('m_combinedRaceLevels',39,-9),('m_randomSeed',6,-8),('m_racePreference',40,-7),('m_teamPreference',41,-6),('m_testMap',13,-5),('m_testAuto',13,-4),('m_examine',13,-3),('m_customInterface',13,-2),('m_observe',20,-1)]]),  #42
    ('_array',[(0,5),42]),  #43
    ('_struct',[[('m_lockTeams',13,-12),('m_teamsTogether',13,-11),('m_advancedSharedControl',13,-10),('m_randomRaces',13,-9),('m_battleNet',13,-8),('m_amm',13,-7),('m_competitive',13,-6),('m_noVictoryOrDefeat',13,-5),('m_fog',20,-4),('m_observers',20,-3),('m_userDifficulty',20,-2),('m_clientDebugFlags',17,-1)]]),  #44
    ('_int',[(1,4)]),  #45
    ('_int',[(1,8)]),  #46
    ('_bitarray',[(0,6)]),  #47
    ('_bitarray',[(0,8)]),  #48
    ('_bitarray',[(0,2)]),  #49
    ('_bitarray',[(0,7)]),  #50
    ('_struct',[[('m_allowedColors',47,-6),('m_allowedRaces',48,-5),('m_allowedDifficulty',47,-4),('m_allowedControls',48,-3),('m_allowedObserveTypes',49,-2),('m_allowedAIBuilds',50,-1)]]),  #51
    ('_array',[(0,5),51]),  #52
    ('_struct',[[('m_randomValue',6,-26),('m_gameCacheName',25,-25),('m_gameOptions',44,-24),('m_gameSpeed',12,-23),('m_gameType',12,-22),('m_maxUsers',2,-21),('m_maxObservers',2,-20),('m_maxPlayers',2,-19),('m_maxTeams',45,-18),('m_maxColors',3,-17),('m_maxRaces',46,-16),('m_maxControls',10,-15),('m_mapSizeX',10,-14),('m_mapSizeY',10,-13),('m_mapFileSyncChecksum',6,-12),('m_mapFileName',26,-11),('m_mapAuthorName',9,-10),('m_modFileSyncChecksum',6,-9),('m_slotDescriptions',52,-8),('m_defaultDifficulty',3,-7),('m_defaultAIBuild',0,-6),('m_cacheHandles',32,-5),('m_hasExtensionMod',13,-4),('m_isBlizzardMap',13,-3),('m_isPremadeFFA',13,-2),('m_isCoopMode',13,-1)]]),  #53
    ('_optional',[1]),  #54
    ('_optional',[2]),  #55
    ('_struct',[[('m_color',55,-1)]]),  #56
    ('_array',[(0,6),6]),  #57
    ('_array',[(0,9),6]),  #58
    ('_struct',[[('m_control',10,-13),('m_userId',54,-12),('m_teamId',1,-11),('m_colorPref',56,-10),('m_racePref',40,-9),('m_difficulty',3,-8),('m_aiBuild',0,-7),('m_handicap',0,-6),('m_observe',20,-5),('m_workingSetSlotId',21,-4),('m_rewards',57,-3),('m_toonHandle',16,-2),('m_licenses',58,-1)]]),  #59
    ('_array',[(0,5),59]),  #60
    ('_struct',[[('m_phase',12,-10),('m_maxUsers',2,-9),('m_maxObservers',2,-8),('m_slots',60,-7),('m_randomSeed',6,-6),('m_hostUserId',54,-5),('m_isSinglePlayer',13,-4),('m_gameDuration',6,-3),('m_defaultDifficulty',3,-2),('m_defaultAIBuild',0,-1)]]),  #61
    ('_struct',[[('m_userInitialData',43,-3),('m_gameDescription',53,-2),('m_lobbyState',61,-1)]]),  #62
    ('_struct',[[('m_syncLobbyState',62,-1)]]),  #63
    ('_struct',[[('m_name',16,-6)]]),  #64
    ('_blob',[(0,6)]),  #65
    ('_struct',[[('m_name',65,-6)]]),  #66
    ('_struct',[[('m_name',65,-8),('m_type',6,-7),('m_data',16,-6)]]),  #67
    ('_struct',[[('m_type',6,-8),('m_name',65,-7),('m_data',30,-6)]]),  #68
    ('_array',[(0,5),10]),  #69
    ('_struct',[[('m_signature',69,-7),('m_toonHandle',16,-6)]]),  #70
    ('_struct',[[('m_gameFullyDownloaded',13,-13),('m_developmentCheatsEnabled',13,-12),('m_multiplayerCheatsEnabled',13,-11),('m_syncChecksummingEnabled',13,-10),('m_isMapToMapTransition',13,-9),('m_startingRally',13,-8),('m_debugPauseEnabled',13,-7),('m_baseBuildNum',6,-6)]]),  #71
    ('_struct',[[]]),  #72
    ('_int',[(0,16)]),  #73
    ('_struct',[[('x',73,-2),('y',73,-1)]]),  #74
    ('_struct',[[('m_which',12,-7),('m_target',74,-6)]]),  #75
    ('_struct',[[('m_fileName',26,-10),('m_automatic',13,-9),('m_overwrite',13,-8),('m_name',9,-7),('m_description',25,-6)]]),  #76
    ('_int',[(-2147483648,32)]),  #77
    ('_struct',[[('x',77,-2),('y',77,-1)]]),  #78
    ('_struct',[[('m_point',78,-4),('m_time',77,-3),('m_verb',25,-2),('m_arguments',25,-1)]]),  #79
    ('_struct',[[('m_data',79,-6)]]),  #80
    ('_int',[(0,20)]),  #81
    ('_struct',[[('m_abilLink',73,-3),('m_abilCmdIndex',2,-2),('m_abilCmdData',21,-1)]]),  #82
    ('_optional',[82]),  #83
    ('_null',[]),  #84
    ('_struct',[[('x',81,-3),('y',81,-2),('z',77,-1)]]),  #85
    ('_struct',[[('m_targetUnitFlags',10,-7),('m_timer',10,-6),('m_tag',6,-5),('m_snapshotUnitLink',73,-4),('m_snapshotControlPlayerId',54,-3),('m_snapshotUpkeepPlayerId',54,-2),('m_snapshotPoint',85,-1)]]),  #86
    ('_choice',[(0,2),{0:('None',84),1:('TargetPoint',85),2:('TargetUnit',86),3:('Data',6)}]),  #87
    ('_struct',[[('m_cmdFlags',81,-9),('m_abil',83,-8),('m_data',87,-7),('m_otherUnit',39,-6)]]),  #88
    ('_int',[(0,9)]),  #89
    ('_bitarray',[(0,9)]),  #90
    ('_array',[(0,9),89]),  #91
    ('_choice',[(0,2),{0:('None',84),1:('Mask',90),2:('OneIndices',91),3:('ZeroIndices',91)}]),  #92
    ('_struct',[[('m_unitLink',73,-4),('m_subgroupPriority',10,-3),('m_intraSubgroupPriority',10,-2),('m_count',89,-1)]]),  #93
    ('_array',[(0,9),93]),  #94
    ('_struct',[[('m_subgroupIndex',89,-4),('m_removeMask',92,-3),('m_addSubgroups',94,-2),('m_addUnitTags',58,-1)]]),  #95
    ('_struct',[[('m_controlGroupId',1,-7),('m_delta',95,-6)]]),  #96
    ('_struct',[[('m_controlGroupIndex',1,-8),('m_controlGroupUpdate',20,-7),('m_mask',92,-6)]]),  #97
    ('_struct',[[('m_count',89,-6),('m_subgroupCount',89,-5),('m_activeSubgroupIndex',89,-4),('m_unitTagsChecksum',6,-3),('m_subgroupIndicesChecksum',6,-2),('m_subgroupsChecksum',6,-1)]]),  #98
    ('_struct',[[('m_controlGroupId',1,-7),('m_selectionSyncData',98,-6)]]),  #99
    ('_array',[(0,3),77]),  #100
    ('_struct',[[('m_recipientId',1,-7),('m_resources',100,-6)]]),  #101
    ('_struct',[[('m_chatMessage',25,-6)]]),  #102
    ('_int',[(-128,8)]),  #103
    ('_struct',[[('x',77,-3),('y',77,-2),('z',77,-1)]]),  #104
    ('_struct',[[('m_beacon',103,-14),('m_ally',103,-13),('m_flags',103,-12),('m_build',103,-11),('m_targetUnitTag',6,-10),('m_targetUnitSnapshotUnitLink',73,-9),('m_targetUnitSnapshotUpkeepPlayerId',103,-8),('m_targetUnitSnapshotControlPlayerId',103,-7),('m_targetPoint',104,-6)]]),  #105
    ('_struct',[[('m_speed',12,-6)]]),  #106
    ('_struct',[[('m_delta',103,-6)]]),  #107
    ('_struct',[[('m_point',78,-8),('m_unit',6,-7),('m_pingedMinimap',13,-6)]]),  #108
    ('_struct',[[('m_verb',25,-7),('m_arguments',25,-6)]]),  #109
    ('_struct',[[('m_alliance',6,-7),('m_control',6,-6)]]),  #110
    ('_struct',[[('m_unitTag',6,-6)]]),  #111
    ('_struct',[[('m_unitTag',6,-7),('m_flags',10,-6)]]),  #112
    ('_struct',[[('m_conversationId',77,-7),('m_replyId',77,-6)]]),  #113
    ('_optional',[16]),  #114
    ('_struct',[[('m_gameUserId',1,-6),('m_observe',20,-5),('m_name',9,-4),('m_toonHandle',114,-3),('m_clanTag',37,-2),('m_clanLogo',38,-1)]]),  #115
    ('_array',[(0,5),115]),  #116
    ('_int',[(0,1)]),  #117
    ('_struct',[[('m_userInfos',116,-7),('m_method',117,-6)]]),  #118
    ('_struct',[[('m_purchaseItemId',77,-6)]]),  #119
    ('_struct',[[('m_difficultyLevel',77,-6)]]),  #120
    ('_choice',[(0,3),{0:('None',84),1:('Checked',13),2:('ValueChanged',6),3:('SelectionChanged',77),4:('TextChanged',26),5:('MouseButton',6)}]),  #121
    ('_struct',[[('m_controlId',77,-8),('m_eventType',77,-7),('m_eventData',121,-6)]]),  #122
    ('_struct',[[('m_soundHash',6,-7),('m_length',6,-6)]]),  #123
    ('_array',[(0,7),6]),  #124
    ('_struct',[[('m_soundHash',124,-2),('m_length',124,-1)]]),  #125
    ('_struct',[[('m_syncInfo',125,-6)]]),  #126
    ('_struct',[[('m_sound',6,-6)]]),  #127
    ('_struct',[[('m_transmissionId',77,-7),('m_thread',6,-6)]]),  #128
    ('_struct',[[('m_transmissionId',77,-6)]]),  #129
    ('_optional',[74]),  #130
    ('_optional',[73]),  #131
    ('_optional',[103]),  #132
    ('_struct',[[('m_target',130,-10),('m_distance',131,-9),('m_pitch',131,-8),('m_yaw',131,-7),('m_reason',132,-6)]]),  #133
    ('_struct',[[('m_skipType',117,-6)]]),  #134
    ('_int',[(0,11)]),  #135
    ('_struct',[[('x',135,-2),('y',135,-1)]]),  #136
    ('_struct',[[('m_button',6,-10),('m_down',13,-9),('m_posUI',136,-8),('m_posWorld',85,-7),('m_flags',103,-6)]]),  #137
    ('_struct',[[('m_posUI',136,-8),('m_posWorld',85,-7),('m_flags',103,-6)]]),  #138
    ('_struct',[[('m_achievementLink',73,-6)]]),  #139
    ('_struct',[[('m_abilLink',73,-8),('m_abilCmdIndex',2,-7),('m_state',103,-6)]]),  #140
    ('_struct',[[('m_soundtrack',6,-6)]]),  #141
    ('_struct',[[('m_planetId',77,-6)]]),  #142
    ('_struct',[[('m_key',103,-7),('m_flags',103,-6)]]),  #143
    ('_struct',[[('m_resources',100,-6)]]),  #144
    ('_struct',[[('m_fulfillRequestId',77,-6)]]),  #145
    ('_struct',[[('m_cancelRequestId',77,-6)]]),  #146
    ('_struct',[[('m_researchItemId',77,-6)]]),  #147
    ('_struct',[[('m_mercenaryId',77,-6)]]),  #148
    ('_struct',[[('m_battleReportId',77,-7),('m_difficultyLevel',77,-6)]]),  #149
    ('_struct',[[('m_battleReportId',77,-6)]]),  #150
    ('_int',[(0,19)]),  #151
    ('_struct',[[('m_decrementMs',151,-6)]]),  #152
    ('_struct',[[('m_portraitId',77,-6)]]),  #153
    ('_struct',[[('m_functionName',16,-6)]]),  #154
    ('_struct',[[('m_result',77,-6)]]),  #155
    ('_struct',[[('m_gameMenuItemIndex',77,-6)]]),  #156
    ('_struct',[[('m_purchaseCategoryId',77,-6)]]),  #157
    ('_struct',[[('m_button',73,-6)]]),  #158
    ('_struct',[[('m_cutsceneId',77,-7),('m_bookmarkName',16,-6)]]),  #159
    ('_struct',[[('m_cutsceneId',77,-6)]]),  #160
    ('_struct',[[('m_cutsceneId',77,-8),('m_conversationLine',16,-7),('m_altConversationLine',16,-6)]]),  #161
    ('_struct',[[('m_cutsceneId',77,-7),('m_conversationLine',16,-6)]]),  #162
    ('_struct',[[('m_observe',20,-10),('m_name',9,-9),('m_toonHandle',114,-8),('m_clanTag',37,-7),('m_clanLogo',38,-6)]]),  #163
    ('_struct',[[('m_recipient',12,-3),('m_string',26,-2)]]),  #164
    ('_struct',[[('m_recipient',12,-3),('m_point',78,-2)]]),  #165
    ('_struct',[[('m_progress',77,-2)]]),  #166
    ('_struct',[[('m_scoreValueMineralsCurrent',77,0),('m_scoreValueVespeneCurrent',77,1),('m_scoreValueMineralsCollectionRate',77,2),('m_scoreValueVespeneCollectionRate',77,3),('m_scoreValueWorkersActiveCount',77,4),('m_scoreValueMineralsUsedInProgressArmy',77,5),('m_scoreValueMineralsUsedInProgressEconomy',77,6),('m_scoreValueMineralsUsedInProgressTechnology',77,7),('m_scoreValueVespeneUsedInProgressArmy',77,8),('m_scoreValueVespeneUsedInProgressEconomy',77,9),('m_scoreValueVespeneUsedInProgressTechnology',77,10),('m_scoreValueMineralsUsedCurrentArmy',77,11),('m_scoreValueMineralsUsedCurrentEconomy',77,12),('m_scoreValueMineralsUsedCurrentTechnology',77,13),('m_scoreValueVespeneUsedCurrentArmy',77,14),('m_scoreValueVespeneUsedCurrentEconomy',77,15),('m_scoreValueVespeneUsedCurrentTechnology',77,16),('m_scoreValueMineralsLostArmy',77,17),('m_scoreValueMineralsLostEconomy',77,18),('m_scoreValueMineralsLostTechnology',77,19),('m_scoreValueVespeneLostArmy',77,20),('m_scoreValueVespeneLostEconomy',77,21),('m_scoreValueVespeneLostTechnology',77,22),('m_scoreValueMineralsKilledArmy',77,23),('m_scoreValueMineralsKilledEconomy',77,24),('m_scoreValueMineralsKilledTechnology',77,25),('m_scoreValueVespeneKilledArmy',77,26),('m_scoreValueVespeneKilledEconomy',77,27),('m_scoreValueVespeneKilledTechnology',77,28),('m_scoreValueFoodUsed',77,29),('m_scoreValueFoodMade',77,30),('m_scoreValueMineralsUsedActiveForces',77,31),('m_scoreValueVespeneUsedActiveForces',77,32),('m_scoreValueMineralsFriendlyFireArmy',77,33),('m_scoreValueMineralsFriendlyFireEconomy',77,34),('m_scoreValueMineralsFriendlyFireTechnology',77,35),('m_scoreValueVespeneFriendlyFireArmy',77,36),('m_scoreValueVespeneFriendlyFireEconomy',77,37),('m_scoreValueVespeneFriendlyFireTechnology',77,38)]]),  #167
    ('_struct',[[('m_playerId',1,0),('m_stats',167,1)]]),  #168
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_unitTypeName',25,2),('m_controlPlayerId',1,3),('m_upkeepPlayerId',1,4),('m_x',10,5),('m_y',10,6)]]),  #169
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_killerPlayerId',54,2),('m_x',10,3),('m_y',10,4),('m_killerUnitTagIndex',39,5),('m_killerUnitTagRecycle',39,6)]]),  #170
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_controlPlayerId',1,2),('m_upkeepPlayerId',1,3)]]),  #171
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_unitTypeName',25,2)]]),  #172
    ('_struct',[[('m_playerId',1,0),('m_upgradeTypeName',25,1),('m_count',77,2)]]),  #173
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1)]]),  #174
    ('_array',[(0,10),77]),  #175
    ('_struct',[[('m_firstUnitIndex',6,0),('m_items',175,1)]]),  #176
    ('_struct',[[('m_playerId',1,0),('m_type',6,1),('m_userId',39,2),('m_slotId',39,3)]]),  #177
]

# Map from protocol NNet.Game.*Event eventid to (typeid, name)
game_event_types = {
    5: (72, 'NNet.Game.SUserFinishedLoadingSyncEvent'),
    7: (71, 'NNet.Game.SUserOptionsEvent'),
    9: (64, 'NNet.Game.SBankFileEvent'),
    10: (66, 'NNet.Game.SBankSectionEvent'),
    11: (67, 'NNet.Game.SBankKeyEvent'),
    12: (68, 'NNet.Game.SBankValueEvent'),
    13: (70, 'NNet.Game.SBankSignatureEvent'),
    14: (75, 'NNet.Game.SCameraSaveEvent'),
    21: (76, 'NNet.Game.SSaveGameEvent'),
    22: (72, 'NNet.Game.SSaveGameDoneEvent'),
    23: (72, 'NNet.Game.SLoadGameDoneEvent'),
    26: (80, 'NNet.Game.SGameCheatEvent'),
    27: (88, 'NNet.Game.SCmdEvent'),
    28: (96, 'NNet.Game.SSelectionDeltaEvent'),
    29: (97, 'NNet.Game.SControlGroupUpdateEvent'),
    30: (99, 'NNet.Game.SSelectionSyncCheckEvent'),
    31: (101, 'NNet.Game.SResourceTradeEvent'),
    32: (102, 'NNet.Game.STriggerChatMessageEvent'),
    33: (105, 'NNet.Game.SAICommunicateEvent'),
    34: (106, 'NNet.Game.SSetAbsoluteGameSpeedEvent'),
    35: (107, 'NNet.Game.SAddAbsoluteGameSpeedEvent'),
    36: (108, 'NNet.Game.STriggerPingEvent'),
    37: (109, 'NNet.Game.SBroadcastCheatEvent'),
    38: (110, 'NNet.Game.SAllianceEvent'),
    39: (111, 'NNet.Game.SUnitClickEvent'),
    40: (112, 'NNet.Game.SUnitHighlightEvent'),
    41: (113, 'NNet.Game.STriggerReplySelectedEvent'),
    43: (118, 'NNet.Game.SHijackReplayGameEvent'),
    44: (72, 'NNet.Game.STriggerSkippedEvent'),
    45: (123, 'NNet.Game.STriggerSoundLengthQueryEvent'),
    46: (127, 'NNet.Game.STriggerSoundOffsetEvent'),
    47: (128, 'NNet.Game.STriggerTransmissionOffsetEvent'),
    48: (129, 'NNet.Game.STriggerTransmissionCompleteEvent'),
    49: (133, 'NNet.Game.SCameraUpdateEvent'),
    50: (72, 'NNet.Game.STriggerAbortMissionEvent'),
    51: (119, 'NNet.Game.STriggerPurchaseMadeEvent'),
    52: (72, 'NNet.Game.STriggerPurchaseExitEvent'),
    53: (120, 'NNet.Game.STriggerPlanetMissionLaunchedEvent'),
    54: (72, 'NNet.Game.STriggerPlanetPanelCanceledEvent'),
    55: (122, 'NNet.Game.STriggerDialogControlEvent'),
    56: (126, 'NNet.Game.STriggerSoundLengthSyncEvent'),
    57: (134, 'NNet.Game.STriggerConversationSkippedEvent'),
    58: (137, 'NNet.Game.STriggerMouseClickedEvent'),
    59: (138, 'NNet.Game.STriggerMouseMovedEvent'),
    60: (139, 'NNet.Game.SAchievementAwardedEvent'),
    62: (140, 'NNet.Game.STriggerTargetModeUpdateEvent'),
    63: (72, 'NNet.Game.STriggerPlanetPanelReplayEvent'),
    64: (141, 'NNet.Game.STriggerSoundtrackDoneEvent'),
    65: (142, 'NNet.Game.STriggerPlanetMissionSelectedEvent'),
    66: (143, 'NNet.Game.STriggerKeyPressedEvent'),
    67: (154, 'NNet.Game.STriggerMovieFunctionEvent'),
    68: (72, 'NNet.Game.STriggerPlanetPanelBirthCompleteEvent'),
    69: (72, 'NNet.Game.STriggerPlanetPanelDeathCompleteEvent'),
    70: (144, 'NNet.Game.SResourceRequestEvent'),
    71: (145, 'NNet.Game.SResourceRequestFulfillEvent'),
    72: (146, 'NNet.Game.SResourceRequestCancelEvent'),
    73: (72, 'NNet.Game.STriggerResearchPanelExitEvent'),
    74: (72, 'NNet.Game.STriggerResearchPanelPurchaseEvent'),
    75: (147, 'NNet.Game.STriggerResearchPanelSelectionChangedEvent'),
    77: (72, 'NNet.Game.STriggerMercenaryPanelExitEvent'),
    78: (72, 'NNet.Game.STriggerMercenaryPanelPurchaseEvent'),
    79: (148, 'NNet.Game.STriggerMercenaryPanelSelectionChangedEvent'),
    80: (72, 'NNet.Game.STriggerVictoryPanelExitEvent'),
    81: (72, 'NNet.Game.STriggerBattleReportPanelExitEvent'),
    82: (149, 'NNet.Game.STriggerBattleReportPanelPlayMissionEvent'),
    83: (150, 'NNet.Game.STriggerBattleReportPanelPlaySceneEvent'),
    84: (150, 'NNet.Game.STriggerBattleReportPanelSelectionChangedEvent'),
    85: (120, 'NNet.Game.STriggerVictoryPanelPlayMissionAgainEvent'),
    86: (72, 'NNet.Game.STriggerMovieStartedEvent'),
    87: (72, 'NNet.Game.STriggerMovieFinishedEvent'),
    88: (152, 'NNet.Game.SDecrementGameTimeRemainingEvent'),
    89: (153, 'NNet.Game.STriggerPortraitLoadedEvent'),
    90: (155, 'NNet.Game.STriggerCustomDialogDismissedEvent'),
    91: (156, 'NNet.Game.STriggerGameMenuItemSelectedEvent'),
    93: (119, 'NNet.Game.STriggerPurchasePanelSelectedPurchaseItemChangedEvent'),
    94: (157, 'NNet.Game.STriggerPurchasePanelSelectedPurchaseCategoryChangedEvent'),
    95: (158, 'NNet.Game.STriggerButtonPressedEvent'),
    96: (72, 'NNet.Game.STriggerGameCreditsFinishedEvent'),
    97: (159, 'NNet.Game.STriggerCutsceneBookmarkFiredEvent'),
    98: (160, 'NNet.Game.STriggerCutsceneEndSceneFiredEvent'),
    99: (161, 'NNet.Game.STriggerCutsceneConversationLineEvent'),
    100: (162, 'NNet.Game.STriggerCutsceneConversationLineMissingEvent'),
    101: (72, 'NNet.Game.SGameUserLeaveEvent'),
    102: (163, 'NNet.Game.SGameUserJoinEvent'),
}

# The typeid of the NNet.Game.EEventId enum.
game_eventid_typeid = 0

# Map from protocol NNet.Game.*Message eventid to (typeid, name)
message_event_types = {
    0: (164, 'NNet.Game.SChatMessage'),
    1: (165, 'NNet.Game.SPingMessage'),
    2: (166, 'NNet.Game.SLoadingProgressMessage'),
    3: (72, 'NNet.Game.SServerPingMessage'),
}

# The typeid of the NNet.Game.EMessageId enum.
message_eventid_typeid = 1

# Map from protocol NNet.Replay.Tracker.*Event eventid to (typeid, name)
tracker_event_types = {
    0: (168, 'NNet.Replay.Tracker.SPlayerStatsEvent'),
    1: (169, 'NNet.Replay.Tracker.SUnitBornEvent'),
    2: (170, 'NNet.Replay.Tracker.SUnitDiedEvent'),
    3: (171, 'NNet.Replay.Tracker.SUnitOwnerChangeEvent'),
    4: (172, 'NNet.Replay.Tracker.SUnitTypeChangeEvent'),
    5: (173, 'NNet.Replay.Tracker.SUpgradeEvent'),
    6: (169, 'NNet.Replay.Tracker.SUnitInitEvent'),
    7: (174, 'NNet.Replay.Tracker.SUnitDoneEvent'),
    8: (176, 'NNet.Replay.Tracker.SUnitPositionsEvent'),
    9: (177, 'NNet.Replay.Tracker.SPlayerSetupEvent'),
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
replay_initdata_typeid = 63


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
