## 🗳️ Vote & Result Kubernetes Deployment and Service (Combined YAMLs)

### 📄 `vote-app.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vote
spec:
  replicas: 1
  selector:
    matchLabels:
      app: vote
  template:
    metadata:
      labels:
        app: vote
    spec:
      containers:
      - name: vote
        image: dockersamples/examplevotingapp_vote
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: vote
spec:
  selector:
    app: vote
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
```

---

### 📄 `result-app.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: result
spec:
  replicas: 1
  selector:
    matchLabels:
      app: result
  template:
    metadata:
      labels:
        app: result
    spec:
      containers:
      - name: result
        image: dockersamples/examplevotingapp_result
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: result
spec:
  selector:
    app: result
  ports:
  - protocol: TCP
    port: 8081
    targetPort: 80
```

---

## 🧰 Tools & Setup Guide

### ✅ Step 1: Install Required Tools
```bash
sudo apt update
sudo apt install unzip curl -y
```

### 🧰 Install AWS CLI
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version
```

### ☸️ Install Kops & Kubectl
```bash
curl -LO https://github.com/kubernetes/kops/releases/latest/download/kops-linux-amd64
chmod +x kops-linux-amd64
sudo mv kops-linux-amd64 /usr/local/bin/kops
kops version

curl -LO "https://dl.k8s.io/release/$(curl -sL https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/kubectl
kubectl version --client
```

---

## ☁️ Step 2: Create S3 Bucket and Cluster
```bash
aws s3 mb s3://arunk8-s3
aws s3 ls
export KOPS_STATE_STORE="s3://arunk8-s3"
```

### Create Kubernetes Cluster
```bash
kops create cluster \
  --name=arun.k8s.local \
  --zones=us-east-1a,us-east-1b \
  --node-count=2 \
  --image=ami-0b529f3487c2c0e7f \
  --state=${KOPS_STATE_STORE} \
  --yes
```

---

## 🐳 Step 3: Build Docker Images

### Clone App Repository
```bash
git clone https://github.com/dockersamples/example-voting-app.git
cd example-voting-app
```

### Frontend (Python Flask)
```bash
cd vote
vi Dockerfile
sudo docker build -t frontend-python .
```

### Worker (.NET)
```bash
cd ../worker
vi Dockerfile
sudo docker build -t workers .
```

### Backend (Node.js)
```bash
cd ../result
vi Dockerfile
sudo docker build -t node-backend .
```

---

## 🔐 Step 4: Push Docker Images to Docker Hub
```bash
docker login -u rajkumar573
sudo docker tag frontend-python rajkumar573/frontend-python:v1
sudo docker tag node-backend rajkumar573/node-backend:v1
sudo docker tag workers rajkumar573/workers:v1

sudo docker push rajkumar573/frontend-python:v1
sudo docker push rajkumar573/node-backend:v1
sudo docker push rajkumar573/workers:v1
```

---

## ☸️ Step 5: Apply Kubernetes Deployments
```bash
cd k8s-specifications/
kubectl apply -f .
kubectl get all
```

---

## 🌐 Step 6: Setup Ingress Controller
```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.10.1/deploy/static/provider/cloud/deploy.yaml
kubectl get pods -n ingress-nginx
kubectl get svc -n ingress-nginx
```

### Update and Apply Ingress Resource
```bash
vi ingress.yaml
kubectl apply -f ingress.yaml
kubectl get ingress
kubectl describe ingress example-ingress
```

---

## ✅ Ingress Resource Example
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
  - http:
      paths:
      - path: /vote
        pathType: Prefix
        backend:
          service:
            name: vote
            port:
              number: 80
      - path: /result
        pathType: Prefix
        backend:
          service:
            name: result
            port:
              number: 8081
```

---

✅ You're now ready to access your app via Ingress!

