# 📘 Intro to Django & Backend Web Development — Lesson Summary

This lesson continues our introduction to Django by exploring how Django manages data, models, migrations, and the admin interface. By the end of this session, we created a fully functional blog app capable of storing and managing posts in a database.

---

## 🚀 What We Accomplished Today

### 1. **Created and Activated a Virtual Environment**
- Set up an isolated Python environment using:
  ```
  python -m venv venv
  ```
- Activated it:
  - Windows: `.\venv\Scripts\activate`
  - Mac/Linux: `source venv/bin/activate`

### 2. **Installed Project Requirements**
- Verified the environment was clean using `pip freeze`
- Installed dependencies from `requirements.txt`:
  ```
  pip install -r requirements.txt
  ```

---

## 🏗️ Django Project Setup

### 3. **Ran the Django Development Server**
Inside the project directory:
```
python manage.py runserver
```
We observed:
- Django version information  
- A warning about **unapplied migrations**

---

## 🗄️ Database Initialization

### 4. **Applied Built‑In Django Migrations**
Stopped the server and ran:
```
python manage.py migrate
```
This created default tables for:
- Authentication  
- Admin  
- Sessions  
- Content types  

### 5. **Created a Superuser**
```
python manage.py createsuperuser
```
This allowed us to log into the Django admin panel.

---

## 🔐 Django Admin Interface

### 6. **Explored the Admin Dashboard**
At:
```
http://localhost:8000/admin/
```
We viewed:
- Users  
- Groups  
- Other built‑in tables  

This confirmed the database and admin interface were working correctly.

---

## 🧩 Creating the Blog App

### 7. **Created a New App Called `blog`**
```
python manage.py startapp blog
```

### 8. **Registered the App**
Added `'blog'` to `INSTALLED_APPS` in `settings.py`.

---

## 📝 Building the Post Model

### 9. **Defined the `Post` Model**
In `blog/models.py` we added fields for:
- `author` (ForeignKey to User)
- `title`
- `text`
- `created_date`
- `published_date`

Plus helper methods:
- `publish()`
- `__str__()`

---

## 🔧 Migrations for the Blog App

### 10. **Created and Applied Migrations**
```
python manage.py makemigrations blog
python manage.py migrate blog
```

This created the `Post` table in the database.

---

## 🛠️ Admin Registration

### 11. **Registered the Post Model**
In `blog/admin.py`:
```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

This made the Post model visible in the admin interface.

---

## ✍️ Adding and Viewing Posts

### 12. **Added a Post Through the Admin**
- Logged into `/admin/`
- Added a new Post entry
- Saved it to the database

---

## 🐚 Accessing Data in the Django Shell

### 13. **Used the Django Shell to Query Posts**
```
python manage.py shell
```

Inside the shell:
```python
from blog.models import Post
all_posts = Post.objects.all()
all_posts
```

We successfully retrieved and inspected stored posts.

---

## 🎉 Conclusion

Today we completed a full Django data workflow:

- Set up a project and virtual environment  
- Created an app  
- Built a model  
- Ran migrations  
- Used the admin interface  
- Added and retrieved data  
- Explored the Django shell  

