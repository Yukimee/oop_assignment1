from db_config import connect_to_db
from datetime import datetime
from booking import Booking


def get_all_pending_bookings():
    # Fetch all pending bookings.
    connection = connect_to_db()
    cursor = connection.cursor()

    try:
        sql = "SELECT * FROM bookings WHERE status = 'pending'"
        cursor.execute(sql)
        bookings = cursor.fetchall()

        if bookings:
            booking_list = [Booking(*row) for row in bookings]  # Convert each row to a Booking object

            for booking in booking_list:
                print(booking.get_booking_details())  # Display car details
        else:
            print("No bookings available.")
    finally:
        cursor.close()
        connection.close()


def update_booking_status(booking_id, status):
    # Allows an admin to approve or reject a booking.
    if status not in ["approved", "rejected"]:
        return "Invalid status! Use 'approved' or 'rejected'."

    connection = connect_to_db()
    cursor = connection.cursor()

    try:
        sql = "UPDATE bookings SET status = ? WHERE booking_id = ?"
        cursor.execute(sql, (status, booking_id))
        connection.commit()
        print(f"Booking {booking_id} has been {status}.")
        return
    except Exception as e:
        return f"Error updating booking: {e}"
    finally:
        cursor.close()
        connection.close()


def book_car(user_id, car_id, start_date, end_date, daily_rate, status):
    # Creates a new booking and saves it to the database.
    connection = connect_to_db()
    cursor = connection.cursor()

    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    try:
        if validate_date(start, end):

            # Insert booking data
            sql = ("INSERT INTO bookings (user_id, car_id, start_date, end_date, total_cost, status) VALUES (?, ?, ?, "
                   "?, ?, ?)")

            booking = Booking(None, user_id, car_id, start_date, end_date, daily_rate, status)
            values = (booking.get_customer_id(), booking.get_car_id(), booking.get_start_date(),
                      booking.get_end_date(), booking.get_total_cost(), booking.get_status())
            cursor.execute(sql, values)
            connection.commit()

            # Update car status
            cursor.execute("UPDATE cars SET available = 0 WHERE car_id = ?", (car_id,))
            connection.commit()

            # Update Booking Data - Booking ID (AutoIncremented)
            sql_get_booking_data = "SELECT * FROM bookings WHERE car_id = ?"
            cursor.execute(sql_get_booking_data, (car_id,))
            connection.commit()

            booking_data = cursor.fetchone()

            if booking_data:
                booking = Booking(*booking_data)
            print(f"Booking confirmed. Booking details: {booking.get_booking_details()}")
            return booking
        else:
            return False
    except Exception as e:
        return f"Error: {e}"
    finally:
        cursor.close()
        connection.close()


def validate_date(start_date, end_date):
    today = datetime.today()

    if start_date < today or end_date < today:
        print(f"Invalid year. Booking start/end date must be from today's date: {datetime.today().date()} onward!")
        return False
    elif start_date > end_date:
        print("End date must be after start date.")
        return False
    return True




