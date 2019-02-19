#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('../src/files/')

project = u'PyFingerprint'
master_doc = 'PyFingerprint'
copyright = '2019, Bastian Raschke <bastian.raschke@posteo.de>'
author = 'Bastian Raschke <bastian.raschke@posteo.de>'
version = __import__('pyfingerprint').__version__
release = version
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store'
]
extensions = [
    'sphinx.ext.autodoc',
]
