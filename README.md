# Kubernetes_Study  
Kubernetes Study ✅

Main documents:

Documentation: https://kubernetes.io/docs  
Blog: https://kubernetes.io/blog/  
Helm Documentation: https://helm.sh/docs  
CKA Gateway API: https://gateway-api.sigs.k8s.io/  

---

**Domains and Competencies**
<details>
<summary>Storage - 10%</summary>
- [] Implement storage classes and dynamic volume provisioning<br>
- [] Configure volume types, access modes and reclaim policies<br>
- [] Manage persistent volumes and persistent volume claims<br>

</details><br>  

<details>
<summary>Troubleshooting – 30%</summary>
- [] Troubleshoot clusters and nodes<br>
- [] Troubleshoot cluster components<br>
- [] Monitor cluster and application resource usage<br>
- [] Manage and evaluate container output streams<br>
- [] Troubleshoot services and networking<br>

</details><br>
<details>
<summary>Workloads and Scheduling – 15%</summary>
- [] Understand application deployments and how to perform rolling update and - rollbacks<br>
- [] Use ConfigMaps and Secrets to configure applications<br>
- [] Configure workload autoscaling<br>
- [] Understand the primitives used to create robust, self-healing, application - deployments<br>
- [] Configure Pod admission and scheduling (limits, node affinity, etc.)<br>

</details><br>
<details>
<summary>Cluster Architecture, Installation and Configuration – 25%</summary>
- [] Manage role based access control (RBAC)<br>
- [] Prepare underlying infrastructure for installing a Kubernetes cluster<br>
- [] Create and manage Kubernetes clusters using kubeadm<br>
- [] Manage the lifecycle of Kubernetes clusters<br>
- [] Implement and configure a highly-available control plane<br>
- [] Use Helm and Kustomize to install cluster components<br>
- [] Understand extension interfaces (CNI, CSI, CRI, etc.)<br>
- [] Understand CRDs, install and configure operators<br>

</details><br>
<details>
<summary>Servicing and Networking – 20%</summary>
- [] Understand connectivity between Pods<br>
- [] Define and enforce Network Policies<br>
- [] Use ClusterIP, NodePort, LoadBalancer service types and endpoints<br>
- [] Use the Gateway API to manage Ingress traffic<br>
- [] Know how to use Ingress controllers and Ingress resources<br>
- [] Understand and use CoreDNS<br>

</details>

## Combined 8-Week CKA Study Plan (Killer Shell Modules + Foundational Topics)

### 📅 CKA Study Calendar Overview

| Subject               | Week_01      | Week_02      | Week_03      | Week_04      | Week_05      | Week_06      | Week_07      | Week_08      |
|-----------------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|
| **Kubernetes KCA**    | 7/10–7/16 | 7/17–7/23 | 7/24–7/30 | 7/31–8/6 | 8/7–8/13 | 8/14–8/20 | 8/21–8/27 | 8/28–9/3 |
| **KillaCoda Modules** | ✅ Playground, ✅ Vim Setup, ~Apiserver Crash, Application Misconfigured 1, ConfigMap Access in Pods | Application Misconfigured 2, Multi Container Issue, Ingress Create | Apiserver Crash, Apiserver Misconfigured, Kubelet Misconfigured, Kube Controller Manager Misconfigured | RBAC ServiceAccount/User Permissions, NetworkPolicy Namespace Selector, Misconfigured, Pod Affinity/Anti-Affinity | Cluster Node Join, Static Pod Move, Cluster Certificate Management | Cluster Setup, Cluster Upgrade | Revisit weak labs, YAML & RBAC, simulate full labs | Final review + light lab refresh |
| **CKA Exam Prep**     | Intro to K8s (2h30m), Stateless App Deploy (45m) | Stateful App Deploy (2h45m), K8s Concepts Quiz (20m) | Administering Clusters (1h08m), Access Troubleshooting (30m), Node Failures (30m) | Component Failures (30m), App Failures (1h), Auth & RBAC (30m) | Network Policies (40m), Security Contexts (40m), ConfigMaps/Secrets (1h) | Cluster Mgmt: Create, Backup, Restore, Upgrade (3h) | Practice Exams: Storage, Troubleshooting, Workloads, Services, Architecture (~5h) | CKA Challenge Lab (1h15m), CKA Final Exam Sim (1h30m) |

---


#### 🥋 30-Day Kubernetes Daily Kata Calendar (7/9–8/7)

| Day | Date | Topic                       | Task                                                                  | Status |
| --- | ---- | --------------------------- | --------------------------------------------------------------------- | ------ |
| 1   | 7/9  | Pods & Labels               | Create, label, and inspect a basic Pod                                | \[x] 2 |
| 2   | 7/10 | Namespaces                  | Create a namespace and deploy a Pod into it                           | \[ ]   |
| 3   | 7/11 | ReplicaSets                 | Create a ReplicaSet with 3 replicas and scale it                      | \[ ]   |
| 4   | 7/12 | Deployments                 | Convert ReplicaSet into Deployment and update it                      | \[ ]   |
| 5   | 7/13 | Services (ClusterIP)        | Expose a Deployment with a ClusterIP service                          | \[ ]   |
| 6   | 7/14 | NodePort                    | Expose your service externally using NodePort                         | \[ ]   |
| 7   | 7/15 | Environment Variables       | Inject env vars via YAML and command line                             | \[ ]   |
| 8   | 7/16 | ConfigMaps                  | Create a ConfigMap and mount as environment variables or volumes      | \[ ]   |
| 9   | 7/17 | Secrets                     | Securely inject Secrets via env or volumes                            | \[ ]   |
| 10  | 7/18 | Probes                      | Add liveness and readiness probes to Pods                             | \[ ]   |
| 11  | 7/19 | Volumes                     | Use `emptyDir` volume for Pod data sharing                            | \[ ]   |
| 12  | 7/20 | Persistent Volumes (PV/PVC) | Create a Persistent Volume and mount it in a Pod                      | \[ ]   |
| 13  | 7/21 | Init Containers             | Add an Init Container to prepare a volume or config                   | \[ ]   |
| 14  | 7/22 | Jobs                        | Create a short-lived Job and monitor its completion                   | \[ ]   |
| 15  | 7/23 | CronJobs                    | Schedule a CronJob to run every minute                                | \[ ]   |
| 16  | 7/24 | Resource Limits             | Set memory and CPU requests and limits                                | \[ ]   |
| 17  | 7/25 | Affinity/Anti-Affinity      | Control scheduling with pod affinity rules                            | \[ ]   |
| 18  | 7/26 | Taints & Tolerations        | Taint a node and allow Pods with toleration                           | \[ ]   |
| 19  | 7/27 | Node Selectors              | Use labels to target specific nodes for scheduling                    | \[ ]   |
| 20  | 7/28 | DaemonSets                  | Run one Pod on every node with a DaemonSet                            | \[ ]   |
| 21  | 7/29 | RBAC & ServiceAccounts      | Create Roles, RoleBindings, and SAs for Pod access                    | \[ ]   |
| 22  | 7/30 | Ingress Basics              | Setup Nginx Ingress Controller and basic rules                        | \[ ]   |
| 23  | 7/31 | Ingress Path Routing        | Define path-based routing for multiple services                       | \[ ]   |
| 24  | 8/1  | Network Policies            | Restrict Pod access using NetworkPolicies                             | \[ ]   |
| 25  | 8/2  | Horizontal Pod Autoscaler   | Scale a Deployment based on CPU usage                                 | \[ ]   |
| 26  | 8/3  | Custom Metrics + HPA        | Extend HPA to use mocked custom metrics                               | \[ ]   |
| 27  | 8/4  | Helm Basics                 | Install an application using a public Helm chart                      | \[ ]   |
| 28  | 8/5  | Helm Templating             | Create your own Helm chart for a basic Deployment                     | \[ ]   |
| 29  | 8/6  | StatefulSets                | Deploy a StatefulSet with unique IDs and stable storage               | \[ ]   |
| 30  | 8/7  | Final Challenge             | Deploy full app (Deployment + Service + Ingress + ConfigMap + Secret) | \[ ]   |

---

#### Killacoda | 20 Scenarios

| Day | Date       | Scenario Title         | Completed (✅/❌) |
| --- | ---------- | ---------------------- | --------------- |
| 1   | 2025-07-09 | Scenario 1 - Vim Setup | \[x] 1          |
| 2   | 2025-07-10 | Scenario 2             | \[ ]            |
| 3   | 2025-07-11 | Scenario 3             | \[ ]            |
| 4   | 2025-07-12 | Scenario 4             | \[ ]            |
| 5   | 2025-07-13 | Scenario 5             | \[ ]            |
| 6   | 2025-07-14 | Scenario 6             | \[ ]            |
| 7   | 2025-07-15 | Scenario 7             | \[ ]            |
| 8   | 2025-07-16 | Scenario 8 - Application Multi Container             | \[ ]            |
| 9   | 2025-07-17 | Scenario 9             | \[ ]            |
| 10  | 2025-07-18 | Scenario 10            | \[ ]            |
| 11  | 2025-07-19 | Scenario 11            | \[ ]            |
| 12  | 2025-07-20 | Scenario 12            | \[ ]            |
| 13  | 2025-07-21 | Scenario 13            | \[ ]            |
| 14  | 2025-07-22 | Scenario 14            | \[ ]            |
| 15  | 2025-07-23 | Scenario 15            | \[ ]            |
| 16  | 2025-07-24 | Scenario 16            | \[ ]            |
| 17  | 2025-07-25 | Scenario 17            | \[ ]            |
| 18  | 2025-07-26 | Scenario 18            | \[ ]            |
| 19  | 2025-07-27 | Scenario 19            | \[ ]            |
| 20  | 2025-07-28 | Scenario 20            | \[ ]            |

---

#### Killacoda | 30 Scenarios

| Day | Date       | Scenario Title                               | Completed (✅/❌) |
| --- | ---------- | -------------------------------------------- | --------------- |
| 1   | 2025-07-09 | Scenarion 1 - Create a Gateway and HTTPRoute | \[❌]            |
| 2   | 2025-07-10 |                                              | \[ ]            |
| 3   | 2025-07-11 |                                              | \[ ]            |
| 4   | 2025-07-12 |                                              | \[ ]            |
| 5   | 2025-07-13 |                                              | \[ ]            |
| 6   | 2025-07-14 |                                              | \[ ]            |
| 7   | 2025-07-15 |                                              | \[ ]            |
| 8   | 2025-07-16 |                                              | \[ ]            |
| 9   | 2025-07-17 |                                              | \[ ]            |
| 10  | 2025-07-18 |                                              | \[ ]            |
| 11  | 2025-07-19 |                                              | \[ ]            |
| 12  | 2025-07-20 |                                              | \[ ]            |
| 13  | 2025-07-21 |                                              | \[ ]            |
| 14  | 2025-07-22 |                                              | \[ ]            |
| 15  | 2025-07-23 |                                              | \[ ]            |
| 16  | 2025-07-24 |                                              | \[ ]            |
| 17  | 2025-07-25 |                                              | \[ ]            |
| 18  | 2025-07-26 |                                              | \[ ]            |
| 19  | 2025-07-27 |                                              | \[ ]            |
| 20  | 2025-07-28 |                                              | \[ ]            |
| 21  | 2025-07-29 |                                              | \[ ]            |
| 22  | 2025-07-30 |                                              | \[ ]            |
| 23  | 2025-07-31 |                                              | \[ ]            |
| 24  | 2025-08-01 |                                              | \[ ]            |
| 25  | 2025-08-02 |                                              | \[ ]            |
| 26  | 2025-08-03 |                                              | \[ ]            |
| 27  | 2025-08-04 |                                              | \[ ]            |
| 28  | 2025-08-05 |                                              | \[ ]            |
| 29  | 2025-08-06 |                                              | \[ ]            |
| 30  | 2025-08-07 |                                              | \[ ]            |

Let me know if you want this exported to Markdown or another format.
