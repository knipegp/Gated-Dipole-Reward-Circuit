#!/usr/bin/env python
from setuptools import setup

setup(
    name='gated-dipole-reward-circuit',
    version='1.0',
    description='A gated-dipole model of addiction',
    author='Jack Demaree, Sarah Di, Diana Edwards, Griffin Knipe',
    url='https://github.com/knipegp/Gated-Dipole-Reward-Circuit',
    packages=['circuits', 'nodes'],
    install_requires=[
        'matplotlib>=3.0.2'
    ]
)
