Catkin-Sphinx
=============

Sphinx plugins for Catkin projects.
Currently provides the ROS theme, better shell prompt highlighting and a sphinx domain for cmake.

Using the ROS theme
-------------------

To use this plugin, add the following to the ``conf.py`` in your project
(which it should have as one of the files used by Sphinx to generate
documentation):

    # Below the definition of html_theme_path:
    import catkin_sphinx
    html_theme_path = [catkin_sphinx.get_theme_path()]

    # Use ROS theme
    html_theme = 'ros-theme'

Using an improved shell prompt highlighting
-------------------------------------------

Add the following to the ``conf.py`` in your project below the definition of the extensions list::

    extensions = extensions + ['catkin_sphinx.ShLexer']

This will slightly improve documentation highlighting for examples like::

    # this will make all following snippets be of type prompt
    .. highlight:: catkin-sh

    # this will create a single code block of type prompt (examples)
    .. code-block:: catkin-sh

      >>> python setup.py install
      # comment
      $ bash prompt

Using the cmake sphinx domain
-----------------------------

Add the following to the ``conf.py`` in your project below the definition of the extensions list::

    extensions = extensions + ['catkin_sphinx.cmake']

Then cmake modules and macros can be documented using the following syntax::

    * :cmake:mod:`foo` Module

    .. cmake:macro:: bar(bam)

      :param bam: foo docstring
      :type bam: string
      :returns: list

Blank lines and indentation are important.
No autodoc extention for cmake files yet.
