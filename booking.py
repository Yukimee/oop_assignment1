class Booking:
    def __init__(self, booking_id, customer_id, car_id, start_date, end_date, daily_rate):
        self.booking_id = booking_id
        self.customer_id = customer_id
        self.car_id = car_id
        self.start_date = start_date
        self.end_date = end_date
        self.daily_rate = daily_rate
        self.total_cost = self.calculate_price()

    def calculate_price(self):
        rental_days = (self.end_date - self.start_date).days
        return rental_days * self.daily_rate
