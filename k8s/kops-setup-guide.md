
# Kubernetes Cluster Setup with Kops on Ubuntu

## Step 1: Install kubectl

```bash
KUBECTL_VERSION=$(curl -sL https://dl.k8s.io/release/stable.txt)
curl -LO "https://dl.k8s.io/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
kubectl version --client
```

---

## Step 2: Install kops

```bash
curl -LO https://github.com/kubernetes/kops/releases/latest/download/kops-linux-amd64
chmod +x kops-linux-amd64
sudo mv kops-linux-amd64 /usr/local/bin/kops
kops version
```

---

## Step 3: Install AWS CLI

```bash
sudo apt update
sudo apt install -y unzip curl
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version
```

---

## Step 4: Configure AWS CLI

```bash
aws configure
```
*(Enter your AWS Access Key, Secret Key, region, and output format)*

---

## Step 5: Create S3 Bucket for Kops State Store

```bash
aws s3 ls
aws s3 mb s3://raj-aja-s3
aws s3 ls
```

---

## Step 6: Export KOPS_STATE_STORE environment variable

```bash
export KOPS_STATE_STORE=s3://raj-aja-s3
```

---

## Step 7: Create Kubernetes Cluster with Kops

```bash
kops create cluster \
  --name=k8s-cluster.k8s.local \
  --zones=us-east-1d \
  --node-count=2 \
  --node-size=t2.medium \
  --master-size=t2.medium \
  --yes
```

---

## Step 8: Validate the Cluster

```bash
kops validate cluster --name k8s-cluster.k8s.local
```

---

## Notes:
- Replace `us-east-1d` with your desired AWS availability zone.
- If you get errors about cluster not reachable, check your AWS security groups and cluster provisioning status.

---
