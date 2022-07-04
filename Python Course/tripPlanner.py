#!bin/bash/python

def tripPlannerWelcome(name):
    print(f'Welcome to trippleanner v1.0, {name}')


def estimatedTimeRounded(estimated_time):
    return round(estimated_time)


def destinationSetup(origin, destination, estimatedTime, modeOfTransport='Car'):
    print(f'Your trip starts off in {origin}')
    print(f'And you are traveling to {destination}')
    print(f'You will be travelling by {modeOfTransport}')
    print(f'It will take approximately {estimatedTime} hours')


tripPlannerWelcome('Whittle')
estimate = estimatedTimeRounded(3.5)
destinationSetup('Hollywood', 'San Diego', estimate)
