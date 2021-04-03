import numpy as np

ihat = np.array([1.0, 0.0])
jhat = np.array([0.0, 1.0])

k = 9.0E9 # Coulomb's constant (N*m^2/C^2)

class PointCharge:
    def __init__(self, charge, pos):
        self.charge = charge # the charge of the point charge (C)
        self.pos = pos       # a vector from the origin to the location of the point charge (m)

class Dipole:
    def __init__(self, position, distance, angle, positive_mass, negative_mass, charge, velocity, angular_vel):
        self.position = position           # vector from the origin to the centre of mass of the dipole (m)
        self.distance = distance           # scalar distance between the pair of charges in the dipole (m)
        self.angle = angle                 # angle of the dipole. 0 when vertically oriented with positive up, increases clockwise (rads)
        self.positive_mass = positive_mass # the mass of the dipole's positive charge (kg)
        self.negative_mass = negative_mass # the mass of the dipole's negative charge (kg)
        self.charge = charge               # the charge of the dipole (C)
        self.velocity = velocity           # the velocity vector of the dipole's centre of mass (m/s)
        self.angular_vel = angular_vel     # the angular velocity of the dipole about the centre of mass (rads/s)
    def centre_of_mass(self):
        """ Return a vector from the negative charge in the dipole to the centre of mass of the dipole. """
        return (self.distance * (ihat * np.sin(self.angle) + jhat * np.cos(self.angle)) * self.positive_mass) / (self.positive_mass + self.negative_mass)
    def moment_of_inertia(self):
        """ Return the moment of inertia of the dipole. """
        return self.negative_mass * np.linalg.norm(self.centre_of_mass()) ** 2 + self.positive_mass * (self.distance - np.linalg.norm(self.centre_of_mass())) ** 2
    def positive_position(self):
        """ Return a vector from origin to the positive charge of the dipole. """
        return self.position + (self.distance * (ihat * np.sin(self.angle) + jhat * np.cos(self.angle)) - self.centre_of_mass())
    def negative_position(self):
        """ Return a vector from origin to the negative charge of the dipole. """
        return self.position - self.centre_of_mass()

class Simulation:
    def __init__(self, dipole, point_charges, dt, paused = True):
        self.dipole = dipole
        self.point_charges = point_charges
        self.dt = dt
        self.paused = paused
    def torque(self):
        """ Return the net torque on the dipole in the simulation. """
        return np.cross(self.dipole.positive_position(), self.force(self.dipole.positive_position(), self.dipole.charge)) + np.cross(self.dipole.negative_position(), self.force(self.dipole.negative_position(), -self.dipole.charge))
    def force(self, position, charge):
        """ Return the force on a charge at a given position. """
        field = np.array([0.0, 0.0])
        for point_charge in self.point_charges:
            field += k * point_charge.charge * (position - point_charge.pos) / (np.linalg.norm(position - point_charge.pos) ** 3)
        return charge * field
    def f_net(self):
        """ Return the net force on the dipole. """
        return self.force(self.dipole.positive_position(), self.dipole.charge) + self.force(self.dipole.negative_position(), -self.dipole.charge)
    def advance(self):
        """ Apply a single iteration of Euler's method. """
        self.dipole.velocity += self.dt * self.f_net() / (self.dipole.positive_mass + self.dipole.negative_mass)
        self.dipole.angular_vel += self.dt * self.torque() / self.dipole.moment_of_inertia()
        self.dipole.position += self.dt * self.dipole.velocity
        self.dipole.angle += self.dt * self.dipole.angular_vel
