# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(866, 689)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.ResourceTab = QtWidgets.QWidget()
        self.ResourceTab.setObjectName("ResourceTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.ResourceTab)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.ResourceTab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 822, 575))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setMaximumSize(QtCore.QSize(400, 400))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/georgiana_lerner_flightsuit.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_18)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.label_16)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setObjectName("label_19")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.label_19)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.label_17)
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setObjectName("label_20")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setWordWrap(True)
        self.label_21.setObjectName("label_21")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.label_21)
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        self.label_22.setObjectName("label_22")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.label_23 = QtWidgets.QLabel(self.groupBox)
        self.label_23.setWordWrap(True)
        self.label_23.setObjectName("label_23")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_23)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.ResourceTab, "")
        self.DetailsTab = QtWidgets.QWidget()
        self.DetailsTab.setObjectName("DetailsTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.DetailsTab)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.DetailsTab)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(13)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(600)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.DetailsTab, "")
        self.NotesTab = QtWidgets.QWidget()
        self.NotesTab.setObjectName("NotesTab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.NotesTab)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.textEdit = QtWidgets.QTextEdit(self.NotesTab)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_5.addWidget(self.textEdit)
        self.tabWidget.addTab(self.NotesTab, "")
        self.VersionsTab = QtWidgets.QWidget()
        self.VersionsTab.setObjectName("VersionsTab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.VersionsTab)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.VersionsTab)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(5)
        self.tableWidget_3.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 4, item)
        self.verticalLayout_8.addWidget(self.tableWidget_3)
        self.tabWidget.addTab(self.VersionsTab, "")
        self.TrackingTab = QtWidgets.QWidget()
        self.TrackingTab.setObjectName("TrackingTab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.TrackingTab)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.TrackingTab)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 3, item)
        self.verticalLayout_6.addWidget(self.tableWidget_2)
        self.tabWidget.addTab(self.TrackingTab, "")
        self.DiscussionTab = QtWidgets.QWidget()
        self.DiscussionTab.setObjectName("DiscussionTab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.DiscussionTab)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.DiscussionTab)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/chat_example.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.scrollArea.raise_()
        self.label_4.raise_()
        self.tabWidget.addTab(self.DiscussionTab, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 866, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Resource = QtWidgets.QAction(MainWindow)
        self.actionOpen_Resource.setObjectName("actionOpen_Resource")
        self.actionCreate_Resource = QtWidgets.QAction(MainWindow)
        self.actionCreate_Resource.setObjectName("actionCreate_Resource")
        self.actionCreate_Collection = QtWidgets.QAction(MainWindow)
        self.actionCreate_Collection.setObjectName("actionCreate_Collection")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.menuFile.addAction(self.actionOpen_Resource)
        self.menuFile.addAction(self.actionCreate_Resource)
        self.menuFile.addAction(self.actionCreate_Collection)
        self.menuEdit.addAction(self.actionPreferences)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KitCAT"))
        self.groupBox.setTitle(_translate("MainWindow", "Resource Tools"))
        self.label_2.setText(_translate("MainWindow", "Original .blend file"))
        self.pushButton.setText(_translate("MainWindow", "Download"))
        self.pushButton_2.setText(_translate("MainWindow", "Upload"))
        self.pushButton_3.setText(_translate("MainWindow", "Sync"))
        self.label_3.setText(_translate("MainWindow", "Preview"))
        self.pushButton_4.setText(_translate("MainWindow", "View"))
        self.pushButton_5.setText(_translate("MainWindow", "Set"))
        self.pushButton_6.setText(_translate("MainWindow", "Sync"))
        self.label_18.setText(_translate("MainWindow", "25 September 2015"))
        self.label_11.setText(_translate("MainWindow", "Date"))
        self.label_16.setText(_translate("MainWindow", "CC By-SA 3.0"))
        self.label_8.setText(_translate("MainWindow", "License"))
        self.label_19.setText(_translate("MainWindow", "2.71"))
        self.label_10.setText(_translate("MainWindow", "Software Version"))
        self.label_9.setText(_translate("MainWindow", "Tags"))
        self.label_17.setText(_translate("MainWindow", "blender, character, model, georgiana, flightsuit"))
        self.label_20.setText(_translate("MainWindow", "Completeness"))
        self.label_21.setText(_translate("MainWindow", "Model, Topology, Materials, Preview, Shape Keys, Rigging, Actions, Animation"))
        self.label_22.setText(_translate("MainWindow", "Caption"))
        self.label_23.setText(_translate("MainWindow", "Georgiana Lerner in the Pinafore Dress (for Part 1 of the Pilot episode, \"No Children in Space)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ResourceTab), _translate("MainWindow", "Resource"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Resource ID"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Access"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Contributed By"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Credit"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "License"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Original Filename"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "Tags"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "Source"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "Named Person(s)"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "Original Sitename"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "Software Version"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "Caption"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Value"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "246"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "Open"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "Admin"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "Bela Szabo (base model), Andrew Pray (spacesuit), Daniel Fu (design), Keneisha Perry (rig, shading), Terry Hancock (textures, shading)"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "CC By-SA 3.0"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("MainWindow", "Georgiana_Flightsuit.blend"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("MainWindow", "blender, character, model, georgiana, flightsuit"))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("MainWindow", "Project Team (Original)"))
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("MainWindow", "Georgiana Lerner"))
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("MainWindow", "Lunatics Project (Original)"))
        item = self.tableWidget.item(10, 0)
        item.setText(_translate("MainWindow", "25 September 2015"))
        item = self.tableWidget.item(11, 0)
        item.setText(_translate("MainWindow", "2.71"))
        item = self.tableWidget.item(12, 0)
        item.setText(_translate("MainWindow", "Georgiana Lerner in the Pinafore Dress (for Part 1 of the Pilot episode, \"No Children in Space)"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DetailsTab), _translate("MainWindow", "Details"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fully rigged character model.<br /><br />Bela Szabo\'s character model of Georgiana in her canonical flightsuit / jumpsuit / playsuit.<br /><br />Based on modelsheets created by Daniel Fu.<br /><br />Rigging by Keneisha Perry using Nathan Vegdahl\'s Rigify script.<br /><br />Shading, Textures by Keneisha Perry and Terry Hancock.<br /><br />Art direction by Terry Hancock</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.NotesTab), _translate("MainWindow", "Notes"))
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Version"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "By"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Comment"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Ticket Refs"))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        item = self.tableWidget_3.item(0, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_3.item(0, 1)
        item.setText(_translate("MainWindow", "30/07/2017"))
        item = self.tableWidget_3.item(0, 2)
        item.setText(_translate("MainWindow", "Katrina"))
        item = self.tableWidget_3.item(0, 3)
        item.setText(_translate("MainWindow", "Fixed colors"))
        item = self.tableWidget_3.item(0, 4)
        item.setText(_translate("MainWindow", "#101"))
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.VersionsTab), _translate("MainWindow", "Versions"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ticket"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Stauts"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Assignment"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Title"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.item(0, 0)
        item.setText(_translate("MainWindow", "100"))
        item = self.tableWidget_2.item(0, 1)
        item.setText(_translate("MainWindow", "Open"))
        item = self.tableWidget_2.item(0, 2)
        item.setText(_translate("MainWindow", "Terry"))
        item = self.tableWidget_2.item(0, 3)
        item.setText(_translate("MainWindow", "Do some stuff"))
        item = self.tableWidget_2.item(1, 0)
        item.setText(_translate("MainWindow", "101"))
        item = self.tableWidget_2.item(1, 1)
        item.setText(_translate("MainWindow", "Closed"))
        item = self.tableWidget_2.item(1, 2)
        item.setText(_translate("MainWindow", "Terry"))
        item = self.tableWidget_2.item(1, 3)
        item.setText(_translate("MainWindow", "Do some other stuff"))
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TrackingTab), _translate("MainWindow", "Issue Tracking"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DiscussionTab), _translate("MainWindow", "Discussion"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionOpen_Resource.setText(_translate("MainWindow", "Open Resource"))
        self.actionCreate_Resource.setText(_translate("MainWindow", "Create Resource"))
        self.actionCreate_Collection.setText(_translate("MainWindow", "Create Collection"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))

import mainwindow_rc
