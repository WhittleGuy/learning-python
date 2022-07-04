#!bin/bash/python


def calculate_expenses(planeTicketPrice, carRentalRate, hotelRate, tripTime):
    carRentalTotal = carRentalRate * tripTime
    hotelTotal = hotelRate * tripTime - 10
    return carRentalTotal + hotelTotal + planeTicketPrice


print(calculate_expenses(200, 100, 100, 5))
