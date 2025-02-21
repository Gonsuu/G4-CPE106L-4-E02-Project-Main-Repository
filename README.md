**Quick Eats - Sprint 1 Setup Instructions**

//These commands are executed in the Ubuntu WSL terminal

### **1. Update System Packages**
Before installing anything, ensure your system is up to date:

type: sudo apt update

### **2. Install Python and Virtual Environment**
Ensure Python are installed:

type: sudo apt install python3

### **3. Create and Activate Virtual Environment**
Navigate to your home directory and set up a virtual environment:

type:  cd ~ #call directory <br>
       sudo apt install python3.12-venv

### **4. Install Git (If Not Installed)**
Check if Git is installed:

type:  git --version

If not, install it:

type:  sudo apt install git

### **5. Clone the GitHub Repository**
Download the project from GitHub:

type: git clone https://github.com/Gonsuu/G4-CPE106L-4-E02-Project-Main-Repository


### **6. Navigate to the Project Directory**

type: cd G4-CPE106L-4-E02-Project-Main-Repository/Sprint01

Verify you're in the correct folder:

type:  pwd

Expected output:

/home/your-ubuntu-username/G4-CPE106L-4-E02-Project-Main-Repository/Sprint01


### **7. Run the Application**

//You must be in the Sprint01 directory to execute this
type:  python3 main.py

### **8. Run Unit Tests**
To verify that everything works correctly, run:

type: python3 <unit-test-filename.py>

### **Additional Notes**
- Ensure **Ubuntu WSL is installed** and running inside **Oracle VirtualBox**.
- If you encounter **permission issues**, try:
  
  sudo chmod -R 755 G4-CPE106L-4-E02-Project-Main-Repository
  
- If you get **"command not found" errors**, ensure Python and Git are installed properly.
