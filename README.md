DevSqlite3==1.2

# Car Rental System (Command Line Interface)

## Overview
This project is a CUI-based Car Rental System developed in Python, using SQLite for data storage. It allows customers view available cars and to book cars.
It also allows admins to manage the car inventory and rental status.

## Project Structure
CarRentalSystem/
│── car_rental.db           # SQLite Database
│── main.py                 # Main entry point
│── car.py                  # Car class (OOP)
│── car_factory.py          # Factory pattern for cars
│── car_management.py       # Manages car operations
│── booking.py              # Booking class (OOP)
│── rental_booking.py       # Handles booking logic
│── rental_management.py    # Admin rental functions
│── user.py                 # User class (OOP)
│── user_factory.py         # Factory pattern for users
│── user_management.py      # Manages user login/register
│── db_config.py            # Database connection
│── requirements.txt        # List of dependencies
│── README.md               # Project documentation
│── docs/                   # Folder for additional documentation
│── release/                # Folder where the ZIP file will be created


## Features
- **User Management**: Register and log in as a customer or admin.
- **Car Management**: Admins can add, update, and delete cars. It also allows admin to manage rental.
- **Rental Booking**: Customers can view available cars and book them.
- **Fee Calculation**: The system calculates rental fees based on duration.

## Technologies Used
- **Python** (Object-Oriented Programming principles)
- **SQLite** (Database management)
- **PyCharm Community** (Development IDE)
- **DBeaver** (Database Browser)
- **Design Pattern Used**: Factory Pattern (for user creation)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Yukimee/oop_assignment1
   cd oop_project

2. Run the system: python main.py


