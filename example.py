from PyQt4.QtGui import QWidget, QApplication
from PyQt4.uic import loadUi as load_ui_widget


class ExampleApplication(QApplication):
    def __init__(self, **kwargs):
        super(ExampleApplication, self).__init__([], **kwargs)

    def start(self):
        self.exec_()


class ExampleWidget(QWidget):
    def __init__(self):
        super(ExampleWidget, self).__init__()
        load_ui_widget("example.ui", self)
        self.setWindowTitle("PyQt Example")
        self.show()


if __name__ == "__main__":
    app = ExampleApplication()
    widget = ExampleWidget()
    app.start()
