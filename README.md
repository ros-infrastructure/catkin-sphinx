Catkin-Sphinx
=============

Sphinx plugins for Catkin projects.

Using
-----

To use this plugin, add the following to the ``conf.py`` in your project
(which it should have as one of the files used by Sphinx to generate
documentation):

    # Below the definition of the extensions list:
    extensions = extensions + ['catkin_sphinx.cmake', 'catkin_sphinx.ShLexer']

    # Below the definition of html_theme_path:
    import catkin_sphinx
    html_theme_path = [catkin_sphinx.get_theme_path()]

