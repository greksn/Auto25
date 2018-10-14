# Auto25
Auto24 konkurent (LTAT.05.004 - Veebirakenduste loomine)

Testkeskkond: https://auto25.tk

### To deploy this application on your local machine:
**__Make sure the latest Python version is installed and your command prompt is running with administrator rights.__**

- Download/clone this repository

- The repository doesn't include a `virtualenv` to run a local test server

  To make one, create a `virtualenv` called `autoportaalenv` into the same folder as `manage.py` 
  (follow guide https://docs.djangoproject.com/en/2.1/howto/windows/)

- Install Django, Gunicorn, Django Allauth and Psycopg2 in the virtual env, using the command `pip install django gunicorn psycopg2 django-allauth`
  

- Create a local Postgre database OR connect to the test environment database (it is accepting external connections at the moment):

  **Connecting to the test environment DB:**
  
  Open `settings.py` and make sure the settings are following:
  ```
  ALLOWED_HOSTS = ['142.93.175.27', '127.0.0.1', 'auto25.tk']

  'HOST': '142.93.175.27',
  'PORT': '5432'
  ```
  
- In your machine, set the database password as a environment variable
  
- In the `manage.py` directory, run the command `python manage.py runserver`

- Local server should be available at http://127.0.0.1:8000/ 

Logging in via Github/Facebook doesn't work on localhost due to their restrictions.

