-- car connect
create database car_connect_data;
use car_connect_data;
/*1. Customer Table: 
• CustomerID (Primary Key): Unique identifier for each customer. 
• FirstName: First name of the customer. 
• LastName: Last name of the customer. 
• Email: Email address of the customer for communication. 
• PhoneNumber: Contact number of the customer. 
• Address: Customer's residential address. 
• Username: Unique username for customer login. 
• Password: Securely hashed password for customer authentication. 
• RegistrationDate: Date when the customer registered. 
2. Vehicle Table: 
• VehicleID (Primary Key): Unique identifier for each vehicle. 
• Model: Model of the vehicle. 
• Make: Manufacturer or brand of the vehicle. 
• Year: Manufacturing year of the vehicle. 
• Color: Color of the vehicle. 
• RegistrationNumber: Unique registration number for each vehicle. 
• Availability: Boolean indicating whether the vehicle is available for rent. 
• DailyRate: Daily rental rate for the vehicle. 
3. Reservation Table: 
• ReservationID (Primary Key): Unique identifier for each reservation. 
• CustomerID (Foreign Key): Foreign key referencing the Customer table. 
• VehicleID (Foreign Key): Foreign key referencing the Vehicle table. 
• StartDate: Date and time of the reservation start. 
• EndDate: Date and time of the reservation end. 
• TotalCost: Total cost of the reservation. 
• Status: Current status of the reservation (e.g., pending, confirmed, completed). 
4. Admin Table: 
• AdminID (Primary Key): Unique identifier for each admin. 
• FirstName: First name of the admin. 
• LastName: Last name of the admin. 
• Email: Email address of the admin for communication. 
• PhoneNumber: Contact number of the admin. 
• Username: Unique username for admin login. 
• Password: Securely hashed password for admin authentication. 
• Role: Role of the admin within the system (e.g., super admin, fleet manager). 
• JoinDate: Date when the admin joined the system.*/

CREATE TABLE IF NOT EXISTS Customer (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    PhoneNumber VARCHAR(15) NOT NULL,
    Address VARCHAR(255),
    Username VARCHAR(50) NOT NULL UNIQUE,
    Password VARCHAR(100) NOT NULL,
    RegistrationDate timestamp default current_timestamp
);


CREATE TABLE IF NOT EXISTS Vehicle (
    VehicleID INT AUTO_INCREMENT PRIMARY KEY,
    Model VARCHAR(50) NOT NULL,
    Make VARCHAR(50) NOT NULL,
    Year INT CHECK (Year >= 1990), -- restrict future buggy years
    Color VARCHAR(30),
    RegistrationNumber VARCHAR(20) UNIQUE NOT NULL,
    Availability BOOLEAN DEFAULT TRUE,
    DailyRate DECIMAL(10,2) CHECK (DailyRate >= 0),
    Category Varchar(50) NOT NULL
);


CREATE TABLE IF NOT EXISTS Reservation (
    ReservationID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT,
    VehicleID INT,
    StartDate DATETIME NOT NULL,
    EndDate DATETIME NOT NULL,
    TotalCost DECIMAL(10,2) CHECK (TotalCost >= 0),
    Status ENUM('Pending', 'Confirmed', 'Completed', 'Cancelled') DEFAULT 'Pending',
    
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (VehicleID) REFERENCES Vehicle(VehicleID)
        ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS Admin (
    AdminID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    PhoneNumber VARCHAR(15),
    Username VARCHAR(50) NOT NULL UNIQUE,
    Password VARCHAR(100) NOT NULL,
    Role ENUM('Super Admin', 'Fleet Manager', 'Support') DEFAULT 'Fleet Manager',
    JoinDate timestamp DEFAULT current_timestamp
);
DESC admin;
desc customer;
desc reservation;
desc vehicle;
INSERT INTO Vehicle (Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate, Category) VALUES
('Swift VXI', 'Maruti Suzuki', 2022, 'White', 'TN01AB1234', 1, 1200.00, 'Budget Hatchback'),
('Creta SX', 'Hyundai', 2023, 'Black', 'TN02BC5678', 1, 2500.00, 'Mid-to-High Range SUV'),
('Innova Crysta', 'Toyota', 2021, 'Silver', 'TN03CD4321', 1, 3000.00, 'Luxury Cars'),
('Altroz XT', 'Tata', 2022, 'Red', 'TN04DE8765', 1, 1400.00, 'Budget Hatchback'),
('Seltos HTX', 'Kia', 2023, 'Blue', 'TN05EF2345', 0, 2600.00, 'Mid-to-High Range SUV'),
('XUV700 AX7', 'Mahindra', 2023, 'Black', 'TN06FG7890', 1, 3200.00, 'Luxury Cars'),
('City ZX', 'Honda', 2020, 'Grey', 'TN07GH6543', 1, 2200.00, 'Sleek Sedans'),
('Ertiga ZXI', 'Maruti Suzuki', 2021, 'White', 'TN08HI9876', 0, 2000.00, 'Sleek Sedans'),
('Tigor EV', 'Tata', 2023, 'Blue', 'TN09IJ1357', 1, 1800.00, 'EV Cars'),
('Venue S+', 'Hyundai', 2022, 'Silver', 'TN10JK8642', 1, 1900.00, 'Budget Hatchback'),
('Punch Creative', 'Tata', 2022, 'Yellow', 'TN11KL1122', 1, 1600.00, 'Budget Hatchback'),
('Compass Limited', 'Jeep', 2021, 'Black', 'TN12MN3344', 1, 3500.00, 'Luxury Cars');
select * from vehicle;

INSERT INTO Admin (FirstName, LastName, Email, PhoneNumber, Username, Password, Role, JoinDate)
VALUES
('Yogesh', 'Raman', 'yogesh.admin@example.com', '9876543210', 'admin_yogesh', 'admin123', 'Super Admin', CURRENT_TIMESTAMP),
('Ram', 'Kumar', 'ram.manager@example.com', '9123456780', 'admin_ram', 'admin456', 'Fleet Manager', CURRENT_TIMESTAMP);

select * from admin;
INSERT INTO Customer (FirstName, LastName, Email, PhoneNumber, Address, Username, Password, RegistrationDate)
VALUES 
('Karthik', 'R', 'karthikr@example.com', '9845612398', '123 MG Road, Chennai', 'karthik98', 'pass123', CURRENT_TIMESTAMP);

select * from customer;
INSERT INTO Reservation (CustomerID, VehicleID, StartDate, EndDate, TotalCost, Status)
VALUES (1, 2, '2024-06-22 10:00:00', '2024-06-25 18:00:00', 7500.00,'Confirmed');
select * from reservation;