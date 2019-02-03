### messageevents Flag

**_userid->_m_userId**
> is the users id that sent the message, this related to the initdata m_syncLobbyState->m_userInitialData-> key. 
>  ```m_syncLobbyState->m_userInitialData[_userid->m_userId]->m_name ```

**_event**
> For chat messages you want to look for NNet.Game.SChatMessage

####Example Reponse
```
 stdClass Object
 (
     [_eventid] => 2
     [_event] => NNet.Game.SLoadingProgressMessage
     [_bits] => 56
     [m_progress] => 33
     [_gameloop] => 0
     [_userid] => stdClass Object
         (
             [m_userId] => 0
         )
 
 )
 stdClass Object
 (
     [_eventid] => 2
     [_event] => NNet.Game.SLoadingProgressMessage
     [_bits] => 56
     [m_progress] => 38
     [_gameloop] => 0
     [_userid] => stdClass Object
         (
             [m_userId] => 0
         )
 
 )
 stdClass Object
 (
     [_eventid] => 2
     [_event] => NNet.Game.SLoadingProgressMessage
     [_bits] => 56
     [m_progress] => 46
     [_gameloop] => 0
     [_userid] => stdClass Object
         (
             [m_userId] => 0
         )
 
 )
 stdClass Object
 (
     [_eventid] => 2
     [_event] => NNet.Game.SLoadingProgressMessage
     [_bits] => 56
     [m_progress] => 54
     [_gameloop] => 0
     [_userid] => stdClass Object
         (
             [m_userId] => 0
         )
 
 )
 stdClass Object
 (
     [_eventid] => 2
     [_event] => NNet.Game.SLoadingProgressMessage
     [_bits] => 56
     [m_progress] => 60
     [_gameloop] => 0
     [_userid] => stdClass Object
         (
             [m_userId] => 0
         )
 
 )
 stdClass Object
 (
     [_eventid] => 2
     [_event] => NNet.Game.SLoadingProgressMessage
     [_bits] => 56
     [m_progress] => 79
     [_gameloop] => 0
     [_userid] => stdClass Object
         (
             [m_userId] => 0
         )
 
 )
 stdClass Object
 (
     [_eventid] => 2
     [_event] => NNet.Game.SLoadingProgressMessage
     [_bits] => 56
     [m_progress] => 99
     [_gameloop] => 0
     [_userid] => stdClass Object
         (
             [m_userId] => 0
         )
 
 )
 stdClass Object
 (
     [m_recipient] => 0
     [_eventid] => 0
     [_event] => NNet.Game.SChatMessage
     [_gameloop] => 155
     [m_string] => glhf
     [_bits] => 72
     [_userid] => stdClass Object
         (
             [m_userId] => 0
         )
 
 )
 stdClass Object
 (
     [m_recipient] => 0
     [_eventid] => 0
     [_event] => NNet.Game.SChatMessage
     [_gameloop] => 257
     [m_string] => glhf (happy) 
     [_bits] => 144
     [_userid] => stdClass Object
         (
             [m_userId] => 1
         )
 
 )
 stdClass Object
 (
     [m_recipient] => 0
     [_eventid] => 0
     [_event] => NNet.Game.SChatMessage
     [_gameloop] => 18062
     [m_string] => gg
     [_bits] => 64
     [_userid] => stdClass Object
         (
             [m_userId] => 1
         )
 
 )
```