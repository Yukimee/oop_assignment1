import car_management
import rental_management
import user_management
from db_setup import create_tables


def prompt_user_to_login():
    # Prompt user to login.
    print("Welcome to Car Rental Services! Please enter email and password to login.")
    email = input("Email: ")
    password = input("Password: ")

    user = user_management.get_user_from_db(email, password)

    if user:
        print(f"Login successful! Welcome, {user.get_name()} ({user.get_role()})")
        return user
    else:
        print("Invalid email or password. Please register if you don't have an account.")
        return None


def prompt_user_to_register():
    # Prompt user to register.
    print("Welcome to Car Rental Services! Please enter your details to register.")
    name = input("Name: ")
    email = input("Email: ")
    password = input("Password: ")
    role = input("Role (Customer/Admin): ").strip().lower()

    if role not in ["customer", "admin"]:
        print("Invalid role. Please enter 'Customer' or 'Admin'.")
        return None

    success = user_management.add_user_to_db(name, email, password, role)
    if success:
        return prompt_user_to_login()
    return None


def validate_role(user):
    # Redirect user based on their role.
    if user.get_role() == "admin":
        prompt_admin_function(user)
    elif user.get_role() == "customer":
        prompt_customer_function(user)


def main():

    create_tables()
    while True:
        print("Please choose an option: \n(1) Login \n(2) Register\n")
        choice = input("Number: ")

        if choice == "1":
            user = prompt_user_to_login()
            if user:
                validate_role(user)
        elif choice == "2":
            user = prompt_user_to_register()
            if user:
                validate_role(user)
        else:
            print("Invalid selection. Please enter '1' or '2'.")


def prompt_admin_function(user_id):
    # Prompt admin to select a function
    print("Please select a function: \n(1) Rental Management \n(2) Car Management\n")
    choice = input("Number: ")

    if choice == "1":
        prompt_admin_rental_management(user_id)
        prompt_admin_function(user_id)
        return
    elif choice == "2":
        prompt_admin_car_management(user_id)
        prompt_admin_function(user_id)
        return
    else:
        print("Invalid selection. Please enter '1' or '2'.")
        prompt_admin_function(user_id)  # Prompt the user again"""


def prompt_admin_rental_management(user_id):
    # Prompt admin to select a function from rental management
    print("Please select a function: \n(1) View Pending Booking \n(2) Update Booking Status "
          "\n(3) Back to Admin Function Menu")
    choice = input("Number: ")

    if choice == "1":
        view_pending_bookings()
        prompt_admin_function(user_id)
        return
    elif choice == "2":
        update_booking_status()
        prompt_admin_function(user_id)
        return
    elif choice == "3":
        prompt_admin_function(user_id)
        return
    else:
        print("Invalid selection. Please enter '1' or '2' or '3'.")
        prompt_admin_rental_management(user_id)  # Prompt the user again"""


def prompt_add_car_details(valid):
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
    print(car_management.delete_car_from_db(car_id))
    return None


def prompt_update_car_details():
    # Prompt admin to add new cars
    print("Please enter car's ID:")
    car_id = input("Car's ID: ")
    mileage = input("Mileage: ")
    availability = input("Availability: ")
    print(car_management.update_car_to_db(car_id, mileage, availability))


def prompt_admin_car_management(user_id):
    # Prompt admin to select a function from car management
    print("Please select a function: \n(1) Add Car \n(2) Delete A Car \n(3) Update Car Mileage "
          "\n(4) Back to Admin Function Menu")
    choice = input("Number: ")

    if choice == "1":
        valid = True
        validity = prompt_add_car_details(valid)
        if validity:
            prompt_admin_function(user_id)
        else:
            prompt_admin_car_management(user_id)
        return
    elif choice == "2":
        prompt_delete_car_details()
        prompt_admin_function(user_id)
        return
    elif choice == "3":
        prompt_update_car_details()
        prompt_admin_function(user_id)
        return
    elif choice == "4":
        prompt_admin_function(user_id)
        return
    else:
        print("Invalid selection. Please enter '1' or '2' or '3' or '4'.")
        prompt_admin_car_management(user_id)  # Prompt the user again"""


def view_pending_bookings():
    rental_management.get_all_pending_bookings()


def update_booking_status():
    booking_id = input("Please enter Booking ID:")
    status = input("Please enter Booking Status: ")

    rental_management.update_booking_status(booking_id, status.strip().lower())


def prompt_customer_function(user):
    print("Please choose an option: \n(1) View Available Cars \n(2) Book Car\n")
    choice = input("Number: ")

    if choice == "1":
        car_list = view_available_car()

        if car_list:
            prompt_customer_function(user)

    elif choice == "2":
        prompt_book_car(user.get_user_id())
        prompt_customer_function(user)

    else:
        print("Invalid selection. Please enter '1' or '2'.")
        prompt_customer_function(user)  # Prompt the user again


def view_available_car():
    car_list = car_management.view_available_cars()
    return car_list


def prompt_book_car(user_id):
    # Prompt customer to book car
    print("Please enter your information below:")
    car_id = input("Car ID: ")
    start_date = input("Start Date(YYYY-MM-DD): ")
    end_date = input("End Date (YYYY-MM-DD): ")
    daily_rate = input("Daily Rate: ")
    booking_detail = rental_management.book_car(user_id, car_id, start_date, end_date, daily_rate, "pending")
    return booking_detail


if __name__ == "__main__":
    main()
