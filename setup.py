#!/usr/bin/env python3

"""
    Setup script for uncompyle3
"""

from distutils.core import setup, Extension

setup (name = "uncompyle3",
       version = "1.1",
       description = "Python3 bytecode decompiler",
       author = "Anton Vorobyov",
       url = "http://github.com/DarkFenX/uncompyle3",
       packages = ['uncompyle3', 'uncompyle3.parser', 'uncompyle3.utils',
                   'uncompyle3.walker'],
       scripts = ['scripts/uncompyle3'],
      )
