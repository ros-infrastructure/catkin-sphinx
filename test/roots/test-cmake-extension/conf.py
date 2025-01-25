from pathlib import Path
import sys

import catkin_sphinx


project = 'test_cmake_extension'

sys.path.append(str(Path(catkin_sphinx.__file__).parent.resolve()))

extensions = ['cmake']
