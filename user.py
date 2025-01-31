import sqlite3
import hashlib


class User:

    def __init__(self, user_id, name, email, role, password):
        self.__user_id = user_id  # Encapsulation - to protect data
        self.__name = name
        self.__email = email
        self.__role = role  # 'customer' or 'admin'
        self.__password = self.__hash_password(password)  # Store hashed password

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

    # Hash password (Abstraction: hides hashing logic)
    def __hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    # Check if password matches stored hash
    def verify_password(self, password):
        return self.__password == hashlib.sha256(password.encode()).hexdigest()

    # Polymorphism: Override in subclasses
    def display_info(self):
        return f"User: {self.__name}, Email: {self.__email}, Role: {self.__role}"


# Inheritance
class Customer(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, "customer", password)

    # Override display_info (Polymorphism)
    def display_info(self):
        return f"Customer: {self.get_name()}, Email: {self.get_email()}"

    def get_user_id(self):
        return self.__user_id


class Admin(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, "admin", password)

    # Override display_info (Polymorphism)
    def display_info(self):
        return f"Admin: {self.get_name()}, Email: {self.get_email()}"


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
