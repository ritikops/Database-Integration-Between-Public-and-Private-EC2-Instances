# Secure Database Integration Between Public and Private EC2 Instances

## **Overview**
This project sets up **two EC2 instances** (Public & Private), where the public instance hosts an application, and the private instance runs a **MySQL database**. A Python script connects the public EC2 instance to the private database.

---

## **Architecture**
- **Public EC2 Instance**: Hosts a Python app that interacts with the database.  
- **Private EC2 Instance**: Hosts the MySQL database.  
- **Security Group Configuration**: Only allows connections from the public EC2.  

---

## **1. Prerequisites**
- An **AWS account**  
- **IAM role** with EC2 and S3 permissions  
- **SSH Key Pair** for EC2 instances  
- **Git & GitHub Account**  

---

## **2. Setup Steps**

### **Step 1: Create Public & Private EC2 Instances**
#### **1.1 Launch Public EC2 Instance**
1. Go to **AWS EC2 Dashboard** > **Launch Instance**.  
2. Select **Ubuntu 22.04**.  
3. Place it in a **public subnet** with an **Elastic IP**.  
4. Create a **security group** with:  
   - SSH (22) → **Your IP**  
   - HTTP (80) → **Anywhere**  
   - MySQL (3306) → **Private EC2 only**  

#### **1.2 Launch Private EC2 Instance**
1. Launch another **Ubuntu 22.04** EC2 instance.  
2. Place it in a **private subnet** (no public IP).  
3. Create a **security group** with:  
   - SSH (22) → **Allow only from Public EC2**  
   - MySQL (3306) → **Allow only from Public EC2**  

---

### **Step 2: Configure MySQL on the Private EC2**
1. SSH into the **private EC2** via the public instance:  
   ```bash
   ssh -i your-key.pem ubuntu@private-instance-private-ip
Install MySQL:

sudo apt update && sudo apt install mysql-server -y
Configure MySQL:
sql

CREATE DATABASE mydb;
CREATE USER 'admin'@'%' IDENTIFIED BY 'StrongPassword';
GRANT ALL PRIVILEGES ON mydb.* TO 'admin'@'%';
FLUSH PRIVILEGES;
Modify MySQL config (/etc/mysql/mysql.conf.d/mysqld.cnf):
Change bind-address = 127.0.0.1 → bind-address = 0.0.0.0
Restart MySQL:

sudo systemctl restart mysql
⚡ 1.3 Install MySQL Client on Public EC2
SSH into public EC2:

ssh -i your-key.pem ubuntu@public-instance-public-ip
Install MySQL client:

sudo apt update && sudo apt install mysql-client -y
Test connection to private MySQL DB:

mysql -h private-instance-private-ip -u admin -p
Exit MySQL:
sql


exit;
💻 1.4 Link Public EC2 to Private DB with Python
Install MySQL Connector on the public EC2:

pip install mysql-connector-python
Create Python script (connect_db.py):
python

import mysql.connector

db_host = "private-instance-private-ip"
db_user = "admin"
db_password = "StrongPassword"
db_name = "mydb"

try:
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100))")
    cursor.execute("INSERT INTO users (name) VALUES ('Ritik'), ('Sonu')")
    conn.commit()

    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()
    print("Database connection successful!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

python3 connect_db.py
Expected Output:

(1, 'Ritik')
(2, 'Sonu')
Database connection successful!
