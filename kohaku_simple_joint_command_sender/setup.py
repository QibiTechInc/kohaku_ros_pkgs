#!/usr/bin/env python
from setuptools import setup

from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
    packages=['kohaku_simple_joint_command_sender'],
    package_dir={'': 'src'},
    )

setup(**setup_args)
