import sqlite3
from datetime import datetime


def view_available_cars():
    connection = sqlite3.connect("car_rental.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM cars WHERE available = 1")
    cars = cursor.fetchall()

    connection.close()

    if not cars:
        print("No cars available.")
    else:
        for car in cars:
            print(car)  # Display car details


def book_car(user_id, car_id, start_date, end_date, daily_rate, status):
    connection = sqlite3.connect("car_rental.db")
    cursor = connection.cursor()

    total_cost = float(calculate_rental_fees(start_date, end_date, daily_rate))

    sql = ("INSERT INTO bookings (user_id, car_id, start_date, end_date, total_cost, status) "
           "VALUES (?, ?, ?, ?, ?, ?)")
    values = (user_id, car_id, start_date, end_date, total_cost, status)
    cursor.execute(sql, values)

    cursor.execute("UPDATE cars SET available = 0 WHERE car_id = ?", (car_id,))
    connection.commit()
    connection.close()
    print(f"Booking confirmed. Total cost: ${total_cost:.2f}")


def calculate_rental_fees(start_date, end_date, daily_rate):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    rental_days = (end - start).days  # To get number of days as an integer
    total_cost = rental_days * daily_rate
    return total_cost
