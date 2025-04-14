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

 Work 
    sudo apt update
    2  ls
    3  sudo apt install openjdk-17-jdk
    4  java --version
    5  ls
    6  apt install unzip
    7  ls
    8  sudo apt install unzip
    9  ls
   10  uzip sonarqube-25.4.0.105899.zip
   11  unzip sonarqube-25.4.0.105899.zip
   12  ls
   13  cd sonarqube-25.4.0.105899/
   14  ls
   15  cd bin/
   16  ls
   17  cd linux-x86-64/
   18  ls
   19  ./sonar.sh
   20  ./sonar.sh start
   21  ./sonar.sh status


 apt update
    2  git clone https://github.com/AmishaMurarka/Number-Guessing-Game.git
    3  ls
    4  cd Number-Guessing-Game/
    5  ls
    6  sonar-scanner   -Dsonar.projectKey=python   -Dsonar.sources=.   -Dsonar.host.url=http://18.234.108.156:9000   -Dsonar.token=sqp_3051aa7f6ec869d028821a2af7d04d4bf0e5d4b0
    7  apt install npm -y
    8  npm install @sonar/scan
    9  sonar-scanner   -Dsonar.projectKey=python   -Dsonar.sources=.   -Dsonar.host.url=http://18.234.108.156:9000   -Dsonar.token=sqp_3051aa7f6ec869d028821a2af7d04d4bf0e5d4b0
   10  cd /opt/
   11  ls
   12  sudo wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-5.0.1.3006-linux.zip
   13  ls
   14  apt install unzip -y
   15  unzip sonar-scanner-cli-5.0.1.3006-linux.zip
   16  vi /etc/profile.d/sonar-scanner.sh
   17  source /etc/profile.d/sonar-scanner.sh
   18  sonar-scanner -v
   19  sonar-scanner   -Dsonar.projectKey=python   -Dsonar.sources=.   -Dsonar.host.url=http://18.234.108.156:9000   -Dsonar.token=sqp_3051aa7f6ec869d028821a2af7d04d4bf0e5d4b0
   20  history
   21  cd /home/ubuntu/Number-Guessing-Game
   22  sonar-scanner   -Dsonar.projectKey=python   -Dsonar.sources=.   -Dsonar.host.url=http://18.234.108.156:9000   -Dsonar.token=sqp_3051aa7f6ec869d028821a2af7d04d4bf0e5d4b0 














