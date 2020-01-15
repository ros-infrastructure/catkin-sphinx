#!/usr/bin/env python

from setuptools import setup

setup(
  name='catkin-sphinx',
  version='0.3.1',
  packages=['catkin_sphinx'],
  package_data={
    'catkin_sphinx': [
      'theme/ros-theme/theme.conf',
      'theme/ros-theme/static/sphinxdoc.css',
      'theme/ros-theme/static/pygments.css'
    ]
  },
  package_dir={'catkin_sphinx': 'src/catkin_sphinx'},
  # The original author was Troy Straszheim
  # Previous maintainers include: Issac Trotts
  # The current maintainer is William Woodall
  author="William Woodall",
  author_email="william@osrfoundation.org",
  url="http://www.ros.org/",
  download_url="http://pr.willowgarage.com/downloads/catkin_sphinx/",
  keywords=["ROS"],
  classifiers=[
    "Programming Language :: Python",
    "License :: OSI Approved :: BSD License"
  ],
  description="Sphinx extension for Catkin projects",
  long_description="Sphinx extension for Catkin projects that provides a "
                   "custom ROS theme and a Sphinx domain for cmake.",
  license="BSD"
)
