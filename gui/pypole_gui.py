import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class PypoleGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pypole")
        self.setLayout(QtWidgets.QVBoxLayout())
        self.dipole_settings()
        self.scene()
        self.point_charge_settings()

    def dipole_settings(self):
        dipole_settings = QtWidgets.QWidget()
        dipole_settings.setLayout(QtWidgets.QHBoxLayout())

        dial = QtWidgets.QDial()
        dipole_charge = QtWidgets.QSpinBox()
        dipole_negative_mass = QtWidgets.QSpinBox()
        dipole_positive_mass = QtWidgets.QSpinBox()
        dipole_distance = QtWidgets.QSpinBox()

        dipole_settings.layout().addWidget(dial)
        dipole_settings.layout().addWidget(dipole_charge)
        dipole_settings.layout().addWidget(dipole_negative_mass)
        dipole_settings.layout().addWidget(dipole_positive_mass)
        dipole_settings.layout().addWidget(dipole_distance)

        dipole_settings.layout().insertSpacing(1, 200)

        self.layout().addWidget(dipole_settings)

    def scene(self):
        scene = QtWidgets.QGraphicsScene()
        view = QtWidgets.QGraphicsView(scene)

        self.layout().addWidget(view)

    def point_charge_settings(self):
        point_charge_settings = QtWidgets.QWidget()
        point_charge_settings.setLayout(QtWidgets.QHBoxLayout())

        point_charge = QtWidgets.QSpinBox()
        play = QtWidgets.QPushButton("play")
        pause = QtWidgets.QPushButton("pause")
        reset = QtWidgets.QPushButton("reset")

        point_charge_settings.layout().addWidget(point_charge)
        point_charge_settings.layout().addWidget(play)
        point_charge_settings.layout().addWidget(pause)
        point_charge_settings.layout().addWidget(reset)

        point_charge_settings.layout().insertSpacing(1, 200)
        point_charge_settings.layout().insertSpacing(4, 100)

        self.layout().addWidget(point_charge_settings)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = PypoleGUI()
    widget.show()

    sys.exit(app.exec_())
