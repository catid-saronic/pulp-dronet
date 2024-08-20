# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'datasetcollector.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1656, 730)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.disconnectWifiButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disconnectWifiButton.sizePolicy().hasHeightForWidth())
        self.disconnectWifiButton.setSizePolicy(sizePolicy)
        self.disconnectWifiButton.setObjectName("disconnectWifiButton")
        self.gridLayout.addWidget(self.disconnectWifiButton, 0, 6, 1, 1)
        self.portLabel = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portLabel.sizePolicy().hasHeightForWidth())
        self.portLabel.setSizePolicy(sizePolicy)
        self.portLabel.setObjectName("portLabel")
        self.gridLayout.addWidget(self.portLabel, 0, 2, 1, 1)
        self.imageInfoLabel = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageInfoLabel.sizePolicy().hasHeightForWidth())
        self.imageInfoLabel.setSizePolicy(sizePolicy)
        self.imageInfoLabel.setAutoFillBackground(False)
        self.imageInfoLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imageInfoLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imageInfoLabel.setLineWidth(2)
        self.imageInfoLabel.setText("")
        self.imageInfoLabel.setObjectName("imageInfoLabel")
        self.gridLayout.addWidget(self.imageInfoLabel, 2, 0, 1, 8)
        self.ipAddressLineEdit = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ipAddressLineEdit.sizePolicy().hasHeightForWidth())
        self.ipAddressLineEdit.setSizePolicy(sizePolicy)
        self.ipAddressLineEdit.setObjectName("ipAddressLineEdit")
        self.gridLayout.addWidget(self.ipAddressLineEdit, 0, 1, 1, 1)
        self.portSpinBox = QtWidgets.QSpinBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portSpinBox.sizePolicy().hasHeightForWidth())
        self.portSpinBox.setSizePolicy(sizePolicy)
        self.portSpinBox.setMaximum(65535)
        self.portSpinBox.setProperty("value", 5000)
        self.portSpinBox.setObjectName("portSpinBox")
        self.gridLayout.addWidget(self.portSpinBox, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.connectWifiButton = QtWidgets.QPushButton(self.frame)
        self.connectWifiButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectWifiButton.sizePolicy().hasHeightForWidth())
        self.connectWifiButton.setSizePolicy(sizePolicy)
        self.connectWifiButton.setObjectName("connectWifiButton")
        self.gridLayout.addWidget(self.connectWifiButton, 0, 5, 1, 1)
        self.cameraLabel = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.cameraLabel.sizePolicy().hasHeightForWidth())
        self.cameraLabel.setSizePolicy(sizePolicy)
        self.cameraLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.cameraLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cameraLabel.setLineWidth(2)
        self.cameraLabel.setMidLineWidth(0)
        self.cameraLabel.setText("")
        self.cameraLabel.setScaledContents(True)
        self.cameraLabel.setObjectName("cameraLabel")
        self.gridLayout.addWidget(self.cameraLabel, 1, 0, 1, 8)
        self.ipAddressLabel = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ipAddressLabel.sizePolicy().hasHeightForWidth())
        self.ipAddressLabel.setSizePolicy(sizePolicy)
        self.ipAddressLabel.setObjectName("ipAddressLabel")
        self.gridLayout.addWidget(self.ipAddressLabel, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.connectButton = QtWidgets.QPushButton(self.frame_2)
        self.connectButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectButton.sizePolicy().hasHeightForWidth())
        self.connectButton.setSizePolicy(sizePolicy)
        self.connectButton.setObjectName("connectButton")
        self.gridLayout_2.addWidget(self.connectButton, 0, 2, 1, 1)
        self.configLogButton = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.configLogButton.sizePolicy().hasHeightForWidth())
        self.configLogButton.setSizePolicy(sizePolicy)
        self.configLogButton.setObjectName("configLogButton")
        self.gridLayout_2.addWidget(self.configLogButton, 4, 3, 1, 1)
        self.disconnectButton = QtWidgets.QPushButton(self.frame_2)
        self.disconnectButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disconnectButton.sizePolicy().hasHeightForWidth())
        self.disconnectButton.setSizePolicy(sizePolicy)
        self.disconnectButton.setObjectName("disconnectButton")
        self.gridLayout_2.addWidget(self.disconnectButton, 0, 3, 1, 1)
        self.batteryLevelBar = QtWidgets.QProgressBar(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batteryLevelBar.sizePolicy().hasHeightForWidth())
        self.batteryLevelBar.setSizePolicy(sizePolicy)
        self.batteryLevelBar.setProperty("value", 24)
        self.batteryLevelBar.setObjectName("batteryLevelBar")
        self.gridLayout_2.addWidget(self.batteryLevelBar, 0, 4, 1, 1)
        self.loggingButton = QtWidgets.QPushButton(self.frame_2)
        self.loggingButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loggingButton.sizePolicy().hasHeightForWidth())
        self.loggingButton.setSizePolicy(sizePolicy)
        self.loggingButton.setObjectName("loggingButton")
        self.gridLayout_2.addWidget(self.loggingButton, 4, 4, 1, 1)
        self.scanButton = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scanButton.sizePolicy().hasHeightForWidth())
        self.scanButton.setSizePolicy(sizePolicy)
        self.scanButton.setObjectName("scanButton")
        self.gridLayout_2.addWidget(self.scanButton, 0, 1, 1, 1)
        self.selectDeviceBox = QtWidgets.QComboBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectDeviceBox.sizePolicy().hasHeightForWidth())
        self.selectDeviceBox.setSizePolicy(sizePolicy)
        self.selectDeviceBox.setObjectName("selectDeviceBox")
        self.gridLayout_2.addWidget(self.selectDeviceBox, 0, 0, 1, 1)
        self.logDataPlot = PlotWidget(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logDataPlot.sizePolicy().hasHeightForWidth())
        self.logDataPlot.setSizePolicy(sizePolicy)
        self.logDataPlot.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logDataPlot.setFrameShadow(QtWidgets.QFrame.Plain)
        self.logDataPlot.setLineWidth(1)
        self.logDataPlot.setMidLineWidth(0)
        self.logDataPlot.setSceneRect(QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.logDataPlot.setObjectName("logDataPlot")
        self.gridLayout_2.addWidget(self.logDataPlot, 3, 0, 1, 5)
        self.controllerComboBox = QtWidgets.QComboBox(self.frame_2)
        self.controllerComboBox.setObjectName("controllerComboBox")
        self.gridLayout_2.addWidget(self.controllerComboBox, 4, 0, 1, 1)
        self.mapControlsButton = QtWidgets.QPushButton(self.frame_2)
        self.mapControlsButton.setObjectName("mapControlsButton")
        self.gridLayout_2.addWidget(self.mapControlsButton, 4, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1656, 24))
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
        self.disconnectWifiButton.setText(_translate("MainWindow", "Disconnect"))
        self.portLabel.setText(_translate("MainWindow", "Port:"))
        self.ipAddressLineEdit.setInputMask(_translate("MainWindow", "000.000.000.000"))
        self.ipAddressLineEdit.setText(_translate("MainWindow", "192.168.4.1"))
        self.connectWifiButton.setText(_translate("MainWindow", "Connect"))
        self.ipAddressLabel.setText(_translate("MainWindow", "IP Address:"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))
        self.configLogButton.setText(_translate("MainWindow", "Configure"))
        self.disconnectButton.setText(_translate("MainWindow", "Disconnect"))
        self.loggingButton.setText(_translate("MainWindow", "Log"))
        self.scanButton.setText(_translate("MainWindow", "Scan"))
        self.mapControlsButton.setText(_translate("MainWindow", "Map controls"))
from pyqtgraph import PlotWidget