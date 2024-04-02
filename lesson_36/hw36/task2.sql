SELECT first_name as "First Name", last_name as "Last Name"
FROM employees;

SELECT department_id
FROM employees
group by department_id;

SELECT *
FROM employees
ORDER BY first_name DESC;

SELECT first_name || " " || last_name as Name, salary, salary * 0.12 as PF
FROM employees;

SELECT min(salary) as "Min salary", max(salary) as "Max salary"
FROM employees;

SELECT first_name || " " || last_name as Name, salary as Salary
FROM employees;

