# Employee ETL Pipeline (End-to-End)

## Project Overview

The Employee ETL Pipeline is an end-to-end data engineering project developed using Python, Pandas, MySQL, and SQL.

The main objective of this project is to automate the process of collecting employee data from a CSV file, cleaning and transforming it, storing it in a MySQL database, and validating the loaded data.

This project demonstrates the complete ETL (Extract, Transform, Load) workflow used in real-world data engineering.

---

# What is ETL?

ETL stands for:

- **Extract** – Read data from a source.
- **Transform** – Clean and prepare the data.
- **Load** – Store the cleaned data into a database.

In this project,

```
Employee Raw CSV
        │
        ▼
Extract Data
        │
        ▼
Clean & Transform
        │
        ▼
Load into MySQL
        │
        ▼
Validate Data
```

---

# Project Objectives

The objectives of this project are:

- Read employee data from a CSV file.
- Clean missing and duplicate data.
- Handle outliers in numerical columns.
- Transform text columns into the required format.
- Convert date columns into proper date format.
- Save the cleaned dataset.
- Create a MySQL database automatically.
- Create the employee table automatically.
- Load cleaned data into MySQL.
- Validate the inserted data using SQL queries.

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main programming language |
| Pandas | Data cleaning and transformation |
| NumPy | Numerical operations |
| MySQL | Database |
| MySQL Connector | Connect Python with MySQL |
| SQL | Database queries |
| VS Code | Code Editor |

---

# Project Folder Structure

```
Employee_ETL_Project/
│
├── data/
│   ├── employee_raw.csv
│   └── employee_cleaned.csv
│
├── scripts/
│   ├── clean_data.py
│   ├── db_connection.py
│   ├── create_database.py
│   ├── create_table.py
│   ├── load_data.py
│   ├── validate_data.py
│   └── main.py
│
├── sql/
│   └── employee_queries.sql
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# ETL Workflow

```
Employee Raw CSV
        │
        ▼
clean_data.py
        │
        ▼
Employee_Cleaned.csv
        │
        ▼
create_database.py
        │
        ▼
create_table.py
        │
        ▼
load_data.py
        │
        ▼
MySQL Database
        │
        ▼
validate_data.py
```

---

# Explanation of Each Script

## clean_data.py

This script is responsible for cleaning and transforming the raw employee dataset.

Operations performed:

- Read raw CSV file
- Display dataset information
- Remove duplicate records
- Handle missing values
- Detect outliers
- Replace missing values using Mean or Median
- Create Full Name
- Split Department and Region
- Convert Join Date into Date format
- Save cleaned CSV

---

## db_connection.py

Creates a connection between Python and MySQL.

---

## create_database.py

Creates the database automatically if it does not already exist.

Database Name:

```
employee_ETL
```

---

## create_table.py

Creates the Employee table inside the database.

---

## load_data.py

Reads the cleaned CSV file and inserts every employee record into MySQL.

Before loading,

```
TRUNCATE TABLE employee;
```

is executed to avoid duplicate records.

---

## validate_data.py

Validates the loaded data by executing SQL queries.

Examples:

- Total number of employees
- Display first five records

---

## main.py

This is the main controller of the project.

It executes every ETL step in the correct order.

```
Cleaning
      ↓
Create Database
      ↓
Create Table
      ↓
Load Data
      ↓
Validation
```

---

# Features

- End-to-End ETL Pipeline
- Automatic Database Creation
- Automatic Table Creation
- Automatic Data Loading
- Data Validation
- Modular Python Code
- Reusable Scripts

---

# Sample Output

```
==========================================
EMPLOYEE ETL PIPELINE STARTED
==========================================

Step 1 : Cleaning Data
✔ Cleaning Completed

Step 2 : Creating Database
✔ Database Created

Step 3 : Creating Table
✔ Table Created

Step 4 : Loading Data
✔ 1020 Records Loaded

Step 5 : Validation
✔ Total Employees : 1020

==========================================
EMPLOYEE ETL PIPELINE COMPLETED
==========================================
```

---

# How to Run the Project

Open the project folder and execute:

```bash
python scripts/main.py
```

---

# Future Improvements

- Apache Spark ETL Pipeline
- AWS S3 Integration
- Azure Blob Storage
- Apache Airflow Automation
- Docker Deployment
- Data Warehouse Integration

---

# Author

**Prasanth Varma**

Computer Science Engineering Student

Learning Data Engineering, Big Data, and Cloud Technologies.