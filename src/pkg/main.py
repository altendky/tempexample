import pathlib
import sys

from PyQt5 import Qt
import PyQt5.uic

import pkg.hellogl


def ignore_mouse_events(cls):
    def resizeEvent(self, event):
        super(cls, self).resizeEvent(event)

        region = Qt.QRegion(self.frameGeometry())
        region -= Qt.QRegion(self.geometry())
        region += self.childrenRegion()
        self.setMask(region)

    cls.resizeEvent = resizeEvent

    # def ignore_event(self, event):
    #     print('ignoring')
    #     # event.ignore()
    #
    # cls.mouseMoveEvent = ignore_event
    # cls.mousePressEvent = ignore_event

    return cls

OverlayUi, OverlayBase = PyQt5.uic.loadUiType(
    pathlib.Path(__file__).with_name('overlay.ui'),
)


@ignore_mouse_events
class Overlay(OverlayBase):
    def setup(self):
        self.ui = OverlayUi()
        self.ui.setupUi(self)

        self.setMouseTracking(True)


class MainWindow(Qt.QMainWindow):
    def __init__(self, parent=None, flags=None):
        args = [parent]
        if flags is not None:
            args.append(flags)

        super().__init__(*args)

        self.stacked = Qt.QStackedWidget()
        self.stacked.layout().setStackingMode(Qt.QStackedLayout.StackAll)
        self.setCentralWidget(self.stacked)

        self.overlay = Overlay()
        self.overlay.setup()
        self.stacked.addWidget(self.overlay)

        self.gl = pkg.hellogl.Window()
        self.stacked.addWidget(self.gl)


def main():
    app = Qt.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
