import sqlite3


def create_tables():
    # Connect to SQLite database (creates `car_rental.db` if it doesn't exist)
    connection = sqlite3.connect("car_rental.db")
    cursor = connection.cursor()

    # Create a table for storing car details
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            make TEXT NOT NULL,
            model TEXT NOT NULL,
            year INTEGER NOT NULL,
            mileage INTEGER NOT NULL,
            available INTEGER CHECK(available IN (0, 1)) NOT NULL,
            min_rent_period INTEGER NOT NULL,
            max_rent_period INTEGER NOT NULL
        );
    ''')

    # Create a table for storing user's details
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT CHECK(role IN ('customer', 'admin')) NOT NULL
        );
    ''')

    # Create a table for storing bookings details
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
        booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        car_id INTEGER,
        start_date TEXT NOT NULL,
        end_date TEXT NOT NULL,
        total_cost INTEGER,
        status TEXT CHECK(status IN ('pending', 'approved', 'rejected')) DEFAULT 'pending',
        FOREIGN KEY (user_id) REFERENCES Users(user_id),
        FOREIGN KEY (car_id) REFERENCES Cars(car_id)
        );
    ''')

    # Create a table for storing payments details for future
    """cursor.execute('''
        CREATE TABLE IF NOT EXISTS payments (
        payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        booking_id INTEGER,
        amount REAL NOT NULL,
        payment_date TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (booking_id) REFERENCES Bookings(booking_id)
        )
    ''')"""

    # Call these methods to create sample databases of users, cars and bookings for testing purpose
    # initial_user_DB(cursor)
    # initial_car_db(cursor)
    # initial_booking_db(cursor)

    # Commit and close connection
    connection.commit()
    connection.close()

    print("Database setup complete!")


def initial_user_DB(cursor):
    # Insert data into users table (Initial data for testing purposes)
    users = [
        ('Srijan', 'srijan@gmail.com', "sss111", "admin"),
        ('Kwang', 'kwang@gmail.com', "kkk111", "admin"),
        ('Katherina', 'katherina@gmail.com', "kkk111", "customer"),
        ('Micheal', 'micheal@gmail.com', "mmm111", "customer"),
        ('Jesslyn', 'jessly@gmail.com', "jjj111", "admin"),
        ('Jason', 'jason@gmail.com', "jjj111", "customer")
    ]

    for user in users:
        cursor.execute('''INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)''', user)


def initial_car_db(cursor):
    # Insert data into cars table (Initial data for testing purposes)
    cars = [
        ('Proton', 'Saga', 2019, 49000, True, 1, 7),
        ('Proton', 'Wira', 2020, 90000, True, 1, 7),
        ('Proton', 'Mewa', 2018, 5000, True, 1, 7),
        ('Perodua', 'Alza', 2022, 65000, True, 1, 7),
        ('Perodua', 'Myvi', 2023, 32000, True, 1, 7),
        ('Perodua', 'Myci', 2024, 4000, True, 1, 7)
    ]

    for car in cars:
        cursor.execute('''INSERT INTO cars (make, model, year, mileage, available, min_rent_period, max_rent_period)
                                  VALUES (?, ?, ?, ?, ?, ?, ?)''', car)


def initial_booking_db(cursor):
    # Insert data into bookings table (Initial data for testing purposes)
    bookings = [
        (9, 15, '2025-02-01', '2025-02-05', 200, 'pending'),
        (10, 23, '2025-01-31', '2025-02-04', 200, 'pending'),
        (11, 24, '2025-02-05', '2025-02-07', 100, 'pending'),
    ]

    for booking in bookings:
        cursor.execute('''INSERT INTO bookings (user_id, car_id, start_date, end_date, total_cost, status) 
                                    VALUES (?, ?, ?, ?, ?, ?)''', booking)


# Run the script to create tables
if __name__ == "__main__":
    create_tables()
