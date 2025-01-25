from pathlib import Path
import sys

import catkin_sphinx


project = 'test_sh_lexer'

sys.path.append(str(Path(catkin_sphinx.__file__).parent.resolve()))

extensions = ['ShLexer']
