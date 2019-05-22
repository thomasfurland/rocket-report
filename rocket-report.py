# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rocket-report.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from report_writer import ReportCard

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.onPushButtonClicked)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 1200)
        MainWindow.setMinimumSize(QtCore.QSize(1600, 1200))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(10, 80, 781, 481))
        self.treeWidget.setMinimumSize(QtCore.QSize(1481, 1000))
        self.treeWidget.setMaximumSize(QtCore.QSize(781, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.treeWidget.setFont(font)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.treeWidget.headerItem().setFont(0, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setCheckState(0, QtCore.Qt.Unchecked)
        item_0.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        item_0.setExpanded(True)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        item_1.setExpanded(True)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setCheckState(0, QtCore.Qt.Unchecked)
        item_0.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        item_0.setExpanded(True)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setCheckState(0, QtCore.Qt.Unchecked)
        item_0.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        item_0.setExpanded(True)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1400, 1100, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 10, 181, 30))
        self.plainTextEdit.setMinimumSize(QtCore.QSize(181, 30))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 43, 111, 31))
        self.checkBox.setMinimumSize(QtCore.QSize(111, 31))
        self.checkBox.setObjectName("checkBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Red Cross Level 1"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Fitness Activities"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Flutter Kick 5m (Assisted)"))
        self.treeWidget.topLevelItem(0).child(0).child(0).setText(0, _translate("MainWindow", "Maintains near-horizontal body position"))
        self.treeWidget.topLevelItem(0).child(0).child(1).setText(0, _translate("MainWindow", "Kicks on front or back or uses a combination"))
        self.treeWidget.topLevelItem(0).child(0).child(2).setText(0, _translate("MainWindow", "Starts kick from hip"))
        self.treeWidget.topLevelItem(0).child(0).child(3).setText(0, _translate("MainWindow", "Moves legs in opposite up and down motion"))
        self.treeWidget.topLevelItem(0).child(0).child(4).setText(0, _translate("MainWindow", "Completes Distance"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "Distance Swim 5m"))
        self.treeWidget.topLevelItem(0).child(1).child(0).setText(0, _translate("MainWindow", "Chooses front or back swim"))
        self.treeWidget.topLevelItem(0).child(1).child(1).setText(0, _translate("MainWindow", "Uses any arm or leg movement"))
        self.treeWidget.topLevelItem(0).child(1).child(2).setText(0, _translate("MainWindow", "Focuses on proper body position and flutter kick"))
        self.treeWidget.topLevelItem(0).child(1).child(3).setText(0, _translate("MainWindow", "Body approaches horizontal on front or back"))
        self.treeWidget.topLevelItem(0).child(1).child(4).setText(0, _translate("MainWindow", "Exhales underwater"))
        self.treeWidget.topLevelItem(0).child(1).child(5).setText(0, _translate("MainWindow", "Completes distance"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "Skills and Water Safety"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "Facility/ Site Orientation"))
        self.treeWidget.topLevelItem(1).child(0).child(0).setText(0, _translate("MainWindow", "Identifies shallow water, deep water, meeting place, and hazards particular to swimming area"))
        self.treeWidget.topLevelItem(1).child(0).child(1).setText(0, _translate("MainWindow", "Waits for instructor\'s permission to enter the water"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "Supervision"))
        self.treeWidget.topLevelItem(1).child(1).child(0).setText(0, _translate("MainWindow", "Explains why adult supervision is important when in, on, and around the water"))
        self.treeWidget.topLevelItem(1).child(2).setText(0, _translate("MainWindow", "Shallow Water Entries and Exits"))
        self.treeWidget.topLevelItem(1).child(2).child(0).setText(0, _translate("MainWindow", "Makes sure an adult (Instructor) is already in the water and ready"))
        self.treeWidget.topLevelItem(1).child(2).child(1).setText(0, _translate("MainWindow", "Performs shallow water entries and exits, appropriate to the facility/ site, eg., wading in, using ramp, stepping off ladder, jumping in, slipping in from seated position at water level"))
        self.treeWidget.topLevelItem(1).child(2).child(2).setText(0, _translate("MainWindow", "Demonstrates safe exits"))
        self.treeWidget.topLevelItem(1).child(3).setText(0, _translate("MainWindow", "Submerge Head"))
        self.treeWidget.topLevelItem(1).child(3).child(0).setText(0, _translate("MainWindow", "Puts entire head in the water for at least 3 seconds"))
        self.treeWidget.topLevelItem(1).child(3).child(1).setText(0, _translate("MainWindow", "Opens eyes underwater"))
        self.treeWidget.topLevelItem(1).child(4).setText(0, _translate("MainWindow", "Exhale Through Mouth and/or Nose"))
        self.treeWidget.topLevelItem(1).child(4).child(0).setText(0, _translate("MainWindow", "Exhales/ blows bubbles through mouth and/ or nose, just below the surface"))
        self.treeWidget.topLevelItem(1).child(4).child(1).setText(0, _translate("MainWindow", "Exhales through mouth and/ or nose with entire head in the water"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "Swimming"))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "Rhythmic Breathing 5 Times"))
        self.treeWidget.topLevelItem(2).child(0).child(0).setText(0, _translate("MainWindow", "Exhales through mouth and/ or nose underwater and inhales through mouth just above surface"))
        self.treeWidget.topLevelItem(2).child(0).child(1).setText(0, _translate("MainWindow", "Performs rhythmic and relaxed breathing with noticable and effective exhalation and inhalation on EACH repetition"))
        self.treeWidget.topLevelItem(2).child(0).child(2).setText(0, _translate("MainWindow", "Performs at least 5 repetitions in any body position"))
        self.treeWidget.topLevelItem(2).child(1).setText(0, _translate("MainWindow", "Front Float and Recovery 3 Sec"))
        self.treeWidget.topLevelItem(2).child(1).child(0).setText(0, _translate("MainWindow", "Assumes stable floating position on front with face in water"))
        self.treeWidget.topLevelItem(2).child(1).child(1).setText(0, _translate("MainWindow", "Floats for at least 3 seconds, in a relaxed manner"))
        self.treeWidget.topLevelItem(2).child(1).child(2).setText(0, _translate("MainWindow", "Comfortably recovers to a vertical position"))
        self.treeWidget.topLevelItem(2).child(2).setText(0, _translate("MainWindow", "Front Glide 5 Sec"))
        self.treeWidget.topLevelItem(2).child(2).child(0).setText(0, _translate("MainWindow", "Glides on front for at least 5 seconds with face in water, in a relaxed manner"))
        self.treeWidget.topLevelItem(2).child(2).child(1).setText(0, _translate("MainWindow", "Maintains streamlined body position, with arms fully extended in front of head"))
        self.treeWidget.topLevelItem(2).child(2).child(2).setText(0, _translate("MainWindow", "Comfortably recovers to vertical position"))
        self.treeWidget.topLevelItem(2).child(3).setText(0, _translate("MainWindow", "Front Glide with Kick 5m"))
        self.treeWidget.topLevelItem(2).child(3).child(0).setText(0, _translate("MainWindow", "Performs front glide with basic flutter kick: opposite up and down leg motions"))
        self.treeWidget.topLevelItem(2).child(3).child(1).setText(0, _translate("MainWindow", "Performs kick for at least 5m, with body approaching horizontal"))
        self.treeWidget.topLevelItem(2).child(3).child(2).setText(0, _translate("MainWindow", "Fully extends arms over head; maintains streamlined body position"))
        self.treeWidget.topLevelItem(2).child(3).child(3).setText(0, _translate("MainWindow", "Exhales underwater"))
        self.treeWidget.topLevelItem(2).child(4).setText(0, _translate("MainWindow", "Back Float and Recovery 3 Sec"))
        self.treeWidget.topLevelItem(2).child(4).child(0).setText(0, _translate("MainWindow", "Assumes stable floating position on back, ears in the water"))
        self.treeWidget.topLevelItem(2).child(4).child(1).setText(0, _translate("MainWindow", "Floats for at least 3 seconds, in a relaxed manner"))
        self.treeWidget.topLevelItem(2).child(4).child(2).setText(0, _translate("MainWindow", "Comfortably recovers to vertical position"))
        self.treeWidget.topLevelItem(2).child(5).setText(0, _translate("MainWindow", "Back Glide 5 Sec"))
        self.treeWidget.topLevelItem(2).child(5).child(0).setText(0, _translate("MainWindow", "Glides on back for at least 5 seconds, in a relaxed manner"))
        self.treeWidget.topLevelItem(2).child(5).child(1).setText(0, _translate("MainWindow", "Maintains streamlined body position with arms and hands resting along side of body"))
        self.treeWidget.topLevelItem(2).child(5).child(2).setText(0, _translate("MainWindow", "Comfortably recovers to vertical position"))
        self.treeWidget.topLevelItem(2).child(6).setText(0, _translate("MainWindow", "Roll-over Glide 5 Sec (Assisted)"))
        self.treeWidget.topLevelItem(2).child(6).child(0).setText(0, _translate("MainWindow", "Glides on front with face in water, then rolls over to back and glides (or floats)"))
        self.treeWidget.topLevelItem(2).child(6).child(1).setText(0, _translate("MainWindow", "Exhales through mouth and/ or nose when face is in water and inhales through mouth when face is out"))
        self.treeWidget.topLevelItem(2).child(6).child(2).setText(0, _translate("MainWindow", "Repeats back to front glide"))
        self.treeWidget.topLevelItem(2).child(6).child(3).setText(0, _translate("MainWindow", "Glides in streamlined and relaxed manner"))
        self.treeWidget.topLevelItem(2).child(6).child(4).setText(0, _translate("MainWindow", "Starts roll with head and shoulders"))
        self.treeWidget.topLevelItem(2).child(6).child(5).setText(0, _translate("MainWindow", "Comfortably recovers to vertical position"))
        self.treeWidget.topLevelItem(2).child(7).setText(0, _translate("MainWindow", "Front Swim 5m"))
        self.treeWidget.topLevelItem(2).child(7).child(0).setText(0, _translate("MainWindow", "Swims 5m using any arm or leg movement or combination of movement"))
        self.treeWidget.topLevelItem(2).child(7).child(1).setText(0, _translate("MainWindow", "Completes Distance"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "Continue"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Student Name"))
        self.checkBox.setText(_translate("MainWindow", "Level Completed"))

    def onPushButtonClicked(self):
        fit = self.treeWidget.topLevelItem(0)
        safe = self.treeWidget.topLevelItem(1)
        swim = self.treeWidget.topLevelItem(2)
        evaluation = {
            "level" : "level1",
            "date": "2019-04-08",
            "instructor": "Thomas",
            "classNumber": "4485362",
            "student": self.plainTextEdit.toPlainText(),
            "completed": self.checkBox.checkState(),
            "skills" : {
                "fitness": {
                    "flutter_kick_5m_assisted" : {
                        "horizontal_body_position" : fit.child(0).child(0).checkState(0),
                        "front_or_back_kick" : fit.child(0).child(1).checkState(0),
                        "kick_from_hip" : fit.child(0).child(2).checkState(0),
                        "vertical_leg_motion" : fit.child(0).child(3).checkState(0),
                        "completed_distance" : fit.child(0).child(4).checkState(0)
                    },
                    "distance_swim_5m" : {
                        "front_or_back_swim" : fit.child(0).child(0).checkState(0),
                        "arm_leg_movement" : fit.child(0).child(0).checkState(0),
                        "body_position_w_flutter_kick" : fit.child(0).child(0).checkState(0),
                        "horizontal_body_position" : fit.child(0).child(0).checkState(0),
                        "exhale_underwater" : fit.child(0).child(0).checkState(0),
                        "completed_distance" : fit.child(0).child(0).checkState(0)
                    }
                },
                "safety": {
                    "facility_site_orientation" : {
                        "identifies_safety_and_hazards" : safe.child(0).child(0).checkState(0),
                        "waits_for_instructor" : safe.child(0).child(1).checkState(0)
                    },
                    "supervision" : {
                        "explains_supervision" : safe.child(1).child(0).checkState(0)
                    },
                    "shallow_entries_exits" : {
                        "waits_for_instructor" : safe.child(2).child(0).checkState(0),
                        "performs_safe_entries_exits" : safe.child(1).child(0).checkState(0),
                        "performs_safe_exits" :safe.child(2).child(2).checkState(0)
                    },
                    "submerge_head" : {
                        "head_underwater_3sec" : safe.child(3).child(0).checkState(0),
                        "eyes_open_underwater" : safe.child(3).child(1).checkState(0)
                    },
                    "exhale_through_mouth_nose" : {
                        "exhale_below_surface" : safe.child(4).child(0).checkState(0),
                        "exhale_w_head_underwater" : safe.child(4).child(1).checkState(0)
                    }
                },
                "swimming" : {
                    "rhythmic_breathing_5_times" : {
                        "exhale_underwater_inhale_air" : swim.child(0).child(0).checkState(0),
                        "rhythmic_relaxed" : swim.child(0).child(1).checkState(0),
                        "5_repetitions" : swim.child(0).child(2).checkState(0)
                    },
                    "front_float_recovery_3sec" : {
                        "stable_face_in_water" : swim.child(1).child(0).checkState(0),
                        "float_3sec_relaxed" : swim.child(1).child(1).checkState(0),
                        "vertical_recovery" : swim.child(1).child(2).checkState(0)
                    },
                    "front_glide_5sec" : {
                        "glide_5sec_relaxed" : swim.child(2).child(0).checkState(0),
                        "streamlined_body_position" : swim.child(2).child(1).checkState(0),
                        "vertical_recovery" : swim.child(2).child(2).checkState(0)
                    },
                    "front_glide_kick_5m" : {
                        "vertical_leg_motion" : swim.child(3).child(0).checkState(0),
                        "kicks_5m_horizontal_body" : swim.child(3).child(1).checkState(0),
                        "streamlined_body_position" : swim.child(3).child(2).checkState(0),
                        "exhale_underwater" :swim.child(3).child(3).checkState(0)
                    },
                    "back_float_recovery_3sec" : {
                        "stable_back_float" : swim.child(4).child(0).checkState(0),
                        "float_3sec_relaxed" : swim.child(4).child(1).checkState(0),
                        "vertical_recovery" : swim.child(4).child(2).checkState(0)
                    },
                    "back_glide_5sec" : {
                        "glide_5sec_relaxed" : swim.child(5).child(0).checkState(0),
                        "streamlined_body_position" : swim.child(5).child(1).checkState(0),
                        "vertical_recovery" : swim.child(5).child(2).checkState(0)
                    },
                    "rollover_glide_5sec_assisted" : {
                        "rolls_front_to_back" : swim.child(6).child(0).checkState(0),
                        "exhale_underwater_inhale_air" : swim.child(6).child(1).checkState(0),
                        "rolls_back_to_front" : swim.child(6).child(2).checkState(0),
                        "streamlined_body_position" : swim.child(6).child(3).checkState(0),
                        "starts_roll_head_shoulders" : swim.child(6).child(4).checkState(0),
                        "vertical_recovery" : swim.child(6).child(5).checkState(0)
                    },
                    "front_swim_5m" : {
                        "arm_leg_movement" : swim.child(7).child(0).checkState(0),
                        "completed_distance" : swim.child(7).child(1).checkState(0)
                    }
                }
            }
        }
        reportcard = ReportCard(evaluation, 'test.db')
        output = "".join(reportcard.build())
        self.dialog = Support(output)
        self.dialog.show()

class Support(QtWidgets.QDialog):
    def __init__(self, text_in):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.text_setter(text_in)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(402, 557)
        Dialog.setMinimumSize(QtCore.QSize(402, 557))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.NoRole, brush)
        Dialog.setPalette(palette)
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(False)
        self.checkBoxComplete = QtWidgets.QCheckBox(Dialog)
        self.checkBoxComplete.setEnabled(True)
        self.checkBoxComplete.setGeometry(QtCore.QRect(270, 480, 91, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBoxComplete.setFont(font)
        self.checkBoxComplete.setCheckable(True)
        self.checkBoxComplete.setObjectName("checkBoxComplete")
        self.checkBoxIncomplete = QtWidgets.QCheckBox(Dialog)
        self.checkBoxIncomplete.setEnabled(True)
        self.checkBoxIncomplete.setGeometry(QtCore.QRect(270, 510, 91, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBoxIncomplete.setFont(font)
        self.checkBoxIncomplete.setObjectName("checkBoxIncomplete")
        self.textEditComment = QtWidgets.QTextEdit(Dialog)
        self.textEditComment.setGeometry(QtCore.QRect(30, 160, 341, 281))
        self.textEditComment.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textEditComment.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEditComment.setObjectName("textEditComment")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 20, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(7)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(210, 20, 161, 61))
        self.textEdit_3.setAutoFillBackground(False)
        self.textEdit_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_4.setGeometry(QtCore.QRect(30, 130, 341, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEditDate = QtWidgets.QTextEdit(Dialog)
        self.textEditDate.setGeometry(QtCore.QRect(210, 450, 161, 31))
        self.textEditDate.setObjectName("textEditDate")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 540, 381, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 7, 20, 542))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(370, 7, 41, 541))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(10, 0, 381, 16))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.textEditNextLevel = QtWidgets.QTextEdit(Dialog)
        self.textEditNextLevel.setGeometry(QtCore.QRect(30, 500, 221, 31))
        self.textEditNextLevel.setObjectName("textEditNextLevel")
        self.textEditInstructor = QtWidgets.QTextEdit(Dialog)
        self.textEditInstructor.setGeometry(QtCore.QRect(30, 450, 171, 31))
        self.textEditInstructor.setObjectName("textEditInstructor")
        self.textEditCurrentLevel = QtWidgets.QTextEdit(Dialog)
        self.textEditCurrentLevel.setGeometry(QtCore.QRect(30, 90, 171, 31))
        self.textEditCurrentLevel.setObjectName("textEditCurrentLevel")
        self.textEdit_Barcode = QtWidgets.QTextEdit(Dialog)
        self.textEdit_Barcode.setGeometry(QtCore.QRect(210, 90, 161, 31))
        self.textEdit_Barcode.setObjectName("textEdit_Barcode")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.checkBoxComplete.setText(_translate("Dialog", "Complete"))
        self.checkBoxIncomplete.setText(_translate("Dialog", "Incomplete"))
        self.textEdit_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe MDL2 Assets\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">* Please</span><span style=\" font-family:\'MS Shell Dlg 2\'; text-decoration: underline;\"> bring this report card back</span><span style=\" font-family:\'MS Shell Dlg 2\';\"> to the next instructor at the beginning of your next lesson set.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Thank you!</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#000000;\">Rocket Report</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Successes and Challenges:</span></p></body></html>"))
        self.textEditDate.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Date:</span></p></body></html>"))
        self.textEditNextLevel.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Please register in level: </span></p></body></html>"))
        self.textEditInstructor.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Instructor: </span></p></body></html>"))
        self.textEditCurrentLevel.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Level: </span></p></body></html>"))
        self.textEdit_Barcode.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Barcode: </span></p></body></html>"))

    def text_setter(self, text):
        self.textEditComment.setText(text)

        
if __name__ == '__main__':
    APP = QtWidgets.QApplication(sys.argv)
    WIDGET = Ui_MainWindow()
    WIDGET.show()
    sys.exit(APP.exec_())