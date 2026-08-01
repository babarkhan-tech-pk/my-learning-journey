-- 1. DATABASE BANAO
CREATE DATABASE SLAF_Management;
GO

USE SLAF_Management;
GO

-- 2. USERS TABLE (Student/Faculty ke liye)
CREATE TABLE Users (
    UserID INT IDENTITY(1,1) PRIMARY KEY,
    UniversityID VARCHAR(20) NOT NULL UNIQUE, 
    UserName VARCHAR(100) NOT NULL,
    UserPassword VARCHAR(16) NOT NULL, 
    UserType VARCHAR(20) NOT NULL CHECK (UserType IN ('Student', 'Faculty')), 
    ContactNumber VARCHAR(15) NOT NULL,
    -- Yeh line automatically UOG ka email generate karegi
    UserEmail AS (CAST(UniversityID AS VARCHAR) + '@uog.edu.pk') PERSISTED 
);
GO

-- 3. ADMINS TABLE 
CREATE TABLE Admins (
    AdminID INT IDENTITY(1,1) PRIMARY KEY,
    AdminName VARCHAR(100) NOT NULL,
    AdminPassword VARCHAR(16) NOT NULL 
);
GO

-- Tumhara aur tumhari team ka data (Passwords simple rakhe hain testing ke liye)
INSERT INTO Admins (AdminName, AdminPassword) VALUES ('SAIF', 'admin1');
INSERT INTO Admins (AdminName, AdminPassword) VALUES ('HASSAN', 'admin2');
INSERT INTO Admins (AdminName, AdminPassword) VALUES ('ZEESHAN', 'admin3');
INSERT INTO Admins (AdminName, AdminPassword) VALUES ('ALI', 'admin4');
INSERT INTO Admins (AdminName, AdminPassword) VALUES ('AHMED', 'admin5');
GO

-- 4. LOST ITEMS TABLE
CREATE TABLE LostItems (
    LI_ID INT IDENTITY(1,1) PRIMARY KEY,
    UserID INT NOT NULL, 
    LI_Name VARCHAR(100) NOT NULL,
    LI_Description TEXT,
    LI_SecretFeature VARCHAR(255) NOT NULL, 
    LI_Location VARCHAR(300), 
    LI_Status VARCHAR(20) DEFAULT 'Still Lost' 
        CHECK (LI_Status IN ('Still Lost', 'Matched', 'Claimed')), 
    LI_Time DATETIME DEFAULT GETDATE(), 
    
    CONSTRAINT FK_LostItems_Users FOREIGN KEY (UserID) REFERENCES Users(UserID)
);
GO

-- 5. FOUND ITEMS TABLE
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
        
    CONSTRAINT FK_FoundItems_Users FOREIGN KEY (FinderID) REFERENCES Users(UserID),
    CONSTRAINT FK_FoundItems_Admins FOREIGN KEY (AdminID) REFERENCES Admins(AdminID)
);
GO

-- 6. CLAIMS TABLE (Lost aur Found ko jorne ke liye)
CREATE TABLE Claims (
    ClaimID INT IDENTITY(1,1) PRIMARY KEY,
    LI_ID INT NOT NULL UNIQUE, 
    FI_ID INT NOT NULL UNIQUE, 
    ClaimDate DATETIME DEFAULT GETDATE(),
    ClaimStatus VARCHAR(50) DEFAULT 'Under Review' 
        CHECK (ClaimStatus IN ('Under Review', 'Verified', 'Not Verified')), 
    AdminNotes TEXT, 
    
    CONSTRAINT FK_Claims_Lost FOREIGN KEY (LI_ID) REFERENCES LostItems(LI_ID),
    CONSTRAINT FK_Claims_Found FOREIGN KEY (FI_ID) REFERENCES FoundItems(FI_ID)
);
GO

SELECT * FROM Users;
SELECT * FROM LostItems;
SELECT * FROM FoundItems;
SELECT * FROM Admins;
SELECT * FROM Claims;

SELECT * 
FROM Admins AS A
INNER JOIN FoundItems AS F
ON A.AdminID = F.AdminID
WHERE A.AdminID = 1