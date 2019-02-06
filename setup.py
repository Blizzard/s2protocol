#!/usr/bin/env python
import sys
from setuptools import setup
import s2protocol.build

install_requires = [
    'mpyq >= 0.2.2',
]
tests_require = [
    'tox',
]

if sys.version_info < (2, 7):
    install_requires.append('argparse')


setup(
    name='s2protocol',
    version=s2protocol.build.game_version(),
    author='Blizzard Entertainment',
    author_email='s2github@blizzard.com',
    url='https://github.com/Blizzard/s2protocol',
    description='Python library to decode StarCraft II replay protocols',
    packages=[
        's2protocol',
        's2protocol.versions',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Games/Entertainment :: Real Time Strategy',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Archiving',
    ],
    install_requires=install_requires,
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            's2protocol = s2protocol.s2protocol:main',
            's2_cli.py = s2protocol.s2_cli:main',
        ]
    },
)
