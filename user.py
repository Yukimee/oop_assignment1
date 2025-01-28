class User:
    def __init__(self, user_id, name, email, role):
        self.__user_id = user_id  # Encapsulation
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


users_db = {}


def register_user(user_id, name, email, role, password):
    if email in users_db:
        return "User already exists!"
    users_db[email] = {"user_id": user_id, "name": name, "role": role, "password": password}
    return "User registered successfully!"


def login_user(email, password):
    if email in users_db and users_db[email]["password"] == password:
        return f"Welcome, {users_db[email]['name']}!"
    return "Invalid login credentials."


# Example usage
print(register_user(1, "Alice", "alice@example.com", "customer", "pass123"))
print(login_user("alice@example.com", "pass123"))

# Example usage
user1 = User(1, "Tommy", "tom@gmail.com", "customer")
user1.display_info()
