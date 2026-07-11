from db_connection import get_connection
import pandas as pd

def load_data():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("USE employee_ETL")

    employee = pd.read_csv(r"C:\Users\prasa\OneDrive\Documents\Prasanth Files\My_Desk\Projects\Employee_ETL_Project\data\employee_cleaned.csv")

      # Clear old data
    cursor.execute("TRUNCATE TABLE employee")

    query = """
    INSERT INTO employee
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    for row in employee.itertuples(index=False):
        cursor.execute(query, tuple(row))

    connection.commit()

    print("Data Loaded Successfully")

    cursor.close()

    connection.close()


if __name__ == "__main__":
    load_data()