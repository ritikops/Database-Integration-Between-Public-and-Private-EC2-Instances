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
