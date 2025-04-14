
## Train Ticket Reservation System – Deployment Documentation

###  Prerequisites
    nsure your Ubuntu system is updated and has the following installed:

      Java (OpenJDK 17)
      Maven
      Git
      Apache Tomcat 9

 ### Step 1: Update System & Install Dependencies
    sudo apt update
    sudo apt install openjdk-17-jre-headless -y
    sudo apt install maven -y
    sudo apt install git -y

 ### Step 2: Clone the Project from GitHub

     git clone https://github.com/shashirajraja/Train-Ticket-Reservation-System.git
     cd Train-Ticket-Reservation-System/  

### Step 3: Build the Project with Maven

      mvn clean
      mvn package
   
      This will create a .war file in the target/ directory.

### Step 4: Setup Apache Tomcat
      Navigate to /opt/ and extract Tomcat:
       cd /opt/
       tar -xvf apache-tomcat-9.0.102.tar.gz
       mv apache-tomcat-9.0.102 apache
       cd apache
       Start the Tomcat server:
       cd bin/
         ./startup.sh
###   Step 5: Configure Tomcat Manager Access (Optional)
     Edit the following files to allow remote access:

     vi ./webapps/host-manager/META-INF/context.xml
     vi ./webapps/manager/META-INF/context.xml
    Add a user in conf/tomcat-users.xml:
   <user username="admin" password="admin" roles="manager-gui,admin-gui"/>

   ###  Step 6: Deploy WAR File
    Copy the WAR file from the target directory to Tomcat’s webapps:

     cp /home/ubuntu/Train-Ticket-Reservation-System/target/*.war /opt/apache/webapps/

 Tomcat will auto-deploy the WAR on next startup or immediately if it's running.
      
      You can now access the web app in your browser:

            http://<your-server-ip>:8080/<project-name>    

![](./images/TrainTicket%20booking.png)



     
