from PySide2.QtWidgets import (
    QApplication
)
from classes.flashcardswindow import FlashcardsWindow
import sys

def guiMain(args):
    app = QApplication(args)
    window = FlashcardsWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
