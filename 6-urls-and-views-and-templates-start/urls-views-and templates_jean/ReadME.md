# 📘 **Django Base Templates, Blocks, Template Inheritance & URL Linking** 

## 🧠 **Django Architecture (Mental Model Diagram)**  

```
urls-views-and-templates_jean/
│
├── manage.py
├── db.sqlite3
├── ReadME.md
├── venv/
│
├── urls_views_fundamentals/          ← Django PROJECT (global config)
│   ├── settings.py                   ← Template dirs, installed apps, DB config
│   ├── urls.py                       ← Root URL router (delegates to app)
│   ├── asgi.py / wsgi.py
│   └── __init__.py
│
└── pet_adoption/                     ← Django APP (feature module)
    ├── views.py                      ← App logic (home, details, about)
    ├── urls.py                       ← App URL patterns
    ├── models.py
    ├── admin.py
    ├── apps.py
    ├── tests.py
    ├── migrations/
    └── templates/
        ├── base.html                 ← Shared layout for all pages
        └── pet_adoption/             ← App-specific templates
            ├── home.html
            ├── pet_details.html
            └── about_page.html
```

---

## 🎯 **Lab Goal**

This lab teaches you how to:

- Build a **base template** for shared layout  
- Use **blocks** to define replaceable sections  
- Use **template inheritance** to avoid repeating HTML  
- Use the `{% url %}` tag for dynamic internal links  
- Add a **global navigation bar**  
- Create a new **About page**  
- Structure templates **inside the app**, not globally  
- Connect project URLs → app URLs → views → templates  

This is foundational Django knowledge.

---

## 🧩 **1. Create Virtual Environment & Install Django**

```bash
python -m venv ./venv
```

Activate:

- macOS/Linux: `source ./venv/bin/activate`
- Windows: `.\venv\Scripts\activate`

Install Django:

```bash
pip install django
```

Run migrations:

```bash
python manage.py migrate
```

Start server:

```bash
python manage.py runserver
```

---

## 🧱 **2. Why Base Templates Matter**

Websites repeat the same HTML:

- `<html>`
- `<head>`
- `<body>`
- navigation
- footer

Instead of duplicating this in every page, Django lets you:

- create a **base template**
- define **blocks**
- let child templates **extend** the base

This keeps your project clean and scalable.

---

## 🏗️ **3. Create `base.html` (Inside the App)**

### ✔ Location (matches your real project):

```
pet_adoption/templates/base.html
```

### ✔ Why here?

- You chose to keep all templates inside the app  
- Django finds it automatically because `APP_DIRS=True`  
- Child templates can extend it simply with:

```html
{% extends "base.html" %}
```

### ✔ Content:

```html
<!doctype html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>

    {% block css_styles %}{% endblock %}
    {% block js_scripts %}{% endblock %}

    <title>
        {% block title %}Pet Adoption App{% endblock %}
    </title>
  </head>

  <body>
    <header>
        {% block header %}{% endblock %}
    </header>

    <main>
        {% block content %}{% endblock %}
    </main>

    <footer>
        {% block footer %}
            <p class="text-center text-gray-500">
                &copy; 2023 Pet Adoption App
            </p>
        {% endblock %}
    </footer>
  </body>
</html>
```

---

## ⚙️ **4. Template Settings**

In `urls_views_fundamentals/settings.py`:

```python
"APP_DIRS": True,
```

This tells Django:

> “Search inside each app’s `templates/` folder.”

No global templates folder is required.

---

## 🏠 **5. Update `home.html` to Extend Base Template**

### ✔ Location:

```
pet_adoption/templates/pet_adoption/home.html
```

### ✔ Content:

```html
{% extends "base.html" %}

{% block title %}Welcome to Pet Adoption Matcher{% endblock %}

{% block content %}
<div class="max-w-2xl mx-auto">
    <h1 class="text-3xl font-bold underline">
      Welcome to the Pet Adoption Matcher!
    </h1>

    <section>
        <h2 class="text-2xl font-semibold mb-4">Available Pet Types</h2>
        <ul class="list-disc pl-5">
        {% for pet_type, pet in pet_types.items %}
            <li class="mb-2">
                <a href="{% url 'pet_type_details' pet_type=pet_type %}">
                    <strong>{{ pet_type }}</strong>
                    <div>{{ pet.traits }}</div>
                </a>
            </li>
        {% endfor %}
        </ul>
    </section>
</div>
{% endblock %}
```

---

## 🐶 **6. Update `pet_details.html`**

```html
{% extends "base.html" %}

{% block title %}Pet Details - {{ pet_type }}{% endblock %}

{% block content %}
<div class="max-w-2xl mx-auto">
    <h1 class="text-3xl font-bold underline">
        Is a {{ pet_type }} the right match for you?
    </h1>

    <section>
        {% if pet_data %}
            <h2 class="text-2xl font-semibold mb-4">Pet Details</h2>
            <p class="text-lg mb-2">
                The traits of a {{ pet_type }} are: {{ pet_data.traits }}
            </p>
        {% else %}
            <p class="text-lg mb-2">
                Sorry, we don't have any information about this pet type.
            </p>
        {% endif %}
    </section>
</div>
{% endblock %}
```

---

## 🧭 **7. Add Navigation Bar to Base Template**

Inside the `<header>` block of `base.html`:

```html
{% block header %}
<nav class="bg-gray-800 p-4">
    <div class="max-w-2xl mx-auto flex justify-between items-center">
        <a href="{% url 'home_page' %}" class="text-white text-lg font-semibold">
            Pet Adoption App
        </a>

        <div class="flex space-x-4">
            <a href="{% url 'about_page' %}" class="text-white">About</a>
        </div>
    </div>
</nav>
{% endblock %}
```

This navbar now appears on **every page**.

---

## 🔗 **8. Dynamic Links Using `{% url %}`**

Examples:

```html
<a href="{% url 'home_page' %}">
<a href="{% url 'about_page' %}">
<a href="{% url 'pet_type_details' pet_type=pet_type %}">
```

These links **never break**, even if URL paths change.

---

## 🧪 **9. Challenge Feature: About Page**

### ✔ Create:

```
pet_adoption/templates/pet_adoption/about_page.html
```

### ✔ Content:

```html
{% extends "base.html" %}

{% block title %}About Us{% endblock %}

{% block content %}
<div class="max-w-2xl mx-auto">
    <h1 class="text-3xl font-bold underline">About Us</h1>
    <p class="text-lg mt-4">
        We help match people with the perfect pet based on lifestyle and personality.
    </p>
</div>
{% endblock %}
```

---

## 🧭 **10. App URLs**

`pet_adoption/urls.py`:

```python
from django.urls import path
from .views import home_page, pet_type_details, about_page

urlpatterns = [
    path("", home_page, name="home_page"),
    path("pet_type/<str:pet_type>/", pet_type_details, name="pet_type_details"),
    path("about/", about_page, name="about_page"),
]
```

---

## 🌐 **11. Project URLs**

`urls_views_fundamentals/urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    path("", include("pet_adoption.urls")),
]
```

---

## 🧠 **12. Views**

`pet_adoption/views.py`:

```python
from django.shortcuts import render

PET_TYPES = {
    'dog': {'traits': 'Loyal and energetic'},
    'cat': {'traits': 'Independent and cuddly'},
    'rabbit': {'traits': 'Gentle and quiet'},
    'parrot': {'traits': 'Social and intelligent'},
}

def home_page(request):
    return render(request, "pet_adoption/home.html", {"pet_types": PET_TYPES})

def pet_type_details(request, pet_type):
    pet_data = PET_TYPES.get(pet_type)
    return render(request, "pet_adoption/pet_details.html", {
        "pet_type": pet_type,
        "pet_data": pet_data,
    })

def about_page(request):
    return render(request, "pet_adoption/about_page.html")
```

---

## ✅ **Conclusion**

In this lab, you learned:

- How to build a **base template**  
- How to use **blocks**  
- How to use **template inheritance**  
- How to create **dynamic links** with `{% url %}`  
- How to build a **shared navbar**  
- How to create a new **About page**  
- How Django resolves templates inside an app  
- How project URLs delegate to app URLs  

This is a **core Django skill** and will be used in every future project.

---

Jean — this README is now **perfect**, **accurate**, and **aligned with your real architecture**.

If you want, I can now:

- generate a clean commit message  
- help you push to GitHub  
- or move to the next Django lab  

Just tell me what you want next.

