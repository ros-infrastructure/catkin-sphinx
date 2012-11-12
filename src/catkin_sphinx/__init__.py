import os


def get_theme_path():
    """Returns the path to the themes bundled with catkin_sphinx"""
    return os.path.join(os.path.abspath(os.path.dirname(__file__)),
                        'theme')
