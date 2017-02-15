# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


readme = open('README.md').read()
history = open('HISTORY.md').read().replace('.. :changelog:', '')


setup(
    name='json-keys-helper',
    version='0.1.0',
    description='Helper functions to retreive keys from any JSON data.',
    long_description=readme + '\n\n' + history,
    author='Madhurima Poddar',
    author_email='madhurima.@gmail.com',
    url='https://github.com/madhurimapoddar/json_keys/',
    py_modules=['json_keys'],
    license="MIT",
    zip_safe=False,
    keywords='json keys helper',
    classifiers=[
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
)
