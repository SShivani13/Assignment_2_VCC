# # GCP Auto-Scaling and Security Configuration
## 📌 Project Overview
This project demonstrates how to set up a Virtual Machine (VM) on **Google Cloud Platform (GCP)**, implement **auto-scaling policies**, and configure **security measures** like IAM roles and firewall rules.

## 🚀 Features
- ✅ **Virtual Machine Deployment** on GCP
- ✅ **Auto-Scaling** based on CPU utilization
- ✅ **IAM Role Configuration** for secure access
- ✅ **Firewall Rules** to manage incoming traffic

## 🛠️ Steps to Implement
### **1️⃣ Creating a Virtual Machine (VM)**
- Navigate to **Compute Engine > VM Instances**.
- Create a new instance choose an OS (e.g., Ubuntu 20.04 LTS), machine type, and security settings.

### **2️⃣ Configuring IAM Roles**
- Go to **IAM & Admin > IAM**.
- Add to grant permissions to another user.
- Assign roles like **Viewer, Editor, Compute Admin**.
- Click Save to apply the changes.
- Permissions granted to another user successfully 
     

### **3️⃣ Setting up Firewall Rules**
- Enter a Name for the rule (e.g., allow-http-https).
- Under Targets, select All instances in the network.
- Choose Ingress as the direction.
- Provide source IPV4 ranges 192.168.2.0/24
- Under Protocols and Ports, allow HTTP (80) and HTTPS (443).
- Click Create to apply the rule


### **4️⃣ Implementing Auto-Scaling**
- Navigate to **Compute Engine > Instance Groups**.
- Create a **Managed Instance Group** with **Auto-Scaling enabled**.
- Enter a Name (Instance-group-1) and give description
- Select New Managed Instance Group(stateless) and choose the VM template.
- Define the Minimum (1) and Maximum Number of Instances (10).
- Enable Auto-scaling based on CPU utilization (60%).
- Click Create.

### **5️⃣ Testing CPU Utilization**
- Create Python file and run the code CPU utilization
- Checking the CPU Utilization
- As CPU utilization increases, a new instance should be created automatically.
- Once the load reduces, extra instances should be removed.

  ### **Conclusion**
I have successfully deployed a virtual machine on Google Cloud Platform, implemented security measures like IAM roles and firewall rules, and configured auto-scaling policies to ensure efficient resource management. By testing CPU utilization, if validated that auto-scaling responds dynamically to workload fluctuations, ensuring cost-effectiveness and optimal performance. These steps provide a scalable and secure cloud infrastructure suitable for handling varying workloads efficiently.


