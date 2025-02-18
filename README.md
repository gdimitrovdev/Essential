# Description
This project is a daily task manager, allowing user to list one-time task, reoccuring tasks and store important files.

# How to run
1. Clone the repository

    ```
    git clone git@github.com:gdimitrovdev/Essential.git
    ```
    or
    ```
    git clone https://github.com/gdimitrovdev/Essential.git
    ```

2. Create a virtual environment

    ```
    python -m venv venv
    ```

3. Activate the virtual environment
    
    Windows:
    ```
    .\venv\Scripts\activate
    ```
    Linux/Mac:
    ```
    source ./venv/bin/activate
    ```

4. Install the requirements

    ```
    pip install -r requirements.txt
    ```

5. Setup environmental variables
    - Copy the .env.sample file into a new .env file and fill it out. The SECRET_KEY can be any value you want.
    - If you want to use a custom PostgreSQL database instead of an in-memory one, change the DEBUG environmental variable to False and set the database environmental variables as well.

6. Run migrations

    ```
    python manage.py migrate
    ```

7. Run the project

    ```
    python manage.py runserver
    ```

# How to use
Open localhost:8000 or 127.0.0.1:8000 in your browser. If you want to use a different port, you need to run this instead:

    ```
    python manage.py runserver <desired_port>
    ```