# Copyright (c) 2015 Blizzard Entertainment
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
    ('_bool',[]),  #13
    ('_array',[(16,0),10]),  #14
    ('_optional',[14]),  #15
    ('_blob',[(16,0)]),  #16
    ('_struct',[[('m_dataDeprecated',15,0),('m_data',16,1)]]),  #17
    ('_struct',[[('m_signature',9,0),('m_version',11,1),('m_type',12,2),('m_elapsedGameLoops',6,3),('m_useScaledTime',13,4),('m_ngdpRootKey',17,5),('m_dataBuildNum',6,6)]]),  #18
    ('_fourcc',[]),  #19
    ('_blob',[(0,7)]),  #20
    ('_int',[(0,64)]),  #21
    ('_struct',[[('m_region',10,0),('m_programId',19,1),('m_realm',6,2),('m_name',20,3),('m_id',21,4)]]),  #22
    ('_struct',[[('m_a',10,0),('m_r',10,1),('m_g',10,2),('m_b',10,3)]]),  #23
    ('_int',[(0,2)]),  #24
    ('_optional',[10]),  #25
    ('_struct',[[('m_name',9,0),('m_toon',22,1),('m_race',9,2),('m_color',23,3),('m_control',10,4),('m_teamId',1,5),('m_handicap',0,6),('m_observe',24,7),('m_result',24,8),('m_workingSetSlotId',25,9),('m_hero',9,10)]]),  #26
    ('_array',[(0,5),26]),  #27
    ('_optional',[27]),  #28
    ('_blob',[(0,10)]),  #29
    ('_blob',[(0,11)]),  #30
    ('_struct',[[('m_file',30,0)]]),  #31
    ('_optional',[13]),  #32
    ('_int',[(-9223372036854775808,64)]),  #33
    ('_blob',[(0,12)]),  #34
    ('_blob',[(40,0)]),  #35
    ('_array',[(0,6),35]),  #36
    ('_optional',[36]),  #37
    ('_array',[(0,6),30]),  #38
    ('_optional',[38]),  #39
    ('_struct',[[('m_playerList',28,0),('m_title',29,1),('m_difficulty',9,2),('m_thumbnail',31,3),('m_isBlizzardMap',13,4),('m_restartAsTransitionMap',32,16),('m_timeUTC',33,5),('m_timeLocalOffset',33,6),('m_description',34,7),('m_imageFilePath',30,8),('m_campaignIndex',10,15),('m_mapFileName',30,9),('m_cacheHandles',37,10),('m_miniSave',13,11),('m_gameSpeed',12,12),('m_defaultDifficulty',3,13),('m_modPaths',39,14)]]),  #40
    ('_optional',[9]),  #41
    ('_optional',[35]),  #42
    ('_optional',[6]),  #43
    ('_struct',[[('m_race',25,-1)]]),  #44
    ('_struct',[[('m_team',25,-1)]]),  #45
    ('_blob',[(0,9)]),  #46
    ('_struct',[[('m_name',9,-18),('m_clanTag',41,-17),('m_clanLogo',42,-16),('m_highestLeague',25,-15),('m_combinedRaceLevels',43,-14),('m_randomSeed',6,-13),('m_racePreference',44,-12),('m_teamPreference',45,-11),('m_testMap',13,-10),('m_testAuto',13,-9),('m_examine',13,-8),('m_customInterface',13,-7),('m_testType',6,-6),('m_observe',24,-5),('m_hero',46,-4),('m_skin',46,-3),('m_mount',46,-2),('m_toonHandle',20,-1)]]),  #47
    ('_array',[(0,5),47]),  #48
    ('_struct',[[('m_lockTeams',13,-16),('m_teamsTogether',13,-15),('m_advancedSharedControl',13,-14),('m_randomRaces',13,-13),('m_battleNet',13,-12),('m_amm',13,-11),('m_ranked',13,-10),('m_competitive',13,-9),('m_practice',13,-8),('m_cooperative',13,-7),('m_noVictoryOrDefeat',13,-6),('m_heroDuplicatesAllowed',13,-5),('m_fog',24,-4),('m_observers',24,-3),('m_userDifficulty',24,-2),('m_clientDebugFlags',21,-1)]]),  #49
    ('_int',[(1,4)]),  #50
    ('_int',[(1,8)]),  #51
    ('_bitarray',[(0,6)]),  #52
    ('_bitarray',[(0,8)]),  #53
    ('_bitarray',[(0,2)]),  #54
    ('_bitarray',[(0,7)]),  #55
    ('_struct',[[('m_allowedColors',52,-6),('m_allowedRaces',53,-5),('m_allowedDifficulty',52,-4),('m_allowedControls',53,-3),('m_allowedObserveTypes',54,-2),('m_allowedAIBuilds',55,-1)]]),  #56
    ('_array',[(0,5),56]),  #57
    ('_struct',[[('m_randomValue',6,-26),('m_gameCacheName',29,-25),('m_gameOptions',49,-24),('m_gameSpeed',12,-23),('m_gameType',12,-22),('m_maxUsers',2,-21),('m_maxObservers',2,-20),('m_maxPlayers',2,-19),('m_maxTeams',50,-18),('m_maxColors',3,-17),('m_maxRaces',51,-16),('m_maxControls',10,-15),('m_mapSizeX',10,-14),('m_mapSizeY',10,-13),('m_mapFileSyncChecksum',6,-12),('m_mapFileName',30,-11),('m_mapAuthorName',9,-10),('m_modFileSyncChecksum',6,-9),('m_slotDescriptions',57,-8),('m_defaultDifficulty',3,-7),('m_defaultAIBuild',0,-6),('m_cacheHandles',36,-5),('m_hasExtensionMod',13,-4),('m_isBlizzardMap',13,-3),('m_isPremadeFFA',13,-2),('m_isCoopMode',13,-1)]]),  #58
    ('_optional',[1]),  #59
    ('_optional',[2]),  #60
    ('_struct',[[('m_color',60,-1)]]),  #61
    ('_array',[(0,4),46]),  #62
    ('_array',[(0,17),6]),  #63
    ('_array',[(0,9),6]),  #64
    ('_struct',[[('m_control',10,-21),('m_userId',59,-20),('m_teamId',1,-19),('m_colorPref',61,-18),('m_racePref',44,-17),('m_difficulty',3,-16),('m_aiBuild',0,-15),('m_handicap',0,-14),('m_observe',24,-13),('m_logoIndex',6,-12),('m_hero',46,-11),('m_skin',46,-10),('m_mount',46,-9),('m_artifacts',62,-8),('m_workingSetSlotId',25,-7),('m_rewards',63,-6),('m_toonHandle',20,-5),('m_licenses',64,-4),('m_tandemLeaderUserId',59,-3),('m_commander',46,-2),('m_commanderLevel',6,-1)]]),  #65
    ('_array',[(0,5),65]),  #66
    ('_struct',[[('m_phase',12,-11),('m_maxUsers',2,-10),('m_maxObservers',2,-9),('m_slots',66,-8),('m_randomSeed',6,-7),('m_hostUserId',59,-6),('m_isSinglePlayer',13,-5),('m_pickedMapTag',10,-4),('m_gameDuration',6,-3),('m_defaultDifficulty',3,-2),('m_defaultAIBuild',0,-1)]]),  #67
    ('_struct',[[('m_userInitialData',48,-3),('m_gameDescription',58,-2),('m_lobbyState',67,-1)]]),  #68
    ('_struct',[[('m_syncLobbyState',68,-1)]]),  #69
    ('_struct',[[('m_name',20,-1)]]),  #70
    ('_blob',[(0,6)]),  #71
    ('_struct',[[('m_name',71,-1)]]),  #72
    ('_struct',[[('m_name',71,-3),('m_type',6,-2),('m_data',20,-1)]]),  #73
    ('_struct',[[('m_type',6,-3),('m_name',71,-2),('m_data',34,-1)]]),  #74
    ('_array',[(0,5),10]),  #75
    ('_struct',[[('m_signature',75,-2),('m_toonHandle',20,-1)]]),  #76
    ('_struct',[[('m_gameFullyDownloaded',13,-15),('m_developmentCheatsEnabled',13,-14),('m_testCheatsEnabled',13,-13),('m_multiplayerCheatsEnabled',13,-12),('m_syncChecksummingEnabled',13,-11),('m_isMapToMapTransition',13,-10),('m_startingRally',13,-9),('m_debugPauseEnabled',13,-8),('m_useGalaxyAsserts',13,-7),('m_platformMac',13,-6),('m_cameraFollow',13,-5),('m_baseBuildNum',6,-4),('m_buildNum',6,-3),('m_versionFlags',6,-2),('m_hotkeyProfile',46,-1)]]),  #77
    ('_struct',[[]]),  #78
    ('_int',[(0,16)]),  #79
    ('_struct',[[('x',79,-2),('y',79,-1)]]),  #80
    ('_struct',[[('m_which',12,-2),('m_target',80,-1)]]),  #81
    ('_struct',[[('m_fileName',30,-5),('m_automatic',13,-4),('m_overwrite',13,-3),('m_name',9,-2),('m_description',29,-1)]]),  #82
    ('_struct',[[('m_sequence',6,-1)]]),  #83
    ('_int',[(-2147483648,32)]),  #84
    ('_struct',[[('x',84,-2),('y',84,-1)]]),  #85
    ('_struct',[[('m_point',85,-4),('m_time',84,-3),('m_verb',29,-2),('m_arguments',29,-1)]]),  #86
    ('_struct',[[('m_data',86,-1)]]),  #87
    ('_int',[(0,23)]),  #88
    ('_struct',[[('m_abilLink',79,-3),('m_abilCmdIndex',2,-2),('m_abilCmdData',25,-1)]]),  #89
    ('_optional',[89]),  #90
    ('_null',[]),  #91
    ('_int',[(0,20)]),  #92
    ('_struct',[[('x',92,-3),('y',92,-2),('z',84,-1)]]),  #93
    ('_struct',[[('m_targetUnitFlags',79,-7),('m_timer',10,-6),('m_tag',6,-5),('m_snapshotUnitLink',79,-4),('m_snapshotControlPlayerId',59,-3),('m_snapshotUpkeepPlayerId',59,-2),('m_snapshotPoint',93,-1)]]),  #94
    ('_choice',[(0,2),{0:('None',91),1:('TargetPoint',93),2:('TargetUnit',94),3:('Data',6)}]),  #95
    ('_int',[(1,32)]),  #96
    ('_struct',[[('m_cmdFlags',88,-6),('m_abil',90,-5),('m_data',95,-4),('m_sequence',96,-3),('m_otherUnit',43,-2),('m_unitGroup',43,-1)]]),  #97
    ('_int',[(0,9)]),  #98
    ('_bitarray',[(0,9)]),  #99
    ('_array',[(0,9),98]),  #100
    ('_choice',[(0,2),{0:('None',91),1:('Mask',99),2:('OneIndices',100),3:('ZeroIndices',100)}]),  #101
    ('_struct',[[('m_unitLink',79,-4),('m_subgroupPriority',10,-3),('m_intraSubgroupPriority',10,-2),('m_count',98,-1)]]),  #102
    ('_array',[(0,9),102]),  #103
    ('_struct',[[('m_subgroupIndex',98,-4),('m_removeMask',101,-3),('m_addSubgroups',103,-2),('m_addUnitTags',64,-1)]]),  #104
    ('_struct',[[('m_controlGroupId',1,-2),('m_delta',104,-1)]]),  #105
    ('_struct',[[('m_controlGroupIndex',1,-3),('m_controlGroupUpdate',12,-2),('m_mask',101,-1)]]),  #106
    ('_struct',[[('m_count',98,-6),('m_subgroupCount',98,-5),('m_activeSubgroupIndex',98,-4),('m_unitTagsChecksum',6,-3),('m_subgroupIndicesChecksum',6,-2),('m_subgroupsChecksum',6,-1)]]),  #107
    ('_struct',[[('m_controlGroupId',1,-2),('m_selectionSyncData',107,-1)]]),  #108
    ('_array',[(0,3),84]),  #109
    ('_struct',[[('m_recipientId',1,-2),('m_resources',109,-1)]]),  #110
    ('_struct',[[('m_chatMessage',29,-1)]]),  #111
    ('_int',[(-128,8)]),  #112
    ('_struct',[[('x',84,-3),('y',84,-2),('z',84,-1)]]),  #113
    ('_struct',[[('m_beacon',112,-9),('m_ally',112,-8),('m_flags',112,-7),('m_build',112,-6),('m_targetUnitTag',6,-5),('m_targetUnitSnapshotUnitLink',79,-4),('m_targetUnitSnapshotUpkeepPlayerId',112,-3),('m_targetUnitSnapshotControlPlayerId',112,-2),('m_targetPoint',113,-1)]]),  #114
    ('_struct',[[('m_speed',12,-1)]]),  #115
    ('_struct',[[('m_delta',112,-1)]]),  #116
    ('_struct',[[('m_point',85,-4),('m_unit',6,-3),('m_pingedMinimap',13,-2),('m_option',84,-1)]]),  #117
    ('_struct',[[('m_verb',29,-2),('m_arguments',29,-1)]]),  #118
    ('_struct',[[('m_alliance',6,-2),('m_control',6,-1)]]),  #119
    ('_struct',[[('m_unitTag',6,-1)]]),  #120
    ('_struct',[[('m_unitTag',6,-2),('m_flags',10,-1)]]),  #121
    ('_struct',[[('m_conversationId',84,-2),('m_replyId',84,-1)]]),  #122
    ('_optional',[20]),  #123
    ('_struct',[[('m_gameUserId',1,-6),('m_observe',24,-5),('m_name',9,-4),('m_toonHandle',123,-3),('m_clanTag',41,-2),('m_clanLogo',42,-1)]]),  #124
    ('_array',[(0,5),124]),  #125
    ('_int',[(0,1)]),  #126
    ('_struct',[[('m_userInfos',125,-2),('m_method',126,-1)]]),  #127
    ('_struct',[[('m_purchaseItemId',84,-1)]]),  #128
    ('_struct',[[('m_difficultyLevel',84,-1)]]),  #129
    ('_choice',[(0,3),{0:('None',91),1:('Checked',13),2:('ValueChanged',6),3:('SelectionChanged',84),4:('TextChanged',30),5:('MouseButton',6)}]),  #130
    ('_struct',[[('m_controlId',84,-3),('m_eventType',84,-2),('m_eventData',130,-1)]]),  #131
    ('_struct',[[('m_soundHash',6,-2),('m_length',6,-1)]]),  #132
    ('_array',[(0,7),6]),  #133
    ('_struct',[[('m_soundHash',133,-2),('m_length',133,-1)]]),  #134
    ('_struct',[[('m_syncInfo',134,-1)]]),  #135
    ('_struct',[[('m_queryId',79,-3),('m_lengthMs',6,-2),('m_finishGameLoop',6,-1)]]),  #136
    ('_struct',[[('m_queryId',79,-2),('m_lengthMs',6,-1)]]),  #137
    ('_struct',[[('m_animWaitQueryId',79,-1)]]),  #138
    ('_struct',[[('m_sound',6,-1)]]),  #139
    ('_struct',[[('m_transmissionId',84,-2),('m_thread',6,-1)]]),  #140
    ('_struct',[[('m_transmissionId',84,-1)]]),  #141
    ('_optional',[80]),  #142
    ('_optional',[79]),  #143
    ('_optional',[112]),  #144
    ('_struct',[[('m_target',142,-6),('m_distance',143,-5),('m_pitch',143,-4),('m_yaw',143,-3),('m_reason',144,-2),('m_follow',13,-1)]]),  #145
    ('_struct',[[('m_skipType',126,-1)]]),  #146
    ('_int',[(0,11)]),  #147
    ('_struct',[[('x',147,-2),('y',147,-1)]]),  #148
    ('_struct',[[('m_button',6,-5),('m_down',13,-4),('m_posUI',148,-3),('m_posWorld',93,-2),('m_flags',112,-1)]]),  #149
    ('_struct',[[('m_posUI',148,-3),('m_posWorld',93,-2),('m_flags',112,-1)]]),  #150
    ('_struct',[[('m_achievementLink',79,-1)]]),  #151
    ('_struct',[[('m_hotkey',6,-2),('m_down',13,-1)]]),  #152
    ('_struct',[[('m_abilLink',79,-3),('m_abilCmdIndex',2,-2),('m_state',112,-1)]]),  #153
    ('_struct',[[('m_soundtrack',6,-1)]]),  #154
    ('_struct',[[('m_planetId',84,-1)]]),  #155
    ('_struct',[[('m_key',112,-2),('m_flags',112,-1)]]),  #156
    ('_struct',[[('m_resources',109,-1)]]),  #157
    ('_struct',[[('m_fulfillRequestId',84,-1)]]),  #158
    ('_struct',[[('m_cancelRequestId',84,-1)]]),  #159
    ('_struct',[[('m_researchItemId',84,-1)]]),  #160
    ('_struct',[[('m_mercenaryId',84,-1)]]),  #161
    ('_struct',[[('m_battleReportId',84,-2),('m_difficultyLevel',84,-1)]]),  #162
    ('_struct',[[('m_battleReportId',84,-1)]]),  #163
    ('_int',[(0,19)]),  #164
    ('_struct',[[('m_decrementMs',164,-1)]]),  #165
    ('_struct',[[('m_portraitId',84,-1)]]),  #166
    ('_struct',[[('m_functionName',20,-1)]]),  #167
    ('_struct',[[('m_result',84,-1)]]),  #168
    ('_struct',[[('m_gameMenuItemIndex',84,-1)]]),  #169
    ('_struct',[[('m_purchaseCategoryId',84,-1)]]),  #170
    ('_struct',[[('m_button',79,-1)]]),  #171
    ('_struct',[[('m_cutsceneId',84,-2),('m_bookmarkName',20,-1)]]),  #172
    ('_struct',[[('m_cutsceneId',84,-1)]]),  #173
    ('_struct',[[('m_cutsceneId',84,-3),('m_conversationLine',20,-2),('m_altConversationLine',20,-1)]]),  #174
    ('_struct',[[('m_cutsceneId',84,-2),('m_conversationLine',20,-1)]]),  #175
    ('_struct',[[('m_leaveReason',1,-1)]]),  #176
    ('_struct',[[('m_observe',24,-7),('m_name',9,-6),('m_toonHandle',123,-5),('m_clanTag',41,-4),('m_clanLogo',42,-3),('m_hijack',13,-2),('m_hijackCloneGameUserId',59,-1)]]),  #177
    ('_optional',[96]),  #178
    ('_struct',[[('m_state',24,-2),('m_sequence',178,-1)]]),  #179
    ('_struct',[[('m_target',93,-1)]]),  #180
    ('_struct',[[('m_target',94,-1)]]),  #181
    ('_struct',[[('m_catalog',10,-4),('m_entry',79,-3),('m_field',9,-2),('m_value',9,-1)]]),  #182
    ('_struct',[[('m_index',6,-1)]]),  #183
    ('_struct',[[('m_shown',13,-1)]]),  #184
    ('_struct',[[('m_recipient',12,-2),('m_string',30,-1)]]),  #185
    ('_struct',[[('m_recipient',12,-2),('m_point',85,-1)]]),  #186
    ('_struct',[[('m_progress',84,-1)]]),  #187
    ('_struct',[[('m_status',24,-1)]]),  #188
    ('_struct',[[('m_scoreValueMineralsCurrent',84,0),('m_scoreValueVespeneCurrent',84,1),('m_scoreValueMineralsCollectionRate',84,2),('m_scoreValueVespeneCollectionRate',84,3),('m_scoreValueWorkersActiveCount',84,4),('m_scoreValueMineralsUsedInProgressArmy',84,5),('m_scoreValueMineralsUsedInProgressEconomy',84,6),('m_scoreValueMineralsUsedInProgressTechnology',84,7),('m_scoreValueVespeneUsedInProgressArmy',84,8),('m_scoreValueVespeneUsedInProgressEconomy',84,9),('m_scoreValueVespeneUsedInProgressTechnology',84,10),('m_scoreValueMineralsUsedCurrentArmy',84,11),('m_scoreValueMineralsUsedCurrentEconomy',84,12),('m_scoreValueMineralsUsedCurrentTechnology',84,13),('m_scoreValueVespeneUsedCurrentArmy',84,14),('m_scoreValueVespeneUsedCurrentEconomy',84,15),('m_scoreValueVespeneUsedCurrentTechnology',84,16),('m_scoreValueMineralsLostArmy',84,17),('m_scoreValueMineralsLostEconomy',84,18),('m_scoreValueMineralsLostTechnology',84,19),('m_scoreValueVespeneLostArmy',84,20),('m_scoreValueVespeneLostEconomy',84,21),('m_scoreValueVespeneLostTechnology',84,22),('m_scoreValueMineralsKilledArmy',84,23),('m_scoreValueMineralsKilledEconomy',84,24),('m_scoreValueMineralsKilledTechnology',84,25),('m_scoreValueVespeneKilledArmy',84,26),('m_scoreValueVespeneKilledEconomy',84,27),('m_scoreValueVespeneKilledTechnology',84,28),('m_scoreValueFoodUsed',84,29),('m_scoreValueFoodMade',84,30),('m_scoreValueMineralsUsedActiveForces',84,31),('m_scoreValueVespeneUsedActiveForces',84,32),('m_scoreValueMineralsFriendlyFireArmy',84,33),('m_scoreValueMineralsFriendlyFireEconomy',84,34),('m_scoreValueMineralsFriendlyFireTechnology',84,35),('m_scoreValueVespeneFriendlyFireArmy',84,36),('m_scoreValueVespeneFriendlyFireEconomy',84,37),('m_scoreValueVespeneFriendlyFireTechnology',84,38)]]),  #189
    ('_struct',[[('m_playerId',1,0),('m_stats',189,1)]]),  #190
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_unitTypeName',29,2),('m_controlPlayerId',1,3),('m_upkeepPlayerId',1,4),('m_x',10,5),('m_y',10,6)]]),  #191
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_killerPlayerId',59,2),('m_x',10,3),('m_y',10,4),('m_killerUnitTagIndex',43,5),('m_killerUnitTagRecycle',43,6)]]),  #192
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_controlPlayerId',1,2),('m_upkeepPlayerId',1,3)]]),  #193
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_unitTypeName',29,2)]]),  #194
    ('_struct',[[('m_playerId',1,0),('m_upgradeTypeName',29,1),('m_count',84,2)]]),  #195
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1)]]),  #196
    ('_array',[(0,10),84]),  #197
    ('_struct',[[('m_firstUnitIndex',6,0),('m_items',197,1)]]),  #198
    ('_struct',[[('m_playerId',1,0),('m_type',6,1),('m_userId',43,2),('m_slotId',43,3)]]),  #199
]

# Map from protocol NNet.Game.*Event eventid to (typeid, name)
game_event_types = {
    5: (78, 'NNet.Game.SUserFinishedLoadingSyncEvent'),
    7: (77, 'NNet.Game.SUserOptionsEvent'),
    9: (70, 'NNet.Game.SBankFileEvent'),
    10: (72, 'NNet.Game.SBankSectionEvent'),
    11: (73, 'NNet.Game.SBankKeyEvent'),
    12: (74, 'NNet.Game.SBankValueEvent'),
    13: (76, 'NNet.Game.SBankSignatureEvent'),
    14: (81, 'NNet.Game.SCameraSaveEvent'),
    21: (82, 'NNet.Game.SSaveGameEvent'),
    22: (78, 'NNet.Game.SSaveGameDoneEvent'),
    23: (78, 'NNet.Game.SLoadGameDoneEvent'),
    25: (83, 'NNet.Game.SCommandManagerResetEvent'),
    26: (87, 'NNet.Game.SGameCheatEvent'),
    27: (97, 'NNet.Game.SCmdEvent'),
    28: (105, 'NNet.Game.SSelectionDeltaEvent'),
    29: (106, 'NNet.Game.SControlGroupUpdateEvent'),
    30: (108, 'NNet.Game.SSelectionSyncCheckEvent'),
    31: (110, 'NNet.Game.SResourceTradeEvent'),
    32: (111, 'NNet.Game.STriggerChatMessageEvent'),
    33: (114, 'NNet.Game.SAICommunicateEvent'),
    34: (115, 'NNet.Game.SSetAbsoluteGameSpeedEvent'),
    35: (116, 'NNet.Game.SAddAbsoluteGameSpeedEvent'),
    36: (117, 'NNet.Game.STriggerPingEvent'),
    37: (118, 'NNet.Game.SBroadcastCheatEvent'),
    38: (119, 'NNet.Game.SAllianceEvent'),
    39: (120, 'NNet.Game.SUnitClickEvent'),
    40: (121, 'NNet.Game.SUnitHighlightEvent'),
    41: (122, 'NNet.Game.STriggerReplySelectedEvent'),
    43: (127, 'NNet.Game.SHijackReplayGameEvent'),
    44: (78, 'NNet.Game.STriggerSkippedEvent'),
    45: (132, 'NNet.Game.STriggerSoundLengthQueryEvent'),
    46: (139, 'NNet.Game.STriggerSoundOffsetEvent'),
    47: (140, 'NNet.Game.STriggerTransmissionOffsetEvent'),
    48: (141, 'NNet.Game.STriggerTransmissionCompleteEvent'),
    49: (145, 'NNet.Game.SCameraUpdateEvent'),
    50: (78, 'NNet.Game.STriggerAbortMissionEvent'),
    51: (128, 'NNet.Game.STriggerPurchaseMadeEvent'),
    52: (78, 'NNet.Game.STriggerPurchaseExitEvent'),
    53: (129, 'NNet.Game.STriggerPlanetMissionLaunchedEvent'),
    54: (78, 'NNet.Game.STriggerPlanetPanelCanceledEvent'),
    55: (131, 'NNet.Game.STriggerDialogControlEvent'),
    56: (135, 'NNet.Game.STriggerSoundLengthSyncEvent'),
    57: (146, 'NNet.Game.STriggerConversationSkippedEvent'),
    58: (149, 'NNet.Game.STriggerMouseClickedEvent'),
    59: (150, 'NNet.Game.STriggerMouseMovedEvent'),
    60: (151, 'NNet.Game.SAchievementAwardedEvent'),
    61: (152, 'NNet.Game.STriggerHotkeyPressedEvent'),
    62: (153, 'NNet.Game.STriggerTargetModeUpdateEvent'),
    63: (78, 'NNet.Game.STriggerPlanetPanelReplayEvent'),
    64: (154, 'NNet.Game.STriggerSoundtrackDoneEvent'),
    65: (155, 'NNet.Game.STriggerPlanetMissionSelectedEvent'),
    66: (156, 'NNet.Game.STriggerKeyPressedEvent'),
    67: (167, 'NNet.Game.STriggerMovieFunctionEvent'),
    68: (78, 'NNet.Game.STriggerPlanetPanelBirthCompleteEvent'),
    69: (78, 'NNet.Game.STriggerPlanetPanelDeathCompleteEvent'),
    70: (157, 'NNet.Game.SResourceRequestEvent'),
    71: (158, 'NNet.Game.SResourceRequestFulfillEvent'),
    72: (159, 'NNet.Game.SResourceRequestCancelEvent'),
    73: (78, 'NNet.Game.STriggerResearchPanelExitEvent'),
    74: (78, 'NNet.Game.STriggerResearchPanelPurchaseEvent'),
    75: (160, 'NNet.Game.STriggerResearchPanelSelectionChangedEvent'),
    77: (78, 'NNet.Game.STriggerMercenaryPanelExitEvent'),
    78: (78, 'NNet.Game.STriggerMercenaryPanelPurchaseEvent'),
    79: (161, 'NNet.Game.STriggerMercenaryPanelSelectionChangedEvent'),
    80: (78, 'NNet.Game.STriggerVictoryPanelExitEvent'),
    81: (78, 'NNet.Game.STriggerBattleReportPanelExitEvent'),
    82: (162, 'NNet.Game.STriggerBattleReportPanelPlayMissionEvent'),
    83: (163, 'NNet.Game.STriggerBattleReportPanelPlaySceneEvent'),
    84: (163, 'NNet.Game.STriggerBattleReportPanelSelectionChangedEvent'),
    85: (129, 'NNet.Game.STriggerVictoryPanelPlayMissionAgainEvent'),
    86: (78, 'NNet.Game.STriggerMovieStartedEvent'),
    87: (78, 'NNet.Game.STriggerMovieFinishedEvent'),
    88: (165, 'NNet.Game.SDecrementGameTimeRemainingEvent'),
    89: (166, 'NNet.Game.STriggerPortraitLoadedEvent'),
    90: (168, 'NNet.Game.STriggerCustomDialogDismissedEvent'),
    91: (169, 'NNet.Game.STriggerGameMenuItemSelectedEvent'),
    93: (128, 'NNet.Game.STriggerPurchasePanelSelectedPurchaseItemChangedEvent'),
    94: (170, 'NNet.Game.STriggerPurchasePanelSelectedPurchaseCategoryChangedEvent'),
    95: (171, 'NNet.Game.STriggerButtonPressedEvent'),
    96: (78, 'NNet.Game.STriggerGameCreditsFinishedEvent'),
    97: (172, 'NNet.Game.STriggerCutsceneBookmarkFiredEvent'),
    98: (173, 'NNet.Game.STriggerCutsceneEndSceneFiredEvent'),
    99: (174, 'NNet.Game.STriggerCutsceneConversationLineEvent'),
    100: (175, 'NNet.Game.STriggerCutsceneConversationLineMissingEvent'),
    101: (176, 'NNet.Game.SGameUserLeaveEvent'),
    102: (177, 'NNet.Game.SGameUserJoinEvent'),
    103: (179, 'NNet.Game.SCommandManagerStateEvent'),
    104: (180, 'NNet.Game.SCmdUpdateTargetPointEvent'),
    105: (181, 'NNet.Game.SCmdUpdateTargetUnitEvent'),
    106: (136, 'NNet.Game.STriggerAnimLengthQueryByNameEvent'),
    107: (137, 'NNet.Game.STriggerAnimLengthQueryByPropsEvent'),
    108: (138, 'NNet.Game.STriggerAnimOffsetEvent'),
    109: (182, 'NNet.Game.SCatalogModifyEvent'),
    110: (183, 'NNet.Game.SHeroTalentTreeSelectedEvent'),
    111: (78, 'NNet.Game.STriggerProfilerLoggingFinishedEvent'),
    112: (184, 'NNet.Game.SHeroTalentTreeSelectionPanelToggledEvent'),
}

# The typeid of the NNet.Game.EEventId enum.
game_eventid_typeid = 0

# Map from protocol NNet.Game.*Message eventid to (typeid, name)
message_event_types = {
    0: (185, 'NNet.Game.SChatMessage'),
    1: (186, 'NNet.Game.SPingMessage'),
    2: (187, 'NNet.Game.SLoadingProgressMessage'),
    3: (78, 'NNet.Game.SServerPingMessage'),
    4: (188, 'NNet.Game.SReconnectNotifyMessage'),
}

# The typeid of the NNet.Game.EMessageId enum.
message_eventid_typeid = 1

# Map from protocol NNet.Replay.Tracker.*Event eventid to (typeid, name)
tracker_event_types = {
    0: (190, 'NNet.Replay.Tracker.SPlayerStatsEvent'),
    1: (191, 'NNet.Replay.Tracker.SUnitBornEvent'),
    2: (192, 'NNet.Replay.Tracker.SUnitDiedEvent'),
    3: (193, 'NNet.Replay.Tracker.SUnitOwnerChangeEvent'),
    4: (194, 'NNet.Replay.Tracker.SUnitTypeChangeEvent'),
    5: (195, 'NNet.Replay.Tracker.SUpgradeEvent'),
    6: (191, 'NNet.Replay.Tracker.SUnitInitEvent'),
    7: (196, 'NNet.Replay.Tracker.SUnitDoneEvent'),
    8: (198, 'NNet.Replay.Tracker.SUnitPositionsEvent'),
    9: (199, 'NNet.Replay.Tracker.SPlayerSetupEvent'),
}

# The typeid of the NNet.Replay.Tracker.EEventId enum.
tracker_eventid_typeid = 2

# The typeid of NNet.SVarUint32 (the type used to encode gameloop deltas).
svaruint32_typeid = 7

# The typeid of NNet.Replay.SGameUserId (the type used to encode player ids).
replay_userid_typeid = 8

# The typeid of NNet.Replay.SHeader (the type used to store replay game version and length).
replay_header_typeid = 18

# The typeid of NNet.Game.SDetails (the type used to store overall replay details).
game_details_typeid = 40

# The typeid of NNet.Replay.SInitData (the type used to store the inital lobby).
replay_initdata_typeid = 69


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
