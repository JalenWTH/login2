# login2
A second version of my login app. This version uses Django modelforms instead of defining the forms as a class in a separate file. This allows me to practically create different version of a form for specific uses using a model as a base. 

For example, to have a login form that only took an email and password and then a sign up form that took and email, password, name, and phone number I would need to define 2 separate forms on a forms.py file. Now, I don't need a forms.py file and the creation of these 2 separate forms is still necessary but much easier and cleaner to read. 

# How To Run This App 

A virtual environment is not necessary for this app because it uses no special packages; just Django and Python. These instruction assume that you already have Python and the pip package manager installed on your computer

## Installing Django

To install Django you can simply use the pip installation. From your terminal/cmd, change directories to the location of your Python installation and run the command:

`python -m pip install Django==4.0.4` 
It might be "python3" instead of "python" on Linux

Check your Django version with:

`python -m django --version`

If you're using a virtual environment, copy your Python installation into the environment and install Django into the Python installation in your environment


## Creating a Django project and app

From your terminal, cd into the place where you'd like to store this app and run this command to start a Django project:

`django-admin startproject projectname`

This project will have your manage.py file and there will be a subdirectory with the same name as the project. There will be a settings.py file in that subdirectory.

You can start the local Django server using `python manage.py runserver` in your project's main directory to ensure everything is working property so far.

To create an app exit the server in your terminal and run `python manage.py startapp appname`. This will create an app directory in your project.

## Files and directory structure

You will need to create a "templates" directory and a "static" directory in your app directory. They **must** be named templates and static. You'll need to create a couple more directories inside of those as well. This is what your app directory strucutre should be:


```
project
  projectname
    settings.py
    urls.py
    ...
    

  app
    templates
      appname
        #templates go here
    
    static
      appname
        stylesheets
          #stylesheets go here
    
    views.py
    urls.py
    models.py
    admin.py
    ...
```

As you can see, there is a urls.py file for the *project* and a urls.py file for the *app*. In the urls.py file for the *project* you will need to have the following code:

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appname', include('appname.urls')),
]
```

The path to any files will be like: `http://127.0.0.1:8000/appname/home`


After this, simply copy over the code from this repository over to the corresponding files.
