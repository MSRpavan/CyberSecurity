# Cybersecurity Projects

Welcome to my Cybersecurity Projects repository! This repository showcases various projects I've worked on related to cybersecurity. Below is an overview of the projects, with a focus on **SQL Injection**.

## Table of Contents
- [SQL Injection Detection and Exploitation](#sql-injection-detection-and-exploitation)

---

## SQL Injection Detection and Exploitation

### Project Overview
SQL Injection (SQLi) is one of the most common vulnerabilities in web applications that allows attackers to interact with the database by manipulating SQL queries. This project focuses on detecting and exploiting SQL injection vulnerabilities in backend systems.

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

### How to Run:

1. **Run the Vulnerable Backend**:
   - Start the vulnerable backend by running the following command:
     ```bash
     python3 VulnerableBackend.py
     ```

2. **Run the Detection Script**:
   - Use the detection script to scan the vulnerable backend code for SQL injection vulnerabilities:
     ```bash
     python3 DetectMultipleVulnerabilities.py
     ```

### Project Structure:

```bash
.
├── VulnerableBackend.py             # Simulated backend with SQL injection vulnerability
├── DetectMultipleVulnerabilities.py # Python script to detect vulnerabilities
└── README.md                        # Project documentation
