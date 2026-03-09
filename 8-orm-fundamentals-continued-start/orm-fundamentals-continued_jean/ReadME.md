
# Django ORM Fundamentals Continued  
*A continuation of the previous lab on Django ORM, Models, Migrations, Templates, Views, and URLs*

In this lab, we take everything we learned previously — **models, migrations, admin, ORM queries, templates, views, and URLs** — and combine them into a real workflow:

👉 **Read data from the database → Pass it to a view → Display it in a template**

This is the foundation of almost every web application.

We begin by copying the previous lab into a new folder:

```
orm-fundamentals-continued_jean
```

This ensures we continue building on the same `Company` model and the same database structure.

---

# Prerequisites

- A virtual environment with packages installed from `requirements.txt`
- The previous lab project copied into a new folder
- Django admin already set up with a superuser
- At least two companies already created in the database from the previous lab

---

# 1. Why We Are Combining Templates, Views, URLs, and the ORM

In the last modules:

- Templates taught us **how to display HTML**
- Views taught us **how to send data to templates**
- URLs taught us **how to access views in the browser**
- The ORM taught us **how to read data from the database**

Now we combine them so we can:

### ✔ Fetch real data from the database  
### ✔ Pass it to a template  
### ✔ Display it on a webpage  

This is the first time we make Django “feel real.”

---

# 2. Setting Up Templates

## Why this step?

Django needs a **base layout** so all pages share the same structure.  
We also need a **page specifically for listing companies**.

This step prepares the HTML foundation for the rest of the lab.

---

## 2.1 Create the global base template

Create:

```
templates/base.html
```

This file defines the layout for all pages.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Django ORM Fundamentals Continued</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f7f7f7;
        }
        header {
            margin-bottom: 30px;
        }
        h1 {
            color: #333;
        }
        ul {
            list-style-type: none;
            padding-left: 0;
        }
        li {
            background: white;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 10px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        a {
            color: #007bff;
        }
    </style>
</head>
<body>

<header>
    <h1>My Software Company</h1>
</header>

{% block content %}
{% endblock %}

</body>
</html>
```

### Why update settings?

Django must know where to find this folder.

In `settings.py`:

```python
'DIRS': [BASE_DIR / "templates"],
```

---

# 3. Creating the Companies List Template

## Why this step?

We need a page where Django will display the companies we fetch from the database.

Inside the `clients` app:

```
clients/templates/clients/list.html
```

Initial version:

```html
{% extends "base.html" %}

{% block content %}
<h2>Companies List</h2>

<ul>
    {% for company in companies %}
        <li class="mb-2">
            <strong>{{ company.name }}</strong>
            <div>{{ company.email }}</div>
        </li>
    {% endfor %}
</ul>

{% endblock %}
```

This template expects a variable called `companies`, which we will send from the view.

---

# 4. Creating the View

## Why this step?

A view is the “middleman” between the database and the template.

- It **fetches data** using the ORM
- It **passes data** to the template

**clients/views.py**

```python
from django.shortcuts import render
from .models import Company

def list_companies(request):
    companies = Company.objects.all()
    return render(request, 'clients/list.html', {'companies': companies})
```

---

# 5. Adding URLs

## Why this step?

Without URLs, we cannot access the view in the browser.

### 5.1 Create clients/urls.py

```python
from django.urls import path
from .views import list_companies

urlpatterns = [
    path('companies/', list_companies, name='companies_list'),
]
```

### 5.2 Include it in the project URLs

**mysoftwarecompany/urls.py**

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('clients.urls')),
]
```

---

# 6. Test the Page

Run:

```bash
python manage.py runserver
```

Visit:

```
http://localhost:8000/clients/companies/
```

You should see the companies from the previous lab.

This confirms:

- Templates work  
- Views work  
- URLs work  
- ORM works  

Now we extend the model.

---

# 7. Adding the `description` Field

## Why this step?

Real companies have descriptions.  
Also, this teaches you how to:

- Add new fields to an existing model  
- Run migrations  
- Update templates to show new data  

This is the **first new field** we add in this lab.

---

### Update the model

**clients/models.py**

```python
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True, default="")

    def __str__(self):
        return self.name
```

### Why TextField?

Because descriptions can be long.  
In SQL, this becomes a `TEXT` column.

---

### Make migrations

```bash
python manage.py makemigrations
```

### Apply migrations

```bash
python manage.py migrate
```

---

# 8. Add Descriptions in the Admin

## Why this step?

We need real data to test our template.

Go to:

```
http://localhost:8000/admin/
```

- Edit each company
- Add a description
- Save

---

# 9. Update Template to Show Descriptions

## Why this step?

We added a new field — now we must display it.

Update **clients/templates/clients/list.html**:

```html
<p>{{ company.description }}</p>
```

Now the page shows:

- Name  
- Email  
- Description  

---

# 10. Adding `created_at` and `updated_at`

## Why this step?

Most real applications track:

- When a record was created  
- When it was last updated  

This teaches you how to use Django’s automatic timestamp fields.

---

### Update the model

```python
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
```

Full model now:

```python
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
```

---

### Make migrations

```bash
python manage.py makemigrations
```

Django asks for a default because existing rows need a timestamp.

Choose:

```
1
```

Press Enter to accept `timezone.now`.

### Apply migrations

```bash
python manage.py migrate
```

---

# 11. Update Template to Show Timestamps

Add:

```html
<p>Created at: {{ company.created_at }}</p>
<p>Information Last updated: {{ company.updated_at }}</p>
```

Now the page shows:

- Name  
- Email  
- Description  
- Created at  
- Updated at  

---

# 12. Challenge: Add a `website` Field

## Why this step?

This teaches you how to add a new field independently and update templates accordingly.

Add to model:

```python
website = models.URLField(blank=True, null=True)
```

Run:

```bash
python manage.py makemigrations
python manage.py migrate
```

Add website URLs in admin.

Update template:

```html
{% if company.website %}
    <p><a href="{{ company.website }}" target="_blank">Visit Website</a></p>
{% endif %}
```

---

# Conclusion

In this lab, we learned how to:

- Combine templates, views, URLs, and ORM queries  
- Display real database records in a webpage  
- Add new fields to a model  
- Run migrations safely  
- Update the admin  
- Update templates to show new data  

This is the core pattern of most web applications:

### **Database → ORM → View → Template → Browser**

