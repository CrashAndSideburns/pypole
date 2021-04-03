import pypole
import pypole_gui
from PySide6 import QtWidgets
import sys

class Pypole(pypole_gui.PypoleGUI):
    def __init__(self, simulation: pypole.Simulation):
        super().__init__()
        self.simulation = simulation
        self.bind_slots()

    def bind_slots(self):
        self.children()[1].children()[1].valueChanged.connect(self.update_angle)
        self.children()[1].children()[2].valueChanged.connect(self.update_dipole_charge)
        self.children()[1].children()[3].valueChanged.connect(self.update_positive_mass)
        self.children()[1].children()[4].valueChanged.connect(self.update_negative_mass)
        self.children()[1].children()[5].valueChanged.connect(self.update_distance)
        # self.children()[2] I haven't the fucking faintest how this is going to get hooked up.
        self.children()[3].children()[1].valueChanged.connect(self.update_source_charge)
        self.children()[3].children()[2].clicked.connect(self.play)
        self.children()[3].children()[3].clicked.connect(self.pause)
        self.children()[3].children()[4].clicked.connect(self.reset)

    def update_angle(self, angle):
        if self.simulation.paused:
            self.simulation.dipole.angle = angle

    def update_dipole_charge(self, charge):
        if self.simulation.paused:
            self.simulation.dipole.charge = charge

    def update_positive_mass(self, mass):
        if self.simulation.paused:
            self.simulation.dipole.positive_mass = mass

    def update_negative_mass(self, mass):
        if self.simulation.paused:
            self.simulation.dipole.negative_mass = mass

    def update_distance(self, distance):
        if self.simulation.paused:
            self.simulation.dipole.distance = distance

    def update_source_charge(self, charge):
        self.simulation.point_charges[0].charge = charge # This is basically a copout. I need to implement selection.

    def play(self):
        self.simulation.paused = False

    def pause(self):
        self.simulation.paused = True

    def reset(self):
        print("Reset simulation!")
        # Don't tell the kids that this isn't implemented yet.

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Pypole(None)
    widget.show()

    sys.exit(app.exec_())
