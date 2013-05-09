#!/usr/bin/env python
import sys
from setuptools import setup


setup(
    name='s2protocol',
    version='1.0.1-dev',
    author='Blizzard Entertainment',
    url='https://github.com/Blizzard/s2protocol',
    description='Python library to decode StarCraft II replay protocols',
    packages=[
        's2protocol',
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
    install_requires=['mpyq'],
)
