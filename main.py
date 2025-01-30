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
    user = user_management.add_user_to_db(name, email, password, role)
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

    prompt_selection = input("Please choose an option to (Add/Delete/Update) car: ").strip().lower()

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
        prompt_admin_function(user_id)  # Prompt the user again


def prompt_add_car_details():
    # Prompt admin to add new cars
    print("Please enter car's detail:")
    make = input("Make: ")
    model = input("Model: ")
    year = input("Year: ")
    mileage = input("Mileage: ")
    min_rent_period = 1
    max_rent_period = 7
    car_management.add_car_to_db(make, model, year, mileage, min_rent_period, max_rent_period)


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
    car_id = input("Car's ID: ")
    start_date = input("Start Date: ")
    end_date = input("End Date (YYYY-MM-DD): ")
    daily_rate = input("Daily Rate (YYYY-MM-DD): ")
    rental_booking.book_car(user_id, car_id, start_date, end_date, daily_rate, "pending")


# Fetch all pending bookings
print("Pending Bookings:", rental_management.get_all_pending_bookings())

# Approve a booking (replace 1 with an actual booking ID)
print(rental_management.update_booking_status(1, "approved"))

# Reject a booking
print(rental_management.update_booking_status(2, "rejected"))


"""if __name__ == "__main__":
    main()"""

