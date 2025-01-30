from car import Car


class CarFactory:
    @staticmethod
    def create_car(car_id, make, model, year, mileage, available, min_rent_period, max_rent_period):
        return Car(car_id, make, model, year, mileage, available, min_rent_period, max_rent_period)


"""# Example usage
car2 = CarFactory.create_car(102, "Honda", "Civic", 2019, 30000, 1, 2, 3)
print(car2.get_car_details())"""
