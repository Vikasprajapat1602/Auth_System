# Django Auth System

## Description

A Django application that allows user signup and login for two types of users: **Patient** and **Doctor**. After login, each user is redirected to their respective dashboard, where all the details entered during signup are displayed.

---

## Features

- User Registration with role selection (**Patient** or **Doctor**)  
- Secure Login and Logout functionality  
- Password and Confirm Password match validation during signup  
- Upload profile picture during registration  
- Dashboard shows all details filled in the signup form, specific to user type  
- Role-based redirection after login  

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
│ ├── migrations/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
│
├── profiles/ # For profile images (media)
│
├── templates/
│ └── accounts/
│ ├── base.html
│ ├── dashboard.html
│ ├── doctor_dashboard.html
│ ├── patient_dashboard.html
│ ├── login.html
│ ├── logout.html
│ ├── register.html
│ └── home.html
│
├── user_auth/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
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

2. **Create and activate virtual environment**

    ```
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

3. **Install requirements**

    ```
    pip install -r requirements.txt
    ```

4. **Apply Migrations**

    ```
    python manage.py migrate
    ```

5. **Create superuser (optional, for admin access)**

    ```
    python manage.py createsuperuser
    ```

6. **Run Server**

    ```
    python manage.py runserver
    ```

7. **Open in browser**  
    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Usage

- **Register:** Go to `/register/` and fill all the required fields, upload a profile picture, select your user type.  
- **Login:** Go to `/login/` and login with your credentials.  
- **Dashboard:** After login, you are redirected to either:  
    - `/patient/dashboard/` (for Patients)  
    - `/doctor/dashboard/` (for Doctors)  
- **Dashboard** shows all your information given at signup.

---

## Checks/Validations

- Password and Confirm Password fields must match during registration.  
- All fields except profile picture are required for signup.  
- Only authenticated users can access dashboards.

---

## Demo Submission

> Please refer to the submission guidelines and upload a video showing:  
> - Registration for both user types  
> - Login and role-based dashboard redirection  
> - Dashboard displaying all signup details

---

## Tech Stack

- Python, Django  
- SQLite3 (default development DB)  
- HTML/CSS (Bootstrap classes in templates)

---

## License

MIT License

