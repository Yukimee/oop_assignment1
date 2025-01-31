class Car:
    def __init__(self, car_id, make, model, year, mileage, available, min_rent_period, max_rent_period):
        self.__car_id = car_id
        self.__make = make
        self.__model = model
        self.__year = year
        self.__mileage = mileage
        self.__available = available
        self.__min_rent_period = min_rent_period
        self.__max_rent_period = max_rent_period

    # Getters (Encapsulation)
    def get_car_id(self):
        return self.__car_id

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_mileage(self):
        return self.__mileage

    def is_available(self):
        return self.__available

    def get_min_rent_period(self):
        return self.__min_rent_period

    def get_max_rent_period(self):
        return self.__max_rent_period

    # Setters
    def set_mileage(self, mileage):
        if mileage >= 0:
            self.__mileage = mileage

    def set_availability(self, status):
        self.__available = status

    def get_car_details(self):
        return (f"{self.__make} {self.__model} ({self.__year}), Mileage: {self.__mileage}, "
                f"Available: {self.__available}, Minimum Rent Period: {self.__min_rent_period}, "
                f"Maximum Rent Period: {self.__max_rent_period}")
