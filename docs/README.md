### Generating documentation using Sphinx

pip install Sphinx
make html


### Data Definitions

#### --header

The Header flag will return some basic information about the replay, version, game loops. 
```
[m_version] => stdClass Object
    (
        [m_baseBuild] => 62347
        [m_minor] => 2
        [m_revision] => 0
        [m_flags] => 1
        [m_major] => 4
        [m_build] => 62347
    )
[m_elapsedGameLoops] => 9840
```


#### ---details
The Details flag gives an overview of the replays information  
[More Information](flags/details.md)

#### ---initdata
The initdata flag gives the lobby state with some basic information about the players in the lobby.  
[More Information](flags/initdata.md)

#### ---messageevents
The messageevents flag gives all the chat messages in the game.   
[More Information](flags/initdata.md)



### Common keys

**_gameloop**
> 
**_event**
> 