#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='flask-navbar',
      version='0.0.1',
      description='Easily create navigation for Flask applications. An extended copy of Flask_nav 0.6',
      long_description=read('README.rst'),
      author='zcyuefan',
      author_email='zcyuefan@126.com',
      url='http://github.com/zcyuefan/flask-navbar',
      license='MIT',
      packages=find_packages(exclude=['tests', 'example']),
      install_requires=['flask', 'visitor', 'dominate'],
      classifiers=[
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ])
