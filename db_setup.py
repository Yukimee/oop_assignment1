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
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payments (
        payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        booking_id INTEGER,
        amount REAL NOT NULL,
        payment_date TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (booking_id) REFERENCES Bookings(booking_id)
        )
    ''')

    # Commit and close connection
    connection.commit()
    connection.close()

    print("Database setup complete!")


# Run the script to create tables
if __name__ == "__main__":
    create_tables()
