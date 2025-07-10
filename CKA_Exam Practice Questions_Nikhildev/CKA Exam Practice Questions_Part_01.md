
Title: Certified Kubernetes Administrator (CKA) Exam Practice Questions - 2023
Source: https://www.youtube.com/watch?v=4THV5o6ntIE&list=PLTCdA9kpJ7okpLcuBqSJMaJaiaay0mg-F


Certified Kubernetes Administrator (CKA) Exam Practice Questions - 2023 - Part 1

| Date   | Title | Source|
|-----------|---------|---------|
| 20250625      |  ✅ Certified Kubernetes Administrator (CKA) Exam Practice Questions - 2023 - Part 1   |  https://www.youtube.com/watch?v=4THV5o6ntIE&list=PLTCdA9kpJ7okpLcuBqSJMaJaiaay0mg-F  |





20250625 Notes:

Application Multi Container Issue
Gather logs
TIP COMMAND: `kubectl -n management edit deploy collect-data`

There is a multi-container Deployment in Namespace **management** which seems to have issues and is not getting ready.

Write the logs of all containers to  **/root/logs.log** .

Can you see the reason for the failure?

1. Need to know the deployments in the **management** namespace.  
   Command: `kubectl get deploy -n management`
   Return:  

```bash
controlplane:~$ kubectl get deploy -n management
NAME           READY   UP-TO-DATE   AVAILABLE   AGE
collect-data   0/2     2            0           6m17s

```

Namespace --> Deployment --> Nodes --> Pods --> Containers

**management** is the namespace
**collect-data** is the deployment resource
**READY** indicates that there 0 of 2 pods ready.
**UPDTODATE** Number of pods uptodate with the specifications.
**AVAILABLE** Number of pods that are available and that can serve traffic.
**AGE** The time the Deployment has existed.

2. Find the containers that are running under the deployment.
   Command: `kubectl edit deploy collect-data -n management`
   Return: Opens the YAML file where you can find the containers names

   Container1: nginx
   Container2: httpd

3. Find the logs of **nginx** collect-data deployment
   Command: `kubectl -n management logs deploy/collect-data -c nginx`
   Return: Shows all logs.

```bash
controlplane:~$ kubectl -n management logs deploy/collect-data
Found 2 pods, using pod/collect-data-5759c5c888-hqs8j
Defaulted container "nginx" out of: nginx, httpd
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2025/06/26 02:18:57 [notice] 1#1: using the "epoll" event method
2025/06/26 02:18:57 [notice] 1#1: nginx/1.21.6
2025/06/26 02:18:57 [notice] 1#1: built by gcc 10.3.1 20211027 (Alpine 10.3.1_git20211027) 
2025/06/26 02:18:57 [notice] 1#1: OS: Linux 6.8.0-51-generic
2025/06/26 02:18:57 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2025/06/26 02:18:57 [notice] 1#1: start worker processes
2025/06/26 02:18:57 [notice] 1#1: start worker process 32
```

4. Write the logs for Container1 [nginx]  to `/root/logs.log `
   Command: `kubectl edit deploy collect-data -n management -c nginx >> /root/logs.log`
   Return:
```bash
controlplane:~$ kubectl -n management logs deploy/collect-data -c nginx >> /root/logs.log
Found 2 pods, using pod/collect-data-5759c5c888-hqs8j
```

5. Write the logs for Container2 [httpd]  to `/root/logs.log `
   Command: `kubectl edit deploy collect-data -n management -c httpd >> /root/logs.log`
   Return:
```bash
controlplane:~$ kubectl -n management logs deploy/collect-data -c httpd >> /root/logs.log
Found 2 pods, using pod/collect-data-5759c5c888-hqs8j
```

6. VALIDATE then Fix the Deployment: Fix the deployment in namespace **management** where both containers try to listen on port 80.
   REMOVE one container.
   Go into the **EDIT** of the YAML file and delete one of the **containers**.

   Command: `kubectl edit deploy collect-data -n management`
   VIM Command: `d6d`
   Return:
```bash
controlplane:~$ kubectl edit deploy collect-data -n management
deployment.apps/collect-data edited
```

7. VALIDATE then run the following to see deploy results.
   Command: `kubectl -n management get deploy`
   Return:

```bash
controlplane:~$ kubectl -n management get deploy
NAME           READY   UP-TO-DATE   AVAILABLE   AGE
collect-data   2/2     2            2           46m
```

# CKA Exam Preparation Question 1
**Task:**
Deply a pod called **nginxpod** with **image nginx in controlplane**.
Make sure pod is not scheduled in worker node.

1. alias k=kubectl
2. kubectl or k
   k get nodes
```bash
controlplane:~$ k get nodes
NAME           STATUS   ROLES           AGE   VERSION
controlplane   Ready    control-plane   37h   v1.33.2
node01         Ready    <none>          36h   v1.33.2
```
3. Above shows a **cluster** with 1 master / controlplane and 1 node01
4. Example to deploy a POD the IMPERITIVE way - commmands OR DECLARATIVE via YAML.
5. IMPERITIVE: `kubectl run nginxpod --image=ngix --dry-run=client -o yaml >1.yaml'

| **Part**           | **Meaning**                                                                          |
| ------------------ | ------------------------------------------------------------------------------------ |
| `kubectl`          | The Kubernetes command-line tool to interact with the cluster                        |
| `run`              | Creates a new **Pod** (imperative command)                                           |
| `nginxpod`         | The **name** of the pod to be created                                                |
| `--image=ngix`     | Specifies the **container image** to use (note: `ngix` is likely a typo for `nginx`) |
| `--dry-run=client` | Simulates the creation **on the client side** without actually submitting it         |
| `-o yaml`          | **Output format** – generate the pod definition in **YAML format**                   |
| `> 1.yaml`         | **Redirects the output** to a file called `1.yaml`                                   |

6. Run `ls1 to show the newly created [1.yaml]
7. Inspect the [1.yaml] file
8. Now we're going to create a pod using the YAML file.
   Command: `kubectl apply -f 1.yaml`
   Return:

```bash
controlplane:~$ kubectl apply -f 1.yaml
pod/nginxpod created
```

**apply**: This subcommand tells Kubernetes to create or update resources as defined in a file.

**-f 1.yaml**: This specifies the input file (1.yaml) that contains the configuration for a Kubernetes resource. The file is typically written in YAML format and describes the desired state (e.g., Pod, Deployment, Service).

9. Run the following:
    Command: `kubectl get po -o wide`
    Note: list all Pods in the current namespace with additional details (i.e., "wide" output).
    Returns:
```bash
controlplane:~$ kubectl get po -o wide 
NAME       READY   STATUS             RESTARTS   AGE     IP            NODE     NOMINATED NODE   READINESS GATES
nginxpod   0/1     ImagePullBackOff   0          2m45s   192.168.1.4   node01   <none>           <none>
```

10. The results show that the POD status is **ImagePullBackOff**  
      **ImagePullBackOff** is a common Kubernetes pod status that indicates the pod failed to pull the container image, and Kubernetes is now backing off from trying again (retrying with increasing delays).

11. Describe the POD events and Error logs
    Command: `kubectl describe pod nginxpod`
    Return: Showed a TYPO in ngix rather than nginx.

```bash
controlplane:~$ kubectl get po -o wide
NAME       READY   STATUS    RESTARTS   AGE   IP            NODE     NOMINATED NODE   READINESS GATES
nginxpod   1/1     Running   0          10m   192.168.1.4   node01   <none>           <none>
```

12. Kubernetes will **schedule** a POD into a NODE unless you specify a node name.
13. TASK - POD should be scheduled on the CONTROL PLANE
14. Delete the pod
    Command: `kubectl delete po nginxpod`
    Return: 
```bash
controlplane:~$ k delete po nginxpod 
pod "nginxpod" deleted
```
15. How to schedule POD onto the CONTROL PLANE
    Command: `kubectl get nodes`

```bash
controlplane:~$ k get nodes
NAME           STATUS   ROLES           AGE   VERSION
controlplane   Ready    control-plane   37h   v1.33.2
node01         Ready    <none>          37h   v1.33.2
```

16. Copy the controlplane name, then edit the 1.yaml file and add **nodeName** under **spec**.

```bash
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:
    run: nginxpod
  name: nginxpod
spec:
  **nodeName: controlplane**
  containers:
  - image: nginx
    name: nginxpod
    resources: {}
  dnsPolicy: ClusterFirst
  restartPolicy: Always
status: {}

```

Errors in 1.yaml

```bash
apiVersion: v1
kind: Pod
metadata:
  name: nginxpod
  labels:
    run: nginxpod
spec:
  nodeName: controlplane
  containers:
    - name: nginxpod
      image: nginx
      resources: {}
  dnsPolicy: ClusterFirst
  restartPolicy: Always


```

```bash
controlplane:~$ kubectl apply -f 1.yaml
pod/nginxpod created
```

```bash
controlplane:~$ kubectl get po -o wide
NAME       READY   STATUS    RESTARTS   AGE   IP            NODE           NOMINATED NODE   READINESS GATES
nginxpod   1/1     Running   0          51s   192.168.0.4   controlplane   <none>           <none>
```

# CKA Exam Preparation Question 2 : MIN 11:47
**Task:**