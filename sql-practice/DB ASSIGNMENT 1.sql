-- ==========================================
-- STEP 1: CREATE DATABASE
-- Logic: Initializes the SLAF system database.
-- ==========================================

CREATE DATABASE SLAF_Management;
GO

-- Switches the active context to our new database
USE SLAF_Management;
GO

-- ==========================================
-- STEP 2A: CREATE USERS TABLE
-- Logic: Creates the main user table with a Computed Column for emails
-- to ensure data consistency without manual entry errors.
-- ==========================================

CREATE TABLE Users (
    UserID INT IDENTITY(1,1) PRIMARY KEY, -- Auto-increments starting at 1
    UniversityID VARCHAR(20) NOT NULL UNIQUE, -- Prevents duplicate student/faculty IDs
    UserName VARCHAR(100) NOT NULL,
    UserPassword VARCHAR(16) NOT NULL, 
    UserType VARCHAR(20) NOT NULL CHECK (UserType IN ('Student', 'Faculty')), -- Domain constraint
    ContactNumber VARCHAR(15) NOT NULL,
    -- Derived Attribute specific to UOG
    UserEmail AS (CAST(UniversityID AS VARCHAR) + '@uog.edu.pk') PERSISTED 
);
GO

-- ==========================================
-- STEP 2B: CREATE ADMINS TABLE
-- Logic: Independent table for the 5 group members managing the system.
-- ==========================================

CREATE TABLE Admins (
    AdminID INT IDENTITY(1,1) PRIMARY KEY,
    AdminName VARCHAR(100) NOT NULL,
    AdminPassword VARCHAR(16) NOT NULL 
);
GO

-- ==========================================
-- STEP 3A: CREATE LOST_ITEMS TABLE
-- Logic: Dependent on Users. Includes a DEFAULT constraint so
-- the status is automatically 'Still Lost' upon creation.
-- ==========================================

CREATE TABLE LostItems (
    LI_ID INT IDENTITY(1,1) PRIMARY KEY,
    UserID INT NOT NULL, -- FK pointing to Users
    LI_Name VARCHAR(100) NOT NULL,
    LI_Description TEXT,
    LI_SecretFeature VARCHAR(255) NOT NULL, -- Hidden verification key
    LI_Location VARCHAR(200),
    LI_Status VARCHAR(20) DEFAULT 'Still Lost' 
        CHECK (LI_Status IN ('Still Lost', 'Matched', 'Claimed')), 
    LI_Time DATETIME DEFAULT GETDATE(), -- Automatically grabs current system time
    
    -- Defining the Foreign Key Constraint
    CONSTRAINT FK_LostItems_Users FOREIGN KEY (UserID) REFERENCES Users(UserID)
);
GO

-- ==========================================
-- STEP 3B: CREATE FOUND_ITEMS TABLE
-- Logic: Dependent on both Users (who found it) and Admins (who hold it).
-- ==========================================

CREATE TABLE FoundItems (
    FI_ID INT IDENTITY(1,1) PRIMARY KEY,
    FinderID INT NOT NULL, 
    AdminID INT NOT NULL, 
    FI_Name VARCHAR(100) NOT NULL,
    FI_Description TEXT,
    FI_SecretFeature VARCHAR(255) NOT NULL, 
    FI_Location VARCHAR(200),
    FI_Time DATETIME DEFAULT GETDATE(),
    FI_Status VARCHAR(20) DEFAULT 'Available' 
        CHECK (FI_Status IN ('Available', 'ClaimPending', 'Returned')), 
        
    -- Defining Multiple Foreign Key Constraints
    CONSTRAINT FK_FoundItems_Users FOREIGN KEY (FinderID) REFERENCES Users(UserID),
    CONSTRAINT FK_FoundItems_Admins FOREIGN KEY (AdminID) REFERENCES Admins(AdminID)
);
GO

-- ==========================================
-- STEP 4: CREATE CLAIMS TABLE
-- Logic: Acts as a transaction record. Uses UNIQUE constraints on FKs
-- to ensure a 1:1 match (one lost item = one found item).
-- ==========================================

CREATE TABLE Claims (
    ClaimID INT IDENTITY(1,1) PRIMARY KEY,
    LI_ID INT NOT NULL UNIQUE, 
    FI_ID INT NOT NULL UNIQUE, 
    ClaimDate DATETIME DEFAULT GETDATE(),
    ClaimStatus VARCHAR(50) DEFAULT 'Under Review' 
        CHECK (ClaimStatus IN ('Under Review', 'Verified', 'Not Verified')), 
    AdminNotes TEXT, 
    
    -- Defining Foreign Key Constraints
    CONSTRAINT FK_Claims_Lost FOREIGN KEY (LI_ID) REFERENCES LostItems(LI_ID),
    CONSTRAINT FK_Claims_Found FOREIGN KEY (FI_ID) REFERENCES FoundItems(FI_ID)
);
GO

-- ==========================================
-- STEP 5: ALTER TABLE COMMANDS
-- Logic: Demonstrates adding a new column and modifying an existing data type
-- without dropping the table.
-- ==========================================

-- Example A: Adding a new column to track the Admin's shift
ALTER TABLE Admins
ADD ShiftTiming VARCHAR(50);
GO

-- Example B: Changing a column's data type (increasing character limit)
ALTER TABLE LostItems
ALTER COLUMN LI_Location VARCHAR(300);
GO

-- ==========================================
-- STEP 6: TRUNCATE AND DROP COMMANDS
-- Logic: Truncate removes data but keeps structure. Drop removes everything.
-- ==========================================

-- Example A: TRUNCATE (Clears all rows, resets IDENTITY, keeps the table shell)
-- Note: Cannot be used on tables referenced by Foreign Keys unless FKs are dropped first.
TRUNCATE TABLE Admins; 

-- Example B: DROP TABLE (Deletes the table and its structure entirely)
-DROP TABLE Claims; 
-GO

