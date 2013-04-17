# mpyq

mpyq is a Python library for reading MPQ (MoPaQ) archives used in many of
Blizzard's games. It was originally developed for data mining Starcraft II
replay files.

In addition to being a library, mpyq also has a command line interface that
exposes some of the library's core functionality such as extracting archives.

At this early stage in development only files compressed with DEFLATE or bzip2
are uncompressed. This means that this library can not be used to extract most
big game asset archives that Blizzard's games use. More compression formats
will be supported in the future.

Also, as mpyq is so far pure Python code, it might be unfeasible to try to
extract very large MPQ archives, even if all the compression methods used
inside the archive were supported.

Note that listing files inside an archive does not require full extraction.
You can safely take a peek inside any MPQ archive with this library.

## Installation

A stable version of mpyq is available from PyPI and can be installed with
either `easy_install` or `pip`.

    $ easy_install mpyq
    $ pip install mpyq

mpyq can be installed manually with the included setup.py script.

    $ python setup.py install

Running this command will install mpyq both as a library and a stand-alone
script that can be run from anywhere, provided that you have added Python's
bin directory to your PATH environment variable.

Alternative way to install mpyq is to clone this git repository somewhere on
your filesystem and then either adjust your PYTHONPATH environment variable to
point to the directory that contains the repository or create a symbolic link
to your Python's site-packages directory pointing at the repository.

Note that the command line interface part of mpyq uses the argparse module,
which was included into Python's standard library in version 2.7. If you
didn't install mpyq from PyPI and you wish to use the command line interface
part with Python 2.6, you should install argparse from PyPI manually.

## Usage

### As a library

    >>> from mpyq import MPQArchive
    >>> archive = MPQArchive('game.SC2Replay')

Now you have a MPQArchive object of the file you opened. One common thing
to do now is to extract the files from the archive.

    >>> files = archive.extract()

This will extract and return the archive's contents in memory. Be advised
that you might not want to do this with multi-gigabyte MPQ files from
World of Warcraft, for example.

Files inside the archive can be also extracted and written to disk.

    >>> archive.extract_to_disk()

If you want to skip reading the (listfile) inside the archive, you can do
so by passing `listfile=False` to the constructor.

    >>> archive = MPQArchive('bad_listfile.SC2Replay', listfile=False)

This might be required if the (listfile) is encrypted or has been tampered
with. Note that you can't list files or extract the whole archive if you do
this -- you need to know in advance which files you want to read.

    >>> archive.read('replay.details')
    '\x05\x1c\x00\x04\x01\x00\x04\x05...'

For more information, consult `help(mpyq)` in your Python console.

### From the command line

    usage: mpyq.py [-h] [-I] [-H] [-b] [-s] [-t] [-x] file

    mpyq reads and extracts MPQ archives.

    positional arguments:
      file                 path to the archive

    optional arguments:
      -h, --help           show this help message and exit
      -I, --headers        print header information from the archive
      -H, --hash-table     print hash table
      -b, --block-table    print block table
      -s, --skip-listfile  skip reading (listfile)
      -t, --list-files     list files inside the archive
      -x, --extract        extract files from the archive

You can extract all the files inside the archive with `-x/--extract`.

    $ mpyq -x game.SC2Replay

This will create a directory called 'game' with the files inside.

You can print the header information from a given archive with `-I/--headers`.

    $ mpyq -I game.SC2Replay
    MPQ archive header
    ------------------
    magic                          'MPQ\x1a'
    header_size                    44
    arhive_size                    19801
    format_version                 1
    sector_size_shift              3
    hash_table_offset              19385
    block_table_offset             19641
    hash_table_entries             16
    block_table_entries            10
    extended_block_table_offset    0
    hash_table_offset_high         0
    block_table_offset_high        0
    offset                         1024

    MPQ user data header
    --------------------
    magic                          'MPQ\x1b'
    user_data_size                 512
    mpq_header_offset              1024
    user_data_header_size          60
    content                        '\x05\x08\x00\x02,StarCraft II replay\x1b
                                    11\x02\x05\x0c\x00\t\x02\x02\t\x00\x04\t
                                    (\x06\t\x00\x08\t\xc8\xfa\x01\n\t\xc8\xf
                                    a\x01\x04\t\x04\x06\t\xa2\x99\x01'

You can display the archive's hash table with `-H/--hash-table`.

    $ mpyq -H game.SC2Replay
    MPQ archive hash table
    ----------------------
     Hash A   Hash B  Locl Plat BlockIdx
    D38437CB 07DFEAEC 0000 0000 00000009
    AAC2A54B F4762B95 0000 0000 00000002
    FFFFFFFF FFFFFFFF FFFF FFFF FFFFFFFF
    FFFFFFFF FFFFFFFF FFFF FFFF FFFFFFFF
    FFFFFFFF FFFFFFFF FFFF FFFF FFFFFFFF
    C9E5B770 3B18F6B6 0000 0000 00000005
    343C087B 278E3682 0000 0000 00000004
    3B2B1EA0 B72EF057 0000 0000 00000006
    5A7E8BDC FF253F5C 0000 0000 00000001
    FD657910 4E9B98A7 0000 0000 00000008
    D383C29C EF402E92 0000 0000 00000000
    FFFFFFFF FFFFFFFF FFFF FFFF FFFFFFFF
    FFFFFFFF FFFFFFFF FFFF FFFF FFFFFFFF
    FFFFFFFF FFFFFFFF FFFF FFFF FFFFFFFF
    1DA8B0CF A2CEFF28 0000 0000 00000007
    31952289 6A5FFAA3 0000 0000 00000003

You can display the archive's block table with `-b/--block-table`.

    $ mpyq -b game.SC2Replay
    MPQ archive block table
    -----------------------
     Offset  ArchSize RealSize  Flags
    0000002C      443      443 81000200
    000001E7      609     1082 81000200
    00000448    16077    42859 81000200
    00004315       94       94 81000200
    00004373       96       96 81000200
    000043D3      591      765 81000200
    00004622      802     1444 81000200
    00004944      247      580 81000200
    00004A3B      120      164 81000200
    00004AB3      262      288 81000200

You can list all files inside the archive with `-t/--list-files`.

    $ mpyq -t game.SC2Replay
    replay.attributes.events            580 bytes
    replay.details                      443 bytes
    replay.game.events                42859 bytes
    replay.initData                    1082 bytes
    replay.load.info                     96 bytes
    replay.message.events                94 bytes
    replay.smartcam.events             1444 bytes
    replay.sync.events                  765 bytes

You can skip reading the listfile with `-s/--skip-listfile`. This might be
necessarry if the listfile is encrypted or corrupted. Note that you cannot
list files or extract the whole archive without the listfile.

## References

The following two documents were used as references for the MPQ format:

 * [http://www.zezula.net/en/mpq/mpqformat.html](http://www.zezula.net/en/mpq/mpqformat.html)
 * [http://wiki.devklog.net/index.php?title=The_MoPaQ_Archive_Format](http://wiki.devklog.net/index.php?title=The_MoPaQ_Archive_Format)


## Copyright

Copyright 2010, 2011 Aku Kotkavuo. See LICENSE for details.
