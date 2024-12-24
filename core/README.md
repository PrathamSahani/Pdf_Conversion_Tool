 Follow the steps below to set up and run the project.
   Make sure Python is installed on your system. Download it from the [official Python website](https://www.python.org/downloads/).

   ```bash
   # Check if Python is installed
   python --version

2. **setup Django**

 ```bash
   #  Django is installed
   pip install django

   # Verify the installation
   django-admin --version
```

### Set Up Your Virtual Environment (Optional)
To avoid dependency issues, it is recommended to create a virtual environment. Here's how:
1. Open the extracted folder in **VS Code**.
2. In the terminal, create the virtual environment:
   ```bash
   python -m venv env
   ```
3. Activate the virtual environment:
   ```bash
   .\env\Scripts\activate.ps1
   ```

### Install Dependencies
Once inside the virtual environment, install Django:
```bash
pip install django
```

### Navigate to the Project Directory
Change to the `core` directory where the `manage.py` file is located:
```bash
cd core
```

### Migrate the Database
Apply database migrations using the following commands:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Create a Superuser 
You can create a superuser to manage the database via Django's admin panel: 
```bash
python manage.py createsuperuser
```
- Follow the prompts to add a username and password of your choice. To access the admin panel you can visit to http://127.0.0.1:8000/admin/ url and see database.


### Start the Server
Finally, start the Django development server:
```bash
python manage.py runserver
