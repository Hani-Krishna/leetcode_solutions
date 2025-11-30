select
    employee_id,
    CASE 
     WHEN Employee_id % 2 = 1 
         AND NAME NOT LIKE 'M%' 
        THEN salary
        ELSE 0
    END AS bonus
FROM Employees 
ORDER BY employee_id;
