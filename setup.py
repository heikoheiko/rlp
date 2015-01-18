#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='rlp',
    version='0.1.0',
    description='RLP ("recursive length prefix") encoding is the main serialization format used in Ethereum',
    long_description=readme + '\n\n' + history,
    author='Vitalik Buterin',
    url='https://github.com/heikoheiko/rlp',
    packages=[
        'rlp',
    ],
    package_dir={'rlp':
                 'rlp'},
    include_package_data=True,
    install_requires=requirements,
    license="WTFPL",
    zip_safe=False,
    keywords='rlp',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
