# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import ctypes
import sys
import psutil
import json
import win10toast
from os import popen

interface_s = list(psutil.net_if_addrs().keys())
icon_path = "change_dns.ico"

notif = win10toast.ToastNotifier()

def is_admin():
    try:
        _ = ctypes.windll.shell32.IsUserAnAdmin()
        return True
    except:
        return False
    
try: 
    with open("config.json", "r") as config_file:
        configs = json.load(config_file)
except:
    notif.show_toast(
        "Problem!",
        "config.json not found!",
        duration=5,
        icon_path=icon_path,
        threaded=True
    )
    exit()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 600)
        Form.setWindowTitle("change dns")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(400, 600))
        Form.setMaximumSize(QtCore.QSize(400, 600))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        Form.setFont(font)
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(0, 5, 400, 60))
        self.title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title.setFrameShadow(QtWidgets.QFrame.Plain)
        self.title.setScaledContents(False)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setWordWrap(False)
        self.title.setOpenExternalLinks(False)
        self.title.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.title.setObjectName("title")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(25, 80, 350, 110))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.provider = QtWidgets.QComboBox(self.groupBox)
        self.provider.setGeometry(QtCore.QRect(25, 30, 300, 60))
        self.provider.setCurrentText("")
        self.provider.setObjectName("provider")
        
        for prv in configs["providers"].keys():
            self.provider.addItem(prv)
            
        self.provider.setCurrentText(configs["default-provider"])
        self.provider.currentIndexChanged.connect(self.set_provider)
        
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(25, 320, 350, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.primary = QtWidgets.QLineEdit(self.groupBox_2)
        self.primary.setGeometry(QtCore.QRect(25, 30, 300, 60))
        self.primary.setStyleSheet("")
        self.primary.setAlignment(QtCore.Qt.AlignCenter)
        self.primary.setClearButtonEnabled(True)
        self.primary.setObjectName("primary")
        
        self.primary.setText(configs["providers"][self.provider.currentText()]["primary"])
        
        self.secondary = QtWidgets.QLineEdit(self.groupBox_2)
        self.secondary.setGeometry(QtCore.QRect(25, 120, 300, 60))
        self.secondary.setStyleSheet("")
        self.secondary.setAlignment(QtCore.Qt.AlignCenter)
        self.secondary.setClearButtonEnabled(True)
        self.secondary.setObjectName("secondary")
        
        self.secondary.setText(configs["providers"][self.provider.currentText()]["secondary"])
        
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(25, 200, 350, 110))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.interfaces = QtWidgets.QComboBox(self.groupBox_3)
        self.interfaces.setGeometry(QtCore.QRect(25, 30, 300, 60))
        self.interfaces.setCurrentText("")
        self.interfaces.setObjectName("interfaces")
        
        self.interfaces.addItem("--- Select ---")
        self.interfaces.model().item(0).setEnabled(False)
        self.interfaces.addItems(interface_s)
        if "Wi-Fi" in interface_s:
            self.interfaces.setCurrentIndex(interface_s.index("Wi-Fi") + 1)
        elif "Ethernet" in interface_s:
            self.interfaces.setCurrentIndex(interface_s.index("Ethernet") + 1)
        else:
            self.interfaces.setCurrentText("--- Select ---")
        
        
        self.gridWidget = QtWidgets.QWidget(Form)
        self.gridWidget.setGeometry(QtCore.QRect(25, 520, 351, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridWidget.sizePolicy().hasHeightForWidth())
        self.gridWidget.setSizePolicy(sizePolicy)
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.connect = QtWidgets.QPushButton(self.gridWidget)
        self.connect.setObjectName("connect")
        
        self.connect.clicked.connect(self.change)
        
        self.gridLayout.addWidget(self.connect, 0, 0, 1, 1)
        self.reset = QtWidgets.QPushButton(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset.sizePolicy().hasHeightForWidth())
        self.reset.setSizePolicy(sizePolicy)
        self.reset.setObjectName("reset")
        
        self.reset.clicked.connect(self.autodns)
        
        self.gridLayout.addWidget(self.reset, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 580, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "change dns"))
        self.title.setText(_translate("Form", "Dns Changer"))
        self.groupBox.setTitle(_translate("Form", "DNS provider"))
        self.groupBox_2.setTitle(_translate("Form", "Config (Primary / Secondary)"))
        self.groupBox_3.setTitle(_translate("Form", "Interface"))
        self.connect.setText(_translate("Form", "Connect"))
        self.reset.setText(_translate("Form", "Reset"))
        self.label.setText(_translate("Form", "https://github.com/kinite-gp"))
        
    def set_provider(self, Form):
        self.primary.setText(configs["providers"][self.provider.currentText()]["primary"])
        self.secondary.setText(configs["providers"][self.provider.currentText()]["secondary"])
        
    def change(self, Form):
        popen(f"netsh interface ipv4 add dns \"{self.interfaces.currentText()}\" {self.primary.text()} index=1")
        popen(f"netsh interface ipv4 add dns \"{self.interfaces.currentText()}\" {self.secondary.text()} index=2")
        popen("ipconfig /flushdns")
        
        notif.show_toast(
            "Success!",
            "your dns changed!",
            duration=5,
            icon_path=icon_path,
            threaded=True
        )
        
    def autodns(self, Form):
        popen(f'netsh interface ip set dnsservers name="{self.interfaces.currentText()}" source=dhcp')
        popen("ipconfig /flushdns")
        
        notif.show_toast(
            "Success!",
            "your dns removed!",
            duration=5,
            icon_path=icon_path,
            threaded=True
        )
        
        
        
if __name__ == "__main__":
    if is_admin():
        app = QtWidgets.QApplication(sys.argv)
        MainWindows = QtWidgets.QMainWindow()
        ui = Ui_Form()
        ui.setupUi(MainWindows)
        MainWindows.show()
        sys.exit(app.exec_())
    else:
        exit()
