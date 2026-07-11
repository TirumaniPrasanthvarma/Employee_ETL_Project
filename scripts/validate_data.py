from db_connection import get_connection

def validate_data():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("USE employee_ETL")

    cursor.execute("SELECT COUNT(*) FROM employee")

    count = cursor.fetchone()

    print("Total Employees :", count[0])

    cursor.execute("SELECT * FROM employee LIMIT 5")

    rows = cursor.fetchall()

    print("\nFirst 5 Employees:\n")

    for row in rows:
        print(row)

    cursor.close()

    connection.close()


if __name__ == "__main__":
    validate_data()