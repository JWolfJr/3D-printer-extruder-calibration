# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'extruder_calibration.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(737, 667)
        MainWindow.setStyleSheet("QWidget#MainWindow{\n"
"background-color:qlineargradient(spread:pad, x1:0.125, y1:0.176136, x2:0.916667, y2:0.897727, stop:0 rgba(54, 54, 54, 224), stop:1 rgba(210, 210, 210, 224));}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.extruded_dist = QtWidgets.QLabel(self.centralwidget)
        self.extruded_dist.setGeometry(QtCore.QRect(40, 30, 141, 31))
        self.extruded_dist.setStyleSheet("background-color: rgb(165, 156, 156);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.extruded_dist.setObjectName("extruded_dist")
        self.original_steps = QtWidgets.QLabel(self.centralwidget)
        self.original_steps.setGeometry(QtCore.QRect(40, 120, 101, 31))
        self.original_steps.setStyleSheet("background-color: rgb(165, 156, 156);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.original_steps.setObjectName("original_steps")
        self.calc_steps = QtWidgets.QLabel(self.centralwidget)
        self.calc_steps.setGeometry(QtCore.QRect(490, 40, 121, 31))
        self.calc_steps.setStyleSheet("background-color: rgb(165, 156, 156);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.calc_steps.setObjectName("calc_steps")
        self.cur_mult = QtWidgets.QLabel(self.centralwidget)
        self.cur_mult.setGeometry(QtCore.QRect(30, 300, 191, 41))
        self.cur_mult.setStyleSheet("background-color: rgb(165, 156, 156);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.cur_mult.setObjectName("cur_mult")
        self.des_mult = QtWidgets.QLabel(self.centralwidget)
        self.des_mult.setGeometry(QtCore.QRect(30, 390, 200, 31))
        self.des_mult.setStyleSheet("background-color: rgb(165, 156, 156);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.des_mult.setObjectName("des_mult")
        self.calc_extrusion = QtWidgets.QLabel(self.centralwidget)
        self.calc_extrusion.setGeometry(QtCore.QRect(490, 350, 211, 31))
        self.calc_extrusion.setStyleSheet("background-color: rgb(165, 156, 156);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.calc_extrusion.setObjectName("calc_extrusion")
        self.act_mult = QtWidgets.QLabel(self.centralwidget)
        self.act_mult.setGeometry(QtCore.QRect(30, 470, 200, 31))
        self.act_mult.setStyleSheet("background-color: rgb(165, 156, 156);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.act_mult.setObjectName("act_mult")
        self.steps_btn = QtWidgets.QPushButton(self.centralwidget)
        self.steps_btn.setGeometry(QtCore.QRect(40, 180, 111, 31))
        self.steps_btn.setStyleSheet("selection-background-color: rgb(0, 170, 255);")
        self.steps_btn.setObjectName("steps_btn")
        self.mult_btn = QtWidgets.QPushButton(self.centralwidget)
        self.mult_btn.setGeometry(QtCore.QRect(30, 530, 141, 31))
        self.mult_btn.setObjectName("mult_btn")
        self.extruded_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.extruded_spinBox.setGeometry(QtCore.QRect(230, 30, 81, 31))
        self.extruded_spinBox.setStyleSheet("background-color: rgb(210, 210, 210);\n"
"border-color: rgb(35, 35, 35);")
        self.extruded_spinBox.setMaximum(120)
        self.extruded_spinBox.setObjectName("extruded_spinBox")
        self.original_spinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.original_spinBox.setGeometry(QtCore.QRect(230, 120, 81, 31))
        self.original_spinBox.setStyleSheet("background-color: rgb(210, 210, 210);\n"
"border-color: rgb(35, 35, 35);")
        self.original_spinBox.setMaximum(140.0)
        self.original_spinBox.setObjectName("original_spinBox")
        self.current_extr_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.current_extr_spinBox.setGeometry(QtCore.QRect(240, 305, 81, 31))
        self.current_extr_spinBox.setStyleSheet("background-color: rgb(210, 210, 210);\n"
"border-color: rgb(35, 35, 35);")
        self.current_extr_spinBox.setMaximum(110)
        self.current_extr_spinBox.setObjectName("current_extr_spinBox")
        self.desired_spinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.desired_spinBox.setGeometry(QtCore.QRect(240, 390, 81, 31))
        self.desired_spinBox.setStyleSheet("background-color: rgb(210, 210, 210);\n"
"border-color: rgb(35, 35, 35);")
        self.desired_spinBox.setObjectName("desired_spinBox")
        self.actual_extrusion_spinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.actual_extrusion_spinBox.setGeometry(QtCore.QRect(240, 470, 81, 31))
        self.actual_extrusion_spinBox.setStyleSheet("background-color: rgb(210, 210, 210);\n"
"border-color: rgb(35, 35, 35);\n"
"")
        self.actual_extrusion_spinBox.setObjectName("actual_extrusion_spinBox")
        self.calculated_steps = QtWidgets.QLabel(self.centralwidget)
        self.calculated_steps.setGeometry(QtCore.QRect(490, 110, 121, 31))
        self.calculated_steps.setStyleSheet("background-color: rgb(210, 210, 210);\n"
"border-color: rgb(35, 35, 35);\n"
"border-radius: 5px;")
        self.calculated_steps.setText("")
        self.calculated_steps.setObjectName("calculated_steps")
        self.calculated_extrusion = QtWidgets.QLabel(self.centralwidget)
        self.calculated_extrusion.setGeometry(QtCore.QRect(490, 420, 121, 31))
        self.calculated_extrusion.setStyleSheet("background-color: rgb(210, 210, 210);\n"
"border-color: rgb(35, 35, 35);\n"
"border-radius: 5px;")
        self.calculated_extrusion.setText("")
        self.calculated_extrusion.setObjectName("calculated_extrusion")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 240, 701, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 737, 24))
        self.menubar.setObjectName("menubar")
        self.menuQuit = QtWidgets.QMenu(self.menubar)
        self.menuQuit.setObjectName("menuQuit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuQuit.addAction(self.actionQuit)
        self.menuQuit.addAction(self.actionAbout)
        self.menubar.addAction(self.menuQuit.menuAction())

        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close)
        self.actionAbout.triggered.connect(MainWindow.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.extruded_spinBox, self.original_spinBox)
        MainWindow.setTabOrder(self.original_spinBox, self.steps_btn)
        MainWindow.setTabOrder(self.steps_btn, self.current_extr_spinBox)
        MainWindow.setTabOrder(self.current_extr_spinBox, self.desired_spinBox)
        MainWindow.setTabOrder(self.desired_spinBox, self.actual_extrusion_spinBox)
        MainWindow.setTabOrder(self.actual_extrusion_spinBox, self.mult_btn)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Extruder Calibrater"))
        self.extruded_dist.setStatusTip(_translate("MainWindow", "The amount of mm of extruded filament"))
        self.extruded_dist.setText(_translate("MainWindow", "Measured Filament"))
        self.original_steps.setStatusTip(_translate("MainWindow", "Extruder steps in the M503 eeprom"))
        self.original_steps.setText(_translate("MainWindow", "Original Steps"))
        self.calc_steps.setText(_translate("MainWindow", "Calculated Steps"))
        self.cur_mult.setStatusTip(_translate("MainWindow", "Number in slicer for flow rate"))
        self.cur_mult.setText(_translate("MainWindow", "Current Extrusion Multiplier"))
        self.des_mult.setStatusTip(_translate("MainWindow", "Enter desired single wall width"))
        self.des_mult.setText(_translate("MainWindow", "Desired Extrusion Width"))
        self.calc_extrusion.setText(_translate("MainWindow", "Calculated Extrusion Multiplier"))
        self.act_mult.setStatusTip(_translate("MainWindow", "Enter measured wall width"))
        self.act_mult.setText(_translate("MainWindow", "Actual Extrusion Width"))
        self.steps_btn.setStatusTip(_translate("MainWindow", "Press to calculate steps/mm"))
        self.steps_btn.setText(_translate("MainWindow", "Calculate Steps"))
        self.mult_btn.setStatusTip(_translate("MainWindow", "Press to calculate extrusion multiplier"))
        self.mult_btn.setText(_translate("MainWindow", "Calculate Multiplier"))
        self.menuQuit.setTitle(_translate("MainWindow", "File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setStatusTip(_translate("MainWindow", "Quits the program and closes window"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setStatusTip(_translate("MainWindow", "About this app"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
