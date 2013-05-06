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
    ('_struct',[[('m_signature',9,0),('m_version',11,1),('m_type',12,2),('m_elapsedGameLoops',6,3)]]),  #13
    ('_fourcc',[]),  #14
    ('_blob',[(0,7)]),  #15
    ('_int',[(0,64)]),  #16
    ('_struct',[[('m_region',10,0),('m_programId',14,1),('m_realm',6,2),('m_name',15,3),('m_id',16,4)]]),  #17
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
    ('_struct',[[('m_playerList',23,0),('m_title',24,1),('m_difficulty',9,2),('m_thumbnail',26,3),('m_isBlizzardMap',27,4),('m_timeUTC',28,5),('m_timeLocalOffset',28,6),('m_description',29,7),('m_imageFilePath',25,8),('m_campaignIndex',10,15),('m_mapFileName',25,9),('m_cacheHandles',32,10),('m_miniSave',27,11),('m_gameSpeed',12,12),('m_defaultDifficulty',3,13),('m_modPaths',34,14)]]),  #35
    ('_optional',[9]),  #36
    ('_optional',[6]),  #37
    ('_struct',[[('m_race',20,-1)]]),  #38
    ('_struct',[[('m_team',20,-1)]]),  #39
    ('_struct',[[('m_name',9,-12),('m_clanTag',36,-11),('m_highestLeague',20,-10),('m_combinedRaceLevels',37,-9),('m_randomSeed',6,-8),('m_racePreference',38,-7),('m_teamPreference',39,-6),('m_testMap',27,-5),('m_testAuto',27,-4),('m_examine',27,-3),('m_customInterface',27,-2),('m_observe',19,-1)]]),  #40
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
    ('_struct',[[('m_randomValue',6,-25),('m_gameCacheName',24,-24),('m_gameOptions',42,-23),('m_gameSpeed',12,-22),('m_gameType',12,-21),('m_maxUsers',2,-20),('m_maxObservers',2,-19),('m_maxPlayers',2,-18),('m_maxTeams',43,-17),('m_maxColors',3,-16),('m_maxRaces',44,-15),('m_maxControls',44,-14),('m_mapSizeX',10,-13),('m_mapSizeY',10,-12),('m_mapFileSyncChecksum',6,-11),('m_mapFileName',25,-10),('m_mapAuthorName',9,-9),('m_modFileSyncChecksum',6,-8),('m_slotDescriptions',50,-7),('m_defaultDifficulty',3,-6),('m_defaultAIBuild',0,-5),('m_cacheHandles',31,-4),('m_isBlizzardMap',27,-3),('m_isPremadeFFA',27,-2),('m_isCoopMode',27,-1)]]),  #51
    ('_optional',[1]),  #52
    ('_optional',[2]),  #53
    ('_struct',[[('m_color',53,-1)]]),  #54
    ('_array',[(0,6),6]),  #55
    ('_array',[(0,9),6]),  #56
    ('_struct',[[('m_control',10,-13),('m_userId',52,-12),('m_teamId',1,-11),('m_colorPref',54,-10),('m_racePref',38,-9),('m_difficulty',3,-8),('m_aiBuild',0,-7),('m_handicap',0,-6),('m_observe',19,-5),('m_workingSetSlotId',20,-4),('m_rewards',55,-3),('m_toonHandle',15,-2),('m_licenses',56,-1)]]),  #57
    ('_array',[(0,5),57]),  #58
    ('_struct',[[('m_phase',12,-10),('m_maxUsers',2,-9),('m_maxObservers',2,-8),('m_slots',58,-7),('m_randomSeed',6,-6),('m_hostUserId',52,-5),('m_isSinglePlayer',27,-4),('m_gameDuration',6,-3),('m_defaultDifficulty',3,-2),('m_defaultAIBuild',0,-1)]]),  #59
    ('_struct',[[('m_userInitialData',41,-3),('m_gameDescription',51,-2),('m_lobbyState',59,-1)]]),  #60
    ('_struct',[[('m_syncLobbyState',60,-1)]]),  #61
    ('_struct',[[('m_name',15,-1)]]),  #62
    ('_blob',[(0,6)]),  #63
    ('_struct',[[('m_name',63,-1)]]),  #64
    ('_struct',[[('m_name',63,-3),('m_type',6,-2),('m_data',15,-1)]]),  #65
    ('_struct',[[('m_type',6,-3),('m_name',63,-2),('m_data',29,-1)]]),  #66
    ('_array',[(0,5),10]),  #67
    ('_struct',[[('m_signature',67,-2),('m_toonHandle',15,-1)]]),  #68
    ('_struct',[[('m_gameFullyDownloaded',27,-7),('m_developmentCheatsEnabled',27,-6),('m_multiplayerCheatsEnabled',27,-5),('m_syncChecksummingEnabled',27,-4),('m_isMapToMapTransition',27,-3),('m_startingRally',27,-2),('m_baseBuildNum',6,-1)]]),  #69
    ('_struct',[[]]),  #70
    ('_int',[(0,16)]),  #71
    ('_struct',[[('x',71,-2),('y',71,-1)]]),  #72
    ('_struct',[[('m_which',12,-2),('m_target',72,-1)]]),  #73
    ('_struct',[[('m_fileName',25,-5),('m_automatic',27,-4),('m_overwrite',27,-3),('m_name',9,-2),('m_description',24,-1)]]),  #74
    ('_int',[(-2147483648,32)]),  #75
    ('_struct',[[('x',75,-2),('y',75,-1)]]),  #76
    ('_struct',[[('m_point',76,-4),('m_time',75,-3),('m_verb',24,-2),('m_arguments',24,-1)]]),  #77
    ('_struct',[[('m_data',77,-1)]]),  #78
    ('_int',[(0,20)]),  #79
    ('_struct',[[('m_abilLink',71,-3),('m_abilCmdIndex',2,-2),('m_abilCmdData',20,-1)]]),  #80
    ('_optional',[80]),  #81
    ('_null',[]),  #82
    ('_struct',[[('x',79,-3),('y',79,-2),('z',75,-1)]]),  #83
    ('_struct',[[('m_targetUnitFlags',10,-7),('m_timer',10,-6),('m_tag',6,-5),('m_snapshotUnitLink',71,-4),('m_snapshotControlPlayerId',52,-3),('m_snapshotUpkeepPlayerId',52,-2),('m_snapshotPoint',83,-1)]]),  #84
    ('_choice',[(0,2),{0:('None',82),1:('TargetPoint',83),2:('TargetUnit',84),3:('Data',6)}]),  #85
    ('_struct',[[('m_cmdFlags',79,-4),('m_abil',81,-3),('m_data',85,-2),('m_otherUnit',37,-1)]]),  #86
    ('_int',[(0,9)]),  #87
    ('_bitarray',[(0,9)]),  #88
    ('_array',[(0,9),87]),  #89
    ('_choice',[(0,2),{0:('None',82),1:('Mask',88),2:('OneIndices',89),3:('ZeroIndices',89)}]),  #90
    ('_struct',[[('m_unitLink',71,-4),('m_subgroupPriority',10,-3),('m_intraSubgroupPriority',10,-2),('m_count',87,-1)]]),  #91
    ('_array',[(0,9),91]),  #92
    ('_struct',[[('m_subgroupIndex',87,-4),('m_removeMask',90,-3),('m_addSubgroups',92,-2),('m_addUnitTags',56,-1)]]),  #93
    ('_struct',[[('m_controlGroupId',1,-2),('m_delta',93,-1)]]),  #94
    ('_struct',[[('m_controlGroupIndex',1,-3),('m_controlGroupUpdate',19,-2),('m_mask',90,-1)]]),  #95
    ('_struct',[[('m_count',87,-6),('m_subgroupCount',87,-5),('m_activeSubgroupIndex',87,-4),('m_unitTagsChecksum',6,-3),('m_subgroupIndicesChecksum',6,-2),('m_subgroupsChecksum',6,-1)]]),  #96
    ('_struct',[[('m_controlGroupId',1,-2),('m_selectionSyncData',96,-1)]]),  #97
    ('_array',[(0,3),75]),  #98
    ('_struct',[[('m_recipientId',1,-2),('m_resources',98,-1)]]),  #99
    ('_struct',[[('m_chatMessage',24,-1)]]),  #100
    ('_int',[(-128,8)]),  #101
    ('_struct',[[('x',75,-3),('y',75,-2),('z',75,-1)]]),  #102
    ('_struct',[[('m_beacon',101,-9),('m_ally',101,-8),('m_flags',101,-7),('m_build',101,-6),('m_targetUnitTag',6,-5),('m_targetUnitSnapshotUnitLink',71,-4),('m_targetUnitSnapshotUpkeepPlayerId',101,-3),('m_targetUnitSnapshotControlPlayerId',101,-2),('m_targetPoint',102,-1)]]),  #103
    ('_struct',[[('m_speed',12,-1)]]),  #104
    ('_struct',[[('m_delta',101,-1)]]),  #105
    ('_struct',[[('m_point',76,-3),('m_unit',6,-2),('m_pingedMinimap',27,-1)]]),  #106
    ('_struct',[[('m_verb',24,-2),('m_arguments',24,-1)]]),  #107
    ('_struct',[[('m_alliance',6,-2),('m_control',6,-1)]]),  #108
    ('_struct',[[('m_unitTag',6,-1)]]),  #109
    ('_struct',[[('m_unitTag',6,-2),('m_flags',10,-1)]]),  #110
    ('_struct',[[('m_conversationId',75,-2),('m_replyId',75,-1)]]),  #111
    ('_optional',[15]),  #112
    ('_struct',[[('m_gameUserId',1,-5),('m_observe',19,-4),('m_name',9,-3),('m_toonHandle',112,-2),('m_clanTag',36,-1)]]),  #113
    ('_array',[(0,5),113]),  #114
    ('_int',[(0,1)]),  #115
    ('_struct',[[('m_userInfos',114,-2),('m_method',115,-1)]]),  #116
    ('_struct',[[('m_purchaseItemId',75,-1)]]),  #117
    ('_struct',[[('m_difficultyLevel',75,-1)]]),  #118
    ('_choice',[(0,3),{0:('None',82),1:('Checked',27),2:('ValueChanged',6),3:('SelectionChanged',75),4:('TextChanged',25),5:('MouseButton',6)}]),  #119
    ('_struct',[[('m_controlId',75,-3),('m_eventType',75,-2),('m_eventData',119,-1)]]),  #120
    ('_struct',[[('m_soundHash',6,-2),('m_length',6,-1)]]),  #121
    ('_array',[(0,7),6]),  #122
    ('_struct',[[('m_soundHash',122,-2),('m_length',122,-1)]]),  #123
    ('_struct',[[('m_syncInfo',123,-1)]]),  #124
    ('_struct',[[('m_sound',6,-1)]]),  #125
    ('_struct',[[('m_transmissionId',75,-2),('m_thread',6,-1)]]),  #126
    ('_struct',[[('m_transmissionId',75,-1)]]),  #127
    ('_optional',[72]),  #128
    ('_optional',[71]),  #129
    ('_struct',[[('m_target',128,-4),('m_distance',129,-3),('m_pitch',129,-2),('m_yaw',129,-1)]]),  #130
    ('_struct',[[('m_skipType',115,-1)]]),  #131
    ('_int',[(0,11)]),  #132
    ('_struct',[[('x',132,-2),('y',132,-1)]]),  #133
    ('_struct',[[('m_button',6,-4),('m_down',27,-3),('m_posUI',133,-2),('m_posWorld',83,-1)]]),  #134
    ('_struct',[[('m_posUI',133,-2),('m_posWorld',83,-1)]]),  #135
    ('_struct',[[('m_achievementLink',71,-1)]]),  #136
    ('_struct',[[('m_abilLink',71,-3),('m_abilCmdIndex',2,-2),('m_state',101,-1)]]),  #137
    ('_struct',[[('m_soundtrack',6,-1)]]),  #138
    ('_struct',[[('m_planetId',75,-1)]]),  #139
    ('_struct',[[('m_key',101,-2),('m_flags',101,-1)]]),  #140
    ('_struct',[[('m_resources',98,-1)]]),  #141
    ('_struct',[[('m_fulfillRequestId',75,-1)]]),  #142
    ('_struct',[[('m_cancelRequestId',75,-1)]]),  #143
    ('_struct',[[('m_researchItemId',75,-1)]]),  #144
    ('_struct',[[('m_mercenaryId',75,-1)]]),  #145
    ('_struct',[[('m_battleReportId',75,-2),('m_difficultyLevel',75,-1)]]),  #146
    ('_struct',[[('m_battleReportId',75,-1)]]),  #147
    ('_int',[(0,19)]),  #148
    ('_struct',[[('m_decrementMs',148,-1)]]),  #149
    ('_struct',[[('m_portraitId',75,-1)]]),  #150
    ('_struct',[[('m_functionName',15,-1)]]),  #151
    ('_struct',[[('m_result',75,-1)]]),  #152
    ('_struct',[[('m_gameMenuItemIndex',75,-1)]]),  #153
    ('_struct',[[('m_reason',101,-1)]]),  #154
    ('_struct',[[('m_purchaseCategoryId',75,-1)]]),  #155
    ('_struct',[[('m_button',71,-1)]]),  #156
    ('_struct',[[('m_cutsceneId',75,-2),('m_bookmarkName',15,-1)]]),  #157
    ('_struct',[[('m_cutsceneId',75,-1)]]),  #158
    ('_struct',[[('m_cutsceneId',75,-3),('m_conversationLine',15,-2),('m_altConversationLine',15,-1)]]),  #159
    ('_struct',[[('m_cutsceneId',75,-2),('m_conversationLine',15,-1)]]),  #160
    ('_struct',[[('m_observe',19,-4),('m_name',9,-3),('m_toonHandle',112,-2),('m_clanTag',36,-1)]]),  #161
    ('_struct',[[('m_recipient',12,-2),('m_string',25,-1)]]),  #162
    ('_struct',[[('m_recipient',12,-2),('m_point',76,-1)]]),  #163
    ('_struct',[[('m_progress',75,-1)]]),  #164
    ('_struct',[[('m_scoreValueMineralsCurrent',75,0),('m_scoreValueVespeneCurrent',75,1),('m_scoreValueMineralsCollectionRate',75,2),('m_scoreValueVespeneCollectionRate',75,3),('m_scoreValueWorkersActiveCount',75,4),('m_scoreValueMineralsUsedInProgressArmy',75,5),('m_scoreValueMineralsUsedInProgressEconomy',75,6),('m_scoreValueMineralsUsedInProgressTechnology',75,7),('m_scoreValueVespeneUsedInProgressArmy',75,8),('m_scoreValueVespeneUsedInProgressEconomy',75,9),('m_scoreValueVespeneUsedInProgressTechnology',75,10),('m_scoreValueMineralsUsedCurrentArmy',75,11),('m_scoreValueMineralsUsedCurrentEconomy',75,12),('m_scoreValueMineralsUsedCurrentTechnology',75,13),('m_scoreValueVespeneUsedCurrentArmy',75,14),('m_scoreValueVespeneUsedCurrentEconomy',75,15),('m_scoreValueVespeneUsedCurrentTechnology',75,16),('m_scoreValueMineralsLostArmy',75,17),('m_scoreValueMineralsLostEconomy',75,18),('m_scoreValueMineralsLostTechnology',75,19),('m_scoreValueVespeneLostArmy',75,20),('m_scoreValueVespeneLostEconomy',75,21),('m_scoreValueVespeneLostTechnology',75,22),('m_scoreValueMineralsKilledArmy',75,23),('m_scoreValueMineralsKilledEconomy',75,24),('m_scoreValueMineralsKilledTechnology',75,25),('m_scoreValueVespeneKilledArmy',75,26),('m_scoreValueVespeneKilledEconomy',75,27),('m_scoreValueVespeneKilledTechnology',75,28),('m_scoreValueFoodUsed',75,29),('m_scoreValueFoodMade',75,30),('m_scoreValueMineralsUsedActiveForces',75,31),('m_scoreValueVespeneUsedActiveForces',75,32)]]),  #165
    ('_struct',[[('m_playerId',1,0),('m_stats',165,1)]]),  #166
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_unitTypeName',24,2),('m_controlPlayerId',1,3),('m_upkeepPlayerId',1,4),('m_x',10,5),('m_y',10,6)]]),  #167
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_killerPlayerId',52,2),('m_x',10,3),('m_y',10,4)]]),  #168
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_controlPlayerId',1,2),('m_upkeepPlayerId',1,3)]]),  #169
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_unitTypeName',24,2)]]),  #170
    ('_struct',[[('m_playerId',1,0),('m_upgradeTypeName',24,1),('m_count',75,2)]]),  #171
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1)]]),  #172
    ('_array',[(0,10),75]),  #173
    ('_struct',[[('m_firstUnitIndex',6,0),('m_items',173,1)]]),  #174
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
    14: (73, 'NNet.Game.SCameraSaveEvent'),
    21: (74, 'NNet.Game.SSaveGameEvent'),
    22: (70, 'NNet.Game.SSaveGameDoneEvent'),
    23: (70, 'NNet.Game.SLoadGameDoneEvent'),
    26: (78, 'NNet.Game.SGameCheatEvent'),
    27: (86, 'NNet.Game.SCmdEvent'),
    28: (94, 'NNet.Game.SSelectionDeltaEvent'),
    29: (95, 'NNet.Game.SControlGroupUpdateEvent'),
    30: (97, 'NNet.Game.SSelectionSyncCheckEvent'),
    31: (99, 'NNet.Game.SResourceTradeEvent'),
    32: (100, 'NNet.Game.STriggerChatMessageEvent'),
    33: (103, 'NNet.Game.SAICommunicateEvent'),
    34: (104, 'NNet.Game.SSetAbsoluteGameSpeedEvent'),
    35: (105, 'NNet.Game.SAddAbsoluteGameSpeedEvent'),
    36: (106, 'NNet.Game.STriggerPingEvent'),
    37: (107, 'NNet.Game.SBroadcastCheatEvent'),
    38: (108, 'NNet.Game.SAllianceEvent'),
    39: (109, 'NNet.Game.SUnitClickEvent'),
    40: (110, 'NNet.Game.SUnitHighlightEvent'),
    41: (111, 'NNet.Game.STriggerReplySelectedEvent'),
    43: (116, 'NNet.Game.SHijackReplayGameEvent'),
    44: (70, 'NNet.Game.STriggerSkippedEvent'),
    45: (121, 'NNet.Game.STriggerSoundLengthQueryEvent'),
    46: (125, 'NNet.Game.STriggerSoundOffsetEvent'),
    47: (126, 'NNet.Game.STriggerTransmissionOffsetEvent'),
    48: (127, 'NNet.Game.STriggerTransmissionCompleteEvent'),
    49: (130, 'NNet.Game.SCameraUpdateEvent'),
    50: (70, 'NNet.Game.STriggerAbortMissionEvent'),
    51: (117, 'NNet.Game.STriggerPurchaseMadeEvent'),
    52: (70, 'NNet.Game.STriggerPurchaseExitEvent'),
    53: (118, 'NNet.Game.STriggerPlanetMissionLaunchedEvent'),
    54: (70, 'NNet.Game.STriggerPlanetPanelCanceledEvent'),
    55: (120, 'NNet.Game.STriggerDialogControlEvent'),
    56: (124, 'NNet.Game.STriggerSoundLengthSyncEvent'),
    57: (131, 'NNet.Game.STriggerConversationSkippedEvent'),
    58: (134, 'NNet.Game.STriggerMouseClickedEvent'),
    59: (135, 'NNet.Game.STriggerMouseMovedEvent'),
    60: (136, 'NNet.Game.SAchievementAwardedEvent'),
    62: (137, 'NNet.Game.STriggerTargetModeUpdateEvent'),
    63: (70, 'NNet.Game.STriggerPlanetPanelReplayEvent'),
    64: (138, 'NNet.Game.STriggerSoundtrackDoneEvent'),
    65: (139, 'NNet.Game.STriggerPlanetMissionSelectedEvent'),
    66: (140, 'NNet.Game.STriggerKeyPressedEvent'),
    67: (151, 'NNet.Game.STriggerMovieFunctionEvent'),
    68: (70, 'NNet.Game.STriggerPlanetPanelBirthCompleteEvent'),
    69: (70, 'NNet.Game.STriggerPlanetPanelDeathCompleteEvent'),
    70: (141, 'NNet.Game.SResourceRequestEvent'),
    71: (142, 'NNet.Game.SResourceRequestFulfillEvent'),
    72: (143, 'NNet.Game.SResourceRequestCancelEvent'),
    73: (70, 'NNet.Game.STriggerResearchPanelExitEvent'),
    74: (70, 'NNet.Game.STriggerResearchPanelPurchaseEvent'),
    75: (144, 'NNet.Game.STriggerResearchPanelSelectionChangedEvent'),
    77: (70, 'NNet.Game.STriggerMercenaryPanelExitEvent'),
    78: (70, 'NNet.Game.STriggerMercenaryPanelPurchaseEvent'),
    79: (145, 'NNet.Game.STriggerMercenaryPanelSelectionChangedEvent'),
    80: (70, 'NNet.Game.STriggerVictoryPanelExitEvent'),
    81: (70, 'NNet.Game.STriggerBattleReportPanelExitEvent'),
    82: (146, 'NNet.Game.STriggerBattleReportPanelPlayMissionEvent'),
    83: (147, 'NNet.Game.STriggerBattleReportPanelPlaySceneEvent'),
    84: (147, 'NNet.Game.STriggerBattleReportPanelSelectionChangedEvent'),
    85: (118, 'NNet.Game.STriggerVictoryPanelPlayMissionAgainEvent'),
    86: (70, 'NNet.Game.STriggerMovieStartedEvent'),
    87: (70, 'NNet.Game.STriggerMovieFinishedEvent'),
    88: (149, 'NNet.Game.SDecrementGameTimeRemainingEvent'),
    89: (150, 'NNet.Game.STriggerPortraitLoadedEvent'),
    90: (152, 'NNet.Game.STriggerCustomDialogDismissedEvent'),
    91: (153, 'NNet.Game.STriggerGameMenuItemSelectedEvent'),
    92: (154, 'NNet.Game.STriggerCameraMoveEvent'),
    93: (117, 'NNet.Game.STriggerPurchasePanelSelectedPurchaseItemChangedEvent'),
    94: (155, 'NNet.Game.STriggerPurchasePanelSelectedPurchaseCategoryChangedEvent'),
    95: (156, 'NNet.Game.STriggerButtonPressedEvent'),
    96: (70, 'NNet.Game.STriggerGameCreditsFinishedEvent'),
    97: (157, 'NNet.Game.STriggerCutsceneBookmarkFiredEvent'),
    98: (158, 'NNet.Game.STriggerCutsceneEndSceneFiredEvent'),
    99: (159, 'NNet.Game.STriggerCutsceneConversationLineEvent'),
    100: (160, 'NNet.Game.STriggerCutsceneConversationLineMissingEvent'),
    101: (70, 'NNet.Game.SGameUserLeaveEvent'),
    102: (161, 'NNet.Game.SGameUserJoinEvent'),
}

# The typeid of the NNet.Game.EEventId enum.
game_eventid_typeid = 0

# Map from protocol NNet.Game.*Message eventid to (typeid, name)
message_event_types = {
    0: (162, 'NNet.Game.SChatMessage'),
    1: (163, 'NNet.Game.SPingMessage'),
    2: (164, 'NNet.Game.SLoadingProgressMessage'),
    3: (70, 'NNet.Game.SServerPingMessage'),
}

# The typeid of the NNet.Game.EMessageId enum.
message_eventid_typeid = 1

# Map from protocol NNet.Replay.Tracker.*Event eventid to (typeid, name)
tracker_event_types = {
    0: (166, 'NNet.Replay.Tracker.SPlayerStatsEvent'),
    1: (167, 'NNet.Replay.Tracker.SUnitBornEvent'),
    2: (168, 'NNet.Replay.Tracker.SUnitDiedEvent'),
    3: (169, 'NNet.Replay.Tracker.SUnitOwnerChangeEvent'),
    4: (170, 'NNet.Replay.Tracker.SUnitTypeChangeEvent'),
    5: (171, 'NNet.Replay.Tracker.SUpgradeEvent'),
    6: (167, 'NNet.Replay.Tracker.SUnitInitEvent'),
    7: (172, 'NNet.Replay.Tracker.SUnitDoneEvent'),
    8: (174, 'NNet.Replay.Tracker.SUnitPositionsEvent'),
}

# The typeid of the NNet.Replay.Tracker.EEventId enum.
tracker_eventid_typeid = 2

# The typeid of NNet.SVarUint32 (the type used to encode gameloop deltas).
svaruint32_typeid = 7

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
    for k,v in value.iteritems():
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
            raise CorruptedError('eventid(%d) at %s' % (eventid, decoder))

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
