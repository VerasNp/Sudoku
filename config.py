import os
import sys
from imp import reload


def set_environment():
    """
    Set environment variables
    :return:
    """
    os.environ["APP_NAME"] = "Sudoku"
