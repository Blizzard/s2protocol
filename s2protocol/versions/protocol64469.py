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
    ('_array',[(16,0),10]),  #14
    ('_optional',[14]),  #15
    ('_blob',[(16,0)]),  #16
    ('_struct',[[('m_dataDeprecated',15,0),('m_data',16,1)]]),  #17
    ('_struct',[[('m_signature',9,0),('m_version',11,1),('m_type',12,2),('m_elapsedGameLoops',6,3),('m_useScaledTime',13,4),('m_ngdpRootKey',17,5),('m_dataBuildNum',6,6),('m_replayCompatibilityHash',17,7),('m_ngdpRootKeyIsDevData',13,8)]]),  #18
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
    ('_int',[(-9223372036854775808,64)]),  #32
    ('_optional',[13]),  #33
    ('_blob',[(0,12)]),  #34
    ('_blob',[(40,0)]),  #35
    ('_array',[(0,6),35]),  #36
    ('_optional',[36]),  #37
    ('_array',[(0,6),30]),  #38
    ('_optional',[38]),  #39
    ('_struct',[[('m_playerList',28,0),('m_title',29,1),('m_difficulty',9,2),('m_thumbnail',31,3),('m_isBlizzardMap',13,4),('m_timeUTC',32,5),('m_timeLocalOffset',32,6),('m_restartAsTransitionMap',33,16),('m_disableRecoverGame',13,17),('m_description',34,7),('m_imageFilePath',30,8),('m_campaignIndex',10,15),('m_mapFileName',30,9),('m_cacheHandles',37,10),('m_miniSave',13,11),('m_gameSpeed',12,12),('m_defaultDifficulty',3,13),('m_modPaths',39,14)]]),  #40
    ('_optional',[9]),  #41
    ('_optional',[35]),  #42
    ('_optional',[6]),  #43
    ('_struct',[[('m_race',25,-1)]]),  #44
    ('_struct',[[('m_team',25,-1)]]),  #45
    ('_blob',[(0,9)]),  #46
    ('_int',[(-2147483648,32)]),  #47
    ('_optional',[47]),  #48
    ('_struct',[[('m_name',9,-19),('m_clanTag',41,-18),('m_clanLogo',42,-17),('m_highestLeague',25,-16),('m_combinedRaceLevels',43,-15),('m_randomSeed',6,-14),('m_racePreference',44,-13),('m_teamPreference',45,-12),('m_testMap',13,-11),('m_testAuto',13,-10),('m_examine',13,-9),('m_customInterface',13,-8),('m_testType',6,-7),('m_observe',24,-6),('m_hero',46,-5),('m_skin',46,-4),('m_mount',46,-3),('m_toonHandle',20,-2),('m_scaledRating',48,-1)]]),  #49
    ('_array',[(0,5),49]),  #50
    ('_struct',[[('m_lockTeams',13,-16),('m_teamsTogether',13,-15),('m_advancedSharedControl',13,-14),('m_randomRaces',13,-13),('m_battleNet',13,-12),('m_amm',13,-11),('m_competitive',13,-10),('m_practice',13,-9),('m_cooperative',13,-8),('m_noVictoryOrDefeat',13,-7),('m_heroDuplicatesAllowed',13,-6),('m_fog',24,-5),('m_observers',24,-4),('m_userDifficulty',24,-3),('m_clientDebugFlags',21,-2),('m_buildCoachEnabled',13,-1)]]),  #51
    ('_int',[(1,4)]),  #52
    ('_int',[(1,8)]),  #53
    ('_bitarray',[(0,6)]),  #54
    ('_bitarray',[(0,8)]),  #55
    ('_bitarray',[(0,2)]),  #56
    ('_struct',[[('m_allowedColors',54,-6),('m_allowedRaces',55,-5),('m_allowedDifficulty',54,-4),('m_allowedControls',55,-3),('m_allowedObserveTypes',56,-2),('m_allowedAIBuilds',55,-1)]]),  #57
    ('_array',[(0,5),57]),  #58
    ('_struct',[[('m_randomValue',6,-28),('m_gameCacheName',29,-27),('m_gameOptions',51,-26),('m_gameSpeed',12,-25),('m_gameType',12,-24),('m_maxUsers',2,-23),('m_maxObservers',2,-22),('m_maxPlayers',2,-21),('m_maxTeams',52,-20),('m_maxColors',3,-19),('m_maxRaces',53,-18),('m_maxControls',10,-17),('m_mapSizeX',10,-16),('m_mapSizeY',10,-15),('m_mapFileSyncChecksum',6,-14),('m_mapFileName',30,-13),('m_mapAuthorName',9,-12),('m_modFileSyncChecksum',6,-11),('m_slotDescriptions',58,-10),('m_defaultDifficulty',3,-9),('m_defaultAIBuild',10,-8),('m_cacheHandles',36,-7),('m_hasExtensionMod',13,-6),('m_hasNonBlizzardExtensionMod',13,-5),('m_isBlizzardMap',13,-4),('m_isPremadeFFA',13,-3),('m_isCoopMode',13,-2),('m_isRealtimeMode',13,-1)]]),  #59
    ('_optional',[1]),  #60
    ('_optional',[2]),  #61
    ('_struct',[[('m_color',61,-1)]]),  #62
    ('_array',[(0,4),46]),  #63
    ('_array',[(0,17),6]),  #64
    ('_array',[(0,9),6]),  #65
    ('_array',[(0,3),6]),  #66
    ('_struct',[[('m_key',6,-2),('m_rewards',64,-1)]]),  #67
    ('_array',[(0,17),67]),  #68
    ('_struct',[[('m_control',10,-26),('m_userId',60,-25),('m_teamId',1,-24),('m_colorPref',62,-23),('m_racePref',44,-22),('m_difficulty',3,-21),('m_aiBuild',10,-20),('m_handicap',0,-19),('m_observe',24,-18),('m_logoIndex',6,-17),('m_hero',46,-16),('m_skin',46,-15),('m_mount',46,-14),('m_artifacts',63,-13),('m_workingSetSlotId',25,-12),('m_rewards',64,-11),('m_toonHandle',20,-10),('m_licenses',65,-9),('m_tandemLeaderId',60,-8),('m_commander',46,-7),('m_commanderLevel',6,-6),('m_hasSilencePenalty',13,-5),('m_tandemId',60,-4),('m_commanderMasteryLevel',6,-3),('m_commanderMasteryTalents',66,-2),('m_rewardOverrides',68,-1)]]),  #69
    ('_array',[(0,5),69]),  #70
    ('_struct',[[('m_phase',12,-11),('m_maxUsers',2,-10),('m_maxObservers',2,-9),('m_slots',70,-8),('m_randomSeed',6,-7),('m_hostUserId',60,-6),('m_isSinglePlayer',13,-5),('m_pickedMapTag',10,-4),('m_gameDuration',6,-3),('m_defaultDifficulty',3,-2),('m_defaultAIBuild',10,-1)]]),  #71
    ('_struct',[[('m_userInitialData',50,-3),('m_gameDescription',59,-2),('m_lobbyState',71,-1)]]),  #72
    ('_struct',[[('m_syncLobbyState',72,-1)]]),  #73
    ('_struct',[[('m_name',20,-6)]]),  #74
    ('_blob',[(0,6)]),  #75
    ('_struct',[[('m_name',75,-6)]]),  #76
    ('_struct',[[('m_name',75,-8),('m_type',6,-7),('m_data',20,-6)]]),  #77
    ('_struct',[[('m_type',6,-8),('m_name',75,-7),('m_data',34,-6)]]),  #78
    ('_array',[(0,5),10]),  #79
    ('_struct',[[('m_signature',79,-7),('m_toonHandle',20,-6)]]),  #80
    ('_struct',[[('m_gameFullyDownloaded',13,-19),('m_developmentCheatsEnabled',13,-18),('m_testCheatsEnabled',13,-17),('m_multiplayerCheatsEnabled',13,-16),('m_syncChecksummingEnabled',13,-15),('m_isMapToMapTransition',13,-14),('m_debugPauseEnabled',13,-13),('m_useGalaxyAsserts',13,-12),('m_platformMac',13,-11),('m_cameraFollow',13,-10),('m_baseBuildNum',6,-9),('m_buildNum',6,-8),('m_versionFlags',6,-7),('m_hotkeyProfile',46,-6)]]),  #81
    ('_struct',[[]]),  #82
    ('_int',[(0,16)]),  #83
    ('_struct',[[('x',83,-2),('y',83,-1)]]),  #84
    ('_struct',[[('m_which',12,-7),('m_target',84,-6)]]),  #85
    ('_struct',[[('m_fileName',30,-10),('m_automatic',13,-9),('m_overwrite',13,-8),('m_name',9,-7),('m_description',29,-6)]]),  #86
    ('_struct',[[('m_sequence',6,-6)]]),  #87
    ('_struct',[[('x',47,-2),('y',47,-1)]]),  #88
    ('_struct',[[('m_point',88,-4),('m_time',47,-3),('m_verb',29,-2),('m_arguments',29,-1)]]),  #89
    ('_struct',[[('m_data',89,-6)]]),  #90
    ('_int',[(0,26)]),  #91
    ('_struct',[[('m_abilLink',83,-3),('m_abilCmdIndex',2,-2),('m_abilCmdData',25,-1)]]),  #92
    ('_optional',[92]),  #93
    ('_null',[]),  #94
    ('_int',[(0,20)]),  #95
    ('_struct',[[('x',95,-3),('y',95,-2),('z',47,-1)]]),  #96
    ('_struct',[[('m_targetUnitFlags',83,-7),('m_timer',10,-6),('m_tag',6,-5),('m_snapshotUnitLink',83,-4),('m_snapshotControlPlayerId',60,-3),('m_snapshotUpkeepPlayerId',60,-2),('m_snapshotPoint',96,-1)]]),  #97
    ('_choice',[(0,2),{0:('None',94),1:('TargetPoint',96),2:('TargetUnit',97),3:('Data',6)}]),  #98
    ('_int',[(1,32)]),  #99
    ('_struct',[[('m_cmdFlags',91,-11),('m_abil',93,-10),('m_data',98,-9),('m_sequence',99,-8),('m_otherUnit',43,-7),('m_unitGroup',43,-6)]]),  #100
    ('_int',[(0,9)]),  #101
    ('_bitarray',[(0,9)]),  #102
    ('_array',[(0,9),101]),  #103
    ('_choice',[(0,2),{0:('None',94),1:('Mask',102),2:('OneIndices',103),3:('ZeroIndices',103)}]),  #104
    ('_struct',[[('m_unitLink',83,-4),('m_subgroupPriority',10,-3),('m_intraSubgroupPriority',10,-2),('m_count',101,-1)]]),  #105
    ('_array',[(0,9),105]),  #106
    ('_struct',[[('m_subgroupIndex',101,-4),('m_removeMask',104,-3),('m_addSubgroups',106,-2),('m_addUnitTags',65,-1)]]),  #107
    ('_struct',[[('m_controlGroupId',1,-7),('m_delta',107,-6)]]),  #108
    ('_struct',[[('m_controlGroupIndex',1,-8),('m_controlGroupUpdate',12,-7),('m_mask',104,-6)]]),  #109
    ('_struct',[[('m_count',101,-6),('m_subgroupCount',101,-5),('m_activeSubgroupIndex',101,-4),('m_unitTagsChecksum',6,-3),('m_subgroupIndicesChecksum',6,-2),('m_subgroupsChecksum',6,-1)]]),  #110
    ('_struct',[[('m_controlGroupId',1,-7),('m_selectionSyncData',110,-6)]]),  #111
    ('_array',[(0,3),47]),  #112
    ('_struct',[[('m_recipientId',1,-7),('m_resources',112,-6)]]),  #113
    ('_struct',[[('m_chatMessage',29,-6)]]),  #114
    ('_int',[(-128,8)]),  #115
    ('_struct',[[('x',47,-3),('y',47,-2),('z',47,-1)]]),  #116
    ('_struct',[[('m_beacon',115,-14),('m_ally',115,-13),('m_flags',115,-12),('m_build',115,-11),('m_targetUnitTag',6,-10),('m_targetUnitSnapshotUnitLink',83,-9),('m_targetUnitSnapshotUpkeepPlayerId',115,-8),('m_targetUnitSnapshotControlPlayerId',115,-7),('m_targetPoint',116,-6)]]),  #117
    ('_struct',[[('m_speed',12,-6)]]),  #118
    ('_struct',[[('m_delta',115,-6)]]),  #119
    ('_struct',[[('m_point',88,-14),('m_unit',6,-13),('m_unitLink',83,-12),('m_unitControlPlayerId',60,-11),('m_unitUpkeepPlayerId',60,-10),('m_unitPosition',96,-9),('m_unitIsUnderConstruction',13,-8),('m_pingedMinimap',13,-7),('m_option',47,-6)]]),  #120
    ('_struct',[[('m_verb',29,-7),('m_arguments',29,-6)]]),  #121
    ('_struct',[[('m_alliance',6,-7),('m_control',6,-6)]]),  #122
    ('_struct',[[('m_unitTag',6,-6)]]),  #123
    ('_struct',[[('m_unitTag',6,-7),('m_flags',10,-6)]]),  #124
    ('_struct',[[('m_conversationId',47,-7),('m_replyId',47,-6)]]),  #125
    ('_optional',[20]),  #126
    ('_struct',[[('m_gameUserId',1,-6),('m_observe',24,-5),('m_name',9,-4),('m_toonHandle',126,-3),('m_clanTag',41,-2),('m_clanLogo',42,-1)]]),  #127
    ('_array',[(0,5),127]),  #128
    ('_int',[(0,1)]),  #129
    ('_struct',[[('m_userInfos',128,-7),('m_method',129,-6)]]),  #130
    ('_struct',[[('m_purchaseItemId',47,-6)]]),  #131
    ('_struct',[[('m_difficultyLevel',47,-6)]]),  #132
    ('_choice',[(0,3),{0:('None',94),1:('Checked',13),2:('ValueChanged',6),3:('SelectionChanged',47),4:('TextChanged',30),5:('MouseButton',6)}]),  #133
    ('_struct',[[('m_controlId',47,-8),('m_eventType',47,-7),('m_eventData',133,-6)]]),  #134
    ('_struct',[[('m_soundHash',6,-7),('m_length',6,-6)]]),  #135
    ('_array',[(0,7),6]),  #136
    ('_struct',[[('m_soundHash',136,-2),('m_length',136,-1)]]),  #137
    ('_struct',[[('m_syncInfo',137,-6)]]),  #138
    ('_struct',[[('m_queryId',83,-8),('m_lengthMs',6,-7),('m_finishGameLoop',6,-6)]]),  #139
    ('_struct',[[('m_queryId',83,-7),('m_lengthMs',6,-6)]]),  #140
    ('_struct',[[('m_animWaitQueryId',83,-6)]]),  #141
    ('_struct',[[('m_sound',6,-6)]]),  #142
    ('_struct',[[('m_transmissionId',47,-7),('m_thread',6,-6)]]),  #143
    ('_struct',[[('m_transmissionId',47,-6)]]),  #144
    ('_optional',[84]),  #145
    ('_optional',[83]),  #146
    ('_optional',[115]),  #147
    ('_struct',[[('m_target',145,-11),('m_distance',146,-10),('m_pitch',146,-9),('m_yaw',146,-8),('m_reason',147,-7),('m_follow',13,-6)]]),  #148
    ('_struct',[[('m_skipType',129,-6)]]),  #149
    ('_int',[(0,11)]),  #150
    ('_struct',[[('x',150,-2),('y',150,-1)]]),  #151
    ('_struct',[[('m_button',6,-10),('m_down',13,-9),('m_posUI',151,-8),('m_posWorld',96,-7),('m_flags',115,-6)]]),  #152
    ('_struct',[[('m_posUI',151,-8),('m_posWorld',96,-7),('m_flags',115,-6)]]),  #153
    ('_struct',[[('m_achievementLink',83,-6)]]),  #154
    ('_struct',[[('m_hotkey',6,-7),('m_down',13,-6)]]),  #155
    ('_struct',[[('m_abilLink',83,-8),('m_abilCmdIndex',2,-7),('m_state',115,-6)]]),  #156
    ('_struct',[[('m_soundtrack',6,-6)]]),  #157
    ('_struct',[[('m_planetId',47,-6)]]),  #158
    ('_struct',[[('m_key',115,-7),('m_flags',115,-6)]]),  #159
    ('_struct',[[('m_resources',112,-6)]]),  #160
    ('_struct',[[('m_fulfillRequestId',47,-6)]]),  #161
    ('_struct',[[('m_cancelRequestId',47,-6)]]),  #162
    ('_struct',[[('m_error',47,-7),('m_abil',93,-6)]]),  #163
    ('_struct',[[('m_researchItemId',47,-6)]]),  #164
    ('_struct',[[('m_mercenaryId',47,-6)]]),  #165
    ('_struct',[[('m_battleReportId',47,-7),('m_difficultyLevel',47,-6)]]),  #166
    ('_struct',[[('m_battleReportId',47,-6)]]),  #167
    ('_struct',[[('m_decrementSeconds',47,-6)]]),  #168
    ('_struct',[[('m_portraitId',47,-6)]]),  #169
    ('_struct',[[('m_functionName',20,-6)]]),  #170
    ('_struct',[[('m_result',47,-6)]]),  #171
    ('_struct',[[('m_gameMenuItemIndex',47,-6)]]),  #172
    ('_int',[(-32768,16)]),  #173
    ('_struct',[[('m_wheelSpin',173,-7),('m_flags',115,-6)]]),  #174
    ('_struct',[[('m_purchaseCategoryId',47,-6)]]),  #175
    ('_struct',[[('m_button',83,-6)]]),  #176
    ('_struct',[[('m_cutsceneId',47,-7),('m_bookmarkName',20,-6)]]),  #177
    ('_struct',[[('m_cutsceneId',47,-6)]]),  #178
    ('_struct',[[('m_cutsceneId',47,-8),('m_conversationLine',20,-7),('m_altConversationLine',20,-6)]]),  #179
    ('_struct',[[('m_cutsceneId',47,-7),('m_conversationLine',20,-6)]]),  #180
    ('_struct',[[('m_leaveReason',1,-6)]]),  #181
    ('_struct',[[('m_observe',24,-12),('m_name',9,-11),('m_toonHandle',126,-10),('m_clanTag',41,-9),('m_clanLogo',42,-8),('m_hijack',13,-7),('m_hijackCloneGameUserId',60,-6)]]),  #182
    ('_optional',[99]),  #183
    ('_struct',[[('m_state',24,-7),('m_sequence',183,-6)]]),  #184
    ('_struct',[[('m_target',96,-6)]]),  #185
    ('_struct',[[('m_target',97,-6)]]),  #186
    ('_struct',[[('m_catalog',10,-9),('m_entry',83,-8),('m_field',9,-7),('m_value',9,-6)]]),  #187
    ('_struct',[[('m_index',6,-6)]]),  #188
    ('_struct',[[('m_shown',13,-6)]]),  #189
    ('_struct',[[('m_recipient',12,-3),('m_string',30,-2)]]),  #190
    ('_struct',[[('m_recipient',12,-3),('m_point',88,-2)]]),  #191
    ('_struct',[[('m_progress',47,-2)]]),  #192
    ('_struct',[[('m_status',24,-2)]]),  #193
    ('_struct',[[('m_scoreValueMineralsCurrent',47,0),('m_scoreValueVespeneCurrent',47,1),('m_scoreValueMineralsCollectionRate',47,2),('m_scoreValueVespeneCollectionRate',47,3),('m_scoreValueWorkersActiveCount',47,4),('m_scoreValueMineralsUsedInProgressArmy',47,5),('m_scoreValueMineralsUsedInProgressEconomy',47,6),('m_scoreValueMineralsUsedInProgressTechnology',47,7),('m_scoreValueVespeneUsedInProgressArmy',47,8),('m_scoreValueVespeneUsedInProgressEconomy',47,9),('m_scoreValueVespeneUsedInProgressTechnology',47,10),('m_scoreValueMineralsUsedCurrentArmy',47,11),('m_scoreValueMineralsUsedCurrentEconomy',47,12),('m_scoreValueMineralsUsedCurrentTechnology',47,13),('m_scoreValueVespeneUsedCurrentArmy',47,14),('m_scoreValueVespeneUsedCurrentEconomy',47,15),('m_scoreValueVespeneUsedCurrentTechnology',47,16),('m_scoreValueMineralsLostArmy',47,17),('m_scoreValueMineralsLostEconomy',47,18),('m_scoreValueMineralsLostTechnology',47,19),('m_scoreValueVespeneLostArmy',47,20),('m_scoreValueVespeneLostEconomy',47,21),('m_scoreValueVespeneLostTechnology',47,22),('m_scoreValueMineralsKilledArmy',47,23),('m_scoreValueMineralsKilledEconomy',47,24),('m_scoreValueMineralsKilledTechnology',47,25),('m_scoreValueVespeneKilledArmy',47,26),('m_scoreValueVespeneKilledEconomy',47,27),('m_scoreValueVespeneKilledTechnology',47,28),('m_scoreValueFoodUsed',47,29),('m_scoreValueFoodMade',47,30),('m_scoreValueMineralsUsedActiveForces',47,31),('m_scoreValueVespeneUsedActiveForces',47,32),('m_scoreValueMineralsFriendlyFireArmy',47,33),('m_scoreValueMineralsFriendlyFireEconomy',47,34),('m_scoreValueMineralsFriendlyFireTechnology',47,35),('m_scoreValueVespeneFriendlyFireArmy',47,36),('m_scoreValueVespeneFriendlyFireEconomy',47,37),('m_scoreValueVespeneFriendlyFireTechnology',47,38)]]),  #194
    ('_struct',[[('m_playerId',1,0),('m_stats',194,1)]]),  #195
    ('_optional',[29]),  #196
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_unitTypeName',29,2),('m_controlPlayerId',1,3),('m_upkeepPlayerId',1,4),('m_x',10,5),('m_y',10,6),('m_creatorUnitTagIndex',43,7),('m_creatorUnitTagRecycle',43,8),('m_creatorAbilityName',196,9)]]),  #197
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_killerPlayerId',60,2),('m_x',10,3),('m_y',10,4),('m_killerUnitTagIndex',43,5),('m_killerUnitTagRecycle',43,6)]]),  #198
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_controlPlayerId',1,2),('m_upkeepPlayerId',1,3)]]),  #199
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_unitTypeName',29,2)]]),  #200
    ('_struct',[[('m_playerId',1,0),('m_upgradeTypeName',29,1),('m_count',47,2)]]),  #201
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_unitTypeName',29,2),('m_controlPlayerId',1,3),('m_upkeepPlayerId',1,4),('m_x',10,5),('m_y',10,6)]]),  #202
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1)]]),  #203
    ('_array',[(0,10),47]),  #204
    ('_struct',[[('m_firstUnitIndex',6,0),('m_items',204,1)]]),  #205
    ('_struct',[[('m_playerId',1,0),('m_type',6,1),('m_userId',43,2),('m_slotId',43,3)]]),  #206
]

# Map from protocol NNet.Game.*Event eventid to (typeid, name)
game_event_types = {
    5: (82, 'NNet.Game.SUserFinishedLoadingSyncEvent'),
    7: (81, 'NNet.Game.SUserOptionsEvent'),
    9: (74, 'NNet.Game.SBankFileEvent'),
    10: (76, 'NNet.Game.SBankSectionEvent'),
    11: (77, 'NNet.Game.SBankKeyEvent'),
    12: (78, 'NNet.Game.SBankValueEvent'),
    13: (80, 'NNet.Game.SBankSignatureEvent'),
    14: (85, 'NNet.Game.SCameraSaveEvent'),
    21: (86, 'NNet.Game.SSaveGameEvent'),
    22: (82, 'NNet.Game.SSaveGameDoneEvent'),
    23: (82, 'NNet.Game.SLoadGameDoneEvent'),
    25: (87, 'NNet.Game.SCommandManagerResetEvent'),
    26: (90, 'NNet.Game.SGameCheatEvent'),
    27: (100, 'NNet.Game.SCmdEvent'),
    28: (108, 'NNet.Game.SSelectionDeltaEvent'),
    29: (109, 'NNet.Game.SControlGroupUpdateEvent'),
    30: (111, 'NNet.Game.SSelectionSyncCheckEvent'),
    31: (113, 'NNet.Game.SResourceTradeEvent'),
    32: (114, 'NNet.Game.STriggerChatMessageEvent'),
    33: (117, 'NNet.Game.SAICommunicateEvent'),
    34: (118, 'NNet.Game.SSetAbsoluteGameSpeedEvent'),
    35: (119, 'NNet.Game.SAddAbsoluteGameSpeedEvent'),
    36: (120, 'NNet.Game.STriggerPingEvent'),
    37: (121, 'NNet.Game.SBroadcastCheatEvent'),
    38: (122, 'NNet.Game.SAllianceEvent'),
    39: (123, 'NNet.Game.SUnitClickEvent'),
    40: (124, 'NNet.Game.SUnitHighlightEvent'),
    41: (125, 'NNet.Game.STriggerReplySelectedEvent'),
    43: (130, 'NNet.Game.SHijackReplayGameEvent'),
    44: (82, 'NNet.Game.STriggerSkippedEvent'),
    45: (135, 'NNet.Game.STriggerSoundLengthQueryEvent'),
    46: (142, 'NNet.Game.STriggerSoundOffsetEvent'),
    47: (143, 'NNet.Game.STriggerTransmissionOffsetEvent'),
    48: (144, 'NNet.Game.STriggerTransmissionCompleteEvent'),
    49: (148, 'NNet.Game.SCameraUpdateEvent'),
    50: (82, 'NNet.Game.STriggerAbortMissionEvent'),
    51: (131, 'NNet.Game.STriggerPurchaseMadeEvent'),
    52: (82, 'NNet.Game.STriggerPurchaseExitEvent'),
    53: (132, 'NNet.Game.STriggerPlanetMissionLaunchedEvent'),
    54: (82, 'NNet.Game.STriggerPlanetPanelCanceledEvent'),
    55: (134, 'NNet.Game.STriggerDialogControlEvent'),
    56: (138, 'NNet.Game.STriggerSoundLengthSyncEvent'),
    57: (149, 'NNet.Game.STriggerConversationSkippedEvent'),
    58: (152, 'NNet.Game.STriggerMouseClickedEvent'),
    59: (153, 'NNet.Game.STriggerMouseMovedEvent'),
    60: (154, 'NNet.Game.SAchievementAwardedEvent'),
    61: (155, 'NNet.Game.STriggerHotkeyPressedEvent'),
    62: (156, 'NNet.Game.STriggerTargetModeUpdateEvent'),
    63: (82, 'NNet.Game.STriggerPlanetPanelReplayEvent'),
    64: (157, 'NNet.Game.STriggerSoundtrackDoneEvent'),
    65: (158, 'NNet.Game.STriggerPlanetMissionSelectedEvent'),
    66: (159, 'NNet.Game.STriggerKeyPressedEvent'),
    67: (170, 'NNet.Game.STriggerMovieFunctionEvent'),
    68: (82, 'NNet.Game.STriggerPlanetPanelBirthCompleteEvent'),
    69: (82, 'NNet.Game.STriggerPlanetPanelDeathCompleteEvent'),
    70: (160, 'NNet.Game.SResourceRequestEvent'),
    71: (161, 'NNet.Game.SResourceRequestFulfillEvent'),
    72: (162, 'NNet.Game.SResourceRequestCancelEvent'),
    73: (82, 'NNet.Game.STriggerResearchPanelExitEvent'),
    74: (82, 'NNet.Game.STriggerResearchPanelPurchaseEvent'),
    75: (164, 'NNet.Game.STriggerResearchPanelSelectionChangedEvent'),
    76: (163, 'NNet.Game.STriggerCommandErrorEvent'),
    77: (82, 'NNet.Game.STriggerMercenaryPanelExitEvent'),
    78: (82, 'NNet.Game.STriggerMercenaryPanelPurchaseEvent'),
    79: (165, 'NNet.Game.STriggerMercenaryPanelSelectionChangedEvent'),
    80: (82, 'NNet.Game.STriggerVictoryPanelExitEvent'),
    81: (82, 'NNet.Game.STriggerBattleReportPanelExitEvent'),
    82: (166, 'NNet.Game.STriggerBattleReportPanelPlayMissionEvent'),
    83: (167, 'NNet.Game.STriggerBattleReportPanelPlaySceneEvent'),
    84: (167, 'NNet.Game.STriggerBattleReportPanelSelectionChangedEvent'),
    85: (132, 'NNet.Game.STriggerVictoryPanelPlayMissionAgainEvent'),
    86: (82, 'NNet.Game.STriggerMovieStartedEvent'),
    87: (82, 'NNet.Game.STriggerMovieFinishedEvent'),
    88: (168, 'NNet.Game.SDecrementGameTimeRemainingEvent'),
    89: (169, 'NNet.Game.STriggerPortraitLoadedEvent'),
    90: (171, 'NNet.Game.STriggerCustomDialogDismissedEvent'),
    91: (172, 'NNet.Game.STriggerGameMenuItemSelectedEvent'),
    92: (174, 'NNet.Game.STriggerMouseWheelEvent'),
    93: (131, 'NNet.Game.STriggerPurchasePanelSelectedPurchaseItemChangedEvent'),
    94: (175, 'NNet.Game.STriggerPurchasePanelSelectedPurchaseCategoryChangedEvent'),
    95: (176, 'NNet.Game.STriggerButtonPressedEvent'),
    96: (82, 'NNet.Game.STriggerGameCreditsFinishedEvent'),
    97: (177, 'NNet.Game.STriggerCutsceneBookmarkFiredEvent'),
    98: (178, 'NNet.Game.STriggerCutsceneEndSceneFiredEvent'),
    99: (179, 'NNet.Game.STriggerCutsceneConversationLineEvent'),
    100: (180, 'NNet.Game.STriggerCutsceneConversationLineMissingEvent'),
    101: (181, 'NNet.Game.SGameUserLeaveEvent'),
    102: (182, 'NNet.Game.SGameUserJoinEvent'),
    103: (184, 'NNet.Game.SCommandManagerStateEvent'),
    104: (185, 'NNet.Game.SCmdUpdateTargetPointEvent'),
    105: (186, 'NNet.Game.SCmdUpdateTargetUnitEvent'),
    106: (139, 'NNet.Game.STriggerAnimLengthQueryByNameEvent'),
    107: (140, 'NNet.Game.STriggerAnimLengthQueryByPropsEvent'),
    108: (141, 'NNet.Game.STriggerAnimOffsetEvent'),
    109: (187, 'NNet.Game.SCatalogModifyEvent'),
    110: (188, 'NNet.Game.SHeroTalentTreeSelectedEvent'),
    111: (82, 'NNet.Game.STriggerProfilerLoggingFinishedEvent'),
    112: (189, 'NNet.Game.SHeroTalentTreeSelectionPanelToggledEvent'),
}

# The typeid of the NNet.Game.EEventId enum.
game_eventid_typeid = 0

# Map from protocol NNet.Game.*Message eventid to (typeid, name)
message_event_types = {
    0: (190, 'NNet.Game.SChatMessage'),
    1: (191, 'NNet.Game.SPingMessage'),
    2: (192, 'NNet.Game.SLoadingProgressMessage'),
    3: (82, 'NNet.Game.SServerPingMessage'),
    4: (193, 'NNet.Game.SReconnectNotifyMessage'),
}

# The typeid of the NNet.Game.EMessageId enum.
message_eventid_typeid = 1

# Map from protocol NNet.Replay.Tracker.*Event eventid to (typeid, name)
tracker_event_types = {
    0: (195, 'NNet.Replay.Tracker.SPlayerStatsEvent'),
    1: (197, 'NNet.Replay.Tracker.SUnitBornEvent'),
    2: (198, 'NNet.Replay.Tracker.SUnitDiedEvent'),
    3: (199, 'NNet.Replay.Tracker.SUnitOwnerChangeEvent'),
    4: (200, 'NNet.Replay.Tracker.SUnitTypeChangeEvent'),
    5: (201, 'NNet.Replay.Tracker.SUpgradeEvent'),
    6: (202, 'NNet.Replay.Tracker.SUnitInitEvent'),
    7: (203, 'NNet.Replay.Tracker.SUnitDoneEvent'),
    8: (205, 'NNet.Replay.Tracker.SUnitPositionsEvent'),
    9: (206, 'NNet.Replay.Tracker.SPlayerSetupEvent'),
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
replay_header_typeid = 18

# The typeid of NNet.Game.SDetails (the type used to store overall replay details).
game_details_typeid = 40

# The typeid of NNet.Replay.SInitData (the type used to store the inital lobby).
replay_initdata_typeid = 73


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
