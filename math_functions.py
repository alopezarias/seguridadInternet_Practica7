from math import floor


def extended_euclides_algorithm(e, phi_n):
    values = [[phi_n, 0], [e, 1]]
    while e != 1:
        values.append([floor(phi_n/e), 0])
        phi_n, e = e, phi_n % e
    for iteration in range(2, len(values)):
        values[iteration][1] = values[iteration-2][1] - values[iteration-1][1]*values[iteration][0]
    return number_to_module(values[len(values)-1][1], values[0][0])


def number_to_module(num, module):
    while num < 0:
        num += module
    return num % module


def modular_potentiation_algorithm(number, power, module):
    power.reverse()
    values = [[number, power[0], 1]]
    for iteration in range(1, len(power)):
        values.append([number_to_module(values[iteration-1][0]**2, module), power[iteration], 0])
    values.append([None, None, 0])
    for iteration in range(1, len(values)):
        if values[iteration-1][1] == 1:
            result = number_to_module(values[iteration-1][0]*values[iteration-1][2], module)
        else:
            result = values[iteration-1][2]
        values[iteration][2] = result
    power.reverse()
    return values[len(values)-1][2]
