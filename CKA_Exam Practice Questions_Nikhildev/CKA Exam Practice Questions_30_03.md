Title: Certified Kubernetes Administrator (CKA) Exam Practice Questions - 2023 - Part 1
Questions: 3/30

Source: https://www.youtube.com/watch?v=4THV5o6ntIE&list=PLTCdA9kpJ7okpLcuBqSJMaJaiaay0mg-F

Order:
Namespace --> Deployment --> Nodes --> Pods --> Containers

Start: 13:00

Question 3: 
Expose an existing pod call *nginxpod*.
Service name as *nginxnodeportsvc*.
Service should access through *Nodeport*.

Nodeport=30200

List all pods:
`kubectl get pods -o wide`

```bash
controlplane:~$ kubectl get pods -o wide
NAME       READY   STATUS    RESTARTS   AGE   IP            NODE           NOMINATED NODE   READINESS GATES
nginxpod   1/1     Running   0          19m   192.168.0.4   controlplane   <none>           <none>
```

*nginxpod* is running.
Expose *nginxpod* through *Nodeport*.

List all svc:
`kubectl get svc`

```bash
controlplane:~$ kubectl get svc
NAME         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP   30d
nginxsvc     ClusterIP   10.104.109.104   <none>        80/TCP    8m59s
```
`kubectl expose pod nginxpod --name=nginxnodeportsvc --port=80 --type=NodePort`

```bash
controlplane:~$ kubectl expose pod nginxpod --name=nginxnodeportsvc --port=80 --type=NodePort
service/nginxnodeportsvc exposed
controlplane:~$ 
```
Check svc:
`kubectl get svc`

```bash
controlplane:~$ kubectl get svc
NAME               TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
kubernetes         ClusterIP   10.96.0.1        <none>        443/TCP        30d
nginxnodeportsvc   NodePort    10.109.85.108    <none>        80:32566/TCP   73s
nginxsvc           ClusterIP   10.104.109.104   <none>        80/TCP         17m
controlplane:~$ 
```

Note:
```markdown
Great question — you’re noticing two Services (`nginxnodeportsvc` and `nginxsvc`) that both point to your NGINX app, but expose it differently. Let’s break it down:

---

### **1. `nginxsvc` (ClusterIP Service)**

* **Type**: `ClusterIP` (the default).
* **Cluster-IP**: `10.104.109.104`.
* **Port(s)**: `80/TCP`.
* **Access**: Only reachable **inside the cluster** (from other Pods/Services).
* Think of this as an **internal load balancer** for your NGINX Pods.

---

### **2. `nginxnodeportsvc` (NodePort Service)**

* **Type**: `NodePort`.
* **Cluster-IP**: `10.109.85.108`.
* **Port(s)**: `80:32566/TCP`.

  * The `80` = service port inside cluster.
  * The `32566` = NodePort, meaning it opens port `32566` on **every Node** in the cluster.
* **Access**: Reachable **from outside the cluster**, via any Node’s IP:

  ```
  http://<NodeIP>:32566
  ```

---

### **3. Relationship**

* Both Services likely **select the same set of NGINX Pods** (via their label selector).
* `nginxsvc` = **internal-only access**.
* `nginxnodeportsvc` = **external + internal access**.
* They don’t directly depend on each other — they are just **two front doors** pointing to the same backend Pods.

---

📌 Analogy:

* `nginxsvc` = office intercom (only people inside the building can call you).
* `nginxnodeportsvc` = public phone number (anyone outside can call you too).

---

👉 Do you want me to show you how to **verify** that both services target the same Pods (using `kubectl describe svc nginxsvc` vs. `kubectl describe svc nginxnodeportsvc`)?

```

*nginxnodeportsvc* should be exposed to port: 30200
Currently it is exposed to port: 32566
`nginxnodeportsvc   NodePort    10.109.85.108    <none>  80:32566/TCP   11m`

We need to edit the svc.

`kubectl edit svc nginxnodeportsvc`

```yaml
spec:
  clusterIP: 10.109.85.108
  clusterIPs:
  - 10.109.85.108
  externalTrafficPolicy: Cluster
  internalTrafficPolicy: Cluster
  ipFamilies:
  - IPv4
  ipFamilyPolicy: SingleStack
  ports:
  - nodePort: 30200
    port: 80
    ...
```
Examine nodes:
`kubectl get nodes -o wide`

```bash
controlplane:~$ kubectl get nodes -o wide
NAME           STATUS   ROLES           AGE   VERSION   INTERNAL-IP   EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION     CONTAINER-RUNTIME
controlplane   Ready    control-plane   30d   v1.33.2   172.30.1.2    <none>        Ubuntu 24.04.1 LTS   6.8.0-51-generic   containerd://1.7.27
node01         Ready    <none>          30d   v1.33.2   172.30.2.2    <none>        Ubuntu 24.04.1 LTS   6.8.0-51-generic   containerd://1.7.27
controlplane:~$ 
```

To access the svc we need to fine the IP address of the *node01* : 172.30.2.2 .  
Then add the port: 30200 to it.
`curl 172.30.2.2:30200`

```bash
controlplane:~$ kubectl get nodes        
NAME           STATUS   ROLES           AGE   VERSION
controlplane   Ready    control-plane   30d   v1.33.2
node01         Ready    <none>          30d   v1.33.2
controlplane:~$ curl 172.30.2.2:30200   
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
...

```

END video: 12:01
Question: 3/30
Source: https://www.youtube.com/watch?v=4THV5o6ntIE&list=PLTCdA9kpJ7okpLcuBqSJMaJaiaay0mg-F









