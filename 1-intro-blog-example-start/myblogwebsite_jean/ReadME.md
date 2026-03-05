
# MyBlogWebsite_Jean

A simple Django blog project built from scratch as part of learning Django’s core architecture.  
This project recreates the instructor’s example but with a clean structure, a new project name, and a deeper understanding of each step.

---

## 1. Project Setup

### Create and activate virtual environment
```bash
python -m venv venv
.\venv\Scripts\activate
```

### Install Django
```bash
pip install django==5.2
pip freeze > requirements.txt
```

### Create Django project
```bash
django-admin startproject myblogwebsite_jean .
```

Run the development server to confirm the project works:
```bash
python manage.py runserver
```

---

## 2. Create the Blog App

### Create the app
```bash
python manage.py startapp blogapp
```

### Register the app in `settings.py`
Add this inside `INSTALLED_APPS`:
```python
'blogapp',
```

---

## 3. Create the First View

Inside `blogapp/views.py`:
```python
from django.shortcuts import render

def home(request):
    return render(request, "blogapp/home.html")
```

---

## 4. App URL Configuration

Create `blogapp/urls.py`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
]
```

---

## 5. Project URL Configuration

Inside `myblogwebsite_jean/urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),
]
```

This makes the blog homepage available at:
```
http://127.0.0.1:8000/
```

---

## 6. Create the First Template

Folder structure:
```
blogapp/
    templates/
        blogapp/
            home.html
```

Inside `home.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Jean's Blog</title>
</head>
<body>
    <h1>Welcome to Jean's Blog!</h1>
    <p>This is your first Django template.</p>
</body>
</html>
```

---

## 7. Run the Project

Start the server:
```bash
python manage.py runserver
```

Visit the homepage:
```
http://127.0.0.1:8000/
```

You should see your rendered HTML template.

---

## Status

This project is currently at the stage where:
- The Django project and app are fully set up
- URL routing is configured
- A template is rendered as the homepage

Next steps (coming soon):
- Create the `Post` model
- Apply migrations
- Register the model in the admin
- Display posts dynamically on the homepage
- Build CRUD functionality

