import sqlite3

class User:
    def __init__(self, user_id, name, password, role):
        self.user_id = user_id
        self.name = name
        self.password = password
        self.role = role  # 'admin' or 'customer'

    def get_role(self):
        return self.role


class Customer(User):
    def __init__(self, user_id, name, password):
        super().__init__(user_id, name, password, "customer")

    def get_user_id(self):
        return self.__user_id


class Admin(User):
    def __init__(self, user_id, name, password):
        super().__init__(user_id, name, password, "admin")


"""class User:
    def __init__(self, user_id, name, email, role):
        self.__user_id = user_id  # Encapsulation - to protect data
        self.__name = name
        self.__email = email
        self.__role = role  # 'customer' or 'admin'

    # Getters and setters
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_role(self):
        return self.__role

    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def display_info(self):
        print(f"User: {self.__name}, Email: {self.__email}, Role: {self.__role}")




# Example usage
user1 = User(1, "Tommy", "tom@gmail.com", "customer")
user1.display_info()
"""

"""
import sqlite3
import hashlib


class User:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def register(self, username, password, email=None):
        hashed_password = self._hash_password(password)
        cursor = self.db_connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                (username, hashed_password, email)
            )
            self.db_connection.commit()
            print("User registered successfully.")
        except sqlite3.IntegrityError:
            print("Error: Username already exists.")

    def login(self, username, password):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()

        if result and self._check_password(password, result[0]):
            print(f"Welcome {username}!")
            return True
        else:
            print("Invalid username or password.")
            return False

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def _check_password(self, password, hashed_password):
        return self._hash_password(password) == hashed_password
"""
