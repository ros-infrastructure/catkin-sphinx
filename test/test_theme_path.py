import catkin_sphinx


def test_theme_path():
    res = catkin_sphinx.get_theme_path()
    assert res
