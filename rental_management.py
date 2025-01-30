from db_config import connect_to_db


def get_all_pending_bookings():
    # Fetches all bookings with status 'pending'.
    connection = connect_to_db()
    cursor = connection.cursor()

    try:
        sql = ("SELECT booking_id, user_id, car_id, start_date, end_date, total_cost, status "
               "FROM bookings WHERE status = 'pending'")
        cursor.execute(sql)
        bookings = cursor.fetchall()

        booking_list = [
            {
                "booking_id": row[0], "user_id": row[1], "car_id": row[2],
                "start_date": row[3], "end_date": row[4], "total_cost": row[5], "status": row[6]
            }
            for row in bookings
        ]
        return booking_list
    finally:
        cursor.close()
        connection.close()


def update_booking_status(booking_id, status):
    """Updates the status of a booking (approved/rejected)."""
    if status not in ["approved", "rejected"]:
        return "Invalid status! Use 'approved' or 'rejected'."

    connection = connect_to_db()
    cursor = connection.cursor()

    try:
        sql = "UPDATE bookings SET status = ? WHERE booking_id = ?"
        cursor.execute(sql, (status, booking_id))
        connection.commit()

        return f"Booking {booking_id} has been {status}."
    except Exception as e:
        return f"Error updating booking: {e}"
    finally:
        cursor.close()
        connection.close()
