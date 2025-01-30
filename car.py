class Car:
    def __init__(self, car_id, make, model, year, mileage, available, min_rent_period, max_rent_period):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.available = available
        self.min_rent_period = min_rent_period
        self.max_rent_period = max_rent_period

    def is_available(self):
        return self.available

    def update_availability(self, status):
        self.available = status

    def get_car_details(self):
        return (f"{self.make} {self.model} ({self.year}), Mileage: {self.mileage}, "
                f"Available: {self.available}, Minimum Rent Period:{self.min_rent_period}, "
                f"Maximum Rent Period: {self.max_rent_period}")
