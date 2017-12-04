from PyQt5.QtCore import QThread, pyqtSignal,Qt,QCoreApplication
from PyQt5.QtSql import QSqlRelationalTableModel,QSqlRelation,QSqlTableModel,QSqlDatabase

from PyQt5.QtWidgets import QWidget,QPushButton,QLabel,QApplication,QTextEdit,QLineEdit,QHBoxLayout,QVBoxLayout,QDialog,QTableView
import time, os, re,sys

class mainUi(QWidget):
    def __init__(self,sch):
        filename = os.getcwd() + '\\db.db'
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(filename)
        super().__init__()

        self.addpcModel = QSqlTableModel(self)
        self.addpcModel.setTable(sch)
        #self.addpcModel.setSort(NAME, Qt.AscendingOrder)
        self.addpcModel.setHeaderData(0, Qt.Horizontal,"ID")
        self.addpcModel.setHeaderData(1, Qt.Horizontal, "电脑名称")
        self.addpcModel.setHeaderData(2, Qt.Horizontal,"仪器名称")
        self.addpcModel.setHeaderData(6, Qt.Horizontal, '最近成功爬取时间')
        self.addpcModel.setHeaderData(3,Qt.Horizontal,'抓取路径')
        self.addpcModel.setHeaderData(4,Qt.Horizontal,'保存路径')
        self.addpcModel.setHeaderData(5,Qt.Horizontal,'最近爬取时间')

        # self.addpcModel.setData(1,'ok')
        self.addpcModel.removeColumn(8)
        self.addpcModel.removeColumn(7)

        self.addpcModel.query()
        self.addpcModel.select()
        # self.addpcModel.select()

        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('欣捷工作站数据文件自动爬取工具')
        self.resize(800,600)

        self.v = QHBoxLayout()   #左右分栏
        self.h1 = QVBoxLayout()
        self.h2 = QVBoxLayout()

        self.h1_1 = QHBoxLayout()
        self.h1_2 = QHBoxLayout()
        self.h1.addLayout(self.h1_1)
        self.h1.addLayout(self.h1_2)


        self.v.addLayout(self.h1)
        self.v.addLayout(self.h2)
        self.v.setStretchFactor(self.h1,6)
        self.v.setStretchFactor(self.h2,4)


        self.btn_start = QPushButton('马上运行',self)
        self.btn_viewlog = QPushButton('查看以前日志',self)
        self.h1_1.addWidget(self.btn_start)
        self.h1_1.addWidget(self.btn_viewlog)

        self.txt_log = QTextEdit('',self)
        self.h1_2.addWidget(self.txt_log)


        self.btn_addpc = QPushButton('添加需要爬取的电脑',self)
        self.sch_view = QTableView()
        self.sch_view.setModel(self.addpcModel)
        self.sch_view.setSelectionMode(QTableView.SingleSelection)
        self.sch_view.setSelectionBehavior(QTableView.SelectRows)
        self.sch_view.setColumnHidden(0, True)
        self.sch_view.resizeColumnsToContents()
        self.h2.addWidget(self.btn_addpc)
        self.h2.addWidget(self.sch_view)



        self.setLayout(self.v)
        self.setWindowOpacity(1)



        self.show()

class addpc(QDialog):
    def __init__(self):
        super().__init__()
        t = self.add_pc()
    def add_pc(self):


        self.setWindowTitle('添加需要爬取数据的电脑')
        self.resize(300, 200)
        self.hd1 = QHBoxLayout()
        self.hd2 = QHBoxLayout()
        self.hd3 = QHBoxLayout()
        self.hd4 = QHBoxLayout()
        self.hd5 = QHBoxLayout()
        self.hd6 = QHBoxLayout()

        self.vd = QVBoxLayout()
        self.vd.addLayout(self.hd1)
        self.vd.addLayout(self.hd2)
        self.vd.addLayout(self.hd3)
        self.vd.addLayout(self.hd4)
        self.vd.addLayout(self.hd5)
        self.vd.addLayout(self.hd6)
        self.lab1 = QLabel('请输入以下信息', self)
        self.hd1.addWidget(self.lab1)
        self.lab2 = QLabel('电脑名称（*）：', self)
        self.txt_pcname = QLineEdit('', self)
        self.hd2.addWidget(self.lab2)
        self.hd2.addWidget(self.txt_pcname)
        self.lab3 = QLabel('仪器编号（*）：', self)
        self.txt_insname = QLineEdit('', self)
        self.hd3.addWidget(self.lab3)
        self.hd3.addWidget(self.txt_insname)

        self.lab4 = QLabel('抓取路径（*）：', self)
        self.txt_spath = QLineEdit('', self)
        self.hd4.addWidget(self.lab4)
        self.hd4.addWidget(self.txt_spath)

        self.lab5 = QLabel('存放路径（*）：', self)
        self.txt_despath = QLineEdit('', self)
        self.hd5.addWidget(self.lab5)
        self.hd5.addWidget(self.txt_despath)

        self.btn_save = QPushButton('保存',self)
        self.btn_cancel = QPushButton('取消',self)
        self.btn_cancel.clicked.connect(self.done)
        self.hd6.addWidget(self.btn_save)
        self.hd6.addWidget(self.btn_cancel)



        self.setLayout(self.vd)
        self.show()


# class add_pc(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.setupUI()
#
#     def setupUI(self):
#         self.setWindowTitle('添加需要爬取数据的电脑')
#         self.resize(300,200)
#         self.h1 = QHBoxLayout()
#         self.h2 = QHBoxLayout()
#         self.h3 = QHBoxLayout()
#         self.h4 = QHBoxLayout()
#         self.h5 = QHBoxLayout()
#
#         self.v = QVBoxLayout()
#         self.v.addLayout(self.h1)
#         self.v.addLayout(self.h2)
#         self.v.addLayout(self.h3)
#         self.v.addLayout(self.h4)
#         self.v.addLayout(self.h5)
#         self.lab1 = QLabel('请输入以下信息',self)
#         self.h1.addWidget(self.lab1)
#         self.lab2 = QLabel('电脑名称（*）：',self)
#         self.txt_pcname = QLineEdit('',self)
#         self.h2.addWidget(self.lab2)
#         self.h2.addWidget(self.txt_pcname)
#
#         self.lab3 = QLabel('仪器编号（*）：',self)
#         self.txt_insname = QLineEdit('',self)
#         self.h3.addWidget(self.lab3)
#         self.h3.addWidget(self.txt_insname)
#
#         self.lab4 = QLabel('抓取路径（*）：',self)
#         self.txt_spath = QLineEdit('',self)
#         self.h4.addWidget(self.lab4)
#         self.h4.addWidget(self.txt_spath)
#
#         self.lab5 = QLabel('数据存放路径（*）：',self)
#         self.txt_despath = QLineEdit('',self)
#         self.h5.addWidget(self.lab5)
#         self.h5.addWidget(self.txt_despath)
#
#
#         self.setLayout(self.v)
#         self.show()



#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     t = mainUi()
#     sys.exit(app.exec_())
