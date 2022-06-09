#!/usr/bin/env python

from setuptools import setup

setup(
  name='catkin-sphinx',
  version='0.3.2',
  packages=['catkin_sphinx'],
  package_data={
    'catkin_sphinx': [
      'theme/ros-theme/theme.conf',
      'theme/ros-theme/static/sphinxdoc.css',
      'theme/ros-theme/static/pygments.css'
    ]
  },
  package_dir={'catkin_sphinx': 'src/catkin_sphinx'},
  author = "Troy Straszheim, Issac Trotts, William Woodall",
  author_email = "straszheim@willowgarage.com, itrotts@willowgarage.com, william@openrobotics.org",
  maintainer="ROS Infrastructure Team",
  project_urls={
    'Source code':
    'https://github.com/ros-infrastructure/catkin-sphinx',
    'Issue tracker':
    'https://github.com/ros-infrastructure/catkin-sphinx/issues',
  },
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
