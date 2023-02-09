#!/usr/bin/env python3

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# for your packages to be recognized by python
d = generate_distutils_setup(
 packages=['ur_moveit'],
 #Original
#  package_dir={'ros_wrapper': 'scripts'}
# Mine
#  package_dir={'scripts': ''}
)

setup(**d)
