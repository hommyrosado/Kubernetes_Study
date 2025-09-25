# 📘 Certified Kubernetes Administrator (CKA) Training Workbook

This workbook consolidates 30 CKA exam-style practice questions into a progressive training guide.
Each module includes **Concepts, Commands, Exercises, and Checkpoints** to help you build mastery.

---

## **Section 1: Core Workloads**

### Q1. Pod Creation & Scheduling
- **Concept**: Pods = smallest deployable unit. Imperative vs Declarative.  
- **Commands**:
  ```bash
  kubectl run nginxpod --image=nginx --dry-run=client -o yaml > pod.yaml
  kubectl apply -f pod.yaml
  ```
  YAML edit:
  ```yaml
  spec:
    nodeName: controlplane
  ```
- **Exercise**: Create `nginxpod` scheduled on `controlplane`.  
- **Checkpoint**:
  ```bash
  kubectl get pods -o wide
  ```
  Must show pod on **controlplane**.

---

### Q2. ClusterIP Service
- **Concept**: Default service type. Internal-only load balancing.  
- **Commands**:
  ```bash
  kubectl expose pod nginxpod --name=nginxsvc --port=80
  kubectl get svc
  curl <ClusterIP>
  ```
- **Exercise**: Expose `nginxpod` as ClusterIP and curl it.  
- **Checkpoint**: Service visible under `kubectl get svc`.

---

### Q3. NodePort Service
- **Concept**: NodePort exposes service externally.  
- **Commands**:
  ```bash
  kubectl expose pod nginxpod --name=nginxnodeportsvc --port=80 --type=NodePort
  kubectl edit svc nginxnodeportsvc  # set nodePort: 30200
  curl <NodeIP>:30200
  ```
- **Exercise**: Access `nginxpod` externally at `<NodeIP>:30200`.  
- **Checkpoint**: Curl returns NGINX page.

---

### Q4. Deployments
- **Concept**: Declarative management of replica sets. Scaling & rollout.  
- **Commands**:
  ```bash
  kubectl create deployment nginx-deploy --image=nginx --replicas=3
  kubectl get deployments
  kubectl scale deployment nginx-deploy --replicas=5
  kubectl rollout status deployment nginx-deploy
  ```
- **Exercise**: Create a Deployment with 3 replicas, scale to 5.  
- **Checkpoint**: `kubectl get pods` shows 5.

---

### Q5. DaemonSets
- **Concept**: Ensure a pod runs on **every node**.  
- **Commands**:
  ```bash
  kubectl create daemonset nginx-ds --image=nginx --namespace=kube-system
  ```
- **Exercise**: Deploy a DaemonSet and verify 1 pod per node.  
- **Checkpoint**:
  ```bash
  kubectl get pods -o wide -n kube-system
  ```

---

### Q6. Static Pods
- **Concept**: Managed by **kubelet**, not API server.  
- **Commands**:
  - Place YAML in: `/etc/kubernetes/manifests/`  
- **Exercise**: Create a static pod manifest `nginx-static.yaml`.  
- **Checkpoint**:
  ```bash
  kubectl get pods -n kube-system
  ```

---

## **Section 2: Config & State Management**

### Q7. ConfigMaps
```bash
kubectl create configmap app-config --from-literal=APP_MODE=prod
kubectl describe configmap app-config
```
- Exercise: Mount as env var in a pod.  
- Checkpoint: `kubectl exec` → `echo $APP_MODE`.

---

### Q8. Secrets
```bash
kubectl create secret generic db-secret --from-literal=DB_PASS=admin123
```
- Exercise: Mount secret into pod.  
- Checkpoint: Verify inside container.

---

### Q9. PersistentVolumes (PV) & PVC
```yaml
kind: PersistentVolume
apiVersion: v1
metadata:
  name: pv-demo
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: /mnt/data
```
- Exercise: Create PV + PVC, mount into pod.  
- Checkpoint: Pod can read/write `/mnt/data`.

---

### Q10. StorageClasses
```bash
kubectl get storageclass
```
- Exercise: Create PVC using default StorageClass.  
- Checkpoint: PVC is **Bound**.

---

## **Section 3: Scheduling & Control**

### Q11. Labels & Selectors
```bash
kubectl label pod nginxpod tier=frontend
kubectl get pods --selector=tier=frontend
```

---

### Q12. Taints & Tolerations
```bash
kubectl taint node node01 key=value:NoSchedule
```

---

### Q13. Node Affinity
```yaml
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
      - matchExpressions:
        - key: disktype
          operator: In
          values:
          - ssd
```

---

### Q14. Pod Affinity / Anti-Affinity
- Similar YAML to control pod co-location or separation.

---

### Q15. Resource Requests & Limits
```yaml
resources:
  requests:
    memory: "128Mi"
    cpu: "500m"
  limits:
    memory: "256Mi"
    cpu: "1"
```

---

### Q16. Horizontal Pod Autoscaler
```bash
kubectl autoscale deployment nginx-deploy --cpu-percent=80 --min=1 --max=5
kubectl get hpa
```

---

## **Section 4: Networking & Policies**

### Q17. NetworkPolicies
```yaml
kind: NetworkPolicy
spec:
  podSelector:
    matchLabels:
      role: db
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: frontend
```

---

### Q18. Ingress
- YAML for path-based routing with NGINX ingress controller.

---

### Q19. DNS
```bash
kubectl exec -it busybox -- nslookup nginxsvc
```

---

### Q20. Multi-container Pods
- InitContainers and sidecars YAML practice.

---

## **Section 5: Security & RBAC**

### Q21. ServiceAccounts
```bash
kubectl create serviceaccount app-sa
```

---

### Q22. Role & RoleBinding
```yaml
kind: Role
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list"]
```

---

### Q23. ClusterRole & ClusterRoleBinding
- Similar but cluster-scoped.

---

### Q24. Admission Controllers
- Enable via kube-apiserver flags.

---

### Q25. SecurityContext
```yaml
securityContext:
  runAsUser: 1000
  capabilities:
    add: ["NET_ADMIN"]
```

---

## **Section 6: Maintenance & Troubleshooting**

### Q26. Logs
```bash
kubectl logs nginxpod
kubectl logs nginxpod -c sidecar
```

---

### Q27. Debugging
```bash
kubectl describe pod nginxpod
kubectl exec -it nginxpod -- /bin/sh
```

---

### Q28. Backup & Restore etcd
```bash
ETCDCTL_API=3 etcdctl snapshot save snapshot.db
ETCDCTL_API=3 etcdctl snapshot restore snapshot.db
```

---

### Q29. Upgrading Clusters
```bash
kubeadm upgrade plan
kubeadm upgrade apply v1.27.0
```

---

### Q30. API Server Components
- Static pod manifests at `/etc/kubernetes/manifests/`.  
- Edit `kube-apiserver.yaml`, `kube-controller-manager.yaml`, etc.

---

# 🏆 Training Strategy
- **Daily drills**: Repeat Q1–Q10 until fluent.  
- **Weekly full-run**: Simulate exam by solving all modules without notes.  
- **Checkpoint method**: Always validate with `kubectl get` / `kubectl describe`.  
