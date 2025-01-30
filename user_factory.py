from user import Admin
from user import Customer


class UserFactory:
    @staticmethod
    def create_user(user_id, name, password, role):
        if role == "admin":
            return Admin(user_id, name, password)
        elif role == "customer":
            return Customer(user_id, name, password)
        else:
            raise ValueError("Invalid user role")
