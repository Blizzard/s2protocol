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
    ('_struct',[[('m_name',9,-18),('m_clanTag',41,-17),('m_clanLogo',42,-16),('m_highestLeague',25,-15),('m_combinedRaceLevels',43,-14),('m_randomSeed',6,-13),('m_racePreference',44,-12),('m_teamPreference',45,-11),('m_testMap',13,-10),('m_testAuto',13,-9),('m_examine',13,-8),('m_customInterface',13,-7),('m_testType',6,-6),('m_observe',24,-5),('m_hero',46,-4),('m_skin',46,-3),('m_mount',46,-2),('m_toonHandle',20,-1)]]),  #47
    ('_array',[(0,5),47]),  #48
    ('_struct',[[('m_lockTeams',13,-15),('m_teamsTogether',13,-14),('m_advancedSharedControl',13,-13),('m_randomRaces',13,-12),('m_battleNet',13,-11),('m_amm',13,-10),('m_competitive',13,-9),('m_practice',13,-8),('m_cooperative',13,-7),('m_noVictoryOrDefeat',13,-6),('m_heroDuplicatesAllowed',13,-5),('m_fog',24,-4),('m_observers',24,-3),('m_userDifficulty',24,-2),('m_clientDebugFlags',21,-1)]]),  #49
    ('_int',[(1,4)]),  #50
    ('_int',[(1,8)]),  #51
    ('_bitarray',[(0,6)]),  #52
    ('_bitarray',[(0,8)]),  #53
    ('_bitarray',[(0,2)]),  #54
    ('_struct',[[('m_allowedColors',52,-6),('m_allowedRaces',53,-5),('m_allowedDifficulty',52,-4),('m_allowedControls',53,-3),('m_allowedObserveTypes',54,-2),('m_allowedAIBuilds',53,-1)]]),  #55
    ('_array',[(0,5),55]),  #56
    ('_struct',[[('m_randomValue',6,-27),('m_gameCacheName',29,-26),('m_gameOptions',49,-25),('m_gameSpeed',12,-24),('m_gameType',12,-23),('m_maxUsers',2,-22),('m_maxObservers',2,-21),('m_maxPlayers',2,-20),('m_maxTeams',50,-19),('m_maxColors',3,-18),('m_maxRaces',51,-17),('m_maxControls',10,-16),('m_mapSizeX',10,-15),('m_mapSizeY',10,-14),('m_mapFileSyncChecksum',6,-13),('m_mapFileName',30,-12),('m_mapAuthorName',9,-11),('m_modFileSyncChecksum',6,-10),('m_slotDescriptions',56,-9),('m_defaultDifficulty',3,-8),('m_defaultAIBuild',10,-7),('m_cacheHandles',36,-6),('m_hasExtensionMod',13,-5),('m_hasNonBlizzardExtensionMod',13,-4),('m_isBlizzardMap',13,-3),('m_isPremadeFFA',13,-2),('m_isCoopMode',13,-1)]]),  #57
    ('_optional',[1]),  #58
    ('_optional',[2]),  #59
    ('_struct',[[('m_color',59,-1)]]),  #60
    ('_array',[(0,4),46]),  #61
    ('_array',[(0,17),6]),  #62
    ('_array',[(0,9),6]),  #63
    ('_array',[(0,3),6]),  #64
    ('_struct',[[('m_key',6,-2),('m_rewards',62,-1)]]),  #65
    ('_array',[(0,17),65]),  #66
    ('_struct',[[('m_control',10,-26),('m_userId',58,-25),('m_teamId',1,-24),('m_colorPref',60,-23),('m_racePref',44,-22),('m_difficulty',3,-21),('m_aiBuild',10,-20),('m_handicap',0,-19),('m_observe',24,-18),('m_logoIndex',6,-17),('m_hero',46,-16),('m_skin',46,-15),('m_mount',46,-14),('m_artifacts',61,-13),('m_workingSetSlotId',25,-12),('m_rewards',62,-11),('m_toonHandle',20,-10),('m_licenses',63,-9),('m_tandemLeaderId',58,-8),('m_commander',46,-7),('m_commanderLevel',6,-6),('m_hasSilencePenalty',13,-5),('m_tandemId',58,-4),('m_commanderMasteryLevel',6,-3),('m_commanderMasteryTalents',64,-2),('m_rewardOverrides',66,-1)]]),  #67
    ('_array',[(0,5),67]),  #68
    ('_struct',[[('m_phase',12,-11),('m_maxUsers',2,-10),('m_maxObservers',2,-9),('m_slots',68,-8),('m_randomSeed',6,-7),('m_hostUserId',58,-6),('m_isSinglePlayer',13,-5),('m_pickedMapTag',10,-4),('m_gameDuration',6,-3),('m_defaultDifficulty',3,-2),('m_defaultAIBuild',10,-1)]]),  #69
    ('_struct',[[('m_userInitialData',48,-3),('m_gameDescription',57,-2),('m_lobbyState',69,-1)]]),  #70
    ('_struct',[[('m_syncLobbyState',70,-1)]]),  #71
    ('_struct',[[('m_name',20,-6)]]),  #72
    ('_blob',[(0,6)]),  #73
    ('_struct',[[('m_name',73,-6)]]),  #74
    ('_struct',[[('m_name',73,-8),('m_type',6,-7),('m_data',20,-6)]]),  #75
    ('_struct',[[('m_type',6,-8),('m_name',73,-7),('m_data',34,-6)]]),  #76
    ('_array',[(0,5),10]),  #77
    ('_struct',[[('m_signature',77,-7),('m_toonHandle',20,-6)]]),  #78
    ('_struct',[[('m_gameFullyDownloaded',13,-19),('m_developmentCheatsEnabled',13,-18),('m_testCheatsEnabled',13,-17),('m_multiplayerCheatsEnabled',13,-16),('m_syncChecksummingEnabled',13,-15),('m_isMapToMapTransition',13,-14),('m_debugPauseEnabled',13,-13),('m_useGalaxyAsserts',13,-12),('m_platformMac',13,-11),('m_cameraFollow',13,-10),('m_baseBuildNum',6,-9),('m_buildNum',6,-8),('m_versionFlags',6,-7),('m_hotkeyProfile',46,-6)]]),  #79
    ('_struct',[[]]),  #80
    ('_int',[(0,16)]),  #81
    ('_struct',[[('x',81,-2),('y',81,-1)]]),  #82
    ('_struct',[[('m_which',12,-7),('m_target',82,-6)]]),  #83
    ('_struct',[[('m_fileName',30,-10),('m_automatic',13,-9),('m_overwrite',13,-8),('m_name',9,-7),('m_description',29,-6)]]),  #84
    ('_struct',[[('m_sequence',6,-6)]]),  #85
    ('_int',[(-2147483648,32)]),  #86
    ('_struct',[[('x',86,-2),('y',86,-1)]]),  #87
    ('_struct',[[('m_point',87,-4),('m_time',86,-3),('m_verb',29,-2),('m_arguments',29,-1)]]),  #88
    ('_struct',[[('m_data',88,-6)]]),  #89
    ('_int',[(0,25)]),  #90
    ('_struct',[[('m_abilLink',81,-3),('m_abilCmdIndex',2,-2),('m_abilCmdData',25,-1)]]),  #91
    ('_optional',[91]),  #92
    ('_null',[]),  #93
    ('_int',[(0,20)]),  #94
    ('_struct',[[('x',94,-3),('y',94,-2),('z',86,-1)]]),  #95
    ('_struct',[[('m_targetUnitFlags',81,-7),('m_timer',10,-6),('m_tag',6,-5),('m_snapshotUnitLink',81,-4),('m_snapshotControlPlayerId',58,-3),('m_snapshotUpkeepPlayerId',58,-2),('m_snapshotPoint',95,-1)]]),  #96
    ('_choice',[(0,2),{0:('None',93),1:('TargetPoint',95),2:('TargetUnit',96),3:('Data',6)}]),  #97
    ('_int',[(1,32)]),  #98
    ('_struct',[[('m_cmdFlags',90,-11),('m_abil',92,-10),('m_data',97,-9),('m_sequence',98,-8),('m_otherUnit',43,-7),('m_unitGroup',43,-6)]]),  #99
    ('_int',[(0,9)]),  #100
    ('_bitarray',[(0,9)]),  #101
    ('_array',[(0,9),100]),  #102
    ('_choice',[(0,2),{0:('None',93),1:('Mask',101),2:('OneIndices',102),3:('ZeroIndices',102)}]),  #103
    ('_struct',[[('m_unitLink',81,-4),('m_subgroupPriority',10,-3),('m_intraSubgroupPriority',10,-2),('m_count',100,-1)]]),  #104
    ('_array',[(0,9),104]),  #105
    ('_struct',[[('m_subgroupIndex',100,-4),('m_removeMask',103,-3),('m_addSubgroups',105,-2),('m_addUnitTags',63,-1)]]),  #106
    ('_struct',[[('m_controlGroupId',1,-7),('m_delta',106,-6)]]),  #107
    ('_struct',[[('m_controlGroupIndex',1,-8),('m_controlGroupUpdate',12,-7),('m_mask',103,-6)]]),  #108
    ('_struct',[[('m_count',100,-6),('m_subgroupCount',100,-5),('m_activeSubgroupIndex',100,-4),('m_unitTagsChecksum',6,-3),('m_subgroupIndicesChecksum',6,-2),('m_subgroupsChecksum',6,-1)]]),  #109
    ('_struct',[[('m_controlGroupId',1,-7),('m_selectionSyncData',109,-6)]]),  #110
    ('_array',[(0,3),86]),  #111
    ('_struct',[[('m_recipientId',1,-7),('m_resources',111,-6)]]),  #112
    ('_struct',[[('m_chatMessage',29,-6)]]),  #113
    ('_int',[(-128,8)]),  #114
    ('_struct',[[('x',86,-3),('y',86,-2),('z',86,-1)]]),  #115
    ('_struct',[[('m_beacon',114,-14),('m_ally',114,-13),('m_flags',114,-12),('m_build',114,-11),('m_targetUnitTag',6,-10),('m_targetUnitSnapshotUnitLink',81,-9),('m_targetUnitSnapshotUpkeepPlayerId',114,-8),('m_targetUnitSnapshotControlPlayerId',114,-7),('m_targetPoint',115,-6)]]),  #116
    ('_struct',[[('m_speed',12,-6)]]),  #117
    ('_struct',[[('m_delta',114,-6)]]),  #118
    ('_struct',[[('m_point',87,-14),('m_unit',6,-13),('m_unitLink',81,-12),('m_unitControlPlayerId',58,-11),('m_unitUpkeepPlayerId',58,-10),('m_unitPosition',95,-9),('m_unitIsUnderConstruction',13,-8),('m_pingedMinimap',13,-7),('m_option',86,-6)]]),  #119
    ('_struct',[[('m_verb',29,-7),('m_arguments',29,-6)]]),  #120
    ('_struct',[[('m_alliance',6,-7),('m_control',6,-6)]]),  #121
    ('_struct',[[('m_unitTag',6,-6)]]),  #122
    ('_struct',[[('m_unitTag',6,-7),('m_flags',10,-6)]]),  #123
    ('_struct',[[('m_conversationId',86,-7),('m_replyId',86,-6)]]),  #124
    ('_optional',[20]),  #125
    ('_struct',[[('m_gameUserId',1,-6),('m_observe',24,-5),('m_name',9,-4),('m_toonHandle',125,-3),('m_clanTag',41,-2),('m_clanLogo',42,-1)]]),  #126
    ('_array',[(0,5),126]),  #127
    ('_int',[(0,1)]),  #128
    ('_struct',[[('m_userInfos',127,-7),('m_method',128,-6)]]),  #129
    ('_struct',[[('m_purchaseItemId',86,-6)]]),  #130
    ('_struct',[[('m_difficultyLevel',86,-6)]]),  #131
    ('_choice',[(0,3),{0:('None',93),1:('Checked',13),2:('ValueChanged',6),3:('SelectionChanged',86),4:('TextChanged',30),5:('MouseButton',6)}]),  #132
    ('_struct',[[('m_controlId',86,-8),('m_eventType',86,-7),('m_eventData',132,-6)]]),  #133
    ('_struct',[[('m_soundHash',6,-7),('m_length',6,-6)]]),  #134
    ('_array',[(0,7),6]),  #135
    ('_struct',[[('m_soundHash',135,-2),('m_length',135,-1)]]),  #136
    ('_struct',[[('m_syncInfo',136,-6)]]),  #137
    ('_struct',[[('m_queryId',81,-8),('m_lengthMs',6,-7),('m_finishGameLoop',6,-6)]]),  #138
    ('_struct',[[('m_queryId',81,-7),('m_lengthMs',6,-6)]]),  #139
    ('_struct',[[('m_animWaitQueryId',81,-6)]]),  #140
    ('_struct',[[('m_sound',6,-6)]]),  #141
    ('_struct',[[('m_transmissionId',86,-7),('m_thread',6,-6)]]),  #142
    ('_struct',[[('m_transmissionId',86,-6)]]),  #143
    ('_optional',[82]),  #144
    ('_optional',[81]),  #145
    ('_optional',[114]),  #146
    ('_struct',[[('m_target',144,-11),('m_distance',145,-10),('m_pitch',145,-9),('m_yaw',145,-8),('m_reason',146,-7),('m_follow',13,-6)]]),  #147
    ('_struct',[[('m_skipType',128,-6)]]),  #148
    ('_int',[(0,11)]),  #149
    ('_struct',[[('x',149,-2),('y',149,-1)]]),  #150
    ('_struct',[[('m_button',6,-10),('m_down',13,-9),('m_posUI',150,-8),('m_posWorld',95,-7),('m_flags',114,-6)]]),  #151
    ('_struct',[[('m_posUI',150,-8),('m_posWorld',95,-7),('m_flags',114,-6)]]),  #152
    ('_struct',[[('m_achievementLink',81,-6)]]),  #153
    ('_struct',[[('m_hotkey',6,-7),('m_down',13,-6)]]),  #154
    ('_struct',[[('m_abilLink',81,-8),('m_abilCmdIndex',2,-7),('m_state',114,-6)]]),  #155
    ('_struct',[[('m_soundtrack',6,-6)]]),  #156
    ('_struct',[[('m_planetId',86,-6)]]),  #157
    ('_struct',[[('m_key',114,-7),('m_flags',114,-6)]]),  #158
    ('_struct',[[('m_resources',111,-6)]]),  #159
    ('_struct',[[('m_fulfillRequestId',86,-6)]]),  #160
    ('_struct',[[('m_cancelRequestId',86,-6)]]),  #161
    ('_struct',[[('m_error',86,-7),('m_abil',92,-6)]]),  #162
    ('_struct',[[('m_researchItemId',86,-6)]]),  #163
    ('_struct',[[('m_mercenaryId',86,-6)]]),  #164
    ('_struct',[[('m_battleReportId',86,-7),('m_difficultyLevel',86,-6)]]),  #165
    ('_struct',[[('m_battleReportId',86,-6)]]),  #166
    ('_struct',[[('m_decrementSeconds',86,-6)]]),  #167
    ('_struct',[[('m_portraitId',86,-6)]]),  #168
    ('_struct',[[('m_functionName',20,-6)]]),  #169
    ('_struct',[[('m_result',86,-6)]]),  #170
    ('_struct',[[('m_gameMenuItemIndex',86,-6)]]),  #171
    ('_int',[(-32768,16)]),  #172
    ('_struct',[[('m_wheelSpin',172,-7),('m_flags',114,-6)]]),  #173
    ('_struct',[[('m_purchaseCategoryId',86,-6)]]),  #174
    ('_struct',[[('m_button',81,-6)]]),  #175
    ('_struct',[[('m_cutsceneId',86,-7),('m_bookmarkName',20,-6)]]),  #176
    ('_struct',[[('m_cutsceneId',86,-6)]]),  #177
    ('_struct',[[('m_cutsceneId',86,-8),('m_conversationLine',20,-7),('m_altConversationLine',20,-6)]]),  #178
    ('_struct',[[('m_cutsceneId',86,-7),('m_conversationLine',20,-6)]]),  #179
    ('_struct',[[('m_leaveReason',1,-6)]]),  #180
    ('_struct',[[('m_observe',24,-12),('m_name',9,-11),('m_toonHandle',125,-10),('m_clanTag',41,-9),('m_clanLogo',42,-8),('m_hijack',13,-7),('m_hijackCloneGameUserId',58,-6)]]),  #181
    ('_optional',[98]),  #182
    ('_struct',[[('m_state',24,-7),('m_sequence',182,-6)]]),  #183
    ('_struct',[[('m_target',95,-6)]]),  #184
    ('_struct',[[('m_target',96,-6)]]),  #185
    ('_struct',[[('m_catalog',10,-9),('m_entry',81,-8),('m_field',9,-7),('m_value',9,-6)]]),  #186
    ('_struct',[[('m_index',6,-6)]]),  #187
    ('_struct',[[('m_shown',13,-6)]]),  #188
    ('_struct',[[('m_recipient',12,-3),('m_string',30,-2)]]),  #189
    ('_struct',[[('m_recipient',12,-3),('m_point',87,-2)]]),  #190
    ('_struct',[[('m_progress',86,-2)]]),  #191
    ('_struct',[[('m_status',24,-2)]]),  #192
    ('_struct',[[('m_scoreValueMineralsCurrent',86,0),('m_scoreValueVespeneCurrent',86,1),('m_scoreValueMineralsCollectionRate',86,2),('m_scoreValueVespeneCollectionRate',86,3),('m_scoreValueWorkersActiveCount',86,4),('m_scoreValueMineralsUsedInProgressArmy',86,5),('m_scoreValueMineralsUsedInProgressEconomy',86,6),('m_scoreValueMineralsUsedInProgressTechnology',86,7),('m_scoreValueVespeneUsedInProgressArmy',86,8),('m_scoreValueVespeneUsedInProgressEconomy',86,9),('m_scoreValueVespeneUsedInProgressTechnology',86,10),('m_scoreValueMineralsUsedCurrentArmy',86,11),('m_scoreValueMineralsUsedCurrentEconomy',86,12),('m_scoreValueMineralsUsedCurrentTechnology',86,13),('m_scoreValueVespeneUsedCurrentArmy',86,14),('m_scoreValueVespeneUsedCurrentEconomy',86,15),('m_scoreValueVespeneUsedCurrentTechnology',86,16),('m_scoreValueMineralsLostArmy',86,17),('m_scoreValueMineralsLostEconomy',86,18),('m_scoreValueMineralsLostTechnology',86,19),('m_scoreValueVespeneLostArmy',86,20),('m_scoreValueVespeneLostEconomy',86,21),('m_scoreValueVespeneLostTechnology',86,22),('m_scoreValueMineralsKilledArmy',86,23),('m_scoreValueMineralsKilledEconomy',86,24),('m_scoreValueMineralsKilledTechnology',86,25),('m_scoreValueVespeneKilledArmy',86,26),('m_scoreValueVespeneKilledEconomy',86,27),('m_scoreValueVespeneKilledTechnology',86,28),('m_scoreValueFoodUsed',86,29),('m_scoreValueFoodMade',86,30),('m_scoreValueMineralsUsedActiveForces',86,31),('m_scoreValueVespeneUsedActiveForces',86,32),('m_scoreValueMineralsFriendlyFireArmy',86,33),('m_scoreValueMineralsFriendlyFireEconomy',86,34),('m_scoreValueMineralsFriendlyFireTechnology',86,35),('m_scoreValueVespeneFriendlyFireArmy',86,36),('m_scoreValueVespeneFriendlyFireEconomy',86,37),('m_scoreValueVespeneFriendlyFireTechnology',86,38)]]),  #193
    ('_struct',[[('m_playerId',1,0),('m_stats',193,1)]]),  #194
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_unitTypeName',29,2),('m_controlPlayerId',1,3),('m_upkeepPlayerId',1,4),('m_x',10,5),('m_y',10,6)]]),  #195
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_killerPlayerId',58,2),('m_x',10,3),('m_y',10,4),('m_killerUnitTagIndex',43,5),('m_killerUnitTagRecycle',43,6)]]),  #196
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_controlPlayerId',1,2),('m_upkeepPlayerId',1,3)]]),  #197
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_unitTypeName',29,2)]]),  #198
    ('_struct',[[('m_playerId',1,0),('m_upgradeTypeName',29,1),('m_count',86,2)]]),  #199
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1)]]),  #200
    ('_array',[(0,10),86]),  #201
    ('_struct',[[('m_firstUnitIndex',6,0),('m_items',201,1)]]),  #202
    ('_struct',[[('m_playerId',1,0),('m_type',6,1),('m_userId',43,2),('m_slotId',43,3)]]),  #203
]

# Map from protocol NNet.Game.*Event eventid to (typeid, name)
game_event_types = {
    5: (80, 'NNet.Game.SUserFinishedLoadingSyncEvent'),
    7: (79, 'NNet.Game.SUserOptionsEvent'),
    9: (72, 'NNet.Game.SBankFileEvent'),
    10: (74, 'NNet.Game.SBankSectionEvent'),
    11: (75, 'NNet.Game.SBankKeyEvent'),
    12: (76, 'NNet.Game.SBankValueEvent'),
    13: (78, 'NNet.Game.SBankSignatureEvent'),
    14: (83, 'NNet.Game.SCameraSaveEvent'),
    21: (84, 'NNet.Game.SSaveGameEvent'),
    22: (80, 'NNet.Game.SSaveGameDoneEvent'),
    23: (80, 'NNet.Game.SLoadGameDoneEvent'),
    25: (85, 'NNet.Game.SCommandManagerResetEvent'),
    26: (89, 'NNet.Game.SGameCheatEvent'),
    27: (99, 'NNet.Game.SCmdEvent'),
    28: (107, 'NNet.Game.SSelectionDeltaEvent'),
    29: (108, 'NNet.Game.SControlGroupUpdateEvent'),
    30: (110, 'NNet.Game.SSelectionSyncCheckEvent'),
    31: (112, 'NNet.Game.SResourceTradeEvent'),
    32: (113, 'NNet.Game.STriggerChatMessageEvent'),
    33: (116, 'NNet.Game.SAICommunicateEvent'),
    34: (117, 'NNet.Game.SSetAbsoluteGameSpeedEvent'),
    35: (118, 'NNet.Game.SAddAbsoluteGameSpeedEvent'),
    36: (119, 'NNet.Game.STriggerPingEvent'),
    37: (120, 'NNet.Game.SBroadcastCheatEvent'),
    38: (121, 'NNet.Game.SAllianceEvent'),
    39: (122, 'NNet.Game.SUnitClickEvent'),
    40: (123, 'NNet.Game.SUnitHighlightEvent'),
    41: (124, 'NNet.Game.STriggerReplySelectedEvent'),
    43: (129, 'NNet.Game.SHijackReplayGameEvent'),
    44: (80, 'NNet.Game.STriggerSkippedEvent'),
    45: (134, 'NNet.Game.STriggerSoundLengthQueryEvent'),
    46: (141, 'NNet.Game.STriggerSoundOffsetEvent'),
    47: (142, 'NNet.Game.STriggerTransmissionOffsetEvent'),
    48: (143, 'NNet.Game.STriggerTransmissionCompleteEvent'),
    49: (147, 'NNet.Game.SCameraUpdateEvent'),
    50: (80, 'NNet.Game.STriggerAbortMissionEvent'),
    51: (130, 'NNet.Game.STriggerPurchaseMadeEvent'),
    52: (80, 'NNet.Game.STriggerPurchaseExitEvent'),
    53: (131, 'NNet.Game.STriggerPlanetMissionLaunchedEvent'),
    54: (80, 'NNet.Game.STriggerPlanetPanelCanceledEvent'),
    55: (133, 'NNet.Game.STriggerDialogControlEvent'),
    56: (137, 'NNet.Game.STriggerSoundLengthSyncEvent'),
    57: (148, 'NNet.Game.STriggerConversationSkippedEvent'),
    58: (151, 'NNet.Game.STriggerMouseClickedEvent'),
    59: (152, 'NNet.Game.STriggerMouseMovedEvent'),
    60: (153, 'NNet.Game.SAchievementAwardedEvent'),
    61: (154, 'NNet.Game.STriggerHotkeyPressedEvent'),
    62: (155, 'NNet.Game.STriggerTargetModeUpdateEvent'),
    63: (80, 'NNet.Game.STriggerPlanetPanelReplayEvent'),
    64: (156, 'NNet.Game.STriggerSoundtrackDoneEvent'),
    65: (157, 'NNet.Game.STriggerPlanetMissionSelectedEvent'),
    66: (158, 'NNet.Game.STriggerKeyPressedEvent'),
    67: (169, 'NNet.Game.STriggerMovieFunctionEvent'),
    68: (80, 'NNet.Game.STriggerPlanetPanelBirthCompleteEvent'),
    69: (80, 'NNet.Game.STriggerPlanetPanelDeathCompleteEvent'),
    70: (159, 'NNet.Game.SResourceRequestEvent'),
    71: (160, 'NNet.Game.SResourceRequestFulfillEvent'),
    72: (161, 'NNet.Game.SResourceRequestCancelEvent'),
    73: (80, 'NNet.Game.STriggerResearchPanelExitEvent'),
    74: (80, 'NNet.Game.STriggerResearchPanelPurchaseEvent'),
    75: (163, 'NNet.Game.STriggerResearchPanelSelectionChangedEvent'),
    76: (162, 'NNet.Game.STriggerCommandErrorEvent'),
    77: (80, 'NNet.Game.STriggerMercenaryPanelExitEvent'),
    78: (80, 'NNet.Game.STriggerMercenaryPanelPurchaseEvent'),
    79: (164, 'NNet.Game.STriggerMercenaryPanelSelectionChangedEvent'),
    80: (80, 'NNet.Game.STriggerVictoryPanelExitEvent'),
    81: (80, 'NNet.Game.STriggerBattleReportPanelExitEvent'),
    82: (165, 'NNet.Game.STriggerBattleReportPanelPlayMissionEvent'),
    83: (166, 'NNet.Game.STriggerBattleReportPanelPlaySceneEvent'),
    84: (166, 'NNet.Game.STriggerBattleReportPanelSelectionChangedEvent'),
    85: (131, 'NNet.Game.STriggerVictoryPanelPlayMissionAgainEvent'),
    86: (80, 'NNet.Game.STriggerMovieStartedEvent'),
    87: (80, 'NNet.Game.STriggerMovieFinishedEvent'),
    88: (167, 'NNet.Game.SDecrementGameTimeRemainingEvent'),
    89: (168, 'NNet.Game.STriggerPortraitLoadedEvent'),
    90: (170, 'NNet.Game.STriggerCustomDialogDismissedEvent'),
    91: (171, 'NNet.Game.STriggerGameMenuItemSelectedEvent'),
    92: (173, 'NNet.Game.STriggerMouseWheelEvent'),
    93: (130, 'NNet.Game.STriggerPurchasePanelSelectedPurchaseItemChangedEvent'),
    94: (174, 'NNet.Game.STriggerPurchasePanelSelectedPurchaseCategoryChangedEvent'),
    95: (175, 'NNet.Game.STriggerButtonPressedEvent'),
    96: (80, 'NNet.Game.STriggerGameCreditsFinishedEvent'),
    97: (176, 'NNet.Game.STriggerCutsceneBookmarkFiredEvent'),
    98: (177, 'NNet.Game.STriggerCutsceneEndSceneFiredEvent'),
    99: (178, 'NNet.Game.STriggerCutsceneConversationLineEvent'),
    100: (179, 'NNet.Game.STriggerCutsceneConversationLineMissingEvent'),
    101: (180, 'NNet.Game.SGameUserLeaveEvent'),
    102: (181, 'NNet.Game.SGameUserJoinEvent'),
    103: (183, 'NNet.Game.SCommandManagerStateEvent'),
    104: (184, 'NNet.Game.SCmdUpdateTargetPointEvent'),
    105: (185, 'NNet.Game.SCmdUpdateTargetUnitEvent'),
    106: (138, 'NNet.Game.STriggerAnimLengthQueryByNameEvent'),
    107: (139, 'NNet.Game.STriggerAnimLengthQueryByPropsEvent'),
    108: (140, 'NNet.Game.STriggerAnimOffsetEvent'),
    109: (186, 'NNet.Game.SCatalogModifyEvent'),
    110: (187, 'NNet.Game.SHeroTalentTreeSelectedEvent'),
    111: (80, 'NNet.Game.STriggerProfilerLoggingFinishedEvent'),
    112: (188, 'NNet.Game.SHeroTalentTreeSelectionPanelToggledEvent'),
}

# The typeid of the NNet.Game.EEventId enum.
game_eventid_typeid = 0

# Map from protocol NNet.Game.*Message eventid to (typeid, name)
message_event_types = {
    0: (189, 'NNet.Game.SChatMessage'),
    1: (190, 'NNet.Game.SPingMessage'),
    2: (191, 'NNet.Game.SLoadingProgressMessage'),
    3: (80, 'NNet.Game.SServerPingMessage'),
    4: (192, 'NNet.Game.SReconnectNotifyMessage'),
}

# The typeid of the NNet.Game.EMessageId enum.
message_eventid_typeid = 1

# Map from protocol NNet.Replay.Tracker.*Event eventid to (typeid, name)
tracker_event_types = {
    0: (194, 'NNet.Replay.Tracker.SPlayerStatsEvent'),
    1: (195, 'NNet.Replay.Tracker.SUnitBornEvent'),
    2: (196, 'NNet.Replay.Tracker.SUnitDiedEvent'),
    3: (197, 'NNet.Replay.Tracker.SUnitOwnerChangeEvent'),
    4: (198, 'NNet.Replay.Tracker.SUnitTypeChangeEvent'),
    5: (199, 'NNet.Replay.Tracker.SUpgradeEvent'),
    6: (195, 'NNet.Replay.Tracker.SUnitInitEvent'),
    7: (200, 'NNet.Replay.Tracker.SUnitDoneEvent'),
    8: (202, 'NNet.Replay.Tracker.SUnitPositionsEvent'),
    9: (203, 'NNet.Replay.Tracker.SPlayerSetupEvent'),
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
replay_initdata_typeid = 71


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
