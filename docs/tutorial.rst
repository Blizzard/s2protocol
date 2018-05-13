.. ref-gettingstarted

===============================
Getting Started with s2protocol
===============================


Installing s2protocol
=====================

The easiest way to get started with ``s2protocol`` is to install it off `PyPI`_
using one of the following commands. Using your terminal, simply run either::

    pip install s2protocol

or...::

    easy_install s2protocol

.. _`PyPI`: https://pypi.python.org/pypi/s2protocol


Alternative Installs
--------------------

If you'd prefer to download the package yourself, `download it`_ then run the
following::

    cd s2protocol
    python setup.py install

Finally, if you'd like to help with the development of ``s2protocol``, you can
clone it directly from GitHub & setup a development install using::

    git clone https://github.com/Blizzard/s2protocol.git
    cd s2protocol
    python setup.py develop

.. _`download it`: https://github.com/Blizzard/s2protocol/archive/master.zip


Using s2protocol Command Line Tool
==================================

If you're just interested in seeing the stats from a given replay file,
``s2protocol`` can be used in a standalone manner. A command line utility,
called ``s2_cli.py`` is installed when the package is installed. Usage
looks like::

    s2_cli.py ~/Desktop/my_pvp_replay.SC2Replay --stats

This will output the stats from the replay file then exit.

Other options you can pass in include:

* ``--gameevents``: Prints out the game events
* ``--messageevents``: Prints out the message events
* ``--trackerevents``: Prints out the tracker events
* ``--attributeevents``: Prints out the attributes events
* ``--header``: Prints out the protocol header
* ``--details``: Prints out the protocol details
* ``--initdata``: Prints out the protocol initdata
* ``--stats``: Prints out the stats

To work inspect different protocol versions:

* ``--versions``: Show all protocol versions
* ``--diff``: Diff two protocol versions

To control the output format:

* ``--json``: Outputs events as JSON structured documents
* ``--ndjson``: Like --json but is each event is newline delimited
