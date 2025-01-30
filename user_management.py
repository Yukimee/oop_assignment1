# To manage user login & registration
import sqlite3

CONNECTION = sqlite3.connect("car_rental.db")


def add_user_to_db(name, email, password, role):
    # Add a new user to the database.
    connection = sqlite3.connect("car_rental.db")
    cursor = connection.cursor()

    try:
        sql = "INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)"
        values = (name, email, password, role)
        if validate_username(name):

            cursor.execute(sql, values)
            connection.commit()
            print(f"Registered successfully as {role}.")

    except sqlite3.IntegrityError:
        return "Email already exists. Please choose a different email."
    finally:
        connection.close()


def get_user_from_db(email, password):
    # Retrieve user from the database
    connection = CONNECTION
    cursor = connection.cursor()

    sql = "SELECT user_id, name, password, role FROM users WHERE email = ? AND password = ? "
    values = (email, password)
    user = cursor.execute(sql, values).fetchone()
    connection.close()

    return user


def validate_username(name):
    if not name.isalnum():
        print("Error: Username must be alphanumeric.")
        return False
    return True
