-- SQL-команды для создания таблиц
CREATE TABLE customers
(
	customer_id VARCHAR(10) PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name varchar(100) NOT NULL
);
CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(50) NOT NULL,
	last_name varchar(50) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date DATE NOT NULL,
	notes text
);
CREATE TABLE orders
(
	order_id int,
	customer_id TEXT REFERENCES customers(customer_id),
	employee_id	int REFERENCES employees(employee_id),
	order_date DATE NOT NULL,
	ship_city varchar(50) NOT NULL
)