# pyqt-skeleton

A simple example of how to get started with PyQt using a UI file
designed in Qt Designer. This is the easiest way to use Qt.

# Core Code

The essential code is show below (and contained in example.py).

```python
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
```

# Screenshots

Here's what it looks like on Windows 10:

![pyside-barebones on Windows 10](/screenshots/windows10.png)
