#!/usr/bin/env python
from distutils.core import setup

__version__ = '0.0.1'

setup(name='euth_wagtail',
      version=__version__,
      description='Wagtail installation for EUth (OPIN) cms',
      url='https://opin.net',
      packages=['euth_wagtail'],
      install_requires=[
          'Django',
          'wagtail',
          'django_bower'
      ])
