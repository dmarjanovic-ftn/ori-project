import sys
from PySide import QtGui

from views.main_window import MainWindow
from train import load_trained_model


class App(QtGui.QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)

        self.model = load_trained_model()

        self.main_window = MainWindow()
        self.main_window.show()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
