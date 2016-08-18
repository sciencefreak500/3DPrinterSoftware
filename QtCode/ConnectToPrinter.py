# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConnectToPrinter.ui'
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
        self.label = QtGui.QLabel(Dialog)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.checkBox)
        self.checkBox_2 = QtGui.QCheckBox(Dialog)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.checkBox_2)
        self.checkBox_3 = QtGui.QCheckBox(Dialog)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.checkBox_3)
        self.checkBox_4 = QtGui.QCheckBox(Dialog)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.checkBox_4)
        self.checkBox_5 = QtGui.QCheckBox(Dialog)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.checkBox_5)
        self.checkBox_6 = QtGui.QCheckBox(Dialog)
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.checkBox_6)
        self.checkBox_7 = QtGui.QCheckBox(Dialog)
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.checkBox_7)
        self.checkBox_8 = QtGui.QCheckBox(Dialog)
        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.checkBox_8)
        self.checkBox_9 = QtGui.QCheckBox(Dialog)
        self.checkBox_9.setObjectName(_fromUtf8("checkBox_9"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.checkBox_9)
        self.checkBox_10 = QtGui.QCheckBox(Dialog)
        self.checkBox_10.setObjectName(_fromUtf8("checkBox_10"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.checkBox_10)
        self.checkBox_11 = QtGui.QCheckBox(Dialog)
        self.checkBox_11.setObjectName(_fromUtf8("checkBox_11"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.checkBox_11)
        self.checkBox_12 = QtGui.QCheckBox(Dialog)
        self.checkBox_12.setObjectName(_fromUtf8("checkBox_12"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.checkBox_12)
        self.checkBox_13 = QtGui.QCheckBox(Dialog)
        self.checkBox_13.setObjectName(_fromUtf8("checkBox_13"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.checkBox_13)
        self.checkBox_14 = QtGui.QCheckBox(Dialog)
        self.checkBox_14.setObjectName(_fromUtf8("checkBox_14"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.checkBox_14)
        self.checkBox_15 = QtGui.QCheckBox(Dialog)
        self.checkBox_15.setObjectName(_fromUtf8("checkBox_15"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.checkBox_15)
        self.checkBox_16 = QtGui.QCheckBox(Dialog)
        self.checkBox_16.setObjectName(_fromUtf8("checkBox_16"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.checkBox_16)
        self.verticalLayout.addLayout(self.formLayout)
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
        self.label.setText(_translate("Dialog", "Select Printers to Connect to:", None))
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
        self.checkBox_11.setText(_translate("Dialog", "CheckBox", None))
        self.checkBox_12.setText(_translate("Dialog", "CheckBox", None))
        self.checkBox_13.setText(_translate("Dialog", "CheckBox", None))
        self.checkBox_14.setText(_translate("Dialog", "CheckBox", None))
        self.checkBox_15.setText(_translate("Dialog", "CheckBox", None))
        self.checkBox_16.setText(_translate("Dialog", "CheckBox", None))

