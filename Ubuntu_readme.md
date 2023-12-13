# Django
Django is a framework for building web applications and it is mainly used with server sides ie, back-end .

## Let's create a Django-admin
1. make vurtul environment
2. make a project directory where you want to store your project
3. navigate to that dir
>  pip install django
5. django-admin startproject project_name
6. This will create a folder with your project_name
7. below is the folder structure
![Alt text](django.png)

8. Look at the photo there is 2 folders created with "project" 
9. To ignore the upper one dir run this command:
> django-admin startproject project_name .

### working of all file names
1. __init__.py //It defines our directory as the package
2. settings.py //define our application settings
3. urls.py     //define urls of our application
4. asgi.py and wsgi.py are used for deployement

Notes: By-default django uses port: 8000

> django-admin //This will provide you all the commands of django

## command to run SERVER:
> django-admin startproject project_name
// This will give you error if you didn't configured your setings in "settings.py" file

> python manage.py runserver 9000 
// port number is optional and this command you are directly running manage.py. So, you didn't going to 
get any error

## Now configure setttings.py
Navigate to settings.py

'''
INSTALLED_APPS = [
    'django.contrib.admin',
    // gives admin interface to managing our data

    'django.contrib.auth',
    //used for authenticating users

    'django.contrib.contenttypes',
    //
    'django.contrib.sessions',
    //It is the temporary memory on the server for managing users data
    //when we made api's with django we did,t use the sessions with app

    'django.contrib.messages',
    //used to displayig one time notification to the user

    'django.contrib.staticfiles',
    //used to serving static files like images, css files and etc.
]
'''

## Now run the app(with your own app_name) to create your app folder structure
> python manage.py startapp app_name

### This will create a new folder at the bottom of your directory
#### Go to that folder called app_name
1.migrations
>> There is migrations folder: used to generating database tables

2. admin.py
>> Here we define how the admin interface for this app is going to look like.

3. apps.py
>> Here we configure this app 

4. models.py
>> Here we define tables

5. tests.py
>> Here we write our unit tests

6. views.py
>> It is the request handeller

###### apps.py
>> Every time if we have created the new app then we have to configure this in our settings

>>settings.py>> Under the INSTALLED_APPS section add >> 'app_name'

###### writing views
>> A view function is a function that takes a "request" and returns "response"
             -->
i.e, request       response       
             <--

i.e, request handler
>> make your functions for creating routes
e.g, '''
    def say_hello(request):
        return HttpResponse('Hello World')
    '''

###### Mapping URLs to views

>> go to "app_name" folder 
>> create new file "urls.py"
>> add your URLconf i.e, routes
e.g., '''
      # url configuration ie., URLconf
      urlpatterns = [
          path('playground/hello', views.say_hello())
      ]
      '''

>>> After creating every app's you have to add the URLconf , follow the instructuions below:
> go to project_name/urls.py
> under "urlpatterns" add the rout for your app(this should be done only once for creating 1 app)
i.e, 
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls'))
]
'''
Here, "playground" rout works as the prefix for our app routes(app_name/urls.py urlpatterns)

NOTE: We always end our routes with a forward slash i.e, "/"

######  Using Templates
>> go to app_name
>> create a folder called "templates" 
>> create html file ex; index.html  