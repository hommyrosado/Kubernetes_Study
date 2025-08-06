# Kubernetes kubectl Quick Reference

This is a comprehensive guide to commonly used `kubectl` commands and flags.

---

## Version Note

These instructions apply to **Kubernetes v1.33**. Check your version with:

```bash
kubectl version
```

---

## kubectl Autocomplete

### Bash

```bash
source <(kubectl completion bash)
```

Add permanently:

```bash
echo "source <(kubectl completion bash)" >> ~/.bashrc
```

Alias with completion:

```bash
alias k=kubectl
complete -o default -F __start_kubectl k
```

### Zsh

```bash
source <(kubectl completion zsh)
echo '[[ $commands[kubectl] ]] && source <(kubectl completion zsh)' >> ~/.zshrc
```

### Fish *(v1.23+)*

```bash
echo 'kubectl completion fish | source' > ~/.config/fish/completions/kubectl.fish
source ~/.config/fish/completions/kubectl.fish
```

---

## --all-namespaces shorthand

Use `-A` instead of `--all-namespaces`

```bash
kubectl get pods -A
```

---

## kubectl Context and Configuration

View current kubeconfig:

```bash
kubectl config view
```

Merge multiple configs:

```bash
KUBECONFIG=~/.kube/config:~/.kube/kubconfig2 kubectl config view
```

Get current user password:

```bash
kubectl config view -o jsonpath='{.users[?(@.name == "e2e")].user.password}'
```

Set context, namespace, credentials:

```bash
kubectl config set-context --current --namespace=example-namespace
kubectl config use-context my-cluster
kubectl config set-credentials user --username=user --password=pass
```

Aliases:

```bash
alias kx='f() { [ "$1" ] && kubectl config use-context $1 || kubectl config current-context ; } ; f'
alias kn='f() { [ "$1" ] && kubectl config set-context --current --namespace $1 || kubectl config view --minify | grep namespace | cut -d" " -f6 ; } ; f'
```

---

## kubectl Apply / Create

Apply manifests:

```bash
kubectl apply -f ./file.yaml
kubectl apply -f ./dir/
kubectl apply -f https://example.com/manifest.yaml
```

Create deployment:

```bash
kubectl create deployment nginx --image=nginx
```

Create multiple objects via stdin:

```bash
kubectl apply -f - <<EOF
<manifests>
EOF
```

Create CronJob:

```bash
kubectl create cronjob hello --image=busybox:1.28 --schedule="*/1 * * * *" -- echo "Hello World"
```

---

## Viewing and Finding Resources

Basic get:

```bash
kubectl get pods
kubectl get svc
kubectl get pods -o wide
kubectl get pod <name> -o yaml
```

Describe:

```bash
kubectl describe nodes <name>
kubectl describe pods <name>
```

Advanced filters:

```bash
kubectl get pods --field-selector=status.phase=Running
kubectl get nodes --selector='!node-role.kubernetes.io/control-plane'
```

List with labels, secrets, events:

```bash
kubectl get pods --show-labels
kubectl get secret my-secret -o go-template='{{range $k,$v := .data}}{{"### "}}{{$k}}{{"\n"}}{{$v|base64decode}}{{"\n\n"}}{{end}}'
kubectl get events --sort-by=.metadata.creationTimestamp
```

---

## Updating Resources

Image update and rollout:

```bash
kubectl set image deployment/frontend www=image:v2
kubectl rollout undo deployment/frontend
kubectl rollout history deployment/frontend
kubectl rollout restart deployment/frontend
```

Replace/patch:

```bash
kubectl replace -f ./pod.json
kubectl patch node my-node -p '{"spec":{"unschedulable":true}}'
```

Annotations/Labels:

```bash
kubectl label pods my-pod new-label=awesome
kubectl annotate pods my-pod icon-url=http://example.com/icon.png
```

---

## Editing Resources

```bash
kubectl edit svc/docker-registry
KUBE_EDITOR=nano kubectl edit svc/docker-registry
```

---

## Scaling Resources

```bash
kubectl scale --replicas=3 deployment/myapp
kubectl autoscale deployment myapp --min=2 --max=10
```

---

## Deleting Resources

```bash
kubectl delete -f ./file.yaml
kubectl delete pod unwanted --now
kubectl delete pod,svc name1 name2
kubectl delete -n my-ns pod,svc --all
```

---

## Interacting with Running Pods

Logs and exec:

```bash
kubectl logs my-pod
kubectl exec -it my-pod -- /bin/sh
kubectl exec my-pod -c my-container -- ls /
```

Run and attach:

```bash
kubectl run -i --tty busybox --image=busybox:1.28 -- sh
kubectl attach my-pod -i
```

Port forwarding:

```bash
kubectl port-forward my-pod 5000:6000
```

Metrics:

```bash
kubectl top pod
kubectl top pod my-pod --sort-by=cpu
```

---

## Copying Files

```bash
kubectl cp /tmp/foo my-pod:/tmp/bar
kubectl cp my-pod:/tmp/foo /tmp/bar
```

Using `tar`:

```bash
tar cf - foo | kubectl exec -i my-pod -- tar xf - -C /bar
```

---

## Deployments and Services

```bash
kubectl logs deploy/my-deployment
kubectl port-forward svc/my-service 5000:80
kubectl exec deploy/my-deployment -- ls
```

---

## Nodes and Cluster

```bash
kubectl cordon my-node
kubectl drain my-node
kubectl uncordon my-node
kubectl cluster-info
kubectl top node
```

---

## Resource Types

```bash
kubectl api-resources
kubectl api-resources --namespaced=false
```

---

## Output Formatting

| Format            | Description                         |
| ----------------- | ----------------------------------- |
| -o json           | Output JSON format                  |
| -o yaml           | Output YAML format                  |
| -o name           | Show only resource names            |
| -o wide           | More info (e.g. node name for pods) |
| -o custom-columns | Define table columns                |
| -o jsonpath=      | Extract specific fields             |
| -o go-template=   | Use Go templating                   |

Examples:

```bash
kubectl get pods -A -o custom-columns='DATA:spec.containers[*].image'
```

---

## Debugging and Verbosity

| Verbosity Flag | Description              |
| -------------- | ------------------------ |
| --v=0          | Basic info               |
| --v=4          | Debug-level output       |
| --v=7          | Show HTTP headers        |
| --v=9          | Full HTTP request bodies |

---

For more examples, see the official [kubectl reference documentation](https://kubernetes.io/docs/reference/kubectl/).
