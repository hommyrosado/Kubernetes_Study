Here’s the entire contents of this page formatted as Markdown:

---

````markdown
# Kubernetes: Pods & Labels – Create, Label, and Inspect a Basic Pod

## ✅ 1. Create a Basic Pod

You can create a basic Pod using a YAML manifest or directly via `kubectl`.

### Option A: Create using YAML (`pod.yaml`)
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  labels:
    app: demo
spec:
  containers:
  - name: nginx-container
    image: nginx
````

Create the pod:

```bash
kubectl apply -f pod.yaml
```

### Option B: Create directly with `kubectl run`

```bash
kubectl run my-pod --image=nginx --labels="app=demo"
```

---

## 🏷️ 2. Label a Pod

If the Pod was created without labels, or you want to **add/update** labels:

```bash
kubectl label pod my-pod env=dev
```

To **overwrite** an existing label:

```bash
kubectl label pod my-pod env=prod --overwrite
```

---

## 🔍 3. Inspect a Pod

### View Pod details:

```bash
kubectl get pods
kubectl get pod my-pod -o wide
kubectl describe pod my-pod
```

### View labels:

```bash
kubectl get pods --show-labels
kubectl get pod my-pod --show-labels
```

### Filter by label:

```bash
kubectl get pods -l app=demo
kubectl get pods -l env=prod
```

---

## 💡 kubectl apply vs kubectl create

| Command          | Use When…                                           | Key Features                         |
| ---------------- | --------------------------------------------------- | ------------------------------------ |
| `kubectl create` | You are **creating a new resource** from a manifest | Fails if the resource already exists |
| `kubectl apply`  | You want to **create or update** a resource         | Declarative — smart merge/update     |

### When to Use:

#### ✅ Use `kubectl create`:

* One-time, **imperative** creation of a resource.
* Example:

  ```bash
  kubectl create -f pod.yaml
  ```

#### ✅ Use `kubectl apply`:

* For **idempotent** and **declarative** configuration — ideal for CI/CD, GitOps.
* Can **update** an existing resource if the YAML changes.
* Example:

  ```bash
  kubectl apply -f pod.yaml
  ```

### Summary:

\| If resource **doesn't exist** | `create` and `apply` both work |
\| If resource **already exists** | `create` = ❌ error, `apply` = ✅ updates |
\| If you’re doing **Git-based config management** | ✅ use `apply` |

**Best Practice:** Use `kubectl apply` for YAML files and version-controlled workflows.

---

## 🔎 What is `-o wide`?

The `-o wide` flag in `kubectl` means **"output wide format"** — it shows additional details compared to the default output.

### Example:

```bash
kubectl get pods -o wide
```

This command includes extra columns such as:

* **NODE**: The node the pod is running on
* **IP**: The pod's internal IP
* **POD IP**
* **CONTAINER** info (image name)
* **START TIME** (in some setups)

### Output Comparison

#### Default:

```
NAME      READY   STATUS    RESTARTS   AGE
my-pod    1/1     Running   0          10m
```

#### With `-o wide`:

```
NAME      READY   STATUS    RESTARTS   AGE   IP            NODE           NOMINATED NODE   READINESS GATES
my-pod    1/1     Running   0          10m   10.244.0.5    minikube       <none>           <none>
```

**Use Case:** When you need **networking or scheduling details**, especially useful in multi-node clusters or for debugging.

---

```

Let me know if you'd like this saved as a `.md` file or published to a GitHub repo!
```
