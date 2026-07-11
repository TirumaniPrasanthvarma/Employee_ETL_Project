from db_connection import get_connection

def create_table():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("USE employee_ETL")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employee(
        Employee_ID VARCHAR(20) PRIMARY KEY,
        Full_Name VARCHAR(100),
        Age INT,
        Department VARCHAR(50),
        Region VARCHAR(50),
        Status VARCHAR(20),
        Join_Date DATE,
        Salary INT,
        Email VARCHAR(100),
        Phone BIGINT,
        Performance_Score VARCHAR(20),
        Remote_Work BOOLEAN
    )
    """)

    print("Employee Table Created Successfully")

    cursor.close()

    connection.close()


if __name__ == "__main__":
    create_table()