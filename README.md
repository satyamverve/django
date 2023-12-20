# django
## ALL COMMANDS
<install: pip install Django>
<upgrade: pip install --upgrade Django>
<version: python3 -m django --version>
<start_project: django-admin startproject project_name> <!-- this will create the django_admin and use (.) to avoid head_folder -->
<run_server: python3 manage.py runserver>
<create_app: run: python3 manage.py startapp app_name>
<migrate: python3 manage.py migrate>  <!-- run this after modify "views.py" -->
<make_migrations: python manage.py makemigrations members>  <!-- run this after describing "models" in "app" file -->
<!-- after running this command a automated file created nameed "0001_initial.py" at "django/members/migrations/" location -->
<view_sql: python manage.py sqlmigrate members 0001>   <!-- 0001 is the file created after migration -->
<open_shell: python manage.py shell>
<view_records: Member.objects.all().values()>
<NOTE: After every changes we have to run the migration command i.e, "python manage.py makemigrations members" and "python manage.py migrate">
<whitehouse: pip install whitenoise> <!-- use to serve static files(javscripts, styling etcv these are called static files) in Django -->
<collect_static_files: python3 manage.py collectstatic> <!-- This will create a folder "productionfiles"(code is written in settings.py) to collect the static files -->
<create_super_user: python3 manage.py createsuperuser> <!-- for creating SUPERUSER first need to run: python manage.py migrate -->


## windows
Install django: py -m pip install Django
check django Version : django-admin --version
or, python3 -m django --version

<!-- Django Create Project -->
>django-admin startproject project_name
>django-admin startproject project_name . (use dot to ignore head_folder_name if you have created or named your folder otherwise bydefault django create the head_folder_name same as your project_name)
I will named my project "my_tennis_club"

## Run Django project 
>> navigate to head_prpoject_name
>run: py manage.py runserver

run(ubuntu): python manage.py runserver 9000  <!-- you can give your specific port number -->

# CREATE APP
An app is a web application that has a specific meaning in your project, like a home page, a contact form, or a members database.

I will name my app "members"
>run: python manage.py startapp members
>> This will creates a folder called "members" with some files

folder structure:
django
    manage.py
    my_tennis_club/
    members/
        migrations/
            __init__.py
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py


### templates
> create a folder called templates in : members/templates
> create html file inside this folder

#### Modify the view.py
>from django.template import loader
>from django.http import HttpResponse
from django.template import loader
<!-- 
def members(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render()) -->

#### Then run this command:
run: py manage.py migrate

>> Now check the server is running or not, if not then start the server
run: py manage.py runserver

## django Models
> Here we create the tables

> navigate the models.py file in app folder
i.e, django/members/models.py:      //remember django is my head_folder_name
> open it and add tables accroding to your need

## SQLite Database
When we created the Django project, we got an empty SQLite database.
It was created in the my_tennis_club root folder, and has the filename db.sqlite3.
By default, all Models created in the Django project will be created as tables in this database.

## Now after describing Models in members file
run(windows): py manage.py makemigrations members
run(ubuntu): python manage.py makemigrations members


After running this command Django creates a file describing the changes and stores the file in the
>> django/members/migrations/ folder with file name 0001_initial.py

<Note that Django inserts an id field for your tables, which is an auto increment number (first record gets the value 1, the second record 2 etc.), this is the default behavior of Django, you can override it by describing your own id field>

## Create table
Now create the table coz django is not created it,Django will create and execute an SQL statement, based on the content of the new file in the django/members/migrations/ folder.

run(windows): py manage.py migrate
run(ubuntu):  python manage.py migrate

<Note: Now we have Member table in our database>

## View SQL
>To view the SQL statement that were executed from the migration above
run(windows): py manage.py sqlmigrate members 0001
run(ubuntu): python manage.py sqlmigrate members 0001


# Django Insert Data
## Add Records
> Now if we want to add records in members Table
We will use the Python interpreter (Python shell) to add some members to it.
To open a Python shell, type this command:
run(windows): py manage.py shell
run(ubuntu): python manage.py shell

>> In the opened shell write the following:
>>> from members.models import Member

### View the records
>>> Member.objects.all().values()
>>> Member.objects.all()
output: <QuerySet []>  ##This is empty QuerySet Object

>>Now add a record to the table on same opened shell in cmd
>>> member = Member(firstname='Emil', lastname='Refsnes')
>>> member.save()

>> to view the added records in db
>>> Member.objects.all().values()

### Add multiple records
>make a list of Member and execute .save() after each entry
e.g,
>>> m1= Member(firstname='sk', lastname='kr')
>>> m2= Member(firstname='rk', lastname='kr')
>>> m3= Member(firstname='earnst', lastname='young')
>>> m_list=[m1,m2,m3]
>>> for x in m_list:
...     x.save()
>>> Member.objects.all().values() ##this will show the tables with stored details

### Update records
>open shell

>>> from members.models import Member
>>> x = Member.objects.all()[4]
x will now represent the member at index 4

>>> x.firstname ##output will be according to the index provided
>> now update
>>> x.firstname = "Stalikken"
>>> x.save()

>>now check the updated details
run: Member.objects.all().values()


### Delete records
>>> from members.models import Member
>>> x = Member.objects.all()[3]
x will now represent the member at index 4(inddex starts with 0)

>x.delete()

# Django update model
>> To add some more fields in the "my_tennis_club/members/models.py:"
>open models.py
>add more fields or changes
run(ubuntu): python manage.py makemigrations members
<NOTE: After every changes we have to run the migration command i.e, python manage.py makemigrations members>

run: python manage.py migrate

# Display Data
>Create template> modify view> 

>>Now open "http://127.0.0.1:8000/members/hello/" to view the models of Member in browser with the integrated html template

>> Now add another template called "details.html" in the "my_tennis_club/members/templates/details.html:" to list more details about a specific member.

## Add Link in all-members Template
The list in index.html should be clickable, and take you to the details page with the ID of the member you clicked on:
>>open my_tennis_club/members/templates/index.html:
>>update this <li>{{ x.firstname }} {{ x.lastname }}</li> line to 
<li><a href="details/{{ x.id }}">{{ x.firstname }} {{ x.lastname }}</a></li>

### Create new view for the new html file in my_tennis_club/members/views.py file 
### Add URLs in my_tennis_club/members/urls.py file

>> Now run the address bar and check the changes
i.e, http://127.0.0.1:8000/members/hello/

# Django add master Template
>> {% extends "master.html" %}
Extends is same like the concept of inheritence in Oops.
extends template is used to write those html stuffs which have been using in all the templates file.

>> navigate "my_tennis_club/members/templates/" and create "master.html"
<!-- master.html -->
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}{% endblock %}</title>
</head>
<body>

{% block content %}
{% endblock %}

</body>
</html>

>> Modify "index.html" and "details.html" temoplates

>> Now run the address bar and check the changes
i.e, http://127.0.0.1:8000/members/hello/


# main.html (for root path)
> Let's create another a template called main for our root path i.e, "http://127.0.0.1:8000/"
> Navigate to "my_tennis_club/members/templates/" and create "main.html"
> create new view for main in "my_tennis_club/members/views.py"
> Add url for this view in "my_tennis_club/members/urls.py"

## Add link back to main
The members page is missing a link back to the main page, so let us add that in the "index.html" template, in the content block:

# Django 404 (page not found)
> for the page which doesn't exist
> navigate "my_tennis_club/my_tennis_club/settings.py"
set 
<SECURITY WARNING: don't run with debug turned on in production!
"DEBUG = False"
ALLOWED_HOSTS = ['*']
>

## customize the 404 Template
> to customize we have to create new template for "404"
> navigate to "my_tennis_club/members/templates" and create "404.html"

# Django Add Test View
When testing different aspects of Django, it can be a good idea to have somewhere to test code without destroying the main project.
>> Follow the steps for testing:
>> Navigate to "my_tennis_club/members/views.py"
> add view for testing
ex; 
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))

>> navigate to "my_tennis_club/members/urls.py" and add path for testing view

>> navigate: my_tennis_club/members/templates
> create new template called "template.html"

>> Now browse "127.0.0.1:8000/testing/"
and the output should be look like 
Apple
Banana
Cherry

# Django Admin
> It is a CRUD* user interface of all the models.

## Create User
run: python manage.py createsuperuser
>Username:
>Bypass password validation and create user anyway? [y/N]: y
>Superuser created successfully.
>start the server

### Missing Model
The Members model is missing, as it should be, you have to tell Django which models that should be visible in the admin interface.

> Include Member in the Admin Interface
> navigate "my_tennis_club/members/admin.py" --> register the model here

<NOTE: When we set "DEBUG =False" in "settings.py" file then we are unable to see the styling of superadmin while opening the "admin"  in browser
So, to see the admin with styling then set "DEBUG=True" in "settings.py" file.
url: http://127.0.0.1:8000/admin/>  


# Django Admin - Set Fields to Display
> Means we can set what to show on the interface in the browser(same like the concept of response_model in fastapi)

>>To change this to a more reader-friendly format, we have two choices:
1. Change the string representation function, __str__() of the Member Model
2. Set the list_details property of the Member Model

<Method:1 Change the String Representation Function>
> navigate: my_tennis_club/members/models.py

> (add this to the Member class)
def __str__(self):
        return f"{self.firstname} {self.lastname}"

## Set list_display
>navigate: my_tennis_club/members/admin.py
>make a class called MemberAdmin(u make any name)

>> Now check your browser: http://127.0.0.1:8000/admin/members/member/ , here you see the display is changed.
<NOTE: Now from here you can "UPDATE", "CREATE(ADD)", "DELETE" members>


# Django Template Variables
>In Django templates, you can render variables by putting them inside {{ }} brackets:
>navigate: templates/template.html
>use {{}}
ex; <h1>Hello {{ firstname }}, how are you?</h1>

## Create variable in View
>navigate: members/views.py

## Create variables in Template
>navigate: templates/template.html

## Now get the data from a Model
>To get data from the Member model, we will have to import it in the views.py file, and extract data from it in the view.

>> Now we can use the data in the template:
>navigate: templates/template.html
>make changes
ex:
<ul>
  {% for x in mymembers %}
    <li>{{ x.firstname }}</li>
  {% endfor %}
</ul>

<NOTE: We use the Django template tag "{% for %}" to loop through the members.>

### These keywords, if and for, are called "template tags" in Django.
>To execute template tags, we surround them in {% %} brackets.

## Django QuerySet
> A QuerySet is a collection of data from a database.
> A QuerySet is built up as a list of objects.
> QuerySets makes it easier to get the data you actually need, by allowing you to filter and order the data at an early stage.


# Django - Add Static File
>When building web applications, we probably want to add some static files like images or css files.
>navigate: "members/" and create a folder called "static"
>> Under satic folder you can add your "CSS" files(I am naming myfirst) i.e., members/static/myfirst.css
>>> add styles according to your choice 

## Modify the template
> The next step will be to include this css file in a HTML template:
>open: my_tennis_club/members/templates/template.html
>> add 
{% load static %}
and 
<link rel="stylesheet" href="{% static 'myfirst.css' %}">
Restart the server for the changes to take effect: py manage.py runserver


# <NOTES f you plan to deploy your work, you should set DEBUG = False in the settings.py file.>

# Django - Installing WhiteNoise
>Django does not have a built-in solution for serving static files, at least not in production when DEBUG has to be False.
>i.e, we use WhiteNoise
<pip install whitenoise>
>> Modify Settings > django/my_tennis_club/settings.py
>>> add "'whitenoise.middleware.WhiteNoiseMiddleware'," in MIDDLEWARE

## Collect Static Files
### Handle Static Files
> Static files in your project, like stylesheets, JavaScripts, and images, are not handled automatically by Django when DEBUG = False.
> When DEBUG = True, this worked fine, all we had to do was to put them in the static folder of the application.
> When DEBUG = False, static files have to be collected and put in a specified folder before we can use it.

### collecting static files
> Specify STATIC_ROOT property in the settings.py file.
i.e,
STATIC_ROOT = BASE_DIR / 'productionfiles'
STATIC_URL = 'static/'

>run: python manage.py collectstatic

>> run the server and check the result in the browser

# Add a Global CSS File
>Means we want to use the css to our other applications in our project can access
> navigate to the projects root directory(head_project_name)
i,e., django/
>> create a folder (I make mystaticfiles)
i.e, django/mystaticfiles
>>> add a css file in this folder(I make myglobal.css)
i.,e django/mystaticfiles/myglobal.css

> Open the "myglobal.css" and add the styling for global applications in your project
>> Modify Settings > django/my_tennis_club/settings.py > Add a STATICFILES_DIRS list

<NOTE:
In the STATICFILES_DIRS list, you can list all the directories where Django should look for static files.
The BASE_DIR keyword represents the root directory of the project, and together with the / "mystaticfiles", it means the mystaticfiles folder in the root directory.
>

# SEARCH ORDER 
>If you have files with the same name, Django will use the first occurrence of the file.
>The search starts in the directories listed in STATICFILES_DIRS, using the order you have provided. Then, if the file is not found, the search continues in the static folder of each application.

## Modify the Template
>navigate: my_tennis_club/members/templates/template.html
>> add these
{% load static %}
>> And refer to the file like this
<link rel="stylesheet" href="{% static 'myglobal.css' %}">

>run(if not work): python manage.py collectstatic

# Add CSS File to the Project
>> navigate: "django/mystaticfiles" and make a file (I name mystyle.css)

## Modify the master template
>navigate: my_tennis_club/members/templates/master.html
and make changes

### CHECK settings
> Make sure the "settings.py" file contains a STATICFILES_DIRS list with a reference to the mystaticfiles folder on the root directory, and that you have specified a STATICFILES_ROOT folder.

<NOTE: Every time you make a change in a static file, you must run the collectstatic command to make the changes take effect:
run: "python manage.py collectstatic">

>> Now check the changes after running the server  in browser: http://127.0.0.1:8000/members/
(customize the styling according to your need)

# DATABASE CONNECTION(MY-SQL)
>navigate: head_project_name/project_name/__init__.py
>> add pymysql
i.e., 
import pymysql
pymysql.install_as_MySQLdb()

> Navigate to "settings.py" file and add your db details
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST':'localhost',
        'PORT':'8000', <!-- 8000 is the bydefault port of django -->
    }
}


# Django Forms
>Django comes with inbuilt user authentication system.
>To create custjomized django authentication user login we use django forms

## create a file "forms.py"
>navigate: "head_folder_name/project_name/app_name"
i.e., "django/my_tennis_club/members/"

> create a file called "forms.py"
>>from django import forms
>>create a class
>>under class define the fields
SYNTAX: Field_name = forms.FieldType(attributes)

### home.html
> create html file for form in templates folder
>navigate "my_tennis_club/members/templates/"
>create "home.html"
e.x: 
<form action = "" method = "post">
	{% csrf_token %}
	{{form }}
	<input type="submit" value=Submit">
</form>

### views.py
>navigate "views.py" 
>create view for forms
e.x;
from django.shortcuts import render
from .forms import InputForm
<!-- create your views here -->
def home_view(request):
	context ={}
	context['form']= InputForm()
	return render(request, "home.html", context)




# UBUNTU IP HOSTING
>> navigate project/settings.py
>> add > ALLOWED_HOSTS = ['Local_IP_address', 'localhost', '127.0.0.1']
>> command to find Local_IP_address > <ifconfig>
<python manage.py migrate>
<python manage.py collectstatic>

>> Now run the django development server
<python manage.py runserver 0.0.0.0:8000>

>> Access the Django project from browser by others
<http://your_local_ip:8000
>

