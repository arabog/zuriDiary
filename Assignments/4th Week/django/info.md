# https://docs.djangoproject.com/en/4.0/intro/tutorial01/

# https://docs.djangoproject.com/en/4.0/topics/install/#installing-official-release

# python3 -m pip install Django

Verifying¶
To verify that Django can be seen by Python, type python3 from your shell. 
Then at the Python3 prompt, try to import Django:

>>> import django
>>> print(django.get_version())

or:

python3 -m django --version

Creating a project
django-admin startproject mysite

The development server
python3 manage.py runserver

Now that the server’s running, visit http://127.0.0.1:8000/ with your 
web browser. You’ll see a “Congratulations!” page, with a rocket 
taking off. It worked!


Changing the port 
By default, the runserver command starts the development server on the internal IP at port 8000.

If you want to change the server’s port, pass it as a command-line argument. For instance, this command starts the server on port 8080:

$ python manage.py runserver 8080

If you want to change the server’s IP, pass it along with the port.

$ python manage.py runserver 0:8000
0 is a shortcut for 0.0.0.0. 

Creating the Polls app
To create your app, make sure you’re in the same directory as manage.py and type this command:

python3 manage.py startapp polls

Write your first view
Let’s write the first view. Open the file polls/views.py and put the following Python code in it:

from django.http import HttpResponse

def index(request):
          return HttpResponse("Hello, world. You're at the polls index.")

This is the simplest view possible in Django. To call the view, we need to map it to a URL - and for this we need a URLconf.

To create a URLconf in the polls directory, create a file called polls/urls.py.

In the polls/urls.py file include the following code:
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

The next step is to point the root URLconf at the polls.urls module. In mysite/urls.py, add an import for django.urls.include and insert an include() in the urlpatterns list, so you have:

<!-- mysite/urls.py -->
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

The include() function allows referencing other URLconfs. Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.

The idea behind include() is to make it easy to plug-and-play URLs. Since polls are in their own URLconf (polls/urls.py), they can be placed under “/polls/”, or under “/fun_polls/”, or under “/content/polls/”, or any other path root, and the app will still work.

When to use include()

You should always use include() when you include other URL patterns. admin.site.urls is the only exception to this.

You have now wired an index view into the URLconf. Verify it’s working with the following command:

python3 manage.py runserver

Go to http://localhost:8000/polls/ in your browser, and you should see the text “Hello, world. You’re at the polls index.”, which you defined in the index view.

Page not found?

If you get an error page here, check that you’re going to http://localhost:8000/polls/ and not http://localhost:8000/.