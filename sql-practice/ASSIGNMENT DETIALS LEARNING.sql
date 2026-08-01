USE Practice

-- table 1

CREATE TABLE Users( 
user_id INTEGER PRIMARY KEY IDENTITY(1,1),
 name VARCHAR(100) NOT NULL,
 email VARCHAR(100) NOT NULL UNIQUE, 
password VARCHAR(100) NOT NULL,
 role VARCHAR(100) CHECK(role IN ('Buyer','Freelancer')),
 country VARCHAR(100) NOT NULL,
 join_date DATE DEFAULT CURRENT_DATE );
 
 -- table 1 data

 INSERT INTO Users (name, email, password, role, country) VALUES
('Alice Smith', 'alice@example.com', 'hashed_pass_1', 'Freelancer', 'United States'),
('Bob Jones', 'bob@example.com', 'hashed_pass_2', 'Freelancer', 'United Kingdom'),
('Charlie Brown', 'charlie@example.com', 'hashed_pass_3', 'Freelancer', 'Canada');

SELECT * FROM Users
 -- table 2

 CREATE TABLE Freelancer( 
freelancer_id INTEGER PRIMARY KEY IDENTITY(1,1),
 user_id INTEGER NOT NULL,
 skills TEXT,
 experience_level TEXT,
 portfolio_link TEXT,
 rating REAL CHECK(rating BETWEEN 0 AND 5),
 FOREIGN KEY (user_id) REFERENCES Users(user_id) );

 -- table 2 data

 INSERT INTO Freelancer (user_id, skills, experience_level, portfolio_link, rating) VALUES
(1, 'Web Development, React, Node.js', 'Expert', 'https://alicesmith.dev', 4.9),
(2, 'Graphic Design, UI/UX, Figma', 'Intermediate', 'https://bobjonesdesign.com', 4.5),
(3, 'Copywriting, SEO, Content Strategy', 'Senior', 'https://charliewrites.com', 4.8);

SELECT * FROM Freelancer

 -- table 3

CREATE TABLE Software_Item(
Item_ID INT IDENTITY(1,1) PRIMARY KEY,
Title VARCHAR(150) NOT NULL,
Description TEXT,
Price DECIMAL(10,2),
Access_Type VARCHAR(20),
Upload_Date DATETIME DEFAULT GETDATE(),
Version VARCHAR(20) UNIQUE,
Freelancer_ID INT,
FOREIGN KEY(freelancer_id) REFERENCES Freelancer(freelancer_id)
);
-- table 3 data

INSERT INTO Software_Item
(Title,Description,Price,Access_Type,Version,Freelancer_ID)
VALUES
('Inventory Management System','Manage store inventory',50,'Paid','1.0',1),
('Chat Application','Real time messaging system',30,'Paid','1.1',1),
('AI Image Generator','Generate AI images',70,'Paid','2.0',2);

SELECT * FROM Software_Item

-- table 4

CREATE TABLE Purchase( 
purchase_id INTEGER PRIMARY KEY IDENTITY(1,1),
 user_id INTEGER, 
purchase_date DATE DEFAULT CURRENT_DATE,
 payment_status TEXT DEFAULT 'Pending',
 license_type TEXT, FOREIGN KEY (user_id) REFERENCES Users(user_id) );

 -- table 4 data
 INSERT INTO Purchase (user_id, license_type) VALUES
(1, 'Single-User'),
(2, 'Enterprise'),
(3, 'Subscription');

SELECT * FROM Purchase

-- Operations

-- Add phone number to Users table
ALTER TABLE Users 
ADD phone VARCHAR(20);
UPDATE Users SET phone = '0301-56789012' WHERE phone IS NULL

-- Add availability status to Freelancer table (Using VARCHAR to avoid TEXT errors)
ALTER TABLE Freelancer 
ADD availability VARCHAR(50) DEFAULT 'Available';
UPDATE Freelancer SET availability = 'Available' WHERE availability IS NULL

-- Add discount column to Purchase table
ALTER TABLE Purchase 
ADD discount REAL DEFAULT 0;
UPDATE Purchase SET discount = 0  WHERE discount IS NULL

-- Modify column types
ALTER TABLE Users 
ALTER COLUMN name VARCHAR(150) NOT NULL;

ALTER TABLE Freelancer 
ALTER COLUMN skills VARCHAR(255);

-- Add UNIQUE constraint to country in Users
ALTER TABLE Users
ADD CONSTRAINT unique_country UNIQUE (country);

-- Add CHECK constraint to experience_level
-- Step 1: Fix the existing data that is breaking the rule
UPDATE Freelancer 
SET experience_level = 'Expert' 
WHERE experience_level = 'Senior';

-- Step 2: Now add the constraint safely!
ALTER TABLE Freelancer 
ADD CONSTRAINT chk_experience 
CHECK (experience_level IN ('Beginner', 'Intermediate', 'Expert'));

-- Add CHECK constraint to payment_status
-- Step 1: Drop the default constraint that is blocking the change
ALTER TABLE Purchase 
DROP CONSTRAINT -- YOUR DEFAULT OBJECT CAME HERE;

-- Step 2: Now change the column type to standard VARCHAR
ALTER TABLE Purchase 
ALTER COLUMN payment_status VARCHAR(50);

-- Step 3: Put the original DEFAULT 'Pending' rule back (giving it a clean name this time)
ALTER TABLE Purchase 
ADD CONSTRAINT df_payment_status DEFAULT 'Pending' FOR payment_status;

-- Step 4: Finally, add your new CHECK constraint safely!
ALTER TABLE Purchase 
ADD CONSTRAINT chk_payment 
CHECK (payment_status IN ('Pending', 'Completed', 'Failed'));

-- ENTER DATA TO CHECK NEW MODIFICATIONS
INSERT INTO Users (name, email, password, role, country) 
VALUES ('David Miller', 'david@example.com', 'hashed_pass_4', 'Freelancer', 'Australia');

-- Assuming David was the 4th user created, so his user_id is 4
-- Step 1: Drop the old hidden constraint using the exact name from your error
ALTER TABLE Freelancer 
DROP CONSTRAINT CK__Freelance__ratin__619B8048;

-- Step 2: Add the new constraint allowing ratings all the way up to 10
ALTER TABLE Freelancer 
ADD CONSTRAINT chk_rating CHECK (rating BETWEEN 0 AND 10);

-- Step 3: Now run your insert again! It will work perfectly.
INSERT INTO Freelancer (user_id, skills, experience_level, portfolio_link, rating) 
VALUES (4, 'Python, SQL, Data Analysis', 'Expert', 'https://davidmiller.dev', 9.5);

INSERT INTO Purchase (user_id,  license_type, payment_status) 
VALUES (4, 'Commercial', 'Completed');

SELECT * FROM Users;
SELECT * FROM Freelancer;
SELECT * FROM Purchase;

-- Drop phone column from Users (Fixed typo from 'User' to 'Users')
ALTER TABLE Users 
DROP COLUMN phone;

-- Drop constraints we just added above
ALTER TABLE Users 
DROP CONSTRAINT unique_country;

ALTER TABLE Purchase 
DROP CONSTRAINT chk_payment;