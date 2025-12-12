SELECT 
u.name,SUM(t.amount) AS balance
FROM Transactions t
JOIN Users u
ON t.account = u.account
GROUP BY u.name HAVING balance > 10000;
