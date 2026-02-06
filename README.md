# Employee Management System (EMS)

A simple and clean Employee Management System built using **Python Flask** and **MySQL**.  
This application allows an admin to manage employee records with full CRUD functionality.

---

## 🚀 Features

- Admin login with session-based authentication  
- Add new employees  
- View employee list  
- Edit employee details  
- Delete employee records  
- Duplicate email validation  
- Clean and simple UI using HTML and CSS  

---

## 🛠 Tech Stack

- **Backend:** Python, Flask  
- **Database:** MySQL  
- **Frontend:** HTML, CSS  
- **Authentication:** Session-based login  

---

## 🗄 Database Design

### Admin Table
- id (Primary Key)
- username
- password

### Employees Table
- id (Primary Key)
- name
- email (Unique)
- department
- salary
- joining_date
- status

---

## ⚙️ How to Run the Project

### 1. Install dependencies
```bash
pip install -r requirements.txt
# Employee Management System (EMS)

A simple and clean Employee Management System built using **Python Flask** and **MySQL**.  
This application allows an admin to manage employee records with full CRUD functionality.

---

## 🚀 Features

- Admin login with session-based authentication  
- Add new employees  
- View employee list  
- Edit employee details  
- Delete employee records  
- Duplicate email validation  
- Clean and simple UI using HTML and CSS  

---

## 🛠 Tech Stack

- **Backend:** Python, Flask  
- **Database:** MySQL  
- **Frontend:** HTML, CSS  
- **Authentication:** Session-based login  

---

## 🗄 Database Design

### Admin Table
- id (Primary Key)
- username
- password

### Employees Table
- id (Primary Key)
- name
- email (Unique)
- department
- salary
- joining_date
- status

---

## ⚙️ How to Run the Project

### 1. Install dependencies
```bash
pip install -r requirements.txt
2. Create the database
Run the SQL script provided in:
database.sql
3. Start the application
python app.py
4. Open in browser
http://127.0.0.1:5000/

🔐 Default Admin Login
Username: admin
Password: admin123

📌 Project Highlights
Uses session-based access control
Prevents duplicate employee entries using database constraints and validations
Follows clean project structure
Easy to understand and extend
📖 Learning Outcome

This project helped me understand:

Flask routing and templates

Database connectivity with MySQL

CRUD operations

Session management

Error handling and validation

Structuring a real-world backend project

📎 Note

This project is created for learning and demonstration purposes and can be extended with features like reports, role-based access, and cloud deployment.
