
# Kubernetes (K8s) Topics – Simple Definitions

## 1. Pod  
A Pod is the smallest unit in Kubernetes. It runs one or more containers together.

## 2. Deployment  
A Deployment is used to manage and update a set of Pods automatically. Example: Rollout new version, rollback, scale replicas.

## 3. ReplicaSet  
Ensures a specified number of pod replicas are running. (Used by Deployment in the background.)

## 4. Service  
A Service exposes your Pods and provides a stable IP and DNS name.  
Types: ClusterIP, NodePort, LoadBalancer, ExternalName.

## 5. Labels & Selectors  
Used to group Kubernetes objects. Example: Select pods with label `app=nginx`.

## 6. Namespace  
Used to separate environments or teams in the same cluster. Example: `default`, `dev`, `prod`.

## 7. DaemonSet  
Ensures a Pod runs on every node (or selected nodes). Example: Log collector like Fluentd.

## 8. StatefulSet  
Used for apps that need persistent identity and storage. Example: Databases like MySQL, Cassandra.

## 9. ConfigMap  
Stores non-sensitive config data (e.g., environment variables, settings). Injected into pods.

## 10. Secret  
Stores sensitive data (e.g., passwords, API keys). Encrypted and injected into pods.

## 11. Job  
Used to run a one-time task (e.g., backup job or DB migration).

## 12. CronJob  
Schedules a job to run at a specific time or interval, like a cron task.

## 13. Ingress  
Controls external access to services (via HTTP/HTTPS). Used to expose web apps.

## 14. Kubelet  
Agent that runs on each node, ensures containers are running.

## 15. Controller Manager  
Manages controllers like ReplicaSet, Deployment, etc.

## 16. Scheduler  
Decides which node a pod should run on based on resource needs.

## 17. etcd  
Key-value database that stores the entire cluster state.

## 18. kubectl  
CLI tool to manage Kubernetes clusters. Example: `kubectl get pods`, `kubectl apply -f file.yaml`

## 19. Resource Requests & Limits  
Define how much CPU/Memory a container can use.

## 20. RBAC (Role-Based Access Control)  
Controls who can do what in the cluster. Objects: `Role`, `RoleBinding`, `ClusterRole`.

## 21. Persistent Volume (PV)  
A PV is a piece of storage in the cluster that has been provisioned by an administrator.

## 22. Persistent Volume Claim (PVC)  
A PVC is a request for storage by a user. It binds to a suitable PV automatically.

## 23. Volume  
A Volume is used to store data that should persist beyond container restarts.

## 24. Init Container  
An Init Container runs before the main container starts. Used to set up tasks like downloading dependencies.

## 25. Taints and Tolerations  
Taints prevent pods from running on certain nodes unless they have matching tolerations. Useful for dedicated nodes.

## 26. Affinity and Anti-Affinity  
Rules that influence how pods are scheduled. Affinity attracts pods to certain nodes; anti-affinity keeps them apart.

## 27. Node Selector  
A simple way to assign pods to specific nodes based on key-value labels. Example: `nodeSelector: { disktype: ssd }`

## 28. NetworkPolicy  
Used to control network traffic between pods. Defines which pods can talk to each other and to external endpoints.

## 29. KubeProxy  
Maintains network rules on nodes to allow communication to services and handles load balancing across pods.

## 30. Helm  
A package manager for Kubernetes. It helps you define, install, and upgrade complex Kubernetes applications using Helm charts.

## 31. Custom Resource Definition (CRD)  
Allows you to define your own custom Kubernetes objects.  
Example YAML to create a CRD:
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: myresources.example.com
spec:
  group: example.com
  versions:
    - name: v1
      served: true
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
  scope: Namespaced
  names:
    plural: myresources
    singular: myresource
    kind: MyResource
    shortNames:
    - mr
```

## 32. Operator  
A program that uses CRDs to manage complex apps and automate operational tasks like upgrades or backups. Operators watch resources and act accordingly.

---

## 33. Prometheus  
An open-source monitoring and alerting system designed for reliability and scalability. It collects metrics from your applications and infrastructure.

Example minimal Prometheus deployment:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: prometheus
spec:
  replicas: 1
  selector:
    matchLabels:
      app: prometheus
  template:
    metadata:
      labels:
        app: prometheus
    spec:
      containers:
      - name: prometheus
        image: prom/prometheus
        ports:
        - containerPort: 9090
```

## 34. Grafana  
A popular open-source visualization and dashboard tool used to display data from Prometheus and other sources.

Example minimal Grafana deployment:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: grafana
spec:
  replicas: 1
  selector:
    matchLabels:
      app: grafana
  template:
    metadata:
      labels:
        app: grafana
    spec:
      containers:
      - name: grafana
        image: grafana/grafana
        ports:
        - containerPort: 3000
```
