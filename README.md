# 📚 Book Review – Django Web Application

![Django](https://img.shields.io/badge/Django-4.x-green)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Database](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-success)

Book Review is a Django-based web application that allows users to browse books, submit reviews, and manage book-related content through a clean and structured backend system.

This project demonstrates full-stack Django development including models, views, templates, authentication, and admin customization.

Visit: https://book-review-0ayd.onrender.com/

---

# 🚀 Features

- ✅ Add and Manage Books
- ✅ Submit Book Reviews
- ✅ User Authentication (Login / Register)
- ✅ Admin Panel Management
- ✅ Dynamic Templates
- ✅ SQLite Database Integration
- ✅ Clean Django MVT Architecture
- ✅ Scalable Project Structure

---

# 🛠️ Tech Stack

| Layer | Technology |
|--------|------------|
| Backend | Django |
| Language | Python |
| Database | SQLite |
| Frontend | HTML, CSS, Bootstrap |
| Version Control | Git & GitHub |

---

# 📁 Project Structure

```

book_review/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
│
├── book_review/        # Main Project Configuration
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── app_name/           # Main Application (Replace with actual app name)
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── templates/
├── static/
└── media/

```

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/book_review.git
cd book_review
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt is not available:

```bash
pip install django
```

---

## 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

---

## 6️⃣ Run Development Server

```bash
python manage.py runserver
```

Open in browser:

http://127.0.0.1:8000/

Admin Panel:

http://127.0.0.1:8000/admin/

---

# 📂 Static & Media Configuration

### settings.py

```python
import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

### urls.py

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # app urls here
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

# 🎯 Learning Outcomes

This project demonstrates:

- Django Models & Relationships
- Template Rendering
- Form Handling
- User Authentication
- Admin Customization
- Database Integration
- Clean Project Architecture

---

# 🔮 Future Improvements

- Rating System (Stars)
- Search & Filter Books
- Pagination
- REST API Version
- User Profile Pages
- Comment Replies
- AJAX-Based Review Submission

---

# 👨‍💻 Author

**Md-Hasibul-Hasan**  
Undergraduate Student  
Django Backend Developer

---

# 📜 License

This project is developed for educational and portfolio purposes.

