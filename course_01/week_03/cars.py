import os
import csv


class BaseCar:
    def __init__(self, car_type, photo_file_name, brand, carrying):
        self.car_type = car_type
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(BaseCar):
    def __init__(self, car_type, photo_file_name, brand, carrying, passenger_seats_count):
        super().__init__(car_type, photo_file_name, brand, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(BaseCar):
    def __init__(self, car_type, photo_file_name, brand, carrying, body_whl):
        super().__init__(car_type, photo_file_name, brand, carrying)
        try:
            body_width, body_height, body_length = body_whl.split('x')
        except ValueError:
            self.body_width = 0.0
            self.body_height = 0.0
            self.body_length = 0.0
        else:
            self.body_width = float(body_width)
            self.body_height = float(body_height)
            self.body_length = float(body_length)

    def get_body_volume(self):
        return self.body_length * self.body_height * self.body_width


class SpecMachine(BaseCar):
    def __init__(self, car_type, photo_file_name, brand, carrying, extra):
        super().__init__(car_type, photo_file_name, brand, carrying)
        self.extra = extra


def get_car_list(filename):
    with open(filename) as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        for row in reader:
            print(row)


if __name__ == '__main__':
    get_car_list('coursera_week3_cars.csv')
