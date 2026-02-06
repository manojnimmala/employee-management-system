from flask import Flask, render_template, request, redirect, session
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRECT_KEY")

# DB connection
db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
cursor = db.cursor(dictionary=True)

# ---------------- LOGIN PAGE ----------------
@app.route("/")
def login_page():
    return render_template("login.html")

# ---------------- LOGIN ----------------
@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    cursor.execute("SELECT * FROM admin WHERE username=%s", (username,))
    admin = cursor.fetchone()

    if not admin or admin["password"] != password:
        return render_template("login.html", error="Invalid username or password")

    session["admin"] = username
    return redirect("/dashboard")

# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    if "admin" not in session:
        return redirect("/")

    return render_template("dashboard.html")

# ---------------- ADD EMPLOYEE ----------------
@app.route("/add", methods=["GET", "POST"])
def add_employee():
    if "admin" not in session:
        return redirect("/")

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        department = request.form["department"]
        salary = request.form["salary"]
        joining_date = request.form["joining_date"]
        status = request.form["status"]

        # Duplicate email check
        cursor.execute("SELECT * FROM employees WHERE email=%s", (email,))
        if cursor.fetchone():
            return render_template(
                "add_employee.html",
                error="Employee with this email already exists"
            )

        cursor.execute(
            """INSERT INTO employees
            (name, email, department, salary, joining_date, status)
            VALUES (%s,%s,%s,%s,%s,%s)""",
            (name, email, department, salary, joining_date, status)
        )
        db.commit()
        return redirect("/employees")

    return render_template("add_employee.html")

# ---------------- VIEW EMPLOYEES ----------------
@app.route("/employees")
def employees():
    if "admin" not in session:
        return redirect("/")

    cursor.execute("SELECT * FROM employees")
    data = cursor.fetchall()
    return render_template("employees.html", employees=data)

# ---------------- EDIT EMPLOYEE ----------------
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_employee(id):
    if "admin" not in session:
        return redirect("/")

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        department = request.form["department"]
        salary = request.form["salary"]
        joining_date = request.form["joining_date"]
        status = request.form["status"]

        # Check duplicate email (excluding current record)
        cursor.execute(
            "SELECT * FROM employees WHERE email=%s AND id!=%s",
            (email, id)
        )
        if cursor.fetchone():
            emp = {"id": id, "name": name, "email": email,
                   "department": department, "salary": salary,
                   "joining_date": joining_date, "status": status}
            return render_template(
                "edit_employee.html",
                emp=emp,
                error="Email already used by another employee"
            )

        cursor.execute(
            """UPDATE employees
               SET name=%s, email=%s, department=%s,
                   salary=%s, joining_date=%s, status=%s
               WHERE id=%s""",
            (name, email, department, salary, joining_date, status, id)
        )
        db.commit()
        return redirect("/employees")

    cursor.execute("SELECT * FROM employees WHERE id=%s", (id,))
    emp = cursor.fetchone()
    return render_template("edit_employee.html", emp=emp)

# ---------------- DELETE EMPLOYEE ----------------
@app.route("/delete/<int:id>")
def delete_employee(id):
    if "admin" not in session:
        return redirect("/")

    cursor.execute("DELETE FROM employees WHERE id=%s", (id,))
    db.commit()
    return redirect("/employees")

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
