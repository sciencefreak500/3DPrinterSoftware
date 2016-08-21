# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddToQueue.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
Names = []
Ports = []

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

class Ui_Dialog(object):
    def __init__(self):
        self.checkbox = []
    
    
    def setupUi(self, Dialog):
        global Names, Ports

        
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(200, 261)
        Dialog.setMinimumSize(QtCore.QSize(250, 261))
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_FileDialog = QtGui.QPushButton(Dialog)
        self.btn_FileDialog.setObjectName(_fromUtf8("btn_FileDialog"))
        self.horizontalLayout.addWidget(self.btn_FileDialog)
        self.lbl_FileName = QtGui.QLabel(Dialog)
        self.lbl_FileName.setObjectName(_fromUtf8("lbl_FileName"))
        self.horizontalLayout.addWidget(self.lbl_FileName)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lbl_NumPrints = QtGui.QLabel(Dialog)
        self.lbl_NumPrints.setObjectName(_fromUtf8("lbl_NumPrints"))
        self.horizontalLayout_2.addWidget(self.lbl_NumPrints)
        self.PrintNumEdit = QtGui.QLineEdit(Dialog)
        self.PrintNumEdit.setObjectName(_fromUtf8("PrintNumEdit"))
        self.horizontalLayout_2.addWidget(self.PrintNumEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        
        self.label = QtGui.QLabel(Dialog)
        self.label.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.buttonList = QtGui.QFormLayout()
        self.buttonList.setObjectName(_fromUtf8("buttonList"))


        guiplacement = 0
        checker = (False,False)
        for index,i in enumerate(Names):
            self.checkbox.append(QtGui.QCheckBox(Dialog))
            self.checkbox[index].setObjectName(_fromUtf8(Names[index]))
            if checker == (True,True):
                guiplacement += 1
                checker = (False,False)             

            if checker == (False,False):
                self.buttonList.setWidget(guiplacement, QtGui.QFormLayout.LabelRole, self.checkbox[index])
                checker = (True,False)
            elif checker == (True,False):
                self.buttonList.setWidget(guiplacement, QtGui.QFormLayout.FieldRole, self.checkbox[index])
                checker = (True,True)
            self.checkbox[index].setText(_translate("Dialog", Names[index], None))

        
        
        self.verticalLayout.addLayout(self.buttonList)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.btn_FileDialog.setText(_translate("Dialog", "Select File", None))
        self.lbl_FileName.setText(_translate("Dialog", "...", None))
        self.lbl_NumPrints.setText(_translate("Dialog", "Number of Prints: ", None))
        self.label.setText(_translate("Dialog", "Select Printers for the job: ", None))
                



