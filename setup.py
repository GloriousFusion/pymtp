#!/usr/bin/env python
# 
# setup.py for pymtp
#

from distutils.core import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name = "pymtp-gf",
      version = "0.1.1",
      description = "Custom fork of PyMTP with changes/updates",
      long_description=read('README'),
      author = "GloriousFusion",
      author_email = "lk.archcontact@gmail.com",
      maintainer = "GloriousFusion",
      maintainer_email = "lk.archcontact@gmail.com",
      url = "https://github.com/GloriousFusion/pymtp-gf",
      py_modules = ["pymtp"],
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Operating System :: POSIX',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
)
