# Write your MySQL query statement below
SELECT EmployeeUNI.unique_id,Employees.name
FROM Employees LEFT JOIN EmployeeUNI 
ON employees.id = employeeUNI.id