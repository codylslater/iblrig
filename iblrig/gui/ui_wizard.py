# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_wizard.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wizard(object):
    def setupUi(self, wizard):
        wizard.setObjectName("wizard")
        wizard.resize(517, 973)
        self.centralwidget = QtWidgets.QWidget(wizard)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setEnabled(False)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.uiPushHelp_2 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiPushHelp_2.sizePolicy().hasHeightForWidth())
        self.uiPushHelp_2.setSizePolicy(sizePolicy)
        self.uiPushHelp_2.setObjectName("uiPushHelp_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.uiPushHelp_2)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.uiGroupDiskSpace = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiGroupDiskSpace.sizePolicy().hasHeightForWidth())
        self.uiGroupDiskSpace.setSizePolicy(sizePolicy)
        self.uiGroupDiskSpace.setObjectName("uiGroupDiskSpace")
        self.formLayout_7 = QtWidgets.QFormLayout(self.uiGroupDiskSpace)
        self.formLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout_7.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_7.setSpacing(6)
        self.formLayout_7.setObjectName("formLayout_7")
        self.uiLableDiskIblrig_2 = QtWidgets.QLabel(self.uiGroupDiskSpace)
        self.uiLableDiskIblrig_2.setObjectName("uiLableDiskIblrig_2")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.uiLableDiskIblrig_2)
        self.uiLableDiskIblrigValue_2 = QtWidgets.QLabel(self.uiGroupDiskSpace)
        self.uiLableDiskIblrigValue_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.uiLableDiskIblrigValue_2.setObjectName("uiLableDiskIblrigValue_2")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.uiLableDiskIblrigValue_2)
        self.uiLableDiskAvailable_2 = QtWidgets.QLabel(self.uiGroupDiskSpace)
        self.uiLableDiskAvailable_2.setObjectName("uiLableDiskAvailable_2")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.uiLableDiskAvailable_2)
        self.uiLableDiskAvailableValue_2 = QtWidgets.QLabel(self.uiGroupDiskSpace)
        self.uiLableDiskAvailableValue_2.setTextFormat(QtCore.Qt.AutoText)
        self.uiLableDiskAvailableValue_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.uiLableDiskAvailableValue_2.setObjectName("uiLableDiskAvailableValue_2")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.uiLableDiskAvailableValue_2)
        self.uiProgressDiskSpace_2 = QtWidgets.QProgressBar(self.uiGroupDiskSpace)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiProgressDiskSpace_2.sizePolicy().hasHeightForWidth())
        self.uiProgressDiskSpace_2.setSizePolicy(sizePolicy)
        self.uiProgressDiskSpace_2.setStatusTip("")
        self.uiProgressDiskSpace_2.setProperty("value", 24)
        self.uiProgressDiskSpace_2.setInvertedAppearance(False)
        self.uiProgressDiskSpace_2.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.uiProgressDiskSpace_2.setObjectName("uiProgressDiskSpace_2")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.uiProgressDiskSpace_2)
        self.gridLayout.addWidget(self.uiGroupDiskSpace, 1, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 2)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setRowStretch(0, 1)
        wizard.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(wizard)
        self.statusbar.setObjectName("statusbar")
        wizard.setStatusBar(self.statusbar)

        self.retranslateUi(wizard)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wizard)

    def retranslateUi(self, wizard):
        _translate = QtCore.QCoreApplication.translate
        wizard.setWindowTitle(_translate("wizard", "MainWindow"))
        self.groupBox.setTitle(_translate("wizard", "Support"))
        self.label_2.setText(_translate("wizard", "Rig Name:"))
        self.label.setText(_translate("wizard", "AnyDesk ID:"))
        self.label_4.setText(_translate("wizard", "0 000 000 000"))
        self.uiPushHelp_2.setStatusTip(_translate("wizard", "open the iblrig documentation in your browser"))
        self.uiPushHelp_2.setText(_translate("wizard", "Open Documentation"))
        self.uiGroupDiskSpace.setTitle(_translate("wizard", "Disk Usage"))
        self.uiLableDiskIblrig_2.setText(_translate("wizard", "IBL Rig Data:"))
        self.uiLableDiskIblrigValue_2.setText(_translate("wizard", "1.2 GB"))
        self.uiLableDiskAvailable_2.setText(_translate("wizard", "Available Space:"))
        self.uiLableDiskAvailableValue_2.setText(_translate("wizard", "80.3 GB"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("wizard", "Behavior"))
