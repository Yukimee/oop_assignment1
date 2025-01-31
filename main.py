import car_management, user_management
from user_factory import UserFactory
import rental_booking
import rental_management


def prompt_user_to_login():
    # Prompt user to login
    print("Welcome to Car Rental Services! Please enter email and password to login.")
    email = input("Email: ")
    password = input("Password: ")

    user = user_management.get_user_from_db(email, password)

    if user:
        user_id, name, password, role = user
        UserFactory.create_user(user_id, name, password, role)
        print(f"Login successful!")
        return user_id, role
    else:
        print("Invalid username or password. If you haven't registered yet, "
              "please take a moment to sign up and join us. Registration is quick and easy, "
              "and it gives you access to all the great features we offer. Don’t miss out on the benefits!")
        return None


def prompt_user_to_register():
    # Prompt user to register
    print("Welcome to Car Rental Services! If you haven't registered yet, please take a moment to sign up and join us.")
    name = input("Name: ")
    email = input("Email: ")
    password = input("Password: ")
    role = input("Customer/Admin: ")
    user_management.add_user_to_db(name, email, password, role)
    return role


def validate_role(user_id, role):
    if role == "admin":
        prompt_admin_function(user_id)
    elif role == "customer":
        prompt_customer_function(user_id)


def main():
    while True:
        prompt_selection = input("Please choose an option (Login/Register): ").strip().lower()

        if prompt_selection == "login":
            user_id, role = prompt_user_to_login()
            validate_role(user_id, role)

        elif prompt_selection == "register":
            prompt_user_to_register()
            user_id, role = prompt_user_to_login()
            validate_role(user_id, role)

        else:
            print("Invalid selection. Please enter 'Login' or 'Register'.")
            main()  # Prompt the user again


def prompt_admin_function(user_id):
    # Prompt admin to select a function
    prompt_selection = input("Please choose an option for Rental (Management/Booking): ").strip().lower()

    if prompt_selection == "management":
        prompt_admin_rental_management(user_id)
        prompt_admin_function(user_id)
        return
    elif prompt_selection == "booking":
        prompt_admin_rental_booking(user_id)
        prompt_admin_function(user_id)
        return
    else:
        print("Invalid selection. Please enter 'Rental' or 'Booking'.")
        prompt_admin_function(user_id)  # Prompt the user again"""


    """prompt_selection = input("Please choose an option to (Add/Delete/Update) car: ").strip().lower()

    if prompt_selection == "add":
        prompt_add_car_details()
        prompt_admin_function(user_id)

    elif prompt_selection == "delete":
        prompt_delete_car_details()
        prompt_admin_function(user_id)

    elif prompt_selection == "update":
        prompt_update_car_details()
        prompt_admin_function(user_id)

    else:
        print("Invalid selection. Please enter 'Add' or 'Delete' or 'Update'.")
        prompt_admin_function(user_id)  # Prompt the user again"""


def prompt_admin_rental_management(user_id):

    prompt_selection = input("Please choose an option to (View/Update/Back to main menu) Bookings: ").strip().lower()

    if prompt_selection == "view":
        view_pending_bookings()
        prompt_admin_function(user_id)
        return
    elif prompt_selection == "update":
        update_booking_status()
        prompt_admin_function(user_id)
        return
    elif prompt_selection == "back to main menu":
        prompt_admin_function(user_id)
        return
    else:
        print("Invalid selection. Please enter 'Add' or 'Delete' or 'Update'.")
        prompt_admin_rental_management(user_id)  # Prompt the user again"""


def prompt_admin_rental_booking(user_id):

    prompt_selection = input("Please choose an option to (Add/Delete/Update/Back to main menu) car: ").strip().lower()

    if prompt_selection == "add":
        valid = True
        validity = prompt_add_car_details()
        if validity:
            prompt_admin_function(user_id)
        else:
            prompt_admin_rental_booking(user_id)
        return
    elif prompt_selection == "delete":
        prompt_delete_car_details()
        prompt_admin_function(user_id)
        return
    elif prompt_selection == "update":
        prompt_update_car_details()
        prompt_admin_function(user_id)
        return
    elif prompt_selection == "back to main menu":
        prompt_admin_function(user_id)
        return
    else:
        print("Invalid selection. Please enter 'Add' or 'Delete' or 'Update'.")
        prompt_admin_rental_booking(user_id)  # Prompt the user again"""


def prompt_add_car_details():
    # Prompt admin to add new cars
    print("Please enter car's detail:")
    make = input("Make: ")
    model = input("Model: ")
    year = input("Year: ")
    mileage = input("Mileage: ")
    min_rent_period = 1
    max_rent_period = 7
    valid = car_management.add_car_to_db(make, model, year, mileage, min_rent_period, max_rent_period)
    return valid


def prompt_delete_car_details():
    # Prompt admin to delete car
    print("Please enter car's ID:")
    car_id = input("Car's ID: ")
    print(car_management.delete_car(car_id))
    return None


def prompt_update_car_details():
    # Prompt admin to add new cars
    print("Please enter car's ID:")
    car_id = input("Car's ID: ")
    mileage = input("Mileage: ")
    availability = input("Availability: ")
    print(car_management.update_car(car_id, mileage, availability))


def view_pending_bookings():
    booking_list = rental_management.get_all_pending_bookings()
    print(booking_list)


def update_booking_status():
    booking_id = input("Please enter Booking ID:")
    status = input("Please enter Booking Status: ")

    rental_management.update_booking_status(booking_id, status)


def prompt_customer_function(user_id):

    prompt_selection = input("Please choose an option to (View/Book) car: ").strip().lower()

    if prompt_selection == "view":
        view_available_car()
        prompt_customer_function(user_id)

    elif prompt_selection == "book":
        prompt_book_car(user_id)
        prompt_customer_function(user_id)

    else:
        print("Invalid selection. Please enter 'View' or 'Book'.")
        prompt_customer_function(user_id)  # Prompt the user again


def view_available_car():
    rental_booking.view_available_cars()


def prompt_book_car(user_id):
    # Prompt customer to book car
    print("Please enter your information below:")
    car_id = input("Car ID: ")
    start_date = input("Start Date(YYYY-MM-DD): ")
    end_date = input("End Date (YYYY-MM-DD): ")
    daily_rate = input("Daily Rate: ")
    rental_booking.book_car(user_id, car_id, start_date, end_date, daily_rate, "pending")


if __name__ == "__main__":
    main()
