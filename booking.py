from datetime import datetime


class Booking:
    def __init__(self, booking_id, customer_id, car_id, start_date, end_date, daily_rate, status="pending"):
        self.__booking_id = booking_id
        self.__customer_id = customer_id
        self.__car_id = car_id
        self.__start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.__end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.__daily_rate = float(daily_rate)
        self.__status = status
        self.__total_cost = self.calculate_price()

    # Getters
    def get_booking_id(self):
        return self.__booking_id

    def get_customer_id(self):
        return self.__customer_id

    def get_car_id(self):
        return self.__car_id

    def get_start_date(self):
        return self.__start_date.strftime("%Y-%m-%d")

    def get_end_date(self):
        return self.__end_date.strftime("%Y-%m-%d")

    def get_daily_rate(self):
        return self.__daily_rate

    def get_status(self):
        return self.__status

    def get_total_cost(self):
        return self.__total_cost

        # Setters
    def set_status(self, status):
        if status in ["pending", "approved", "rejected"]:
                self.__status = status

    def calculate_price(self):
        rental_days = (self.__end_date - self.__start_date).days
        total_cost = float(rental_days * self.__daily_rate)
        return total_cost


    def get_booking_details(self):
        return (f"Booking ID: {self.__booking_id}, Customer ID: {self.__customer_id}, Car ID: {self.__car_id}, "
                    f"Start Date: {self.__start_date.strftime('%Y-%m-%d')}, End Date: {self.__end_date.strftime('%Y-%m-%d')}, "
                    f"Total Cost: ${self.__total_cost:.2f}, Status: {self.__status}")
