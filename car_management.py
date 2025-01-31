from db_config import connect_to_db


def add_car_to_db(make, model, year, mileage, min_rent_period, max_rent_period):
    # Adds a new car to the database.
    connection = connect_to_db()
    cursor = connection.cursor()

    try:
        sql = ("INSERT INTO cars (make, model, year, mileage, available, min_rent_period, max_rent_period) "
               "VALUES (?, ?, ?, ?, ?, ?, ?)")
        values = (make, model, year, mileage, True, min_rent_period, max_rent_period)

        if validate_car_details(int(year), int(mileage), min_rent_period, max_rent_period):
            cursor.execute(sql, values)
            connection.commit()
            print("Car added successfully!")
        else:
            return False
    except Exception as e:
        return f"Error: {e}"
    finally:
        cursor.close()
        connection.close()


def update_car_to_db(car_id, mileage=None, available=None):
    # Updates car details such as mileage or availability.
    connection = connect_to_db()
    cursor = connection.cursor()

    try:
        updates = []
        values = []

        if mileage is not None:
            updates.append("mileage = ?")
            values.append(mileage)
        if available is not None:
            updates.append("available = ?")
            values.append(available)

        if not updates:
            return "No updates provided."

        sql = f"UPDATE cars SET {', '.join(updates)} WHERE car_id = ?"
        values.append(car_id)

        cursor.execute(sql, values)
        connection.commit()
        return "Car updated successfully!"
    except Exception as e:
        return f"Error: {e}"
    finally:
        cursor.close()
        connection.close()


def delete_car_from_db(car_id):
    # Deletes a car from the database.
    connection = connect_to_db()
    cursor = connection.cursor()

    try:
        sql = "DELETE FROM cars WHERE car_id = ?"
        cursor.execute(sql, (car_id,))
        connection.commit()
        return "Car deleted successfully!"
    except Exception as e:
        return f"Error: {e}"
    finally:
        cursor.close()
        connection.close()


def get_all_cars_from_db():
    # Fetches all cars from the database.
    connection = connect_to_db()
    cursor = connection.cursor()

    try:
        sql = "SELECT * FROM cars"
        cursor.execute(sql)
        cars = cursor.fetchall()
        return cars
    finally:
        cursor.close()
        connection.close()


def validate_car_details(year, mileage, min_rent_period, max_rent_period):
    if year < 1900 or year > 2025:
        print("Invalid year. Must be between 1900 and 2025.")
        return False
    if mileage < 0:
        print("Mileage cannot be negative.")
        return False
    if min_rent_period < 1 or max_rent_period < min_rent_period:
        print("Invalid rental period range.")
        return False
    return True
