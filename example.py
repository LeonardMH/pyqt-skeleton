from PyQt4.QtGui import QWidget, QApplication
from PyQt4 import uic


class ExampleWidget(QWidget):
    def __init__(self, filepath):
        super(ExampleWidget, self).__init__()
        uic.loadUi(filepath, self)


if __name__ == "__main__":
    app = QApplication([])
    widget = ExampleWidget("example.ui")
    widget.show()
    app.exec_()
