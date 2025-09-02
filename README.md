🎓 Student Management System

📌 Overview

This is a desktop-based Student Management System built using Python (Tkinter) for the GUI and MySQL as the backend database.

It allows you to:

➕ Add new student records
📋 Display all records in a table
✏ Update existing student details
❌ Delete records
🔍 Search students by name, roll number, contact, college, or date of birth
---

⚙ Tech Stack

Frontend (GUI): Tkinter, ttk, tkcalendar
Backend (Database): MySQL
Database Driver: PyMySQL

📂 Features

User-friendly GUI
Data stored in MySQL database (sms1)
Scrollable table view for student records
Form inputs for all student details:
Name, Roll No., Course, Semester, Technology
Contact, College, Address, Gender, DOB
---

🛠 Installation & Setup

1. Clone the repository

git clone https://github.com/your-username/student-management-system.git
cd student-management-system

2. Install dependencies

Make sure you have Python 3.8+ installed. Install required libraries:

pip install pymysql tkcalendar

3. Setup MySQL Database

1. Open MySQL and create a database:

CREATE DATABASE sms1;
USE sms1;


2. Create a table named data:

CREATE TABLE data (
    name VARCHAR(100),
    rollno VARCHAR(20) PRIMARY KEY,
    course VARCHAR(50),
    sem VARCHAR(10),
    tech VARCHAR(50),
    contact VARCHAR(15),
    college VARCHAR(100),
    address VARCHAR(200),
    gender VARCHAR(10),
    dob VARCHAR(20)
);

🚀 Future Improvements

Add login system for admin security

Export records to Excel/CSV

Deploy using an installer (PyInstaller)

🙌 Contributions

Feel free to fork the repo, open issues, and submit pull requests.
