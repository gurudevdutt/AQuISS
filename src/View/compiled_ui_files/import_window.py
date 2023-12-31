# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/View/ui_files/import_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(792, 512)
        self.text_info = QtWidgets.QTextEdit(Dialog)
        self.text_info.setGeometry(QtCore.QRect(340, 30, 441, 161))
        self.text_info.setObjectName("text_info")
        self.list_experiment = QtWidgets.QListView(Dialog)
        self.list_experiment.setGeometry(QtCore.QRect(10, 30, 311, 351))
        self.list_experiment.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.list_experiment.setObjectName("list_experiment")
        self.btn_export = QtWidgets.QPushButton(Dialog)
        self.btn_export.setGeometry(QtCore.QRect(710, 470, 75, 23))
        self.btn_export.setObjectName("btn_export")
        self.text_error = QtWidgets.QTextBrowser(Dialog)
        self.text_error.setGeometry(QtCore.QRect(340, 220, 441, 161))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.text_error.sizePolicy().hasHeightForWidth())
        self.text_error.setSizePolicy(sizePolicy)
        self.text_error.setObjectName("text_error")
        self.btn_open_source = QtWidgets.QPushButton(Dialog)
        self.btn_open_source.setGeometry(QtCore.QRect(710, 410, 75, 23))
        self.btn_open_source.setObjectName("btn_open_source")
        self.source_path = QtWidgets.QLineEdit(Dialog)
        self.source_path.setGeometry(QtCore.QRect(50, 410, 651, 20))
        self.source_path.setObjectName("source_path")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 410, 46, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 440, 46, 13))
        self.label_2.setObjectName("label_2")
        self.target_path = QtWidgets.QLineEdit(Dialog)
        self.target_path.setGeometry(QtCore.QRect(50, 440, 651, 20))
        self.target_path.setObjectName("target_path")
        self.btn_open_target = QtWidgets.QPushButton(Dialog)
        self.btn_open_target.setGeometry(QtCore.QRect(710, 440, 75, 23))
        self.btn_open_target.setObjectName("btn_open_target")
        self.btn_select_all = QtWidgets.QPushButton(Dialog)
        self.btn_select_all.setGeometry(QtCore.QRect(10, 380, 75, 23))
        self.btn_select_all.setObjectName("btn_select_all")
        self.btn_select_none = QtWidgets.QPushButton(Dialog)
        self.btn_select_none.setGeometry(QtCore.QRect(90, 380, 75, 23))
        self.btn_select_none.setObjectName("btn_select_none")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(340, 10, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(340, 200, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_5.setObjectName("label_5")
        self.cmb_select_type = QtWidgets.QComboBox(Dialog)
        self.cmb_select_type.setGeometry(QtCore.QRect(220, 10, 101, 22))
        self.cmb_select_type.setObjectName("cmb_select_type")
        self.cmb_select_type.addItem("")
        self.cmb_select_type.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Export Window"))
        self.btn_export.setText(_translate("Dialog", "Export"))
        self.btn_open_source.setText(_translate("Dialog", "open"))
        self.label.setText(_translate("Dialog", "Source"))
        self.label_2.setText(_translate("Dialog", "Target"))
        self.btn_open_target.setText(_translate("Dialog", "open"))
        self.btn_select_all.setText(_translate("Dialog", "Select All"))
        self.btn_select_none.setText(_translate("Dialog", "Select None"))
        self.label_3.setText(_translate("Dialog", "Information"))
        self.label_4.setText(_translate("Dialog", "Export Status"))
        self.label_5.setText(_translate("Dialog", "Available"))
        self.cmb_select_type.setItemText(0, _translate("Dialog", "Experiment"))
        self.cmb_select_type.setItemText(1, _translate("Dialog", "Device"))
