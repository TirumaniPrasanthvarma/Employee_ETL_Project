from db_connection import get_connection

def create_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS employee_ETL")

    print("Database Created Successfully")

    cursor.execute("USE employee_ETL")

    print("Using employee_ETL Database")

    cursor.close()

    connection.close()


if __name__ == "__main__":
    create_database()