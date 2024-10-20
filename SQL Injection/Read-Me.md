# SQL Injection Vulnerability Detection Project

This repository contains a project that demonstrates SQL injection vulnerabilities in a backend application and provides a detection mechanism to identify such vulnerabilities in the code.

## Project Overview

SQL Injection (SQLi) is one of the most critical security vulnerabilities affecting web applications today. It occurs when an attacker is able to manipulate SQL queries by injecting malicious SQL code through user inputs. This can lead to unauthorized access to sensitive data, data modification, and even complete control over the database.

In this project, we created a simulated backend application using Python that is intentionally vulnerable to SQL injection attacks. We also developed a detection script that scans the backend code to identify common vulnerabilities such as SQL injection, hardcoded credentials, and improper error handling.

## What is SQL Injection?

SQL Injection is a code injection technique that exploits a security vulnerability in an application's software. It occurs when an application uses untrusted input to construct SQL queries without proper validation or sanitization. As a result, an attacker can insert arbitrary SQL code into a query, allowing them to perform actions such as:

- Bypassing authentication mechanisms
- Retrieving sensitive data from the database
- Modifying or deleting data
- Executing administrative operations on the database
## Components

### 1. Vulnerable Backend Code

The `VulnerableBackend.py` file contains a simulated backend application that demonstrates several SQL injection vulnerabilities:

- User login functionality
- User registration functionality
- Password update functionality
- User deletion functionality

All these functionalities are implemented using unsafe SQL queries that concatenate user input directly into the SQL statements, making them susceptible to SQL injection attacks.

### 2. Detection Code

The `DetectMultipleVulnerabilities.py` file is a Python script designed to scan the backend code for common vulnerabilities, including:

- SQL injection vulnerabilities
- Hardcoded credentials
- Improper error handling

The detection script uses regular expressions to identify these issues in the code.
### Key Features:
1. **Vulnerable Backend Application**:
   - Created a simulated backend system vulnerable to SQL injection using Python and MySQL.
   - The backend allows login, user registration, password updates, and user deletion, all through vulnerable SQL queries.
   
2. **SQL Injection Exploit**:
   - Demonstrated how an attacker can exploit SQL injection vulnerabilities to gain unauthorized access.
   - Bypassed authentication using crafted SQL payloads.

3. **Vulnerability Detection Script**:
   - Developed a Python-based detection script that scans backend code for common vulnerabilities:
     - SQL Injection vulnerabilities in user input fields.
     - Hardcoded credentials in the source code.
     - Improper error handling that may expose sensitive information.

### Technology Stack:
- **Backend**: Python, MySQL
- **Database**: MySQL
- **Detection Script**: Python (with Regular Expressions for vulnerability detection)


## How to Run the Project

1. **Run the Vulnerable Backend**:
   - Start the vulnerable backend by running the following command:
     ```bash
     python3 VulnerableBackend.py
     ```

2. **Run the Detection Script**:
   - Use the detection script to scan the vulnerable backend code for SQL injection vulnerabilities:
     ```bash
     python3 DetectMultipleVulnerabilities.py
### Prerequisites

Ensure you have Python and the `mysql-connector` package installed. You can install the package using pip:

```bash
pip install mysql-connector-python
