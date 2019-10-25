--1. List the following details of each employee: employee number, last name, first name, gender, and salary.
select e.emp_no, e.last_name, e.first_name, e.gender, s.salary from "employees" e
join "salaries" s
on e.emp_no = s.emp_no;

--2. List employees who were hired in 1986.
select e.emp_no, e.last_name, e.first_name, e.hire_date from "employees" e
where e.hire_date between '1/1/1986' and '12/31/1986'
order by e.hire_date;

--3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.
select m.dept_no, dn.dept_name, m.emp_no, e.last_name, e.first_name, m.from_date, m.to_date
from "dept_manager" m
left join "departments" dn on m.dept_no = dn.dept_no
left join "employees" e on e.emp_no = m.emp_no;

--4. List the department of each employee with the following information: employee number, last name, first name, and department name.

select e.emp_no, e.last_name, e.first_name, d.dept_name
from "employees" e
left join "dept_emp" de
on e.emp_no = de.emp_no
left join "departments" d
on de.dept_no = d.dept_no;

--5. List all employees whose first name is "Hercules" and last names begin with "B."

select e.emp_no, e.last_name, e.first_name from "employees" e
where e.first_name = 'Hercules' and e.last_name like 'B%';

--6. List all employees in the Sales department, including their employee number, last name, first name, and department name.
select e.emp_no, e.last_name, e.first_name, d.dept_name
from "employees" e
left join "dept_emp" de
on de.emp_no = e.emp_no
left join "departments" d
on de.dept_no = d.dept_no
where d.dept_name = 'Sales';


--7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.

select e.emp_no, e.last_name, e.first_name, d.dept_name
from "employees" e
left join "dept_emp" de
on de.emp_no = e.emp_no
left join "departments" d
on de.dept_no = d.dept_no
where d.dept_name = 'Sales' or d.dept_name = 'Development';

--8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.

select e.last_name, count(e.last_name) as Count_of_names from employees e
group by e.last_name
order by Count_of_names desc;