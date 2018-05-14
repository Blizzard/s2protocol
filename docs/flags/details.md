### Details Flag

**m_timeLocalOffset**
> returns the offset for the timezone the replay was played in (users local timezone)  
>  ```m_timeUTC / (10 * 1000 * 1000) - 11644473600 - ((m_timeLocalOffset / 10000000)) ```

**m_title**
> Map name in users localization 

**m_cacheHandles**
> describe the packages/components used in the replay. Can be used to determine what version of the game the replay was  
``` 
if (strpos($cache_handle,hash("sha256","Standard Data: Swarm.SC2Mod")) !== false) {//HOTS} 
else if (strpos($cache_handle,hash("sha256","Standard Data: Void.SC2Mod")) !== false) {//LOTV} 
else if (strpos($cache_handle,hash("sha256","Standard Data: Liberty.SC2Mod")) !== false) {//WOL} 
```
 
**m_timeUTC**

> UTC time of the replay played date (dont recall off hand if its the start or end date)

**m_gameSpeed**
> The speed at which the game was played 0 = Slower, 1 = Slow, 2 = Normal, 3 = Fast, 4 = Faster

**m_playerList**
> List of players in the lobby

**m_playerList->m_color**
> Players selected color in game RGBA

**m_playerList->m_teamId**
> Players team, starts at 0

**m_playerList->m_observe**
> If the player was an observer or an actual player

**m_playerList->m_control**
> Unknown

**m_playerList->m_race**
> Players Race they got in game, wont show random. Is localization specific.

**m_playerList->m_handicap**
>  Handicap value that was selected for player

**m_playerList->m_result**
> Shows where the player placed at in the replay based on what the player seen 
(aka team games if a player leaves they dont really know the exact ending of the game). 1 = 1st, 2 = 2nd, ext

**m_playerList->m_toon->m_region**
> 1 = us, 2 = eu, 3 = kr, 4 = sea, 5 = cn, 98 = local battle.net server (WCS, ext)

####Example Reponse
```
 stdClass Object
 (
     [m_disableRecoverGame] => 
     [m_imageFilePath] => 
     [m_description] => 
     [m_timeLocalOffset] => -252000000000
     [m_thumbnail] => stdClass Object
         (
             [m_file] => Minimap.tga
         )
 
     [m_defaultDifficulty] => 3
     [m_restartAsTransitionMap] => 
     [m_title] => Backwater LE
     [m_campaignIndex] => 0
     [m_modPaths] => 
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
 
     [m_timeUTC] => 131620973259425400
     [m_isBlizzardMap] => 1
     [m_mapFileName] => 
     [m_gameSpeed] => 4
     [m_playerList] => Array
         (
             [0] => stdClass Object
                 (
                     [m_color] => stdClass Object
                         (
                             [m_r] => 180
                             [m_a] => 255
                             [m_g] => 20
                             [m_b] => 30
                         )
 
                     [m_teamId] => 0
                     [m_observe] => 0
                     [m_control] => 2
                     [m_race] => Protoss
                     [m_handicap] => 100
                     [m_toon] => stdClass Object
                         (
                             [m_programId] => u0000u0000S2
                             [m_id] => 20704188
                             [m_region] => 1
                             [m_realm] => 1
                         )
 
                     [m_result] => 1
                     [m_workingSetSlotId] => 0
                     [m_hero] => 
                     [m_name] => DeezyProTeez
                 )
 
             [1] => stdClass Object
                 (
                     [m_color] => stdClass Object
                         (
                             [m_r] => 0
                             [m_a] => 255
                             [m_g] => 66
                             [m_b] => 255
                         )
 
                     [m_teamId] => 1
                     [m_observe] => 0
                     [m_control] => 2
                     [m_race] => Zerg
                     [m_handicap] => 100
                     [m_toon] => stdClass Object
                         (
                             [m_programId] => u0000u0000S2
                             [m_id] => 336658
                             [m_region] => 1
                             [m_realm] => 1
                         )
 
                     [m_result] => 2
                     [m_workingSetSlotId] => 1
                     [m_hero] => 
                     [m_name] => <sc2rep>Breath
                 )
 
         )
 
     [m_miniSave] => 
     [m_difficulty] => 
 )
```