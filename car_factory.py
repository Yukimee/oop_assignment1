from car import Car


class CarFactory:
    @staticmethod
    def create_car(car_id, make, model, year, mileage, available, min_rent_period, max_rent_period):
        return Car(car_id, make, model, year, mileage, available, min_rent_period, max_rent_period)
