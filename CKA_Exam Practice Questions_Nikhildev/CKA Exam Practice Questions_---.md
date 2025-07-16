
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

`kubectl get deploy -n namespace management`

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
  nodeName: controlplane
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