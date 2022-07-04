#!bin/bash/python

train_mass = 22000
train_acceleration = 10


def f_to_c(f_temp):
    return (f_temp - 32) * 5/9


def c_to_f(c_temp):
    return c_temp * 9/5 + 32


def getForce(mass, acceleration):
    return mass * acceleration


def getEnergy(mass, c=3.0*10**8):
    return mass * c**2


def getWork(mass, acceleration, distance):
    force = getForce(mass, acceleration)
    return force * distance


print(getEnergy(1))
