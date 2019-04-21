Going through the Django tutorial on Udemy
Here are some notes to help you out

# The Django Work Flow


## Set up virtual env (venv or Conda)
1. Download Conda (sets up virtual envs and manages packages for different languages)
2. conda create --name <myDjangoEnv> django
	conda info --envs
3. source activate <myDjangoEnv>
4. source deactivate


## Create Project
1. ```$ django-admin startproject <project_name>```
2. ```$ cd <project>```
3. Create universal folders in parent directory
    * templates (html)
    * static (js, css, images)
4. Add these folders/directories (for Django to scan) to settings.py
    * TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")
    * and to TEMPLATES list dict key 'DIRS'
5. urls.py takes care of routing (probably to apps)
    * may want to create an app with a view for landing page
    * can redirect to urls.py file of apps with include(\*.urls)


## Create Apps inside Project
1. ```$ python manage.py startapp <app_name>```
    * add to INSTALLED_APPS list in settings.py
2. views.py allows you to do stuff (grab/verify/process data) and specify what to return
    * def users(request):
    * return render(request, 'index.html', context=user_dict)
    * url.py -> this -> templates/.../*.html
3. Configure html
    * create base html files in templates dir and customize with templating
        1. {{}} for static content
        2. {% %} for things like loops and other logic


## Create Models (in App)
1. Create class in models.py
    1. class User(models.Model):
    2. define __str__(self) for the class (should be the key value)
2. register it in admin.py
    1. "admin.site.register(User)"
3. Actually take the model and make it real
	  1. ```$ python manage.py migrate``` (make sure app is in settings.py under INSTALLED_APPS list)
	  2. ```$ python manage.py makemigrations <app_name>```
	  3. ```$ python manage.py migrate```
3. Can create values by importing models
    * User.objects.get_or_create(email=fake_email)[0]
4. Can grab the values from views.py
	  * "User.objects.order_by('email')"


## Using Built-In Admin Page (must have at least 1 model migrated)
1. python manage.py createsuperuser
2. go to the local page + '/admin'
    * sign in and look at data


## Check stuff in shell
python manage.py shell
print(Topic.objects.all())
t = Topic(top_name="Social Network")
t.save()


# Notes

## Relative templates
1. <a href="{% url 'var_name_in_app_urls.py:view_name' %}">Other page</a>
    1. 'admin:index' exists by default
    2. 'index' exists by default

## Reusable templates
### Example Reusable HTML File
```
<links to JS, CSS>
<bunch of html like navbars>
	<body>
		{% block body_block %}
		{% endblock %}
	</body>
<footer html/>
```

### Example HTML File
```
<!DOCTYPE html>
{% extends "base.html" %}
{% block body_block %}
<unique html>
{%endblock}
```

## Create data with Faker
```$ pip install Faker --user```

## Django Framework
Model, Template, Views

## HTML Template files
{% load static %}

## Model -> Forms
Can accept some, all, or exclude some
1. fields()
2. __all__
3. exclude=()


Django Forms function as a "model" (validator) for form pages. In fact, they can even be used as modes, via forms.ModelForm


* LEFT OFF AT Lecture 142. Probably using Node over Django but learned a lot
