# Hospital Management System

This project is a **Hospital Management System** built using **Flask** as the web framework, with **MongoDB** for NoSQL storage and **MySQL** for relational database management. The system allows you to manage **patients**, **doctors**, **appointments**, and **billing**.

## Table of Contents

1. [Setup Instructions](#setup-instructions)
2. [Running the Application](#running-the-application)
3. [MongoDB Setup](#mongodb-setup)
4. [MySQL Setup](#mysql-setup)
5. [Routes and Features](#routes-and-features)
6. [Resetting Data](#resetting-data)
7. [Verifying Data](#verifying-data)
8. [Troubleshooting](#troubleshooting)

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone <repository_url>
cd hospital-management-system

2. Install Dependencies
Make sure you have Python installed. Then, install the required libraries:
pip install -r requirements.txt


3. Install MySQL and MongoDB
Install MySQL: Follow the installation instructions for your OS at MySQL Downloads.
Install MongoDB: Follow the installation instructions at MongoDB Download Center.


4. Configure MongoDB
Make sure MongoDB is running locally on port 27017 (default). You can start MongoDB with:
On Windows: Start MongoDB as a service.
On Linux/macOS: Use the command sudo service mongod start.


5. Configure MySQL
Ensure that MySQL is running on the default port 3306. Create a database named HospitalManagement in MySQL and create the necessary tables:

sql
Copy code
CREATE DATABASE HospitalManagement;
USE HospitalManagement;

CREATE TABLE Patients (
    Patient_ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT,
    Gender VARCHAR(10),
    Address TEXT,
    Phone VARCHAR(15),
    Medical_History TEXT
);

CREATE TABLE Doctors (
    Doctor_ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Specialization VARCHAR(100),
    Phone VARCHAR(15),
    Experience INT
);

CREATE TABLE Appointments (
    Appointment_ID INT PRIMARY KEY,
    Patient_ID INT,
    Doctor_ID INT,
    Date DATE,
    Time TIME,
    Status VARCHAR(20),
    FOREIGN KEY (Patient_ID) REFERENCES Patients(Patient_ID)
);

CREATE TABLE Billing (
    Bill_ID INT PRIMARY KEY,
    Appointment_ID INT,
    Total_Amount DECIMAL(10, 2),
    Payment_Status VARCHAR(20),
    FOREIGN KEY (Appointment_ID) REFERENCES Appointments(Appointment_ID)
);
