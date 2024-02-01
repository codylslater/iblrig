# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'iblrig\gui\ui_frame2ttl.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frame2ttl(object):
    def setupUi(self, frame2ttl):
        frame2ttl.setObjectName("frame2ttl")
        frame2ttl.resize(200, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frame2ttl.sizePolicy().hasHeightForWidth())
        frame2ttl.setSizePolicy(sizePolicy)
        frame2ttl.setMinimumSize(QtCore.QSize(200, 200))
        frame2ttl.setMaximumSize(QtCore.QSize(200, 200))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(frame2ttl)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.uiLabelLight = QtWidgets.QLabel(frame2ttl)
        self.uiLabelLight.setObjectName("uiLabelLight")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.uiLabelLight)
        self.uiLabelDark = QtWidgets.QLabel(frame2ttl)
        self.uiLabelDark.setObjectName("uiLabelDark")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.uiLabelDark)
        self.uiLabelHardware = QtWidgets.QLabel(frame2ttl)
        self.uiLabelHardware.setObjectName("uiLabelHardware")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.uiLabelHardware)
        self.uiLabelFirmware = QtWidgets.QLabel(frame2ttl)
        self.uiLabelFirmware.setObjectName("uiLabelFirmware")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.uiLabelFirmware)
        self.uiLabelPort = QtWidgets.QLabel(frame2ttl)
        self.uiLabelPort.setObjectName("uiLabelPort")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.uiLabelPort)
        self.uiLabelPortValue = QtWidgets.QLabel(frame2ttl)
        self.uiLabelPortValue.setText("")
        self.uiLabelPortValue.setObjectName("uiLabelPortValue")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.uiLabelPortValue)
        self.uiLabelHardwareValue = QtWidgets.QLabel(frame2ttl)
        self.uiLabelHardwareValue.setText("")
        self.uiLabelHardwareValue.setObjectName("uiLabelHardwareValue")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.uiLabelHardwareValue)
        self.uiLabelFirmwareValue = QtWidgets.QLabel(frame2ttl)
        self.uiLabelFirmwareValue.setText("")
        self.uiLabelFirmwareValue.setObjectName("uiLabelFirmwareValue")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.uiLabelFirmwareValue)
        self.uiLabelLightValue = QtWidgets.QLabel(frame2ttl)
        self.uiLabelLightValue.setText("")
        self.uiLabelLightValue.setObjectName("uiLabelLightValue")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.uiLabelLightValue)
        self.uiLabelDarkValue = QtWidgets.QLabel(frame2ttl)
        self.uiLabelDarkValue.setText("")
        self.uiLabelDarkValue.setObjectName("uiLabelDarkValue")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.uiLabelDarkValue)
        self.verticalLayout_2.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.uiLabelResult = QtWidgets.QLabel(frame2ttl)
        self.uiLabelResult.setText("")
        self.uiLabelResult.setObjectName("uiLabelResult")
        self.verticalLayout_2.addWidget(self.uiLabelResult)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(frame2ttl)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(frame2ttl)
        self.buttonBox.accepted.connect(frame2ttl.accept) # type: ignore
        self.buttonBox.rejected.connect(frame2ttl.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(frame2ttl)

    def retranslateUi(self, frame2ttl):
        _translate = QtCore.QCoreApplication.translate
        frame2ttl.setWindowTitle(_translate("frame2ttl", "Frame2TTL Calibration"))
        self.uiLabelLight.setText(_translate("frame2ttl", "Light Threshold:"))
        self.uiLabelDark.setText(_translate("frame2ttl", "Dark Threshold:"))
        self.uiLabelHardware.setText(_translate("frame2ttl", "Hardware Revision:"))
        self.uiLabelFirmware.setText(_translate("frame2ttl", "Firmware Version:"))
        self.uiLabelPort.setText(_translate("frame2ttl", "Serial Port:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frame2ttl = QtWidgets.QDialog()
    ui = Ui_frame2ttl()
    ui.setupUi(frame2ttl)
    frame2ttl.show()
    sys.exit(app.exec_())
