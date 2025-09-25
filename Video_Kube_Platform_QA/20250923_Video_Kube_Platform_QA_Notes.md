
| Feature     | **Manifest**                            | **Helm Chart**                                                         |
| ----------- | --------------------------------------- | ---------------------------------------------------------------------- |
| Format      | Plain YAML/JSON                         | YAML + templating (Go templates)                                       |
| Scope       | Single resource or small set            | Full app stack, reusable                                               |
| Reusability | Low (manual edits per environment)      | High (values override defaults)                                        |
| Versioning  | Git/manual                              | Built-in version control via Helm repo                                 |
| Complexity  | Simple                                  | More complex, but powerful                                             |
| Best For    | Small, simple apps or one-off resources | Large, configurable apps (e.g., NGINX ingress, Prometheus, PostgreSQL) |

👉 Rule of Thumb:

Use **manifests** for simple setups, labs, and when you need full control over every YAML.

Use **Helm charts** when deploying complex, repeatable, configurable applications across multiple environments (dev, test, prod).

| Feature          | **Helm**                                | **Terraform**                              |
| ---------------- | --------------------------------------- | ------------------------------------------ |
| Language         | YAML + Go templates (`values.yaml`)     | HCL (HashiCorp Configuration Language)     |
| Scope            | App packaging/deployment **inside K8s** | Infra provisioning (cloud + K8s clusters)  |
| State Management | No persistent state; relies on cluster  | Maintains a **state file**                 |
| Idempotency      | “Best effort” (may reinstall charts)    | Strict idempotency (infra always matches)  |
| Ecosystem        | Helm Hub (charts for common apps)       | Terraform Registry (modules for providers) |
| Best For         | Installing & managing apps in K8s       | Provisioning infra + K8s clusters          |

How They Work Together

Terraform provisions the Kubernetes cluster + cloud resources.

Helm installs and manages the apps inside the cluster.

Example workflow:

Terraform provisions AWS EKS cluster + VPC + IAM roles.

Terraform outputs cluster credentials.

Helm deploys Prometheus, ArgoCD, NGINX ingress into the cluster.

👉 Rule of Thumb:

Use Terraform for infrastructure provisioning.

Use Helm for application deployment inside Kubernetes.


Introduction to Kubernetes:

9/23/25 - Kubernetes Architecture
Here’s a **distilled set of the most pertinent information** with **key terms and definitions** extracted from your lesson text:

---

# 📌 Kubernetes Architecture – Key Terms & Definitions

### Kubernetes

* **Definition:** An orchestration tool for managing containerized applications.
* **Nature:** A distributed system with its own terminology (“vernacular”).

---

### Cluster

* **Definition:** The highest-level abstraction in Kubernetes; refers to all the machines (nodes) that make up the entire running system.
* **Composition:** Consists of **nodes** (worker + master).

---

### Node

* **Definition:** A machine in the cluster (can be a VM or physical).
* **Types:**

  * **Worker Node:** Runs containers (via Kubernetes components).
  * **Master Node:** Runs the **control plane**.

---

### Control Plane

* **Definition:** The set of APIs and software that Kubernetes users interact with.
* **Also Known As:** **Master components**.
* **Responsibilities:** Schedules containers onto nodes, manages cluster state.

---

### Scheduling

* **Definition:** The process of deciding which node a container runs on.
* **Note:** Unlike in time scheduling, here it refers to **resource placement** (e.g., CPU/memory needs, QoS rules).

---

### Pod

* **Definition:** The smallest deployable unit in Kubernetes; a group of one or more containers that run on the same node.
* **Purpose:** Containers in a Pod share networking and storage resources.

---

### Service

* **Definition:** An abstraction that defines networking rules for exposing Pods.
* **Scope:** Can expose Pods to other Pods in the cluster or to the public internet.

---

### Deployment

* **Definition:** A higher-level abstraction for managing Pods.
* **Responsibilities:**

  * Controls rollout and rollback of Pods
  * Handles updates
  * Manages **horizontal scaling**

---

# ✅ Recap (Simplified)

* **Kubernetes = orchestration tool**
* **Cluster = group of nodes**
* **Nodes = machines (worker/master)**
* **Control plane = runs on master, manages cluster**
* **Scheduler = places containers on nodes**
* **Pod = smallest unit (one or more containers)**
* **Service = exposes Pods (internal & external)**
* **Deployment = manages Pods (updates, scaling, rollout/rollback)**

---


9/23/25 - Interacting with Kubernetes
Here’s a **distilled set of key terms and definitions** extracted from your lesson text:

---

# 📌 Interacting with Kubernetes – Key Terms & Definitions

### Master Components / Control Plane

* **Definition:** Core components that manage cluster state.
* **API Server:** Master component that acts as the **front end** of the control plane; receives requests to **retrieve or modify cluster state**.

---

### Interaction Methods with Kubernetes

1. **REST API Calls**

   * Direct communication with the API server.
   * Rarely used unless no client library is available for your language.

2. **Client Libraries**

   * Official libraries exist for **Go, Python, Java, .NET, JavaScript**.
   * Community libraries exist for other languages.
   * Handle **authentication and REST requests** for developers.

3. **Kubectl (Kube Control)**

   * **Most common method.**
   * Command-line tool to interact with Kubernetes clusters (local or remote).
   * Converts high-level commands into API server requests.
   * Essential for day-to-day Kubernetes work.

4. **Web Dashboard**

   * Graphical interface for viewing cluster resources.
   * Optional, not available in all clusters.
   * Useful but less powerful than Kubectl.

---

### Kubectl – Core Commands

* **kubectl create**

  * Creates a new resource (via command or YAML manifest file).
* **kubectl delete**

  * Deletes a resource (via command or file).
* **kubectl get**

  * Lists resources of a specific type (e.g., `kubectl get pods`).
* **kubectl describe**

  * Shows detailed info about a resource (e.g., `kubectl describe pod <name>`).
* **kubectl logs**

  * Displays container logs for a specific pod (or container inside a multi-container pod).

---

# ✅ Recap (Simplified)

* **API Server = entry point** to Kubernetes control plane.
* **Interaction methods:** REST API → Client Libraries → **Kubectl (primary)** → Web Dashboard (optional).
* **Kubectl = main tool**, supports creating, deleting, listing, describing, and viewing logs of resources.

---


9/23/25 - PODS
Here’s a **distilled breakdown** of the most **pertinent information, key terms, and definitions** from the lesson:

---

# 📌 Kubernetes Pods & Manifests – Key Terms & Definitions

### Pod

* **Definition:** The **basic building block** in Kubernetes.
* **Contains:** One or more containers (lesson focuses on single-container pods).
* **Networking:**

  * Each pod gets **one IP address** in the container network.
  * All pods can communicate with each other by default.

---

### Pod Declaration / Properties

* Similar to `docker run` but in Kubernetes manifests.
* Includes:

  * **Container image**
  * **Ports to publish**
  * **Restart policy** (what happens when container fails)
  * **CPU and memory limits/requests**
  * Other Kubernetes-specific fields

---

### Manifest File

* **Definition:** YAML/JSON file that describes resources in Kubernetes (e.g., Pods, Deployments).
* **Structure:**

  * **apiVersion** – specifies which API version the resource uses
  * **kind** – identifies the resource type (e.g., Pod, Node)
  * **metadata** – includes **name** (must be unique within a namespace) and optional **labels**
  * **spec** – specification/configuration for the resource
* **Usage:** Sent to the **API server** via `kubectl`.

---

### Kubectl (Command-Line Tool)

* **kubectl create -f <file>** – creates a resource from a manifest file.
* **kubectl get <resource>** – lists resources (e.g., `kubectl get pods`).
* **kubectl describe <resource> <name>** – detailed info about a resource, useful for debugging.
* **kubectl logs <pod>** – prints logs from containers in a pod.
* **kubectl delete <resource> <name>** – deletes a resource.

---

### Labels

* **Definition:** Key-value pairs attached to resources.
* **Purpose:** Help identify resources and enable **selection/filtering** (e.g., `kubectl get pods -l region=us-east`).

---

### Resource Requests & Limits

* **Request:** Minimum resources (CPU/memory) required to schedule a pod.
* **Limit:** Maximum resources a container can consume.
* **Quality of Service (QoS):**

  * **BestEffort:** No requests/limits set; scheduled easily but first to be evicted.
  * **Guaranteed:** Requests = limits; ensures resources will always be available.
* **Impact:** Helps optimize utilization and prevent contention.

---

### Key Networking Concept

* Pods’ IPs belong to the **container network**, not directly accessible from outside.
* To expose pods externally, **Services** are needed (covered in next lesson).

---

# ✅ Recap (Simplified)

* **Pod = smallest unit** (one or more containers, one IP).
* **Manifests define resources** with `apiVersion`, `kind`, `metadata`, `spec`.
* **Kubectl commands:** `create`, `get`, `describe`, `logs`, `delete`.
* **Labels = resource identifiers** for organization and selection.
* **Resource requests/limits = QoS** (BestEffort vs Guaranteed).
* Pods communicate internally by default; external access requires **Services**.

---

9/23/25 - Services
Here’s a **distilled summary** of the lesson with the **most pertinent key terms and definitions**:

---

# 📌 Kubernetes Services – Key Terms & Definitions

### Problem with Pods

* **Pods have dynamic IPs**: When rescheduled, they get a **new IP**.
* This makes them **unreliable for direct access**.

---

### Service

* **Definition:** A Kubernetes abstraction that defines **networking rules** for accessing a group of Pods.
* **Purpose:** Provides a **stable, static IP and DNS name** to reach Pods, even as Pods are rescheduled or replaced.
* **Selector:** Uses **labels** to match Pods (e.g., `app=webserver`).
* **Load Balancing:** Distributes traffic across multiple Pods in the group.
* **Endpoints:** The list of Pod IPs/ports that match the selector; automatically updated by Kubernetes.

---

### Service Manifest – Key Fields

* **apiVersion** – API version.
* **kind** – Service.
* **metadata** – Includes **name** and optional **labels** (good practice to match Pods).
* **spec:**

  * **selector** – Label(s) of target Pods.
  * **ports** – Defines port mappings.
  * **type** – Defines how the service is exposed.

---

### Service Types (focus: NodePort)

* **ClusterIP (default):** Service only accessible **within the cluster**.
* **NodePort:**

  * Allocates a **port (30,000–32,767)** on every node.
  * Allows external access by sending requests to **<NodeIP>:<NodePort>**.
  * Acts as a bridge between external clients and Pods.
* **External-IP (not for NodePort):** Public IP for external access (covered later).

---

### Kubectl Commands for Services

* **kubectl create -f <file>** – Create a service from a manifest.
* **kubectl get services** – List services (shows **name, Cluster-IP, External-IP, ports, age**).
* **kubectl describe service <name>** – Detailed info including **endpoints (Pods)**.
* **kubectl describe nodes | grep -i address -A 1** – Get node IP addresses.

---

# ✅ Recap (Simplified)

* **Pods have changing IPs → Services solve this.**
* **Service = stable access point** with load balancing.
* **Selector** links services to Pods using **labels**.
* **NodePort service:** Exposes Pods externally on a fixed port across all nodes.
* Access via `curl <NodeIP>:<NodePort>` → routes traffic to Pods.

---


