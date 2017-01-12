import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic


class ExampleWidget(QWidget):
    def __init__(self, filepath):
        super(ExampleWidget, self).__init__()
        uic.loadUi(filepath, self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = ExampleWidget("example.ui")
    widget.show()

    sys.exit(app.exec_())
