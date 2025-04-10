### Flask Application Setup & Deployment with Gunicorn and systemd
  
  This documentation describes the steps taken to set up a Flask application in a virtual environment, install the necessary dependencies, run the application with Gunicorn, and create a systemd service file for automatic management.



### 1. Install pip for Python 3 and verify its version
sudo apt install python3-pip -y
ls
pip3 --version

### 2. Install required Python packages from requirements.txt (if applicable)
sudo pip3 install -r requirements.txt

### 3. Create a virtual environment in the project directory
python3 -m venv venv

### 4. (Optional) Install Python3.12-venv if required by your system
sudo apt install python3.12-venv

### 5. Activating the virtual environment
  Note: Do not use sudo with source. Ensure you are in the correct directory.
cd ~
source venv/bin/activate

### 6. Navigate into your Flask app directory (Flask-App)
cd ~/Flask-App

### 7. (Optional) Re-create or confirm the virtual environment in the project folder
python3 -m venv venv
source venv/bin/activate

### 8. Install Flask and other dependencies inside the virtual environment
pip3 install flask

### 9. Run the Flask development server
python3 app.py

### 10. Install Gunicorn, the WSGI HTTP server for running your Flask app
pip install gunicorn

### 11. Test Gunicorn manually by running:
gunicorn --bind 0.0.0.0:8000 app:app

### 12. Create and edit the systemd service file for your Flask app
sudo nano /etc/systemd/system/flask-app.service

### 13. Reload systemd to recognize the new service file
sudo systemctl daemon-reload

### 14. Enable the service (set to start automatically at boot)
sudo systemctl enable flask-app

### 15. Start the service
sudo systemctl start flask-app

### 16. Check the status of your service
sudo systemctl status flask-app

### 17. Follow the logs for the Flask app service
sudo journalctl -u flask-app -f

### 18. Allow incoming traffic on port 8000 (if using ufw or another firewall)
sudo ufw allow 8000
=========================================

### 1. Install pip and Create a Virtual Environment
 Install pip for Python 3:
 sudo apt install python3-pip -y

### Verify pip Installation:
pip3 --version

### Create a Virtual Environment:
python3 -m venv venv

### Activate the Virtual Environment:
source venv/bin/activate
 
 ### 2. Setting Up Your Flask Application

 Navigate to Your Flask Application Directory:
   cd ~/Flask-App

(Optional) Re-Create the Virtual Environment in Your Project Folder:
python3 -m venv venv
source venv/bin/activate


Install Flask:
Inside your virtual environment, install Flask:
pip3 install flask


Run the Application in Development Mode:

Start your Flask app using:
python3 app.py

### 3. Testing with Gunicorn
  pip install gunicorn

Run Gunicorn to Serve the Application:
Test Gunicorn by running:

gunicorn --bind 0.0.0.0:8000 app:app

### 4. Creating the systemd Service File

[Unit]
Description=Gunicorn instance to serve Flask-App
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/Flask-App
ExecStart=/home/ubuntu/Flask-App/venv/bin/gunicorn --workers 3 --bind 0.0.0.0:8000 app:app

# Allow up to 90 seconds for graceful shutdown
TimeoutStopSec=90
Restart=always
KillMode=mixed

[Install]
WantedBy=multi-user.target


5. Enabling and Starting the systemd Service
Reload systemd:
After creating or modifying your service file, reload the systemd daemon:

sudo systemctl daemon-reload
sudo systemctl enable flask-app

sudo systemctl start flask-app
sudo systemctl status flask-app

View Service Logs:
sudo journalctl -u flask-app -f

6. Network and Firewall Configuration
  Allow Traffic on the Application Port:
If a firewall (like UFW) is running, allow traffic on port 8000:

sudo ufw allow 8000
![](./images/pythontask.png)