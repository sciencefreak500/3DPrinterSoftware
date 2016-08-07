# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PrintProgramUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName(_fromUtf8("window"))
        window.resize(465, 289)
        self.centralwidget = QtGui.QWidget(window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.UpButton = QtGui.QPushButton(self.centralwidget)
        self.UpButton.setObjectName(_fromUtf8("UpButton"))
        self.verticalLayout.addWidget(self.UpButton)
        self.DownButton = QtGui.QPushButton(self.centralwidget)
        self.DownButton.setObjectName(_fromUtf8("DownButton"))
        self.verticalLayout.addWidget(self.DownButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.PrintQueue = QtGui.QListWidget(self.centralwidget)
        self.PrintQueue.setObjectName(_fromUtf8("PrintQueue"))
        self.gridLayout.addWidget(self.PrintQueue, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 465, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        window.setStatusBar(self.statusbar)
        self.actionPrint = QtGui.QAction(window)
        self.actionPrint.setObjectName(_fromUtf8("actionPrint"))
        self.actionExit = QtGui.QAction(window)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAdd_To_Queue = QtGui.QAction(window)
        self.actionAdd_To_Queue.setObjectName(_fromUtf8("actionAdd_To_Queue"))
        self.actionRemove_from_Queue = QtGui.QAction(window)
        self.actionRemove_from_Queue.setObjectName(_fromUtf8("actionRemove_from_Queue"))
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionAdd_To_Queue)
        self.menuEdit.addAction(self.actionRemove_from_Queue)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        window.setWindowTitle(_translate("window", "3DPrint-Automation", None))
        self.UpButton.setText(_translate("window", "↑", None))
        self.DownButton.setText(_translate("window", "↓", None))
        self.menuFile.setTitle(_translate("window", "File", None))
        self.menuEdit.setTitle(_translate("window", "Edit", None))
        self.actionPrint.setText(_translate("window", "Print", None))
        self.actionExit.setText(_translate("window", "Exit", None))
        self.actionAdd_To_Queue.setText(_translate("window", "Add To Queue", None))
        self.actionRemove_from_Queue.setText(_translate("window", "Remove from Queue", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
   

