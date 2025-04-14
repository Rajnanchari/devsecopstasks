number-guessing-game-sonarqube

# 🔍 SonarQube Setup & Code Analysis with SonarScanner

This documentation provides step-by-step instructions to set up SonarQube on an Ubuntu EC2 instance and run SonarScanner on a Python project (`Number-Guessing-Game`).

---

## 🧱 Prerequisites

- Ubuntu EC2 instance
- OpenJDK 17+
- Internet access
- Git installed

---

## 🚀 1. Update & Install Java

```bash
sudo apt update
sudo apt install openjdk-17-jdk -y
java --version

2. Download & Extract SonarQube

wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-10.4.0.105899.zip
sudo apt install unzip -y
unzip sonarqube-10.4.0.105899.zip
cd sonarqube-10.4.0.105899/bin/linux-x86-64

Start SonarQube Server

./sonar.sh start
./sonar.sh status

git clone https://github.com/AmishaMurarka/Number-Guessing-Game.git
cd Number-Guessing-Game/

cd /opt
sudo wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-5.0.1.3006-linux.zip
sudo unzip sonar-scanner-cli-5.0.1.3006-linux.zip
sudo mv sonar-scanner-5.0.1.3006-linux sonar-scanner


sudo nano /etc/profile.d/sonar-scanner.sh

export PATH=$PATH:/opt/sonar-scanner/bin
export SONAR_SCANNER_OPTS="-server"

source /etc/profile.d/sonar-scanner.sh

sonar-scanner -v

cd /home/ubuntu/Number-Guessing-Game
nano sonar-project.properties

sonar.projectKey=number-guessing-game-python
sonar.sources=.
sonar.host.url=http://18.234.108.156:9000
sonar.login=sqp_3051aa7f6ec869d028821a2af7d04d4bf0e5d4b0

sonar-scanner

ANALYSIS SUCCESSFUL, you can browse http://18.234.108.156:9000/dashboard?id=number-guessing-game-python

 instance one: 
       sudo apt update
       ls
      sudo apt install openjdk-17-jdk
      java --version
      ls
      sudo apt install unzip
      unzip sonarqube-25.4.0.105899.zip
      ls
      cd sonarqube-25.4.0.105899/
      cd bin/
      ls
      cd linux-x86-64/
      ls
      ./sonar.sh
      ./sonar.sh start
     ./sonar.sh status

instance Two:
       apt update
      git clone https://github.com/AmishaMurarka/Number-Guessing-Game.git
      ls
      cd Number-Guessing-Game/
    
    sonar-scanner   -Dsonar.projectKey=python   -Dsonar.sources=.   -Dsonar.host.url=http://18.234.108.156:9000   -Dsonar.token=sqp_3051aa7f6ec869d028821a2af7d04d4bf0e5d4b0
      npm install @sonar/scan
      sonar-scanner   -Dsonar.projectKey=python   -Dsonar.sources=.   -Dsonar.host.url=http://18.234.108.156:9000   -Dsonar.token=sqp_3051aa7f6ec869d028821a2af7d04d4bf0e5d4b0
    cd /opt/
   
     sudo wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-5.0.1.3006-linux.zip
     ls
     apt install unzip -y
     unzip sonar-scanner-cli-5.0.1.3006-linux.zip
     vi /etc/profile.d/sonar-scanner.sh
     source /etc/profile.d/sonar-scanner.sh
     sonar-scanner -v
     sonar-scanner   -Dsonar.projectKey=python   -Dsonar.sources=.   -Dsonar.host.url=http://18.234.108.156:9000   -Dsonar.token=sqp_3051aa7f6ec869d028821a2af7d04d4bf0e5d4b0
   
    cd /home/ubuntu/Number-Guessing-Game
   sonar-scanner   -Dsonar.projectKey=python   -Dsonar.sources=.   -Dsonar.host.url=http://18.234.108.156:9000   -Dsonar.token=sqp_3051aa7f6ec869d028821a2af7d04d4bf0e5d4b0 














