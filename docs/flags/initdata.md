### initdata Flag

**m_syncLobbyState->m_userInitialData**
> returns useful information about players before they started the game (league, mmr, name, clan tag)

**m_syncLobbyState->m_userInitialData->m_highestLeague**
> The highest ranked league they have made it too (might be related to the game mode not 100% sure)   
> 1 =  bronze, 2 = silver, 3 = gold, 4 = platinum, 5 = diamond, 6 = master, 7 = grand master, 8 = unranked

**m_syncLobbyState->m_userInitialData->m_scaledRating**
> MMR (Match Making Rating) at time of match, before it started. 

####Example Response
> This is a trimmed response to make it easier to read
```
 stdClass Object
 (
     [m_syncLobbyState] => stdClass Object
         (
             [m_userInitialData] => Array
                 (
                     [0] => stdClass Object
                         (
                             [m_testAuto] => 
                             [m_mount] => 
                             [m_observe] => 0
                             [m_teamPreference] => stdClass Object
                                 (
                                     [m_team] => 
                                 )
 
                             [m_toonHandle] => 
                             [m_customInterface] => 
                             [m_highestLeague] => 5
                             [m_clanTag] => 
                             [m_testMap] => 
                             [m_clanLogo] => 
                             [m_examine] => 
                             [m_testType] => 0
                             [m_combinedRaceLevels] => 4294967295
                             [m_randomSeed] => 0
                             [m_scaledRating] => 4294
                             [m_racePreference] => stdClass Object
                                 (
                                     [m_race] => 
                                 )
 
                             [m_skin] => 
                             [m_hero] => 
                             [m_name] => DeezyProTeez
                         )
 
                     [1] => stdClass Object
                         (
                             [m_testAuto] => 
                             [m_mount] => 
                             [m_observe] => 0
                             [m_teamPreference] => stdClass Object
                                 (
                                     [m_team] => 
                                 )
 
                             [m_toonHandle] => 
                             [m_customInterface] => 
                             [m_highestLeague] => 6
                             [m_clanTag] => sc2rep
                             [m_testMap] => 
                             [m_clanLogo] => 
                             [m_examine] => 
                             [m_testType] => 0
                             [m_combinedRaceLevels] => 4294967295
                             [m_randomSeed] => 0
                             [m_scaledRating] => 4631
                             [m_racePreference] => stdClass Object
                                 (
                                     [m_race] => 
                                 )
 
                             [m_skin] => 
                             [m_hero] => 
                             [m_name] => Breath
                         )
                 )
 
             [m_lobbyState] => stdClass Object
                 (
                     [m_maxUsers] => 2
                     [m_slots] => Array
                         (
                             [0] => stdClass Object
                                 (
                                     [m_toonHandle] => 1-S2-1-20704188
                                     [m_rewardOverrides] => Array
                                         (
                                         )
 
                                     [m_userId] => 0
                                     [m_skin] => 
                                     [m_difficulty] => 3
                                     [m_aiBuild] => 0
                                     [m_teamId] => 0
                                     [m_rewards] => Array
                                         (
                                             [0] => 2588696470
                                             [1] => 268555963
                                             [2] => 1932524020
                                             [3] => 569055983
                                             [4] => 3659500125
                                             [5] => 800865563
                                             [6] => 1500394717
                                             [7] => 522060623
                                             [8] => 207557107
                                             [9] => 2820704051
                                             [10] => 1697980591
                                             [11] => 0
                                             [12] => 2265163032
                                             [13] => 306523769
                                             [14] => 4144653506
                                             [15] => 3335041079
                                             [16] => 2908506816
                                             [17] => 1555175204
                                             [18] => 1333792768
                                             [19] => 0
                                             [20] => 2112492252
                                             [21] => 3774144990
                                             [22] => 18730036
                                             [23] => 1440277345
                                             [24] => 3881125246
                                             [25] => 2777065642
                                             [26] => 2951153716
                                             [27] => 648212375
                                             [28] => 2011421739
                                             [29] => 2428064812
                                             [30] => 15768155
                                             [31] => 2009110693
                                             [32] => 2442224836
                                             [33] => 135098568
                                             [34] => 1185292261
                                             [35] => 3979921667
                                             [36] => 570858554
                                             [37] => 574205234
                                             [38] => 1804753350
                                             [39] => 535257061
                                             [40] => 2359737029
                                             [41] => 3927507442
                                             [42] => 4008355342
                                             [43] => 3199996399
                                             [44] => 3673336716
                                             [45] => 3065782512
                                             [46] => 861201319
                                             [47] => 2411195921
                                             [48] => 656055948
                                             [49] => 3717180683
                                             [50] => 415049813
                                             [51] => 1664806146
                                             [52] => 1751841167
                                             [53] => 2104220742
                                             [54] => 1434315354
                                             [55] => 835964495
                                             [56] => 4067220888
                                             [57] => 2798322801
                                             [58] => 1701027258
                                             [59] => 2418337610
                                             [60] => 2615206337
                                             [61] => 3381814647
                                             [62] => 3776162522
                                             [63] => 2200440608
                                             [64] => 3312681754
                                             [65] => 3200889017
                                             [66] => 0
                                             [67] => 695505991
                                             [68] => 3662634844
                                             [69] => 334383271
                                             [70] => 879683935
                                             [71] => 2326149197
                                             [72] => 3356965872
                                             [73] => 4037382619
                                             [74] => 1896734762
                                             [75] => 877192560
                                             [76] => 3535385893
                                             [77] => 170345607
                                             [78] => 0
                                             [79] => 1625603542
                                             [80] => 1819379161
                                             [81] => 2211791455
                                             [82] => 2429550722
                                             [83] => 2419802213
                                             [84] => 4241103608
                                             [85] => 1127476957
                                         )
 
                                     [m_commanderLevel] => 1
                                     [m_logoIndex] => 0
                                     [m_artifacts] => Array
                                         (
                                             [0] => 
                                             [1] => 
                                             [2] => 
                                         )
 
                                     [m_commanderMasteryTalents] => Array
                                         (
                                             [0] => 0
                                             [1] => 0
                                             [2] => 0
                                             [3] => 0
                                             [4] => 0
                                             [5] => 0
                                         )
 
                                     [m_colorPref] => stdClass Object
                                         (
                                             [m_color] => 1
                                         )
 
                                     [m_commanderMasteryLevel] => 0
                                     [m_racePref] => stdClass Object
                                         (
                                             [m_race] => 2
                                         )
 
                                     [m_tandemId] => 0
                                     [m_hero] => 
                                     [m_commander] => 
                                     [m_mount] => 
                                     [m_handicap] => 100
                                     [m_observe] => 0
                                     [m_control] => 2
                                     [m_licenses] => Array
                                         (
                                         )
 
                                     [m_tandemLeaderId] => 
                                     [m_hasSilencePenalty] => 
                                     [m_workingSetSlotId] => 0
                                 )
 
                             [1] => stdClass Object
                                 (
                                     [m_toonHandle] => 1-S2-1-336658
                                     [m_rewardOverrides] => Array
                                         (
                                         )
 
                                     [m_userId] => 1
                                     [m_skin] => 
                                     [m_difficulty] => 3
                                     [m_aiBuild] => 0
                                     [m_teamId] => 1
                                     [m_rewards] => Array
                                         (
                                             [0] => 2588696470
                                             [1] => 268555963
                                             [2] => 1932524020
                                             [3] => 569055983
                                             [4] => 3659500125
                                             [5] => 800865563
                                             [6] => 1500394717
                                             [7] => 522060623
                                             [8] => 207557107
                                             [9] => 2820704051
                                             [10] => 1697980591
                                             [11] => 0
                                             [12] => 2265163032
                                             [13] => 306523769
                                             [14] => 4144653506
                                             [15] => 3335041079
                                             [16] => 2908506816
                                             [17] => 1555175204
                                             [18] => 1333792768
                                             [19] => 0
                                             [20] => 2112492252
                                             [21] => 3774144990
                                             [22] => 985481741
                                             [23] => 75577589
                                             [24] => 3881125246
                                             [25] => 2777065642
                                             [26] => 3677861098
                                             [27] => 648212375
                                             [28] => 3136699255
                                             [29] => 2428064812
                                             [30] => 15768155
                                             [31] => 2009110693
                                             [32] => 2442224836
                                             [33] => 135098568
                                             [34] => 1185292261
                                             [35] => 3979921667
                                             [36] => 570858554
                                             [37] => 574205234
                                             [38] => 1804753350
                                             [39] => 535257061
                                             [40] => 2359737029
                                             [41] => 3927507442
                                             [42] => 4008355342
                                             [43] => 1789342096
                                             [44] => 3399536420
                                             [45] => 3065782512
                                             [46] => 861201319
                                             [47] => 2411195921
                                             [48] => 656055948
                                             [49] => 3717180683
                                             [50] => 1713229670
                                             [51] => 1664806146
                                             [52] => 1751841167
                                             [53] => 2104220742
                                             [54] => 1434315354
                                             [55] => 835964495
                                             [56] => 244296426
                                             [57] => 2798322801
                                             [58] => 1701027258
                                             [59] => 2702942825
                                             [60] => 3868852090
                                             [61] => 3381814647
                                             [62] => 3776162522
                                             [63] => 2200440608
                                             [64] => 3312681754
                                             [65] => 3200889017
                                             [66] => 0
                                             [67] => 695505991
                                             [68] => 3662634844
                                             [69] => 334383271
                                             [70] => 308738891
                                             [71] => 3008846121
                                             [72] => 3356965872
                                             [73] => 4037382619
                                             [74] => 4049662203
                                             [75] => 877192560
                                             [76] => 677139769
                                             [77] => 170345607
                                             [78] => 0
                                             [79] => 1625603542
                                             [80] => 1819379161
                                             [81] => 2211791455
                                             [82] => 2429550722
                                             [83] => 2276535543
                                             [84] => 2419802213
                                             [85] => 3404898509
                                             [86] => 2976815359
                                             [87] => 3834465703
                                             [88] => 4241103608
                                             [89] => 1127476957
                                             [90] => 928246938
                                             [91] => 2063317397
                                         )
 
                                     [m_commanderLevel] => 1
                                     [m_logoIndex] => 0
                                     [m_artifacts] => Array
                                         (
                                             [0] => 
                                             [1] => 
                                             [2] => 
                                         )
 
                                     [m_commanderMasteryTalents] => Array
                                         (
                                             [0] => 0
                                             [1] => 0
                                             [2] => 0
                                             [3] => 0
                                             [4] => 0
                                             [5] => 0
                                         )
 
                                     [m_colorPref] => stdClass Object
                                         (
                                             [m_color] => 2
                                         )
 
                                     [m_commanderMasteryLevel] => 0
                                     [m_racePref] => stdClass Object
                                         (
                                             [m_race] => 1
                                         )
 
                                     [m_tandemId] => 1
                                     [m_hero] => 
                                     [m_commander] => 
                                     [m_mount] => 
                                     [m_handicap] => 100
                                     [m_observe] => 0
                                     [m_control] => 2
                                     [m_licenses] => Array
                                         (
                                         )
 
                                     [m_tandemLeaderId] => 
                                     [m_hasSilencePenalty] => 
                                     [m_workingSetSlotId] => 1
                                 )
                         )
 
                     [m_defaultDifficulty] => 3
                     [m_isSinglePlayer] => 
                     [m_phase] => 0
                     [m_hostUserId] => 
                     [m_maxObservers] => 14
                     [m_defaultAIBuild] => 0
                     [m_pickedMapTag] => 0
                     [m_randomSeed] => 4237049481
                     [m_gameDuration] => 0
                 )
 
             [m_gameDescription] => stdClass Object
                 (
                     [m_maxRaces] => 3
                     [m_maxTeams] => 2
                     [m_hasExtensionMod] => 
                     [m_maxColors] => 16
                     [m_isBlizzardMap] => 1
                     [m_gameOptions] => stdClass Object
                         (
                             [m_competitive] => 1
                             [m_practice] => 
                             [m_lockTeams] => 1
                             [m_amm] => 1
                             [m_battleNet] => 1
                             [m_fog] => 0
                             [m_noVictoryOrDefeat] => 
                             [m_heroDuplicatesAllowed] => 1
                             [m_buildCoachEnabled] => 
                             [m_advancedSharedControl] => 
                             [m_cooperative] => 
                             [m_clientDebugFlags] => 265
                             [m_observers] => 0
                             [m_teamsTogether] => 
                             [m_randomRaces] => 
                             [m_userDifficulty] => 0
                         )
 
                     [m_defaultDifficulty] => 3
                     [m_isCoopMode] => 
                     [m_mapFileName] => 
                     [m_defaultAIBuild] => 0
                     [m_gameType] => 0
                     [m_hasNonBlizzardExtensionMod] => 
                     [m_randomValue] => 4237049481
                     [m_maxObservers] => 14
                     [m_isRealtimeMode] => 
                     [m_maxUsers] => 2
                     [m_modFileSyncChecksum] => 876111259
                     [m_mapSizeX] => 168
                     [m_maxPlayers] => 2
                     [m_cacheHandles] => Array
                         (
                             [0] => http://us.depot.battle.net:1119/6de41503baccd05656360b6f027db88169fa1989bb6357b1b215a2547939f5fb.s2ma
                             [1] => http://us.depot.battle.net:1119/421c8aa0f3619b652d23a2735dfee812ab644228235e7a797edecfe8b67da30e.s2ma
                             [2] => http://us.depot.battle.net:1119/66093832128453efffbb787c80b7d3eec1ad81bde55c83c930dea79c4e505a04.s2ma
                             [3] => http://us.depot.battle.net:1119/d92dfc48c484c59154270b924ad7d57484f2ab9a47621c7ab16431bf66c53b40.s2ma
                             [4] => http://us.depot.battle.net:1119/081f205bd11216ae031fa15af97639064accd763272923f20c09e4fb1c0b55ea.s2ma
                             [5] => http://us.depot.battle.net:1119/7f41411aa597f4b46440d42a563348bf53822d2a68112f0104f9b891f6f05ae1.s2ma
                             [6] => http://us.depot.battle.net:1119/522a96c39d8dca54190d91f632c2e34fa4c58e7687fdd8759b682c653e463dec.s2ma
                         )
 
                     [m_gameSpeed] => 4
                     [m_maxControls] => 1
                     [m_gameCacheName] => Dflt
                     [m_mapAuthorName] => 1-S2-1-258901
                     [m_isPremadeFFA] => 
                     [m_mapSizeY] => 160
                     [m_mapFileSyncChecksum] => 3264396611
                     [m_slotDescriptions] => Array
                         (
                             [0] => stdClass Object
                                 (
                                     [m_allowedRaces] => Array
                                         (
                                             [0] => 3
                                             [1] => 7
                                         )
 
                                     [m_allowedColors] => Array
                                         (
                                             [0] => 16
                                             [1] => 65279
                                         )
 
                                     [m_allowedAIBuilds] => Array
                                         (
                                             [0] => 255
                                             [1] => 2.8269555624688E+76
                                         )
 
                                     [m_allowedDifficulty] => Array
                                         (
                                             [0] => 32
                                             [1] => 4261871616
                                         )
 
                                     [m_allowedObserveTypes] => Array
                                         (
                                             [0] => 3
                                             [1] => 7
                                         )
 
                                     [m_allowedControls] => Array
                                         (
                                             [0] => 255
                                             [1] => 5.7896044618658E+76
                                         )
 
                                 )
 
                             [1] => stdClass Object
                                 (
                                     [m_allowedRaces] => Array
                                         (
                                             [0] => 3
                                             [1] => 7
                                         )
 
                                     [m_allowedColors] => Array
                                         (
                                             [0] => 16
                                             [1] => 65279
                                         )
 
                                     [m_allowedAIBuilds] => Array
                                         (
                                             [0] => 255
                                             [1] => 2.8269555624688E+76
                                         )
 
                                     [m_allowedDifficulty] => Array
                                         (
                                             [0] => 32
                                             [1] => 4261871616
                                         )
 
                                     [m_allowedObserveTypes] => Array
                                         (
                                             [0] => 3
                                             [1] => 7
                                         )
 
                                     [m_allowedControls] => Array
                                         (
                                             [0] => 255
                                             [1] => 5.7896044618658E+76
                                         )
                                 )
                         )
                 )
         )
 )

```