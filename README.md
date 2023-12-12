# django

## windows
Install django: py -m pip install Django
check django Version : django-admin --version

<!-- Django Create Project -->
django-admin startproject project_name . (use dot to ignore head folder)
I will named my project "my_tennis_club"

## Run Django project 
>> navigate to project_name
run: py manage.py runserver

# CREATE APP
An app is a web application that has a specific meaning in your project, like a home page, a contact form, or a members database.

I will name my app "members"
run: py manage.py startapp members
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