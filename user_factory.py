from user import Admin, Customer


class UserFactory:
    @staticmethod
    def create_user(user_id, name, email, password, role):
        if role.lower() == "admin":
            return Admin(user_id, name, email, password)
        elif role.lower() == "customer":
            return Customer(user_id, name, email, password)
        else:
            raise ValueError("Invalid user role")
