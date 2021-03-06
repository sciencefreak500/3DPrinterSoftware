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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(703, 537)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.BackLayout = QtGui.QHBoxLayout()
        self.BackLayout.setObjectName(_fromUtf8("BackLayout"))
        self.vertPrinterLayout = QtGui.QVBoxLayout()
        self.vertPrinterLayout.setObjectName(_fromUtf8("vertPrinterLayout"))
        self.lbl_Printers = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Laksaman"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_Printers.setFont(font)
        self.lbl_Printers.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Printers.setObjectName(_fromUtf8("lbl_Printers"))
        self.vertPrinterLayout.addWidget(self.lbl_Printers)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.checkNetwork = QtGui.QCheckBox(self.centralwidget)
        self.checkNetwork.setCheckable(True)
        self.checkNetwork.setObjectName(_fromUtf8("checkNetwork"))
        self.horizontalLayout_6.addWidget(self.checkNetwork)
        self.vertPrinterLayout.addLayout(self.horizontalLayout_6)
        self.listPrinterList = QtGui.QListWidget(self.centralwidget)
        self.listPrinterList.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listPrinterList.setFont(font)
        self.listPrinterList.setDragEnabled(False)
        self.listPrinterList.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.listPrinterList.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listPrinterList.setSelectionRectVisible(False)
        self.listPrinterList.setObjectName(_fromUtf8("listPrinterList"))
        self.vertPrinterLayout.addWidget(self.listPrinterList)
        self.horizPrinterButtons = QtGui.QHBoxLayout()
        self.horizPrinterButtons.setObjectName(_fromUtf8("horizPrinterButtons"))
        self.btn_Connect = QtGui.QPushButton(self.centralwidget)
        self.btn_Connect.setObjectName(_fromUtf8("btn_Connect"))
        self.horizPrinterButtons.addWidget(self.btn_Connect)
        self.btn_Disconnect = QtGui.QPushButton(self.centralwidget)
        self.btn_Disconnect.setObjectName(_fromUtf8("btn_Disconnect"))
        self.horizPrinterButtons.addWidget(self.btn_Disconnect)
        self.vertPrinterLayout.addLayout(self.horizPrinterButtons)
        self.BackLayout.addLayout(self.vertPrinterLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lbl_Arduino = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Laksaman"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_Arduino.setFont(font)
        self.lbl_Arduino.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Arduino.setObjectName(_fromUtf8("lbl_Arduino"))
        self.verticalLayout_2.addWidget(self.lbl_Arduino)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.lcd_Printers = QtGui.QLCDNumber(self.centralwidget)
        self.lcd_Printers.setObjectName(_fromUtf8("lcd_Printers"))
        self.horizontalLayout_16.addWidget(self.lcd_Printers)
        self.lcd_Arduinos = QtGui.QLCDNumber(self.centralwidget)
        self.lcd_Arduinos.setObjectName(_fromUtf8("lcd_Arduinos"))
        self.horizontalLayout_16.addWidget(self.lcd_Arduinos)
        self.lcd_Files = QtGui.QLCDNumber(self.centralwidget)
        self.lcd_Files.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lcd_Files.setFont(font)
        self.lcd_Files.setObjectName(_fromUtf8("lcd_Files"))
        self.horizontalLayout_16.addWidget(self.lcd_Files)
        self.verticalLayout_2.addLayout(self.horizontalLayout_16)
        self.listArduino = QtGui.QListView(self.centralwidget)
        self.listArduino.setObjectName(_fromUtf8("listArduino"))
        self.verticalLayout_2.addWidget(self.listArduino)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_editArduino = QtGui.QPushButton(self.centralwidget)
        self.btn_editArduino.setObjectName(_fromUtf8("btn_editArduino"))
        self.horizontalLayout.addWidget(self.btn_editArduino)
        self.btn_testArduino = QtGui.QPushButton(self.centralwidget)
        self.btn_testArduino.setObjectName(_fromUtf8("btn_testArduino"))
        self.horizontalLayout.addWidget(self.btn_testArduino)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.btn_connectArduino = QtGui.QPushButton(self.centralwidget)
        self.btn_connectArduino.setObjectName(_fromUtf8("btn_connectArduino"))
        self.verticalLayout_2.addWidget(self.btn_connectArduino)
        self.BackLayout.addLayout(self.verticalLayout_2)
        self.vertQueueLayout = QtGui.QVBoxLayout()
        self.vertQueueLayout.setObjectName(_fromUtf8("vertQueueLayout"))
        self.lbl_PrintingQueue = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Laksaman"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_PrintingQueue.setFont(font)
        self.lbl_PrintingQueue.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_PrintingQueue.setObjectName(_fromUtf8("lbl_PrintingQueue"))
        self.vertQueueLayout.addWidget(self.lbl_PrintingQueue)
        self.horizQueueButtons = QtGui.QHBoxLayout()
        self.horizQueueButtons.setObjectName(_fromUtf8("horizQueueButtons"))
        self.btn_addItem = QtGui.QPushButton(self.centralwidget)
        self.btn_addItem.setEnabled(True)
        self.btn_addItem.setCheckable(False)
        self.btn_addItem.setAutoDefault(False)
        self.btn_addItem.setDefault(False)
        self.btn_addItem.setFlat(False)
        self.btn_addItem.setObjectName(_fromUtf8("btn_addItem"))
        self.horizQueueButtons.addWidget(self.btn_addItem)
        self.btn_clearList = QtGui.QPushButton(self.centralwidget)
        self.btn_clearList.setDefault(False)
        self.btn_clearList.setFlat(False)
        self.btn_clearList.setObjectName(_fromUtf8("btn_clearList"))
        self.horizQueueButtons.addWidget(self.btn_clearList)
        self.vertQueueLayout.addLayout(self.horizQueueButtons)
        self.list_PrintQueue = QtGui.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.list_PrintQueue.setFont(font)
        self.list_PrintQueue.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.list_PrintQueue.setDragEnabled(True)
        self.list_PrintQueue.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.list_PrintQueue.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.list_PrintQueue.setObjectName(_fromUtf8("list_PrintQueue"))
        self.vertQueueLayout.addWidget(self.list_PrintQueue)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.btn_Edit = QtGui.QPushButton(self.centralwidget)
        self.btn_Edit.setEnabled(True)
        self.btn_Edit.setAutoFillBackground(False)
        self.btn_Edit.setFlat(False)
        self.btn_Edit.setObjectName(_fromUtf8("btn_Edit"))
        self.horizontalLayout_4.addWidget(self.btn_Edit)
        self.btn_Remove = QtGui.QPushButton(self.centralwidget)
        self.btn_Remove.setObjectName(_fromUtf8("btn_Remove"))
        self.horizontalLayout_4.addWidget(self.btn_Remove)
        self.vertQueueLayout.addLayout(self.horizontalLayout_4)
        self.btn_Print = QtGui.QPushButton(self.centralwidget)
        self.btn_Print.setObjectName(_fromUtf8("btn_Print"))
        self.vertQueueLayout.addWidget(self.btn_Print)
        self.BackLayout.addLayout(self.vertQueueLayout)
        self.horizontalLayout_2.addLayout(self.BackLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 703, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_Item = QtGui.QAction(MainWindow)
        self.actionAdd_Item.setObjectName(_fromUtf8("actionAdd_Item"))
        self.actionRemove_Selected_Item = QtGui.QAction(MainWindow)
        self.actionRemove_Selected_Item.setObjectName(_fromUtf8("actionRemove_Selected_Item"))
        self.actionConnect = QtGui.QAction(MainWindow)
        self.actionConnect.setObjectName(_fromUtf8("actionConnect"))
        self.actionDisconnect_Selected = QtGui.QAction(MainWindow)
        self.actionDisconnect_Selected.setObjectName(_fromUtf8("actionDisconnect_Selected"))
        self.actionClear_List = QtGui.QAction(MainWindow)
        self.actionClear_List.setObjectName(_fromUtf8("actionClear_List"))
        self.actionPrint = QtGui.QAction(MainWindow)
        self.actionPrint.setObjectName(_fromUtf8("actionPrint"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionEdit_Item_Properties = QtGui.QAction(MainWindow)
        self.actionEdit_Item_Properties.setObjectName(_fromUtf8("actionEdit_Item_Properties"))
        self.actionMove_Selected = QtGui.QAction(MainWindow)
        self.actionMove_Selected.setObjectName(_fromUtf8("actionMove_Selected"))
        self.actionMove_Selected_Down = QtGui.QAction(MainWindow)
        self.actionMove_Selected_Down.setObjectName(_fromUtf8("actionMove_Selected_Down"))
        self.actionMove_Selected_Up = QtGui.QAction(MainWindow)
        self.actionMove_Selected_Up.setObjectName(_fromUtf8("actionMove_Selected_Up"))
        self.actionMove_Selected_Down_2 = QtGui.QAction(MainWindow)
        self.actionMove_Selected_Down_2.setObjectName(_fromUtf8("actionMove_Selected_Down_2"))
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionConfigure = QtGui.QAction(MainWindow)
        self.actionConfigure.setObjectName(_fromUtf8("actionConfigure"))
        self.actionDocumentation = QtGui.QAction(MainWindow)
        self.actionDocumentation.setObjectName(_fromUtf8("actionDocumentation"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionEdit_Selected_Item = QtGui.QAction(MainWindow)
        self.actionEdit_Selected_Item.setObjectName(_fromUtf8("actionEdit_Selected_Item"))
        self.menuFile.addAction(self.actionAdd_Item)
        self.menuFile.addAction(self.actionEdit_Selected_Item)
        self.menuFile.addAction(self.actionRemove_Selected_Item)
        self.menuFile.addAction(self.actionClear_List)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionConnect)
        self.menuFile.addAction(self.actionDisconnect_Selected)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionEdit_Item_Properties)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionPreferences)
        self.menuEdit.addAction(self.actionConfigure)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.lbl_Printers.setText(_translate("MainWindow", "Printers", None))
        self.checkNetwork.setText(_translate("MainWindow", "Network", None))
        self.btn_Connect.setText(_translate("MainWindow", "Connect", None))
        self.btn_Disconnect.setText(_translate("MainWindow", "Disconnect", None))
        self.lbl_Arduino.setText(_translate("MainWindow", "Arduino", None))
        self.btn_editArduino.setText(_translate("MainWindow", "Edit Selected", None))
        self.btn_testArduino.setText(_translate("MainWindow", "Test Selected", None))
        self.btn_connectArduino.setText(_translate("MainWindow", "Connect", None))
        self.lbl_PrintingQueue.setText(_translate("MainWindow", "Printing Queue", None))
        self.btn_addItem.setText(_translate("MainWindow", "Add Item", None))
        self.btn_clearList.setText(_translate("MainWindow", "Clear List", None))
        self.btn_Edit.setText(_translate("MainWindow", "Edit Selected", None))
        self.btn_Remove.setText(_translate("MainWindow", "Remove Selected", None))
        self.btn_Print.setText(_translate("MainWindow", "Print", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionAdd_Item.setText(_translate("MainWindow", "Add Item", None))
        self.actionRemove_Selected_Item.setText(_translate("MainWindow", "Remove Selected Item", None))
        self.actionConnect.setText(_translate("MainWindow", "Connect", None))
        self.actionDisconnect_Selected.setText(_translate("MainWindow", "Disconnect Selected", None))
        self.actionClear_List.setText(_translate("MainWindow", "Clear List", None))
        self.actionPrint.setText(_translate("MainWindow", "Print", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionEdit_Item_Properties.setText(_translate("MainWindow", "Edit Item Properties", None))
        self.actionMove_Selected.setText(_translate("MainWindow", "Move Selected Up", None))
        self.actionMove_Selected_Down.setText(_translate("MainWindow", "Move Selected Down", None))
        self.actionMove_Selected_Up.setText(_translate("MainWindow", "Move Selected Up", None))
        self.actionMove_Selected_Down_2.setText(_translate("MainWindow", "Move Selected Down", None))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences", None))
        self.actionConfigure.setText(_translate("MainWindow", "Configure", None))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionEdit_Selected_Item.setText(_translate("MainWindow", "Edit Selected Item", None))

