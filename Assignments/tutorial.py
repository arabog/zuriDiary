# to check all the python packages installed
pip freeze 

# to install virtual environment
pip install virtualenv pipenv

# create a virtual environment
virtualenv zurienv 

# activate a virtual env
source zurienv\scripts\activate

# install django
pip install django

# start a project
django-admin startproject zuriproject

# run server
python3 manage.py runserver

# resolve migration error
python3 manage.py migrate

# new app
python3 manage.py startapp appname


# create admin details
python3 manage createsuperuser
# provide ur desired username & password

# model samples
class Schools(models.Model):
          name = models.CharField(max_length=23)
          address = models.CharField(max_length=23)

# to apply d changes md in d model
python3 manage.py makemigrations

# to enforce d migration
python3 manage.py migrate

# import it where u want to use it eg admin.py
from .models import Schools

admin.site.register(Schools)

