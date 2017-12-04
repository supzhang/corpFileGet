from ui import mainUi,addpc

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal


class xj(mainUi):

    def __init__(self):
        super().__init__('schedule')
        self.btn_addpc.clicked.connect(self.add_pc)


    def start(self):
        pass

    def get_log(self):
        pass

    def add_pc(self):
        dform = addpc()
        dform.exec_()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    u = xj()
    sys.exit(app.exec_())