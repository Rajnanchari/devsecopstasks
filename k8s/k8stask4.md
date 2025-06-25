
# Setting Up Local Kubernetes Using KIND (Kubernetes IN Docker)

This guide walks through setting up a local Kubernetes cluster using [KIND](https://kind.sigs.k8s.io/), installing `kubectl`, creating multi-node clusters, deploying applications, and managing them using `kubectl`.

---

## 🛠️ Prerequisites

Ensure the following packages are installed:

```bash
sudo apt install -y curl
```

---

## 📦 Install KIND

```bash
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.22.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
kind version
```

---

## 📥 Install `kubectl`

```bash
curl -LO "https://dl.k8s.io/release/$(curl -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
kubectl version --client
```

---

## ⚙️ Create KIND Cluster (Default)

```bash
kind create cluster
kubectl get nodes
```

---

## 🧹 Delete KIND Cluster

```bash
kind delete cluster --name kind-kind
```

---

## 🏗️ Create a Multi-Node Cluster

1. Create a configuration file `multi-node-cluster.yaml`:

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
  - role: worker
  - role: worker
```

2. Create the cluster:

```bash
kind create cluster --config multi-node-cluster.yaml --image kindest/node:v1.30.0
kubectl get nodes
```

---

## 📦 Deploy Nginx Pod

```bash
kubectl run nginx --image=nginx
kubectl get pods
kubectl describe pod nginx
```

---

## 📄 Export and Edit Pod YAML

```bash
kubectl get pod nginx -o yaml > nginx.yaml
cat nginx.yaml
vi nginx.yaml
```

Make necessary edits and apply:

```bash
kubectl apply -f nginx.yaml
kubectl get pods
kubectl describe pod nginx-new
```

Repeat if needed:

```bash
kubectl delete -f nginx.yaml
kubectl apply -f nginx.yaml
```

---

## 📜 View Pod Logs

```bash
kubectl logs nginx-new
```

---

## 🐳 Docker Commands (Optional Debugging)

```bash
docker ps
docker rm -f <container_id>
```

---

## 🧠 Learnings

- **KIND** simplifies running Kubernetes clusters locally using Docker.
- Easy multi-node cluster simulation using YAML config.
- Use `kubectl` to manage resources inside the KIND cluster.
- Helpful for testing, learning, and CI setups.

---

## 📚 Resources

- [KIND Official Docs](https://kind.sigs.k8s.io/)
- [Kubernetes Documentation](https://kubernetes.io/docs/home/)

---

![](./images/k85.1.png)
![](./images/k85.png)
![](./images/1.png)
![](./images/2.png)
![](./images/3.png)
![](./images/4.png)
