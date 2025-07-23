Here's a **consolidated Markdown reference** of all the `kubectl` command categories shown in your images:

---

# 🧠 Kubernetes `kubectl` Command Cheat Sheet

## 🧩 Pod Commands

```bash
kubectl get pod                           # Get pod
kubectl get pod -o wide                   # Get pod wide information
kubectl get pod -w                        # Get pod with watch
kubectl get pod -o yaml                   # Get pod in YAML format
kubectl edit pod <pod_name>              # Edit pod
kubectl describe pod <pod_name>          # Describe pod
kubectl delete pod <pod_name>            # Delete pod
kubectl logs pod <pod_name>              # Get pod logs
kubectl exec -it pod <pod_name> /bin/bash # Exec into pod
```

---

## 🖥️ Node Commands

```bash
kubectl describe node <node_name>               # Describe node
kubectl get node <node_name> -o yaml            # Get node YAML
kubectl get node <node_name>                    # Get node
kubectl drain node <node_name>                  # Drain node
kubectl cordon node <node_name>                 # Cordon node
kubectl uncordon node <node_name>               # Uncordon node
```

---

## 🏗️ Creating Objects

```bash
kubectl apply -f <file_name>.yaml                            # Create resource from file
kubectl apply -f <file1>.yaml -f <file2>.yaml                # Create from multiple files
kubectl apply -f ./<directory_name>                          # Apply all YAMLs from a directory
kubectl apply -f https://<url>                               # Apply from URL

kubectl run <pod_name> --image=<image_name>                  # Create pod
kubectl run <pod_name> --image=<image_name> --port <port> --expose    # Pod + expose as service
kubectl run <pod_name> --image=<image_name> --dry-run=client -o yaml > <file>.yaml  # Output pod YAML

kubectl create deployment <deployment_name> --image=<image_name>      # Create deployment
kubectl create deployment <deployment_name> --image=<image_name> --dry-run=client -o yaml > <file>.yaml  # Output deployment YAML

kubectl create service <type> <service_name> --tcp=<port:target_port> # Create service
kubectl create service <type> <service_name> --tcp=<port:target_port> --dry-run=client -o yaml > <file>.yaml  # Output service YAML

kubectl expose deployment <deployment_name> --type=<type> --port=<port> --target-port=<target_port>  # Expose service
```

---

## 📦 ConfigMap Commands

```bash
kubectl create configmap <name> --from-literal=key=value          # Key-value literal
kubectl create configmap <name> --from-file=<file_name>           # From file
kubectl create configmap <name> --from-env-file=<file_name>       # From env file
```

---

## 🔐 Secret Commands

```bash
kubectl create secret generic <name> --from-literal=key=value     # From literal
kubectl create secret generic <name> --from-file=<file_name>      # From file

kubectl get secret <secret_name>         # Get secret
kubectl describe secret <secret_name>    # Describe secret
kubectl delete secret <secret_name>      # Delete secret
kubectl edit secret <secret_name>        # Edit secret
```

---

## 📊 Monitoring Usage

```bash
kubectl top node <node_name>             # Get node CPU/memory usage
kubectl top pods <pod_name>              # Get pod CPU/memory usage
```

---

## 🚀 Deployment Commands

```bash
kubectl get deployment <name>                    # Get deployment
kubectl get deployment <name> -o yaml            # YAML format
kubectl get deployment <name> -o wide            # Wide format
kubectl edit deployment <name>                   # Edit
kubectl describe deployment <name>               # Describe
kubectl delete deployment <name>                 # Delete
kubectl scale deployment <name> --replicas=<n>   # Scale
```

---

## 🧭 Service Commands

```bash
kubectl get service <name>                       # Get service
kubectl get service <name> -o yaml               # YAML
kubectl get service <name> -o wide               # Wide
kubectl edit service <name>                      # Edit
kubectl describe service <name>                  # Describe
kubectl delete service <name>                    # Delete
```

---

## 🌐 Ingress Commands

```bash
kubectl get ingress                              # Get ingress
kubectl get ingress -o yaml                      # YAML
kubectl get ingress -o wide                      # Wide
kubectl edit ingress <name>                      # Edit
kubectl describe ingress <name>                  # Describe
kubectl delete ingress <name>                    # Delete
```

---

## 🧩 Endpoints Commands

```bash
kubectl get endpoints <name>                     # Get endpoints
```

---

## ⚙️ DaemonSet Commands

```bash
kubectl get daemonset <name>                     # Get
kubectl get daemonset <name> -o yaml             # YAML
kubectl edit daemonset <name>                    # Edit
kubectl describe daemonset <name>                # Describe
kubectl delete daemonset <name>                  # Delete
```

---

## 🛠️ Job Commands

```bash
kubectl get job <name>                           # Get
kubectl get job <name> -o yaml                   # YAML
kubectl edit job <name>                          # Edit
kubectl describe job <name>                      # Describe
kubectl delete job <name>                        # Delete
```

---

## 🔄 Rollout Commands

```bash
kubectl rollout restart deployment <name>                                # Restart
kubectl rollout undo deployment <name>                                   # Undo latest
kubectl rollout undo deployment <name> --to-revision=<rev>              # Undo to revision
kubectl rollout history deployment <name>                                # Get history
kubectl rollout history deployment <name> --revision=<rev>              # Get specific revision
```

---

Let me know if you'd like this exported as a downloadable `.md` file or as a printable PDF.
