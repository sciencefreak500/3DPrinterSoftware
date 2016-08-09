# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddToQueue.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(200, 261)
        Dialog.setMinimumSize(QtCore.QSize(200, 261))
        Dialog.setMaximumSize(QtCore.QSize(200, 261))
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
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(Dialog)
        self.label.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.buttonList = QtGui.QFormLayout()
        self.buttonList.setObjectName(_fromUtf8("buttonList"))

        
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.buttonList.setWidget(0, QtGui.QFormLayout.LabelRole, self.checkBox)
        
        self.checkBox_2 = QtGui.QCheckBox(Dialog)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.buttonList.setWidget(1, QtGui.QFormLayout.LabelRole, self.checkBox_2)
        
        self.checkBox_3 = QtGui.QCheckBox(Dialog)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.buttonList.setWidget(1, QtGui.QFormLayout.FieldRole, self.checkBox_3)
        
        self.checkBox_4 = QtGui.QCheckBox(Dialog)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.buttonList.setWidget(2, QtGui.QFormLayout.LabelRole, self.checkBox_4)
        
        self.checkBox_5 = QtGui.QCheckBox(Dialog)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.buttonList.setWidget(3, QtGui.QFormLayout.LabelRole, self.checkBox_5)
        
        self.checkBox_6 = QtGui.QCheckBox(Dialog)
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.buttonList.setWidget(4, QtGui.QFormLayout.LabelRole, self.checkBox_6)
        
        self.checkBox_7 = QtGui.QCheckBox(Dialog)
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.buttonList.setWidget(4, QtGui.QFormLayout.FieldRole, self.checkBox_7)
        
        self.checkBox_8 = QtGui.QCheckBox(Dialog)
        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
        self.buttonList.setWidget(3, QtGui.QFormLayout.FieldRole, self.checkBox_8)
        
        self.checkBox_9 = QtGui.QCheckBox(Dialog)
        self.checkBox_9.setObjectName(_fromUtf8("checkBox_9"))
        self.buttonList.setWidget(2, QtGui.QFormLayout.FieldRole, self.checkBox_9)
        
        self.checkBox_10 = QtGui.QCheckBox(Dialog)
        self.checkBox_10.setObjectName(_fromUtf8("checkBox_10"))
        self.buttonList.setWidget(0, QtGui.QFormLayout.FieldRole, self.checkBox_10)

        
        self.verticalLayout.addLayout(self.buttonList)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

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
        self.checkBox.setText(_translate("Dialog", "CheckBox", None))
        self.checkBox_2.setText(_translate("Dialog", "CheckBox", None))
        self.checkBox_3.setText(_translate("Dialog", "CheckBox", None))
        self.checkBox_4.setText(_translate("Dialog", "CheckBox", None))
        self.checkBox_5.setText(_translate("Dialog", "CheckBox", None))
        self.checkBox_6.setText(_translate("Dialog", "CheckBox", None))
        self.checkBox_7.setText(_translate("Dialog", "CheckBox", None))
        self.checkBox_8.setText(_translate("Dialog", "CheckBox", None))
        self.checkBox_9.setText(_translate("Dialog", "CheckBox", None))
        self.checkBox_10.setText(_translate("Dialog", "CheckBox", None))







