-- SQL IS NOT CASE SENSITIVE

-- LIST DOWN EXISTING DATABASES
-- EXEC sp_databases
-- select name from sys.databases

-- CEATING A NEW DATABASE
-- create database school_db
-- create database demo

-- USING DATABASES
use school_db

-- CHECKING IN WHICH DATABASE YOU ARE CURRENTLY
-- select DB_NAME() 

-- DELETING A DATABASE
-- drop database demo

-- CREATING A TABLE IN DATABASE
--create table students(
--student_id INT,
--std_name VARCHAR(100),
--age INT,
--grade CHAR
--)

-- CHECKING EXISTING TABLES ,IN '' WRITE TABLE NAME
--exec sp_help 'students'

-- INSERTIG DATA INTO TABLES
-- insert into students(std_id, std_name, std_grade, age)
-- values(101,'ALi','A',20)

-- insert into students values(102, 'ahmed', 'B', 20),(103, 'Hassan', 'A', 22)

-- READING DATA FROM A TABLE
-- select * from students

-- READING A SIGNLE COLUMN
-- select std_name from students

-- UPDATING DATA IN A TABLE
-- update students set std_name = 'GUl' where std_id = 103

-- DELETING DATA FROM A TABLE
-- delete from students where std_id = 101

-- TRUNCATE QUERY TO DELETE ALL DATA IN A TABLE
-- truncate table students

-- CRUD OPERATION EXERCISE
-- insert into students values (101,'Ahmed','A',20),(102,'Ali','A',20),(103,'Ahsan','A',20)
-- update students set std_grade='B' where std_id = 101
-- insert into students values(104,'AAA','C', 22)
-- delete from students where std_id = 104
-- select * from students where std_name = 'Ali'
-- select age from students where std_name = 'Ali'

-- WHY WE NEED CONSTRAINTS
-- 1. THIS WILL ADD 101 ID AGAIN MEAN DUPLICATE DATA
-- insert into students values (101,'Mujtaba','C',29)
-- 2. THIS WILL ADD NULL EMPTY VALUE IN TABLE
-- insert into students(std_id,std_grade,age) values (105,'A',21)
-- 3. EVERY TIME WE HAVE TO CHECK WHAT IS THE LAST STD_ID TO ASSIGN A UNIQE ID
-- HOW CAN WE ASSIGN IT AUTOMATICALY BY USING IDENTITY
-- IDENTITY CONSTARTINT USED IN IDS LIKE IDENTITY(START AT 1, INCREASE 1 EACH TIME) = IDENTITY ( 1,1)
-- std_id INT IDENTITY (1,1)
-- DEFAULT CONSTARINT , IF YOU DONT GIVE A VALUE IT WILL ADD DEFAULT VALUE BUT IF YOU WILL ADD A VALUE IT WILL REPLACE IT
-- p_craeted DATETIME DEFAULT GETDATE()
-- 4. PRIMARY KEYS
-- PRIMARY KEY IS A COLUMN IN A TABLE WHICH HAVE FOLLOWING PROPERTIES
--  ..1. MUST CONTAIN UNIQUE VALUES
--  ..2. NULL VALUES NOT ACCEPTABLE
--  ..3. EACH TABLE HAVE JUST ONE PRIMARY KEY , FOR MORE THAN ONE PRIMARY KEYS USE OBJECT
-- HERE IS AN EXAMPLE OF ALL CONSTRAINTS
-- DROP TABLE students
-- WE WILL DROP PREVIOUS TABLE AND CRAETE NEW TABLE WITH THE SAME NAME USING ALL CONSTRAINTS
CREATE TABLE students(
std_id INT PRIMARY KEY IDENTITY(1,1),
std_name VARCHAR(100) NOT NULL,
std_email VARCHAR(100) UNIQUE,
std_craeted_at DATETIME DEFAULT GETDATE()
)
INSERT INTO students (std_name, std_email) VALUES ('BABAR','babar@db.com')
INSERT INTO students (std_name, std_email) VALUES ('AHSAN','ahsan@db.com')
select * from students

-- TASK : EMPLOYEE DATABASE WITH CONSTRAINTS
CREATE DATABASE Employees_DB
USE Employees_DB
CREATE TABLE Employee_table(
emp_id INT IDENTITY(101,1) PRIMARY KEY,
fname VARCHAR(100) NOT NULL,
lname VARCHAR(100) NOT NULL,
email VARCHAR(100) NOT NULL UNIQUE,
job_title VARCHAR(100) NOT NULL,
department VARCHAR(100) NOT NULL,
salary DECIMAL(10,2) DEFAULT 30000.00,
hire_date DATE NOT NULL DEFAULT CONVERT(DATE,GETDATE()),
city VARCHAR(100) NOT NULL
)
INSERT INTO Employee_table

(fname, lname, email, job_title, department, salary, hire_date, city)

VALUES

('Aarav', 'Sharma', 'aarav.sharma@example.com', 'Director', 'Management', 180000, '2019-02-10', 'Mumbai'),

('Diya', 'Patel', 'diya.patel@example.com', 'Lead Engineer', 'Tech', 120000, '2020-08-15', 'Bengaluru'),

('Rohan', 'Mehra', 'rohan.mehra@example.com', 'Software Engineer', 'Tech', 85000, '2022-05-20', 'Bengaluru'),

('Priya', 'Singh', 'priya.singh@example.com', 'HR Manager', 'Human Resources', 95000, '2019-11-05', 'Mumbai'),

('Arjun', 'Kumar', 'arjun.kumar@example.com', 'Data Scientist', 'Tech', 110000, '2021-07-12', 'Hyderabad'),

('Ananya', 'Gupta', 'ananya.gupta@example.com', 'Marketing Lead', 'Marketing', 90000, '2020-03-01', 'Delhi'),

('Vikram', 'Reddy', 'vikram.reddy@example.com', 'Sales Executive', 'Sales', 75000, '2023-01-30', 'Mumbai'),

('Sameera', 'Rao', 'sameera.rao@example.com', 'Software Engineer', 'Tech', 88000, '2023-06-25', 'Pune'),

('Ishaan', 'Verma', 'ishaan.verma@example.com', 'Recruiter', 'Human Resources', 65000, '2022-09-01', 'Mumbai'),

('Kavya', 'Joshi', 'kavya.joshi@example.com', 'Product Designer', 'Design', 92000, '2021-04-18', 'Bengaluru'),

('Zain', 'Khan', 'zain.khan@example.com', 'Sales Manager', 'Sales', 115000, '2019-09-14', 'Delhi'),

('Nisha', 'Desai', 'nisha.desai@example.com', 'Jr. Data Analyst', 'Tech', 70000, '2024-02-01', 'Hyderabad'),

('Aditya', 'Nair', 'aditya.nair@example.com', 'Marketing Analyst', 'Marketing', 68000, '2022-10-10', 'Delhi'),

('Fatima', 'Ali', 'fatima.ali@example.com', 'Sales Executive', 'Sales', 78000, '2022-11-22', 'Mumbai'),

('Kabir', 'Shah', 'kabir.shah@example.com', 'DevOps Engineer', 'Tech', 105000, '2020-12-01', 'Pune')

SELECT * FROM Employee_table

-- SECTION 4 , SEARCHING DATA
-- 1. WHERE CLAUSE
SELECT * FROM Employee_table WHERE department = 'SALES'
SELECT * FROM Employee_table WHERE salary > 150000
SELECT * FROM Employee_table WHERE department != 'Tech'
SELECT * FROM Employee_table WHERE hire_date > '2022-01-01'
-- 2. DISTINICT
-- REMOVES DUPLICATE DATA, PRINT ONLY ONE TIME IF SAME DATA EXITS MORE THAN ONE
SELECT DISTINCT department FROM Employee_table
SELECT DISTINCT city FROM Employee_table
-- 3. ORDER BY
-- SORTING , A-Z FORMAT, ETC
SELECT * FROM Employee_table ORDER BY salary -- LOWER TO HIGHER
SELECT * FROM Employee_table ORDER BY salary DESC -- HIGHER TO LOW
SELECT * FROM Employee_table ORDER BY hire_date DESC
SELECT * FROM Employee_table ORDER BY fname
SELECT department, fname FROM Employee_table ORDER BY department, fname
-- 4. LIKE
-- SEARCH FOR SIMILAR WORDS IF YOU DONT KNOW EXACT COLUMN NAMES
-- % MEANS ANY CHARACTER BEFORE OR AFTER
SELECT * FROM Employee_table WHERE department LIKE '%MAN%'
SELECT * FROM Employee_table WHERE fname LIKE 'A%' -- IT MEANS ANY CHARACTER AT THE END BUT FIRST LETTER SHOULD BE A
SELECT * FROM Employee_table WHERE fname LIKE '%A' -- ENDS WITHA 
SELECT * FROM Employee_table WHERE email LIKE '%GUPTA%' -- CONATAINS GUPTA
SELECT * FROM Employee_table WHERE city LIKE 'DELHI' -- CITY = DELHI
SELECT * FROM Employee_table WHERE fname LIKE '[^A]%' -- NOT STARTS WITH A
SELECT * FROM Employee_table WHERE fname LIKE '_a%' -- SECOND CHARACTER IS A
SELECT * FROM Employee_table WHERE fname LIKE '[AB]%' -- START WITH EITHER A OR B
SELECT * FROM Employee_table WHERE fname LIKE '____' -- ANY NAME WHICH HAVE 4 CHARACTERS

-- 5. TOP
-- SELECTS THE RECORDS FROM TOP YOU CAN GIVE VALUE HOW MANY TOP COLUMNS YOU NEED
SELECT TOP 5 * FROM Employee_table -- 5 TOP RECORDS
SELECT TOP 3 * FROM Employee_table ORDER BY  salary DESC -- TOP 3 EMPLOYEES HAVE HIGH SALARY
SELECT TOP 5 * FROM Employee_table ORDER BY hire_date 
SELECT TOP 3 * FROM Employee_table WHERE department = 'marketing'
SELECT TOP 2 * FROM Employee_table ORDER BY fname

-- EXERCISE
SELECT DISTINCT department FROM Employee_table 
SELECT * FROM Employee_table ORDER BY salary
SELECT TOP 3 * FROM Employee_table
SELECT * FROM Employee_table WHERE fname LIKE 'A%'
SELECT * FROM Employee_table WHERE fname LIKE '_____'

-- LOGICAL OPERATORS :> AND , OR
-- 1. AND , IF BOTH CONDITIONS ARE TRUE
SELECT * FROM Employee_table WHERE salary = 75000 AND department = 'Sales'
SELECT * FROM Employee_table WHERE city = 'Delhi' AND salary = 90000
-- 2. OR , IF EITHER ONE CONDITION IS TRUE
SELECT * FROM Employee_table WHERE city = 'Mumbai' OR salary = 70000 OR department = 'Tech'

-- IN , NOT IN, BETWEEEN
-- 1. IN :> IT SELECTS FROM MULTIPLE COLUMNS YOU GIVE
SELECT * FROM Employee_table WHERE department IN ('Sales','Marketing','Tech')
-- NOT IN IS OPPOSITE OF IN
SELECT * FROM Employee_table WHERE department NOT IN ('Sales','Marketing','Tech')
-- 3. BETWEEN , WHERE YOU HAVE RANGE
SELECT * FROM Employee_table WHERE salary BETWEEN 60000 AND 75000

-- CASE
-- WHEN YOU HAVE MULTIPLE CONDITIONS JUST LIKE SWITCH CASES IN C++, JAVA ETC
-- CATAGORIZE EMPLOYEES BASED ON THEIR SALARY
SELECT fname, lname, salary,
CASE
	WHEN salary > 100000 THEN 'HIGH EARNER'
	WHEN salary BETWEEN 80000 AND 100000 THEN 'MEDIUM EARNER'
	ELSE 'STANDARD EARNER'
END AS salary_band
FROM Employee_table
-- CALCULATE BONUS
SELECT fname, lname, department, salary,
CASE
	WHEN department = 'Tech' THEN salary*0.12
	WHEN department IN ('Sales','Marketing') THEN salary*0.10
	ELSE salary*0.5
END AS bonus_amount
FROM Employee_table

-- IS NULL :> TO CHECK WHETHER IS ANY NULL VALUE PRESENTS
SELECT * FROM Employee_table WHERE fname IS NULL

-- NOT LIKE :> TO GET THE DATA WHICH IS NOT SAME AS WE WANT
-- THOSE EMPLOYES WHOSE NAME DOESNT START WITH A
SELECT * FROM Employee_table WHERE fname NOT LIKE 'A%'

-- AGGERAGATE FUNCTIONS
-- 1. COUNT
SELECT COUNT(emp_id) FROM Employee_table
-- 2. SUM
SELECT SUM(salary) FROM Employee_table
-- 3. AVG
SELECT AVG(salary) FROM Employee_table
-- 4. MIN
SELECT MIN(salary) FROM Employee_table
-- 5. MAX
SELECT MAX(salary) FROM Employee_table

-- GROUP BY
-- TO IDENTIFY RELEATED RECORDS
-- GROUPING EMLOYEES BY DEPARTMENTS
SELECT department FROM Employee_table GROUP BY department
SELECT department, COUNT(emp_id) FROM Employee_table GROUP BY department -- COUNTING EMPLOYEES IN EACH DEPARTMENT
SELECT department, AVG(salary) FROM Employee_table GROUP BY department -- AVERAGE SALARY OF ECAH DEPARTMENT

-- MULTI LEVEL / COLUMN GROUPING
SELECT department , city , COUNT (emp_id)
FROM Employee_table GROUP BY department , city
ORDER BY department
-- THIS WILL SORT BY DEPARTMENT AND TELL IN WHCIH DEPARTMENT , EMPLOYES FROM WHICH CITY

-- HAVING CLAUSE / WHERE DOES NOT WORK WITH GROUP BY SO WE HAVE HAVING CLAUSE
SELECT department, COUNT (emp_id)
FROM Employee_table GROUP BY department 
HAVING COUNT(emp_id) > 2
-- THIS WILL SHOW DEPARTMENTS HAVING EMPLOYE MORE THAN 2
SELECT job_title , AVG(salary)
FROM Employee_table GROUP BY job_title
HAVING AVG(salary) > 90000
-- JOB TITLE HAVING AVERAGE SALARY MORE THAN 90,000

-- ROLL UP IS USED WITH GROUP  BY TO FIND THE SUB TOTAL AND GRAND TOTAL OF THE COLUMNS
SELECT department, COUNT (emp_id)

FROM Employee_table GROUP BY ROLLUP(department)
-- THIS WILL SHOW TOTAL EMPLOYEE COUNT AT THE END

-- COALESCE WILL REPLACE NULL VALUE WITH YOUR GIVEN COLUMN NAME
-- HERE THE COALESCE() FUNCTION WILL TAKE TWO PARAMETER 1ST WHICH COLUMN IT TAKE 2ND WHICH NAME IT GIVE TO NEW COLUMN
SELECT COALESCE(department,'total') AS department , COALESCE(city, 'total') AS city , COUNT (emp_id)
FROM Employee_table GROUP BY ROLLUP(department , city)
ORDER BY department
-- THIS WILL SHOW DEPARTMENT AND CITY VISE EMPLOYES WITH SUBTOTAL AND GRANTOTAL

-- SUB QUERIES / NESTED QUERIES / QUERIES INSIDE QUERIES
-- 1. SINGLE ROW QUERY , SINGLE ROW IN RESULT
SELECT * FROM Employee_table 
WHERE salary > (SELECT AVG(salary) FROM Employee_table )
-- FIRST IT WILL RUN INNER QUERY (SELECT AVG(salary) FROM Employee_table ),
-- AND THEN IT RUNS OUTER QUERY SELECT * FROM Employee_table WHERE salary >
-- 2. MULTI ROW QUERY , MULTIPLE ROWS IN RESULT
SELECT * FROM Employee_table 
WHERE department IN (
SELECT department FROM Employee_table WHERE city = 'Mumbai'
)
-- 3. CORELEATED QUERY / DEPENDENT ON EACH OTHER / OUTER QUERY RUNS FIRST
SELECT * FROM Employee_table e1
WHERE salary = (
SELECT MAX(salary) FROM Employee_table e2
WHERE e1.department = e2.department
)
-- SAME THING AGAIN WITH OTHER QUERY
SELECT * FROM Employee_table WHERE salary IN (
SELECT MAX(salary) FROM Employee_table GROUP BY department
)

-- 3. INLINE VIEW QUERY
SELECT department , avg 
FROM (
	SELECT department , AVG(salary) AS avg FROM Employee_table 
	GROUP BY department
) AS dept_avg
WHERE avg > 90000

-- SECTION 6 -- STRING FUNCTIONS
-- 1. CONCAT
SELECT CONCAT(fname, ' ' , lname) AS full_name FROM Employee_table

-- 2. CONCAT WS
-- IF WE WANT A PATTERN LIKE , ONE : TWO : THREE , OR ANY SEPRATER BETWEEN VALUES
-- IN CONCAT WS IN FIRST PARAMETER WE PROVIDE SEPRATOR
SELECT CONCAT_WS(',', fname, lname) FROM Employee_table

-- 3 . SUBSTRING / HOW MANY CHARACTERS YOU WANT TO PRINT
-- FROM HOW TO HOW MANY CHARCTERS YOU WANT TO PRINT
SELECT SUBSTRING(fname, 1,5) FROM Employee_table

-- 4. REPLACE / TO REPLACE A STRING
-- REPLACE ( STRING IN WHICH REPLACE , WHICH PART TO REPLACE , WHICH NEW PART WILL COME THEER)
SELECT REPLACE('HELLO WORLD','HELLO','JELLO')
SELECT REPLACE(department , 'Human Resources', 'HR') FROM Employee_table

-- 5. REVERSE / REVERSE THE STRING
SELECT REVERSE('HELLO')

-- 6. LEN / TO FIND THE LENGTH OF STRING
SELECT LEN(email) FROM Employee_table

-- 7. UPPER / LOWER
SELECT UPPER(fname) FROM Employee_table
SELECT LOWER(fname) FROM Employee_table

-- 8. LEFT / RIGHT 
-- HOW MANY CHARCTERS DO YOU WANT FROM WHICH SIDE
SELECT LEFT('BABAR KHAN',3)
SELECT RIGHT('BABAR KHAN',4)

-- 9. TRIM / TO REMOVE WHITE SPACES JUST FROM START
SELECT TRIM('   BABAR KHAN    ')

-- 10. CHARINDEX / OUR DESIRED CHARTERS ARE WHERE IN STRING
SELECT CHARINDEX('AR','BABAR KHAN')