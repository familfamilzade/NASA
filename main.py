import math


def landing_calculator(mass, gravity):
    return math.floor(mass * gravity * 0.033 - 42)


def launching_calculator(mass, gravity):
    return math.floor(mass * gravity * 0.042 - 33)


def fuel_to_launch(mass, gravity):
    needed_fuel = 0
    fuel_for_mass = launching_calculator(mass, gravity)
    needed_fuel += fuel_for_mass
    fuel_to_carry_fuel = launching_calculator(fuel_for_mass, gravity)

    while fuel_to_carry_fuel > 0:
        needed_fuel += fuel_to_carry_fuel
        fuel_to_carry_fuel = launching_calculator(fuel_to_carry_fuel, gravity)

    return needed_fuel


def fuel_to_land(mass, gravity):
    needed_fuel = 0
    fuel_for_mass = landing_calculator(mass, gravity)
    needed_fuel += fuel_for_mass
    fuel_to_carry_fuel = landing_calculator(fuel_for_mass, gravity)

    while fuel_to_carry_fuel > 0:
        needed_fuel += fuel_to_carry_fuel
        fuel_to_carry_fuel = landing_calculator(fuel_to_carry_fuel, gravity)

    return needed_fuel


def whole_mission_fuel(ship_mass, directives):
    total_fuel = 0
    for i in range(len(directives) - 1, -1, -1):
        total_fuel += fuel_to_land(ship_mass + total_fuel, directives[i][1])
        total_fuel += fuel_to_launch(ship_mass + total_fuel, directives[i][0])
    return total_fuel


if __name__ == '__main__':
    directives = []
    ship_mass = int(input('Enter the mass of the ship: '))
    num_of_flights = int(input('Enter the number of flights: '))

    for i in range(num_of_flights):
        flight = (float(input('Launch: ')), float(input('Land: ')))
        directives.append(flight)
    print(f"Total fuel needed: {whole_mission_fuel(ship_mass, directives)}")
