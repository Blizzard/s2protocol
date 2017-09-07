.. s2protocol documentation master file, created by
   sphinx-quickstart on Wed May  8 23:42:19 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

==========
s2protocol
==========

``s2protocol`` is a reference Python library and standalone tool to decode
`StarCraft II`_ replay files into Python data structures.

Currently, ``s2protocol`` can decode these structures and events:

* replay header
* game details
* replay init data
* game events
* message events
* tracker events

``s2protocol`` can be used as a base-build-specific library to decode binary
blobs, or it can be run as a standalone tool to pretty print information from
supported replay files.

Note that ``s2protocol`` does not expose game balance information or provide
any kind of high level analysis of replays; it's meant to be just the first
tool in the chain for your data mining application.

.. _`StarCraft II`: http://starcraft2.com/


Supported Versions
==================

``s2protocol`` supports all StarCraft II replay files that were written with
retail versions of the game. The current plan is to support all future publicly
released versions, including public betas.

.. toctree::
   :maxdepth: 2

   tutorial


Reference
=========

Contents:

.. toctree::
   :maxdepth: 2

   refs/s2protocol

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

