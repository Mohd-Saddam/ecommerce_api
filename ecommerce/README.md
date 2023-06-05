
Clone this repository to your local machine using the following command:
git clone https://github.com/Mohd-Saddam/ecommerce_api.git

Navigate to the project directory:
    cd ecommerce

Set Up a Virtual Environment (optional but recommended)
Create a virtual environment to isolate the project dependencies:

    python -m venv env


Activate the virtual environment:

For Windows:
    env\Scripts\activate
For macOS/Linux:
    source env/bin/activate


Install Dependencies
Install the project dependencies using pip:
    pip install -r requirements.txt

Apply the database migrations:
    python manage.py makemigrations
    python manage.py migrate


Create a superuser to access the admin interface:

    python manage.py createsuperuser


Run the Server
Start the Django development server:

    python manage.py runserver


Open your web browser and go to http://localhost:8000/ to access the application.