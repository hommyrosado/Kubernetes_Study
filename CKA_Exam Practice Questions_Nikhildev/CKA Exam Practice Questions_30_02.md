Title: Certified Kubernetes Administrator (CKA) Exam Practice Questions - 2023 - Part 1
Questions: 2/30

Source: https://www.youtube.com/watch?v=4THV5o6ntIE&list=PLTCdA9kpJ7okpLcuBqSJMaJaiaay0mg-F

Order:
Namespace --> Deployment --> Nodes --> Pods --> Containers

Start: 11:47

Question 2: 
Expose an existing pod called *ngixpod* as a service.  
The service name should be *nginxsvc* 
See previous question for how to get to this point.
Pod port = 80

COMMAND:
`kubectl expose pod nginxpod`

```bash
controlplane:~$ kubectl expose pod nginxpod --name=nginxsvc --port=80
service/nginxsvc exposed
controlplane:~$ 
```
Examine:
`kubectl get svc`

```bash
controlplane:~$ kubectl get svc
NAME         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP   30d
nginxsvc     ClusterIP   10.104.109.104   <none>        80/TCP    88s
controlplane:~$ 
```
You can check the svc by using curl and a `ClusterIP` IP address.

`curl 10.104.109.104`
```bash
controlplane:~$ kubectl get svc
NAME         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP   30d
nginxsvc     ClusterIP   10.104.109.104   <none>        80/TCP    88s
controlplane:~$ curl 10.104.109.104 
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
<body>
...

```


