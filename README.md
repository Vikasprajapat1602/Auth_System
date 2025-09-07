# Django Auth + Blog System

A Django application with **User Authentication** (for **Patient** and **Doctor**) and a **Blog System** where doctors can create blog posts and patients can view them.

---

## Features

### 🔑 Authentication System (Task 1)
- User Registration with role selection (**Patient** or **Doctor**)  
- Secure Login and Logout functionality  
- Upload profile picture during registration  
- Password & Confirm Password match validation  
- Dashboard shows all details filled in the signup form  
- Role-based redirection after login (**Patient Dashboard** / **Doctor Dashboard**)  

### 📝 Blog System (Task 2)
- Four Categories available:  
  - Mental Health  
  - Heart Disease  
  - Covid19  
  - Immunization  
- Doctor can create blog posts with:  
  - Title  
  - Image  
  - Category  
  - Summary  
  - Content  
  - Draft/Published option  
- Patients can view published blogs category-wise  
- Blogs created by a doctor are visible in their dashboard  

---

## Signup Form Fields
- First Name  
- Last Name  
- Profile Picture  
- Username  
- Email ID  
- Password  
- Confirm Password  
- Address (Line1, City, State, Pincode)  
- User Type (Patient / Doctor)  

---

## Folder Structure

user_auth/
├── accounts/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── blog/   # New app for Blog System
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── profiles/   # For profile images (media)
│
├── templates/
│   ├── accounts/
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── doctor_dashboard.html
│   │   ├── patient_dashboard.html
│   │   ├── login.html
│   │   ├── logout.html
│   │   ├── register.html
│   │   └── home.html
│   │
│   └── blog/   # New templates for Blog System
│       ├── blog_list.html
│       ├── blog_detail.html
│       ├── blog_form.html
│       └── my_blogs.html
│
├── user_auth/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
├── .gitignore
└── README.md


---

## How to Run

1. **Clone the repository**

    ```
    git clone https://github.com/Vikasprajapat1602/Auth_System.git
    cd Auth_System
    ```

2. **Apply Migrations**

    ```
    python manage.py migrate
    ```

3. **Create superuser (optional, for admin access)**

    ```
    python manage.py createsuperuser
    ```

4. **Run Server**

    ```
    python manage.py runserver
    ```

5. **Open in browser**  
    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Usage

- **Register:** Go to `/register/` and fill all the required fields, upload a profile picture, select your user type.  
- **Login:** Go to `/login/` and login with your credentials.
- **Blogs:** Go to `/blogs/` and view all blogs  
- **Dashboard:** After login, you are redirected to either:  
    - `/patient/dashboard/` (for Patients)  
    - `/doctor/dashboard/` (for Doctors)  
- **Dashboard** shows all your information given at signup.
- **Doctor** Create blogs, save as draft or publish
- **Patient** View blogs under categories
- Blogs are listed category-wise and can be read in detail

---

## Checks/Validations

- Password and Confirm Password fields must match during registration.  
- All fields except profile picture are required for signup.  
- Only authenticated users can access dashboards.

---

## Tech Stack

- Python, Django  
- MySQL  
- HTML/CSS (Bootstrap classes in templates)


