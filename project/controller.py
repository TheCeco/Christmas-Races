from project.car.muscle_car import MuscleCar
from project.race import Race
from project.car.sports_car import SportsCar
from project.driver import Driver


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type, model, speed_limit):
        if car_type == 'MuscleCar' or car_type == 'SportsCar':
            for car in self.cars:
                if car.model == model:
                    raise Exception(f"Car {model} is already created!")

            if car_type == 'SportsCar':
                self.cars.append(SportsCar(model, speed_limit))
            else:
                self.cars.append(MuscleCar(model, speed_limit))

            return f"{car_type} {model} is created."

    def create_driver(self, name):
        for driver in self.drivers:
            if driver.name == name:
                raise Exception(f"Driver {driver.name} is already created!")

        self.drivers.append(Driver(name))
        return f"Driver {name} is created."

    def create_race(self, race_name):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")

        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: Driver, car_type):
        driver = self.__validate(driver_name, self.drivers, f"Driver {driver_name} could not be found!")

        for car in reversed(self.cars):
            if car.__class__.__name__ == car_type:
                if not car.is_taken and driver.car is None:
                    driver.car = car
                    car.is_taken = True
                    return f"Driver {driver.name} chose the car {car.model}."
                if not car.is_taken and driver.car is not None:
                    driver.car.is_taken = False
                    old_model = driver.car.model
                    driver.car = car
                    car.is_taken = True
                    return f"Driver {driver.name} changed his car from {old_model} to {driver.car.model}."

        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")
        raise Exception(f"Car {car_type} could not be found!")

    def add_driver_to_race(self, race_name, driver_name):

        race = self.__validate(race_name, self.races, f"Race {race_name} could not be found!")
        driver = self.__validate(driver_name, self.drivers, f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver.name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver.name} is already added in {race.name} race."

        race.drivers.append(driver)
        return f"Driver {driver.name} added in {race.name} race."

    def start_race(self, race_name):
        race = self.__validate(race_name, self.races, f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        result = ''
        for idx in range(3):
            driver = sorted(race.drivers, key=lambda x: -x.car.speed_limit)[idx]
            result += f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.\n"
            driver.number_of_wins += 1
        return result.strip()

    def __find_car(self, car):
        for c in self.cars:
            if c.model == car:
                return c

    def __validate(self, name, memo, err_mes):
        for m in memo:
            if m.name == name:
                return m
        raise Exception(err_mes)
