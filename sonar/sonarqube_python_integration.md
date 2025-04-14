# SonarQube Integration for Python Project

## Overview

This documentation details the steps to:
- Set up a **SonarQube server** on **Instance One**
- Run **SonarQube analysis** on a Python project from **Instance Two**

---

## 📍 Instance One: SonarQube Server Setup

### 1. Update System Packages
```bash
sudo apt update
ls
```

### 2. Install Java (OpenJDK 17)
```bash
sudo apt install openjdk-17-jdk
java --version
ls
```

### 3. Install Unzip Utility
```bash
sudo apt install unzip
```

### 4. Unzip SonarQube
```bash
unzip sonarqube-25.4.0.105899.zip
ls
cd sonarqube-25.4.0.105899/
```

### 5. Start SonarQube Server
```bash
cd bin/
ls
cd linux-x86-64/
ls
./sonar.sh
./sonar.sh start
./sonar.sh status
```

---

## 📍 Instance Two: Python Project Setup and SonarQube Analysis

### 1. Update System
```bash
apt update
```

### 2. Clone the Project
```bash
git clone https://github.com/AmishaMurarka/Number-Guessing-Game.git
ls
cd Number-Guessing-Game/
```

### 3. Attempt Sonar Scanner via npm (Optional)
```bash
sonar-scanner -Dsonar.projectKey=python -Dsonar.sources=. -Dsonar.host.url=http://18.234.108.156:9000 -Dsonar.token=sqp_3051aa7f6ec869d028821a2af7d04d4bf0e5d4b0

npm install @sonar/scan
```

### 4. Install Official Sonar Scanner CLI
```bash
cd /opt/
sudo wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-5.0.1.3006-linux.zip
ls
apt install unzip -y
unzip sonar-scanner-cli-5.0.1.3006-linux.zip
```

### 5. Add Sonar Scanner to PATH
Create a profile script to add sonar-scanner to system PATH:
```bash
vi /etc/profile.d/sonar-scanner.sh
```

Add the following content:
```bash
export PATH=$PATH:/opt/sonar-scanner-5.0.1.3006-linux/bin
```

Apply the changes:
```bash
source /etc/profile.d/sonar-scanner.sh
```

### 6. Verify Installation
```bash
sonar-scanner -v
```

### 7. Run Sonar Scanner Analysis
From the project directory:
```bash
cd /home/ubuntu/Number-Guessing-Game
sonar-scanner -Dsonar.projectKey=python -Dsonar.sources=. -Dsonar.host.url=http://18.234.108.156:9000 -Dsonar.token=sqp_3051aa7f6ec869d028821a2af7d04d4bf0e5d4b0
```

---

## ✅ Notes

- Ensure the SonarQube server is accessible from Instance Two.
- Replace `sonar.token` with your own secure token from the SonarQube dashboard.
- Port `9000` should be open in the firewall for access to the SonarQube dashboard.

