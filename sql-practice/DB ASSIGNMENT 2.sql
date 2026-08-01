 -- Part 0 : DATABASE AND TABLE CREATION

 -- CREATING DATABASE
 CREATE DATABASE University_DB

 -- USING DATABASE WE HAVE CREATED
 USE University_DB

 -- CREATING TABLE
 CREATE TABLE Students( 
 StudentID INT, 
 FullName VARCHAR(100), 
 Email VARCHAR(100), 
 City VARCHAR(50), 
 DateOfBirth DATE, 
 Marks INT
);

-- INSERTING DATA INTO TABLE
INSERT INTO Students (StudentID, FullName, Email, City, DateOfBirth, Marks)
VALUES 
(1, 'Ahmed Khan', 'ahmed.k@example.com', 'Gujrat', '2004-05-15', 85),
(2, 'Fatima Ali', 'fatima.a@example.com', 'Lahore', '2005-02-20', 92),
(3, 'Usman Tariq', 'usman.t@example.com', 'Islamabad', '2003-11-10', 78),
(4, 'Ayesha Malik', 'ayesha.m@example.com', 'Rawalpindi', '2004-08-05', 88),
(5, 'Bilal Raza', 'bilal.r@example.com', 'Faisalabad', '2005-01-25', 75),
(6, 'Zainab Qureshi', 'zainab.q@example.com', 'Gujranwala', '2004-09-30', 95),
(7, 'Hamza Sheikh', 'hamza.s@example.com', 'Multan', '2003-12-12', 81);

-- *******************************************************************************************

-- ................................ASSIGNMENT STARTS HERE.................

-- Part 1: Basic Queries 

-- 1. Display all records from the Students table.

-- * WILL SELECT ALL AVAILABLE DATA FROM STUDENTS
SELECT * FROM Students;

-- 2. Show only FullName and Marks of students who scored more than 70.

-- THIS WILL DISPLAY FullName and Marks FROM Stuents TABLE HAVING MARKS MORE THAN 70.
SELECT FullName , Marks FROM Students WHERE Marks > 70;

-- 3. Find students who belong to the city 'Lahore'.

-- THIS WILL ONLY DISPLAY STUDENTS WHICH BELONGS TO LAHORE.
SELECT * FROM Students WHERE City = 'Lahore';

-- *******************************************************************************************

-- Part 2: String Functions

-- 4. Display all student names in uppercase using UPPER().

-- DISPLAY FullName OF STUDENTS WHILE CONVERT IT INTO CAPITAL LETTERS.
SELECT UPPER(FullName) FROM Students;

-- 5. Display all student emails in lowercase using LOWER().

-- DISPLAY ALL EMAILS IN LOWERCASE ORDER.
SELECT LOWER(Email) FROM Students;

-- 6. Show the length of each student’s name using LEN().

-- SHOW THE LENGTH OF FullName OF STUDENTS.
SELECT LEN(FullName) FROM Students;

-- *******************************************************************************************

-- Part 3: Data Conversion

-- 7. Convert DateOfBirth into VARCHAR format using CONVERT().

-- THIS WILL SELECT FullName and DateOfBirth FROM TABLE..
-- THEN CONVERT DateOfBirth TO VARCHAR(20) DATATYPE FROM DATE DATATYPE.
SELECT FullName, DateOfBirth ,
CONVERT(VARCHAR(20), DateOfBirth) 
FROM Students;

-- 8. Display student names along with their birth year only.

-- DISPLAY STUDENTS FullName WITH THEIR BIRTH YEAR ONLY NOT MONTH OR DAY.
SELECT  FullName, YEAR(DateOfBirth) FROM Students;

-- *******************************************************************************************

-- Part 4: Sorting Data

-- 9. Display all students sorted by Marks in descending order using ORDER BY.

-- THIS WILL DISPLAY ALL DATA OF STUDENTS ORDER BY HIGHER TO LOWER MARKS.
SELECT * FROM STUDENTS ORDER BY Marks DESC;

-- 10.Display students sorted by FullName in ascending order.

-- THIS WILL DISPLAY STUDENTS FullName SORTED ALPHABATICALLY..
-- MEAN THE NAME STARTING WITH A COMES FIRST THE NAME STARTING WITH B AND SO ON.
SELECT * FROM Students ORDER BY FullName;

-- *******************************************************************************************

-- Part 5: Combined Queries

-- 11.Display student names in uppercase and sort them by marks (highest to lowest).

-- IT WILL SELECT FullName OF STUDENTS FROM TABLE IN UPPERCASE FORMAT..
-- THEN IT WILL ORDER STUDENTS BASED ON HIGHER TO LOWER MARKS..
-- AND SHOW ONLY FULLNAME AT THE END IN UPPERCASE FORMAT.
SELECT UPPER(FullName) FROM Students ORDER BY Marks DESC;

-- 12. Show student emails in lowercase and sort them alphabetically.

-- SIMPLY CONVERT STUDENTS EMAILS INTO LOWER CASE..
-- THEN ORDER THEM BASE ON ALPHABATICAL ORDER a,b,c,d AND SO ON...
SELECT LOWER(Email) FROM Students ORDER BY Email;

-- 13.Display the length of names for students who scored above 60, ordered by name length.

-- IT WILL FIND THE LENGTH OF STUDENTS NAMES..
-- SELECT ONLY THOSE STUDENTS WHO HAVE MARKS MORE THAN 60..
-- THEN OREDR STUDENTS BASED ON THE LENGTH OF THEIR NAMES FROM LOWER TO HEIGHER..
-- AND FINALY DISPLAY THE LENGHTH OF STUDENTS NAMES HAVING MARKS MORE THAN 60 ORDERD BY NAME LENGTH..
SELECT LEN(FullName) FROM Students WHERE Marks > 60 ORDER BY LEN(FullName);

