
# 📦 CollectTracker Docker Deployment Guide

This guide documents the steps taken to clone, build, and deploy the **CollectTracker** project using Docker and Apache2 to serve the React frontend.

---

## 🚀 Step-by-Step Commands Used

```bash
# Step 1: Update the package list
sudo apt update

# Step 2: Clone the project repository
git clone https://github.com/Bighairymtnman/CollectTracker.git

# Step 3: Navigate into the project directory
cd CollectTracker/

# Step 4: Create Dockerfile (added below)
sudo vi Dockerfile

# Step 5: Install Docker if not already installed
sudo apt install docker.io

# Step 6: Allow Docker to be run without sudo
sudo chmod 666 /var/run/docker.sock

# Step 7: Build the Docker image
docker build -t collectertracker .

# Step 8: Run the Docker container
docker run -d --name collect -p 80:80 collectertracker

# Step 9: Verify the container is running
docker ps
```

---

## 📄 Dockerfile Used

```Dockerfile
# Build stage: React frontend
FROM node:18 AS builder
WORKDIR /app
COPY client/package*.json ./client/
RUN cd client && npm install
COPY client ./client
RUN cd client && npm run build

# Final stage: Apache web server
FROM ubuntu:22.04
RUN apt update &&     apt install -y apache2 &&     apt clean &&     rm -rf /var/lib/apt/lists/*
COPY --from=builder /app/client/build/ /var/www/html/
EXPOSE 80
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
```

---

## ✅ Access the App

Once the container is running, open a browser and go to:

```
http://<your-server-ip>/
```

This will display the deployed React frontend of the CollectTracker app served via Apache inside the Docker container.


---

## ☁️ Push Image to Docker Hub

After successfully building and running your Docker image locally, follow these steps to tag and push the image to Docker Hub:

```bash
# Step 1: Tag your local image for Docker Hub
docker tag collectertracker rajkumar573/collectertracker

# Step 2: Log in to Docker Hub
docker login

# Step 3: Push the image to your Docker Hub repository
docker push rajkumar573/collectertracker
```

Once pushed, the image will be available at:
```
https://hub.docker.com/r/rajkumar573/collectertracker
```
You can now pull and run this image on any compatible Docker environment using:

```bash
docker pull rajkumar573/collectertracker
docker run -d -p 80:80 rajkumar573/collectertracker
```
