# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'iblrig/gui/ui_micromanipulator.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(869, 443)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/iblrig_logo"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.uiLine_phi = QtWidgets.QLineEdit(self.centralwidget)
        self.uiLine_phi.setObjectName("uiLine_phi")
        self.gridLayout.addWidget(self.uiLine_phi, 1, 5, 1, 1)
        self.uiLine_y = QtWidgets.QLineEdit(self.centralwidget)
        self.uiLine_y.setObjectName("uiLine_y")
        self.gridLayout.addWidget(self.uiLine_y, 1, 1, 1, 1)
        self.uiLine_depth = QtWidgets.QLineEdit(self.centralwidget)
        self.uiLine_depth.setObjectName("uiLine_depth")
        self.gridLayout.addWidget(self.uiLine_depth, 1, 3, 1, 1)
        self.uiLine_theta = QtWidgets.QLineEdit(self.centralwidget)
        self.uiLine_theta.setObjectName("uiLine_theta")
        self.gridLayout.addWidget(self.uiLine_theta, 1, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 5, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.uiLine_z = QtWidgets.QLineEdit(self.centralwidget)
        self.uiLine_z.setObjectName("uiLine_z")
        self.gridLayout.addWidget(self.uiLine_z, 1, 2, 1, 1)
        self.uiPush_submit = QtWidgets.QPushButton(self.centralwidget)
        self.uiPush_submit.setObjectName("uiPush_submit")
        self.gridLayout.addWidget(self.uiPush_submit, 4, 5, 1, 1)
        self.uiPush_np24 = QtWidgets.QPushButton(self.centralwidget)
        self.uiPush_np24.setObjectName("uiPush_np24")
        self.gridLayout.addWidget(self.uiPush_np24, 4, 3, 1, 1)
        self.uiPush_show = QtWidgets.QPushButton(self.centralwidget)
        self.uiPush_show.setObjectName("uiPush_show")
        self.gridLayout.addWidget(self.uiPush_show, 4, 4, 1, 1)
        self.uiLine_x = QtWidgets.QLineEdit(self.centralwidget)
        self.uiLine_x.setObjectName("uiLine_x")
        self.gridLayout.addWidget(self.uiLine_x, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.uiMpl = MplWidget(self.centralwidget)
        self.uiMpl.setObjectName("uiMpl")
        self.gridLayout.addWidget(self.uiMpl, 3, 0, 1, 6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 869, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Micro-Manipulator coordinates"))
        self.label_5.setText(_translate("MainWindow", "THETA (degrees)"))
        self.label.setText(_translate("MainWindow", "X-ML (UM)"))
        self.label_6.setText(_translate("MainWindow", "PHI (degrees)"))
        self.label_3.setText(_translate("MainWindow", "Z-DV (UM)"))
        self.label_2.setText(_translate("MainWindow", "Y-AP (UM)"))
        self.uiPush_submit.setText(_translate("MainWindow", "Submit"))
        self.uiPush_np24.setText(_translate("MainWindow", "NP2.4 compute"))
        self.uiPush_show.setText(_translate("MainWindow", "Show location"))
        self.label_4.setText(_translate("MainWindow", "DEPTH (UM)"))
from iblrig.gui.micromanipulator import MplWidget
from iblrig.gui import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
