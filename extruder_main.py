from PyQt5 import QtWidgets, QtCore
import sys

from PyQt5.QtWidgets import QMainWindow, QMessageBox
from extruder_calibration import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)



class sub(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

    def setup_slots(self):
        self.steps_btn.clicked.connect(self.extrude)
        self.mult_btn.clicked.connect(self.flow)
        self.actionAbout.triggered.connect(self.show_about)

    
    def extrude(self):
        dist = self.extruded_spinBox.value()
        left = 120 - dist
        corr = 100 / left
        act = self.original_spinBox.value()
        new = round(corr, 2) * round(act, 2)
        self.calculated_steps.setText(str(new))


    def flow(self):
        calc_extr = self.current_extr_spinBox.value() * self.desired_spinBox.value() / self.actual_extrusion_spinBox.value()
        #self.calculated_extrusion.setText(str(calc_extr))
        self.calculated_extrusion.setText(str(round(calc_extr, 2)))


    def show_about(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("This app helps to dial in your extruder value. Hover over each input for exact instruction on how to get needed value. Basic commands are as follows. Use M83 to set the extruder to relative mode. Then M503 to retrieve current settings. M500 to save.")
        msg.setWindowTitle("About this extruder app!")
        msg.setStandardButtons(QMessageBox.Ok)
        
        msg.exec_()




MainWindow = QtWidgets.QMainWindow()
ui = sub()
ui.setupUi(MainWindow)
ui.setup_slots()
MainWindow.show()
sys.exit(app.exec_())
