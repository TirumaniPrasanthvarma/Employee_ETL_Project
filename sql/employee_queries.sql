
USE employee_ETL;

SELECT * FROM employee;

SELECT COUNT(*) FROM employee;

SELECT Department, AVG(Salary)
FROM employee
GROUP BY Department;

SELECT Region, COUNT(*)
FROM employee
GROUP BY Region;

SELECT *
FROM employee
WHERE Salary > 100000;