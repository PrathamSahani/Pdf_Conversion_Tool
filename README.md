### Pdf_Conversion_Tool
📄 The real-time PDF conversion tool offers over 12 powerful functionalities to simplify your document management. 🔄 You can effortlessly convert PDFs to various formats and vice versa, making it a versatile solution for all your needs. With a proper login and register system, users gain unlimited access to the tool’s features, ensuring a seamless and efficient experience. 🚀 Say goodbye to file format hassles and enjoy ultimate convenience!
Demo Video <a href="https://www.loom.com/share/d8ab4f3d42cc453587b076a87b76dccb" > Click Here </a>
 
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

### Set Up Your Virtual Environment 
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

### Start the Server
Finally, start the Django development server:
```bash
python manage.py runserver

