## 🌐 **Kubernetes Service Types: ClusterIP vs NodePort**

### 🎯 **Objective:**

Learn how Kubernetes Services expose Pods internally and externally. Compare `ClusterIP` vs `NodePort`, and validate reachability from within and outside the cluster.

---

## ✅ **Task Steps**

### 🔧 Step 1: Create Deployment `myapp`

```bash
kubectl create deployment myapp --image=nginx:1.23.4-alpine --replicas=1
✅ Expose container port 80:

```
kubectl edit deployment myapp
Update the containers section:

yaml
Copy
Edit
containers:
- name: nginx
  image: nginx:1.23.4-alpine
  ports:
  - containerPort: 80
Apply changes and confirm:
```

```
kubectl get deployments
kubectl describe deployment myapp
🛠️ Step 2: Create Service of type ClusterIP
```
kubectl expose deployment myapp --name=myapp --port=80 --target-port=80 --type=ClusterIP
✅ Confirm service:

bash
Copy
Edit
kubectl get svc myapp
📈 Step 3: Scale Deployment to 2 replicas
bash
Copy
Edit
kubectl scale deployment myapp --replicas=2
kubectl get pods -l app=myapp
🧪 Step 4: Access Service Internally (via BusyBox)
bash
Copy
Edit
kubectl run busybox --image=busybox --rm -it --restart=Never -- sh
Inside BusyBox shell:

sh
Copy
Edit
wget -qO- http://myapp
✅ You should see the HTML from NGINX.

🌍 Step 5: Test External Access (Fails)
From your host system:

bash
Copy
Edit
wget http://<ClusterIP>
❌ This will fail because ClusterIP is internal-only.

🔁 Step 6: Change Service Type to NodePort
bash
Copy
Edit
kubectl patch svc myapp -p '{"spec": {"type": "NodePort"}}'
kubectl get svc myapp
🔍 Note the new NodePort (e.g., 31500)

🌐 Step 7: Access Service from Outside
From your host (if using KIND or Minikube, use the node’s IP):

bash
Copy
Edit
wget http://<NodeIP>:<NodePort>
✅ You should get a response from NGINX.

💬 Discussion
❓ Can you expose Pods without a Deployment?
Yes — you can create a Service that points directly to a standalone Pod using labels. But:

It's not recommended in production

Services expect a selector, which is easier with Deployments

Pods can get deleted/replaced — use Deployments for stability

❓ When to Use Which Service Type?
Service Type	Use Case
ClusterIP	Default. Internal traffic only within the cluster.
NodePort	Exposes service on a static port across all nodes. Useful for local or basic external access.
LoadBalancer	Uses cloud provider’s load balancer (e.g., AWS ELB) to expose the app.
ExternalName	Maps a service to a DNS name outside the cluster (e.g., for legacy services).

yaml
Copy
Edit

---

✅ You're all set! You can paste this into any Markdown editor like VS Code or Obsidian, and save it as `k8s_service_types.md`. Let me know if you need a PDF or formatted LinkedIn version.