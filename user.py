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

