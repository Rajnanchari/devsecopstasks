collecttracker-sonarqube-setup.md
md
Copy
Edit
# 🚀 Deploy & Analyze CollectTracker (React + Node.js) with SonarQube

This guide walks through setting up the CollectTracker app, deploying it via Apache2, and analyzing JavaScript code using SonarQube.

---

## ⚙️ 1. Install Prerequisites

```bash
sudo apt update
sudo apt install git npm apache2 -y
📥 2. Clone the Repository
bash
Copy
Edit
git clone https://github.com/Bighairymtnman/CollectTracker.git
cd CollectTracker/
📁 3. Project Structure
bash
Copy
Edit
CollectTracker/
├── client/   # Frontend (React)
└── server/   # Backend (Node.js)
📦 4. Install Dependencies
Root project dependencies (if any):
bash
Copy
Edit
npm install
Install frontend dependencies:
bash
Copy
Edit
cd client/
npm install
Install backend dependencies:
bash
Copy
Edit
cd ../server/
npm install
🧪 5. Development Mode
To run the server (Node.js) in dev mode:

bash
Copy
Edit
npm run dev
🛠️ 6. Build Frontend for Production
bash
Copy
Edit
cd ../client/
npm run build
This creates a build/ directory containing the production-ready frontend.

🌐 7. Deploy Frontend via Apache2
bash
Copy
Edit
sudo apt install apache2 -y
sudo systemctl start apache2

# Remove default Apache index
cd /var/www/html/
sudo rm index.html

# Copy React build files to Apache document root
sudo cp -r /home/ubuntu/CollectTracker/client/build/* /var/www/html/
🔍 8. Set Up SonarQube for JavaScript Code Analysis
Step 1: Ensure SonarQube is Running
If not already installed:

bash
Copy
Edit
# Install Java
sudo apt install openjdk-17-jdk -y

# Download and unzip SonarQube
wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-25.4.0.105899.zip
unzip sonarqube-25.4.0.105899.zip
sudo chown -R ubuntu:ubuntu sonarqube-25.4.0.105899

# Start SonarQube
cd sonarqube-25.4.0.105899/bin/linux-x86-64/
./sonar.sh start
Then access in your browser:

cpp
Copy
Edit
http://<your-server-ip>:9000
Login:

Username: admin

Password: admin (change it after first login)

Generate a token from:
My Account → Security → Generate Token

✅ 9. Run SonarQube Analysis for JavaScript
From project root:
Create a file called sonar-project.properties:

properties
Copy
Edit
# sonar-project.properties
sonar.projectKey=CollectTracker
sonar.projectName=CollectTracker App
sonar.projectVersion=1.0

sonar.sourceEncoding=UTF-8
sonar.host.url=http://<your-server-ip>:9000
sonar.login=<your-token>

sonar.sources=client/src,server
sonar.exclusions=**/node_modules/**,**/build/**
Replace <your-server-ip> and <your-token> accordingly.

Then run:

bash
Copy
Edit
npx sonar-scanner
🔐 Make sure you have npx (comes with npm), and SonarQube is running.

📝 Notes
SonarQube will scan both frontend (client/src) and backend (server/) JavaScript code.

You can open results at:
http://<your-server-ip>:9000/dashboard?id=CollectTracker

If you want SonarQube to run in the background on boot, consider setting it up as a systemd service.

