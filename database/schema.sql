---- Create database (run in SQL Server Management Studio)
--IF DB_ID('portfolio_db') IS NULL
--    CREATE DATABASE portfolio_db;
--GO

--USE portfolio_db;
--GO

---- Table for contact messages
--IF OBJECT_ID('contact_messages', 'U') IS NULL
--BEGIN
--    CREATE TABLE contact_messages (
--        id INT IDENTITY(1,1) PRIMARY KEY,
--        name NVARCHAR(100),
--        email NVARCHAR(100),
--        message NVARCHAR(MAX),
--        created_at DATETIME DEFAULT GETDATE()
--    )
--END
--GO

SELECT * FROM contact_messages;