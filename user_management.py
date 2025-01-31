from user import User
import sqlite3
from db_config import connect_to_db


def add_user_to_db(name, email, password, role):
    # Add a new user to the database securely.
    connection = connect_to_db()
    cursor = connection.cursor()

    try:
        sql = "INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)"
        user = User(None, name, email, role, password)  # Create User object
        values = (user.get_name(), user.get_email(), password, user.get_role())

        cursor.execute(sql, values)
        connection.commit()
        print(f"Registered successfully as {role}.")
        return True
    except sqlite3.IntegrityError:
        return "Email already exists. Please choose a different email."
    finally:
        connection.close()


def get_user_from_db(email, password):
    # Retrieve user from the database and verify credentials.
    connection = connect_to_db()
    cursor = connection.cursor()

    sql = "SELECT user_id, name, email, role, password FROM users WHERE email = ?"
    cursor.execute(sql, (email,))
    user_data = cursor.fetchone()

    connection.close()

    if user_data:
        user = User(*user_data)
        if user.verify_password(password):
            return user  # Return a User object instead of a tuple
        else:
            return None  # Invalid password
    return None  # User not found


def validate_username(name):
    if not name.isalnum():
        print("Error: Username must be alphanumeric.")
        return False
    return True
