import os


def get_theme_path():
    """Returns the path to the themes bundled with catkin_sphinx"""
    this_dir = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(this_dir, 'theme')
