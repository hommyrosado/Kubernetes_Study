
Min: 3:16
Playgrounds Kubernetes Version

Command: `kubectl get nodes`

```bash

controlplane:~$ kubectl get nodes
NAME           STATUS   ROLES           AGE   VERSION
controlplane   Ready    control-plane   21d   v1.33.2
node01         Ready    <none>          21d   v1.33.2
controlplane:~$ 

```

1 master  and 1 node CLUSTER

Next SELECT CKA Section

---
Min: 4:00
Application Multi Container Issue ( # 7/20 )
Gather logs

There is a multi-container Deployment in Namespace *management* which seems to have issues and is not getting ready.

Write the logs of all containers to /root/logs.log .

Can you see the reason for failure?

Task: Write the logs of the deployment in the namespace *management*

Find the deployments in the *management* namespace

`kubectl get deploy -n management`

```bash
controlplane:~$ kubectl get deploy -n management
NAME           READY   UP-TO-DATE   AVAILABLE   AGE
collect-data   0/2     2            0           58s
controlplane:~$ 
```

Next identify what are the containers running under the deployment. 
Order:
Namespace --> Deployment --> Nodes --> Pods --> Containers

**management** is the namespace
**collect-data** is the deployment resource
**READY** indicates that there 0 of 2 pods ready.
**UPDTODATE** Number of pods uptodate with the specifications.
**AVAILABLE** Number of pods that are available and that can serve traffic.
**AGE** The time the Deployment has existed.

`kubectl -n management edit deploy/collect-data`
or
`kubectl edit deploy collect-data -n management`

Results in the following section of YAML (deployment configuration) that we are concerned with two containers:  
Container 1: nginx
Container 2: httpd

```yaml
    spec:
      containers:
      - image: nginx:1.21.6-alpine
        imagePullPolicy: IfNotPresent
        name: nginx
        resources: {}
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
      - image: httpd:2.4.52-alpine
        imagePullPolicy: IfNotPresent
        name: httpd
        resources: {}
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
      dnsPolicy: ClusterFirst
      restartPolicy: Always
      schedulerName: default-scheduler
      securityContext: {}
      terminationGracePeriodSeconds: 30

```

Find the logs for nginx.
`kubectl logs -n management deploy/collect-data -c nginx`

```bash
controlplane:~$ kubectl logs -n management deploy/collect-data -c nginx
Found 2 pods, using pod/collect-data-5759c5c888-cb5tx
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2025/07/16 03:57:59 [notice] 1#1: using the "epoll" event method
2025/07/16 03:57:59 [notice] 1#1: nginx/1.21.6
2025/07/16 03:57:59 [notice] 1#1: built by gcc 10.3.1 20211027 (Alpine 10.3.1_git20211027) 
2025/07/16 03:57:59 [notice] 1#1: OS: Linux 6.8.0-51-generic
2025/07/16 03:57:59 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2025/07/16 03:57:59 [notice] 1#1: start worker processes
2025/07/16 03:57:59 [notice] 1#1: start worker process 32

```

Write the logs to `/root/logs.log`

`kubectl logs -n management deploy/collect-data -c nginx >> /root/logs.log`

```bash
controlplane:~$ kubectl logs -n management deploy/collect-data -c nginx >> /root/logs.log
Found 2 pods, using pod/collect-data-5759c5c888-9srrq
```

Do the same for the second container.
`kubectl logs -n management deploy/collect-data -c httpd >> /root/logs.log`

```bash
controlplane:~$ kubectl logs -n management deploy/collect-data -c httpd >> /root/logs.log
Found 2 pods, using pod/collect-data-5759c5c888-cb5tx
```

Check the result.

Fix the Deployment in Namespace management where both containers try to listen on port 80.

Remove one container.

Edit the YAML file and delete the HTTPD container section.

`kubectl edit deploy/collect-data -n managment`

VI / VIM: dd to delete entire line


---
Min: 8:30
Playground session

`alias k=kubectl`

`k get nodes`

```bash
controlplane:~$ k get nodes
NAME           STATUS   ROLES           AGE   VERSION
controlplane   Ready    control-plane   21d   v1.33.2
node01         Ready    <none>          21d   v1.33.2

```

Deploy a POD in two ways:
1. Imperitive - use commands
2. Declarative - describe desired state using a YAML file

Imperitive way of running a POD in a cluster

`kubectl run nginxpod --image=nginx --dry-run=client -o yaml >1.yaml`

Inspect the YAML file: 1.yaml

```yaml
controlplane:~$ cat 1.yaml 
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:
    run: nginxpod
  name: nginxpod
spec:
  containers:
  - image: nginx
    name: nginxpod
    resources: {}
  dnsPolicy: ClusterFirst
  restartPolicy: Always
status: {}

```

Now create a pod using the same YAML file.

`kubectl apply -f 1.yaml`

```yaml
controlplane:~$ kubectl apply -f 1.yaml 
pod/nginxpod created

```

Check pod(s)

`kubectl get pod -o wide`
`kubectl get pods -o wide`
`kubectl get po -o wide`

```bash
controlplane:~$ kubectl get pod -o wide
NAME       READY   STATUS    RESTARTS   AGE   IP            NODE     NOMINATED NODE   READINESS GATES
nginxpod   1/1     Running   0          89s   192.168.1.4   node01   <none>           <none>
controlplane:~$ kubectl get pods -o wide
NAME       READY   STATUS    RESTARTS   AGE   IP            NODE     NOMINATED NODE   READINESS GATES
nginxpod   1/1     Running   0          97s   192.168.1.4   node01   <none>           <none>
controlplane:~$ kubectl get po -o wide
NAME       READY   STATUS    RESTARTS   AGE    IP            NODE     NOMINATED NODE   READINESS GATES
nginxpod   1/1     Running   0          105s   192.168.1.4   node01   <none>           <none>

```
By default kubernetes will schedule a POD into a worker node [node01].

The following will schedule the POD on the control plane.

`kubectl delete po nginxpod`

```bash
controlplane:~$ kubectl delete po nginxpod
pod "nginxpod" deleted
```

How to schedule POD on the control plane ...

`kubectl get nodes`
Get the name of the control plane.

```bash
controlplane:~$ k get nodes
NAME           STATUS   ROLES           AGE   VERSION
controlplane   Ready    control-plane   21d   v1.33.2
node01         Ready    <none>          21d   v1.33.2
```

Edit the 1.yaml file.
Under the `spec` section define the node name.


```yaml
controlplane:~$ cat 1.yaml 
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:
    run: nginxpod
  name: nginxpod
spec:
**  nodeName: controlplane**
  containers:
  - image: nginx
    name: nginxpod
    resources: {}
  dnsPolicy: ClusterFirst
  restartPolicy: Always
status: {}

```

Re-apply the pod creation from the 1.yaml.
`kubectl apply -f 1.yaml`

`k get pod`
`k get pod -o wide`

```bash
controlplane:~$ kubectl apply -f 1.yaml 
pod/nginxpod created
controlplane:~$ ^C
controlplane:~$ k get pod
NAME       READY   STATUS    RESTARTS   AGE
nginxpod   1/1     Running   0          19s
controlplane:~$ k get pod -o wide
NAME       READY   STATUS    RESTARTS   AGE   IP            NODE           NOMINATED NODE   READINESS GATES
nginxpod   1/1     Running   0          28s   192.168.0.4   controlplane   <none>           <none>
controlplane:~$ 

```

Now the pod is created in the controlplane / master node.

END: 12:30

---
Begin Question 2
Start: 12:33

Expose a existing pod call nginxpod as a service, service name should be **nginxsvc**

Pod port=80
`kubectl expose pod nginxpod --name=nginxpod --port=80`
Results:
service/exposed

Check on services
`kubectl get service` or `kubectl get svc`


`curl <ip address>`
END: 13:46

---

Question #3:

Expose the existing pod call **nginxpod**, service name as **nginxnodeportsvc**, service should access through **Nodeport**

Nodeport=30200

Expose the pod through the NodePort.
`kubectl expose pod nginxpod --name=nginxnodeportsvc --port=80 --type=NodePort`

`kubectl get svc`

```bash
controlplane:~$ kubectl get svc
NAME               TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
kubernetes         ClusterIP   10.96.0.1        <none>        443/TCP        37h
nginxnodeportsvc   NodePort    10.102.114.115   <none>        80:31222/TCP   10m
nginxsvc           ClusterIP   10.101.94.192    <none>        80/TCP         22m
```

Port for [nginxnodeportsvc] shows as 31222. Should be 30200.

`kubectl edit svc nginxnodeportsvc`

Locate the following section and change:
```yaml
  ports:
  - nodePort: 31222
```

Run to view if port has changed:
`kubectl get svc`
Then to test, run the following to run a curl command on the IP address and append the port number.

`kubectl get node -o wide`
```bash
controlplane:~$ kubectl get node -o wide
NAME           STATUS   ROLES           AGE   VERSION   INTERNAL-IP   EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION     CONTAINER-RUNTIME
controlplane   Ready    control-plane   37h   v1.33.2   172.30.1.2    <none>        Ubuntu 24.04.1 LTS   6.8.0-51-generic   containerd://1.7.27
node01         Ready    <none>          36h   v1.33.2   172.30.2.2    <none>        Ubuntu 24.04.1 LTS   6.8.0-51-generic   containerd://1.7.27
```

Run:
`curl 172.30.2.2:30200`

END: 16:47
--

**Begin part 2**
Question #4:

You can find an existing deployment frontend in production namespace.
Scale down the replicas to 2 and change the image to nginx:1.25

Find the deployment in the **production** namespace.

`kubectl get deployment -n production`

Results show: deployment **frontend** consisting of 3 pods 3/3

Solve by either editing the existing deployment...
Or use IMPERITIVE COMMANDS.

1. Edit the deployment
`kubectl edit deploy frontend -n production`
Find **replicas** and change to 2
Change image name: nginx:1.25

Run to check if deployment has scaled down to 2/2.
`kubectl get deployment -n production`

Run **describe** to get detailed information on resource
`kubectl describe deploy frontend -n production`


2. Imperitive command - check deployments before `kubectl get deployments -n production`
First scale down the deployment
`kubectl scale deploy frontend --replicas=2 -n production`
Result:
deployment.apps/frontend scaled
Frontend 2/2
Second change the image.
`kubectl set image deploy frontend nginx=nginx:1.25 -n production`
Result:
deployment.apps/frontend image updated

Get description for verification.
`kubectl describe deploy frontend -n production`
Scroll up and down to see Replicas and Image.


--

Question # 5:
Autoscale the existing deployment **frontend** in **production** namespace at 80% of pod CPU usage.
Set Minimum replicas=3 and Maximum replicas=5

Impliment HPA - Horizontal Pod AutoScaler
Horizontal Pod Autoscaler (HPA) automatically scales the number of pods

Check deployments in production namespace.
`kubectl get deploy -n production`

Shows: frontend

Solve with IMPERITIVE command
`kubectl -n production autoscale deploy frontend --min=3 --max=5 --cpu-percentage=80`

Result:
horizontalpodautoscaler.autoscaling/frontend autoscaled

Check and verify
`kubectl get hpa -n production`

Result:
```bash
controlplane $ kubectl get deploy -n production
NAME      READY   UP-TO-DATE   AVAILABLE   AGE
frontend  2/2     2            2           40m

controlplane $ kubectl -n production autoscale deploy frontend --min=3 --max=5 --cpu-percent=80
horizontalpodautoscaler.autoscaling/frontend autoscaled

controlplane $ k get hpa -n production
NAME      REFERENCE              TARGETS         MINPODS   MAXPODS   REPLICAS   AGE
frontend  Deployment/frontend   <unknown>/80%    3         5         0          14s

controlplane $
```

END Q5: 25:03
---


Question # 6:
Expose existing deployment in production namespace named as **frontend** through Nodeport and Nodeport service name should be **frontendsvc**

Previous question asked to: Expose the **pod** through the NodePort.
This question is Expose the **deployment** through Nodeport.

[Namespace --> Deployment --> Nodes --> Pods --> Containers]

Check the deployment in production namespace.
`kubectl get deploy -n production`

Shows: frontend 2/2 Ready 

We have to expose the frontend deployment.

`kubectl -n production expose deploy frontend --name=frontendsvc --port=80 --type=NodePort`

Return:
service/frontendsvc exposed

Check the service

`kubectl get svc` or `kubectl get svc -n production`

Should show:

```bash
controlplane $ k get deploy -n production
NAME      READY   UP-TO-DATE   AVAILABLE   AGE
frontend  2/2     2            2           8m58s

controlplane $ k -n production expose deploy frontend --name=frontendsvc --port=80 --type=NodePort
service/frontendsvc exposed

controlplane $ k get svc -n production
NAME          TYPE       CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
frontendsvc   NodePort   10.105.69.93   <none>        80:30194/TCP     8s

controlplane $

```

We determine that the service is exposed: frontendsvc   NodePort   10.105.69.93 

Check if the service is exposing or not:
`kubectl get nodes -o wide`

```bash
controlplane $ k get nodes -o wide
NAME          STATUS   ROLES           AGE    VERSION   INTERNAL-IP   EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION      CONTAINER-RUNTIME
controlplane  Ready    control-plane   7d2h   v1.27.1   172.30.1.2    <none>        Ubuntu 20.04.5 LTS   5.4.0-131-generic   containerd://1.6.12
node01        Ready    <none>          7d2h   v1.27.1   172.30.2.2    <none>        Ubuntu 20.04.5 LTS   5.4.0-131-generic   containerd://1.6.12

controlplane $
```

The example uses the `frontendsvc   NodePort   10.105.69.93   <none>        80:30194/TCP ` frontendsvc PORT: ending in **30194**.
`curl 172.30.2.2:30194`

Which results in html page code in console.

CAUTIONL: May have to expose the service NodePort through a specific port: 30200. 
You may have to edit `kubectl edit svc frontendsvc -n production`

Locate the following section and change:
```yaml
  ports:
  - nodePort: 31222
```

Check service
`kubectl get 
TIME: 28:08

**Begin Part 3**
Reviews Kubernetes documentation.

Examine how to create a pod from the kubernetes documentation.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
```

Create the pod:
`kubectl apply -f 1.yaml`

Now try to create a deployment:


Deployment sample:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

Apply:
`kubectl apply -f nginx-deployment.yaml`

Result: deployment.apps/nginx-deployment created

See the newly created deployment **deploy**
`kubectl get deploy`
 'Deployment' is a type of controller.
 It controls the state of pods to match the desired state defined in the Deployment spec.

 Kubernetes structure:

```bash
controllers/
├── nginx-deployment.yaml   # <- defines a Deployment controller
services/
├── nginx-service.yaml      # <- defines a Service
pods/
├── nginx-pod.yaml          # <- standalone Pod

```

Examines example of finding content in the kubernetes documentation.
Example of Persistence Volumes.
Edit the content as per the question.

Create PV on the cluster.


```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: task-pv-volume
  labels:
    type: local
spec:
  storageClassName: manual
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/mnt/data"


```

controlplane:~/pods/storage$ k apply -f pv-volume.yaml 
persistentvolume/task-pv-volume created

`kubectl get pv`

Result:

```bash
controlplane:~/pods/storage$ k get pv -o wide
NAME            CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS     CLAIM   STORAGECLASS   VOLUMEMODE   VOLUMEATTRIBUTESCLASS   REASON   AGE
task-pv-volume  10Gi       RWO            Retain            Available          manual         Filesystem   <unset>                 63s
controlplane:~/pods/storage$

```



