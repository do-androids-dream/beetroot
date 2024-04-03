SELECT first_name, last_name, employees.department_id, departments.depart_name
FROM employees
JOIN departments on employees.department_id = departments.department_id;

SELECT first_name, last_name, departments.depart_name, locations.country_id, locations.state_province
FROM employees
JOIN departments on employees.department_id = departments.department_id
JOIN locations on departments.location_id = locations.location_id;

SELECT first_name, last_name, employees.department_id, departments.depart_name
FROM employees
JOIN departments on employees.department_id = departments.department_id
WHERE employees.department_id IN (80, 40);

SELECT first_name, last_name, employees.department_id, departments.depart_name
FROM employees
RIGHT JOIN departments on employees.department_id = departments.department_id;

SELECT e1.employee_id, e1.first_name, e1.manager_id, e2.first_name as manager_name
FROM employees as e1, employees as e2
where e1.manager_id = e2.employee_id;

SELECT e.first_name || " " || e.last_name as "Full Name", jobs.job_title, jobs.max_salary - e.salary as "Salary Diff"
FROM employees AS e
JOIN jobs ON jobs.job_id = e.job_id;

SELECT j.job_title, avg(e.salary)
FROM jobs as j
JOIN employees as e ON e.job_id = j.job_id
GROUP BY j.job_title;

SELECT e.first_name || " " || e.last_name as "Full Name", e.salary, l.city
FROM employees AS e
JOIN jobs ON jobs.job_id = e.job_id
JOIN departments as d ON d.department_id = e.department_id
JOIN locations as l ON d.location_id = l.location_id
WHERE l.city = "London";

SELECT d.depart_name, count(employee_id) as Employees
FROM departments as d
JOIN employees as e ON e.department_id = d.department_id
GROUP BY d.depart_name;