Title: Certified Kubernetes Administrator (CKA) Exam Practice Questions - 2023 - Part 1
Questions: 1/30

Source: https://www.youtube.com/watch?v=4THV5o6ntIE&list=PLTCdA9kpJ7okpLcuBqSJMaJaiaay0mg-F

Order:
Namespace --> Deployment --> Nodes --> Pods --> Containers

Start: 6:54

Question 1:  
Deploy a pod called `nginxpod` with image `nginx` in *controlplane*.
Make sure pod is not scheduled in worker node.

Click on playgrounds.
Click on Kubernetes 1.##
`alias k=kubectl`
`kubectl get nodes`

```bash
controlplane:~$ k get nodes
NAME           STATUS   ROLES           AGE   VERSION
controlplane   Ready    control-plane   30d   v1.33.2
node01         Ready    <none>          30d   v1.33.2
```

Deploy a Pod in two ways.
1. Imperative - using commands for creating resources in the cluster.
2. Declarative - Describe the desired state of cluster or resources using a YAML (manifest) file. “This is what I want — go make it so.”

Quick distinction

YAML = the format (human-readable data serialization).

Manifest = the content (the Kubernetes object definition, usually written in YAML).

What a Manifest Is
- A manifest is a file that declares the desired state of a Kubernetes object (Deployment, Pod, Service, ConfigMap, etc.).
- Written in YAML (most common) or JSON.
- It tells the Kubernetes API server: “This is what I want — go make it so.”

Imperative command:
`kubectl run nginnxpod --image=nginx --dry-run=client -o yml > 1.yml`
Will create the `1.yaml` file.

2. Explanation of flags
- k`ubectl run → create` a Pod (not Deployment).
- `--image=nginx` → container image.
- `--dry-run=client` → don’t actually create it, just print the manifest.
- `-o yaml` → output in YAML format.
- `> 1.yml` → redirect output into file 1.yml.
Inspect the `1.yaml` file.

vi or vim
`vi 1.yaml`

Now create a pod with the `1.yaml` file.
`kubectl apply -f 1.yaml`

```bash
controlplane:~$ k apply -f 1.yaml
pod/nginxpod created
```
List all pods:
`kubectl get pods`
`kubectl get po -o wide`

```bash
controlplane:~$ k get pods
NAME       READY   STATUS    RESTARTS   AGE
nginxpod   1/1     Running   0          2m39s
```
```bash
controlplane:~$ k get po -o wide
NAME       READY   STATUS    RESTARTS   AGE     IP            NODE     NOMINATED NODE   READINESS GATES
nginxpod   1/1     Running   0          3m45s   192.168.1.4   node01   <none>           <none>
```
Port `192.168.1.4` is schedule into worker node `node01`.

By defaule Kubernetes will schedul a pod into a worker node unless specified.
According to the question, the pod should be schedule on the `controlplane`.
We will delete the pod and recreate it.

Delete the pod.
`kubectl delet pod nginxpod`

```bash
controlplane:~$ k delete pod nginxpod
pod "nginxpod" deleted
```

Then we will shchedule the pod on the correct `controlplane` node.
Edit the `1.yaml` file and update the `spec` section with `nodeName`.

```yaml
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
Re-apply the `1.yaml`
`kubectl apply -f 1.yaml`

```bash
controlplane:~$ kubectl apply -f 1.yaml
pod/nginxpod created
```
`kubectl get pods -o wide`

```bash
controlplane:~$ k get pods
NAME       READY   STATUS    RESTARTS   AGE
nginxpod   1/1     Running   0          27s
controlplane:~$ k get pods -o wide
NAME       READY   STATUS    RESTARTS   AGE   IP            NODE           NOMINATED NODE   READINESS GATES
nginxpod   1/1     Running   0          35s   192.168.0.4   controlplane   <none>           <none>
```
Now you can see the pod is scheduled on the master node / controlplane.

---------




