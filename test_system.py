import unittest
from user_management import register_user, get_user_from_db
from car_management import add_car, update_car, delete_car, get_all_cars
from rental_booking import book_car, view_available_cars


class TestUserManagement(unittest.TestCase):
    def test_register_user(self):
        result = register_user("testuser", "testpass", "customer", "password", "role")
        self.assertIsNone(result)  # Expect no return value on success

    def test_login_user_valid(self):
        user = get_user_from_db("testuser", "testpass")
        self.assertIsNotNone(user)

    def test_login_user_invalid(self):
        user = get_user_from_db("invaliduser", "wrongpass")
        self.assertIsNone(user)


class TestCarManagement(unittest.TestCase):
    def test_add_car(self):
        result = add_car("Toyota", "Corolla", 2020, 50000)
        self.assertIsNone(result)

    def test_update_car(self):
        result = update_car(1, "mileage", 55000)
        self.assertIsNone(result)

    def test_delete_car(self):
        result = delete_car(1)
        self.assertIsNone(result)


class TestBookingSystem(unittest.TestCase):
    def test_view_available_cars(self):
        result = view_available_cars()
        self.assertIsNone(result)

    def test_book_car(self):
        result = book_car(1, 2, "2025-02-01", "2025-02-10", 50)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
