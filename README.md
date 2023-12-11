# Authentication-System-Flask

This is a simple authentication system built with Flask, Flask-SQLAlchemy, Flask-Login, and Flask-Migrate. It provides user registration, login, and logout functionalities along with a sample user database.

## Features

- User Registration: Allow users to create new accounts with a unique username and password.
- User Login: Authenticate users with their credentials and create a session for them.
- User Logout: End the user's session and redirect them to the login page.
- Database: Utilizes SQLAlchemy to interact with a SQLite database.
- User Model: Includes a `Student` and `Company` model with basic user information.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-Migrate
- Flask-Forms

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Sharo-11/Authentication-System-Flask.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Initialize the database:

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

### Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. Open your browser and navigate to `http://127.0.0.1:5000`.

3. Explore the authentication system by visiting the home, login, and register pages.

## Contributing

Contributions are welcome! If you find any issues or have suggestions, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

