# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projectUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(786, 701)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 481, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.programLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.programLayout.setContentsMargins(0, 0, 0, 0)
        self.programLayout.setObjectName("programLayout")
        self.helpBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.helpBtn.setObjectName("helpBtn")
        self.programLayout.addWidget(self.helpBtn, 1, 0, 1, 1)
        self.IOLayout = QtWidgets.QHBoxLayout()
        self.IOLayout.setObjectName("IOLayout")
        self.outputLayout = QtWidgets.QVBoxLayout()
        self.outputLayout.setObjectName("outputLayout")
        self.nameLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.nameLabel.setObjectName("nameLabel")
        self.outputLayout.addWidget(self.nameLabel)
        self.nameEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.nameEdit.setInputMask("")
        self.nameEdit.setText("")
        self.nameEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.nameEdit.setPlaceholderText("")
        self.nameEdit.setObjectName("nameEdit")
        self.outputLayout.addWidget(self.nameEdit)
        self.saveBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.saveBtn.setObjectName("saveBtn")
        self.outputLayout.addWidget(self.saveBtn)
        self.IOLayout.addLayout(self.outputLayout)
        self.inputLayout = QtWidgets.QVBoxLayout()
        self.inputLayout.setObjectName("inputLayout")
        self.inpLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.inpLabel.setObjectName("inpLabel")
        self.inputLayout.addWidget(self.inpLabel)
        self.allSelectorLayout = QtWidgets.QHBoxLayout()
        self.allSelectorLayout.setObjectName("allSelectorLayout")
        self.filesLayout = QtWidgets.QVBoxLayout()
        self.filesLayout.setObjectName("filesLayout")
        self.csvFileBtn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.csvFileBtn.setObjectName("csvFileBtn")
        self.fileSelect = QtWidgets.QButtonGroup(mainWindow)
        self.fileSelect.setObjectName("fileSelect")
        self.fileSelect.addButton(self.csvFileBtn)
        self.filesLayout.addWidget(self.csvFileBtn)
        self.txtFileBtn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.txtFileBtn.setObjectName("txtFileBtn")
        self.fileSelect.addButton(self.txtFileBtn)
        self.filesLayout.addWidget(self.txtFileBtn)
        self.allSelectorLayout.addLayout(self.filesLayout)
        self.selectorLayout = QtWidgets.QVBoxLayout()
        self.selectorLayout.setObjectName("selectorLayout")
        self.csvInput = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.csvInput.setEnabled(False)
        self.csvInput.setObjectName("csvInput")
        self.selectorLayout.addWidget(self.csvInput)
        self.txtInput = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.txtInput.setEnabled(False)
        self.txtInput.setObjectName("txtInput")
        self.selectorLayout.addWidget(self.txtInput)
        self.allSelectorLayout.addLayout(self.selectorLayout)
        self.inputLayout.addLayout(self.allSelectorLayout)
        self.IOLayout.addLayout(self.inputLayout)
        self.programLayout.addLayout(self.IOLayout, 0, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Сбор статистических данных"))
        self.helpBtn.setText(_translate("mainWindow", "Помощь"))
        self.nameLabel.setText(_translate("mainWindow", "Введите имя файла:"))
        self.saveBtn.setText(_translate("mainWindow", "Сохранить"))
        self.inpLabel.setText(_translate("mainWindow", "Выберите формат ввода:"))
        self.csvFileBtn.setText(_translate("mainWindow", "Файл формата .csv"))
        self.txtFileBtn.setText(_translate("mainWindow", "Файл формата .txt"))
        self.csvInput.setText(_translate("mainWindow", "Выберите файл .csv"))
        self.txtInput.setText(_translate("mainWindow", "Выберите файл .txt"))
