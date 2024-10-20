import re

# Function to detect SQL injection vulnerability
def detect_sql_injection(line):
    sql_injection_pattern = re.compile(r"(SELECT|INSERT|UPDATE|DELETE)\s.*[\"']\s*\+\s*.*[\"']")
    return sql_injection_pattern.search(line)

# Function to detect hardcoded credentials
def detect_hardcoded_credentials(line):
    credentials_pattern = re.compile(r"(password\s*=\s*[\"'][^\"']+[\"'])")
    return credentials_pattern.search(line)

# Function to detect improper error handling
def detect_error_handling(line):
    error_handling_pattern = re.compile(r"(print\()")
    return error_handling_pattern.search(line)

# Function to scan the file for vulnerabilities
def check_file_for_vulnerabilities(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    vulnerability_found = False
    print(f"Scanning file: {file_path}")
    
    for line_number, line in enumerate(lines, 1):
        # Check for SQL Injection
        if detect_sql_injection(line):
            print(f"Potential SQL injection vulnerability found at line {line_number}: {line.strip()}")
            vulnerability_found = True
        
        # Check for hardcoded credentials
        if detect_hardcoded_credentials(line):
            print(f"Hardcoded credentials found at line {line_number}: {line.strip()}")
            vulnerability_found = True
    
        if detect_error_handling(line):
            print(f"Improper error handling found at line {line_number}: {line.strip()}")
            vulnerability_found = True

    if not vulnerability_found:
        print("No vulnerabilities found.")

if __name__ == "__main__":
    backend_file = "VulnerableBackend.py"
    check_file_for_vulnerabilities(backend_file)
