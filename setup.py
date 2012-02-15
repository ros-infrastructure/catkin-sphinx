#!/usr/bin/env python

from distutils.core import setup

setup(name='catkin-sphinx',
      version='0.1.0',
      packages=['catkin_sphinx'],
      package_dir = {'':'src'},
      author = "Troy Straszheim", 
      author_email = "straszheim@willowgarage.com",
      url = "http://www.ros.org/",
      download_url = "http://pr.willowgarage.com/downloads/catkin_sphinx/", 
      keywords = ["ROS"],
      classifiers = [
        "Programming Language :: Python", 
        "License :: OSI Approved :: BSD License" ],
      description = "ROS package library", 
      long_description = """\
cmake domain extension for sphinx
""",
      license = "BSD"
      )
