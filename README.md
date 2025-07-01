# Kubernetes_Study
Kubernetes Study  
✅

---

## Combined 8-Week CKA Study Plan (Killer Shell Modules + Foundational Topics)

### 📅 CKA Study Calendar Overview

| Subject                  | Week\_01                                                                                            | Week\_02                                                           | Week\_03                                                                                               | Week\_04                                                                                                          | Week\_05                                                                 | Week\_06                                            | Week\_07                                                                           | Week\_08                                              |
| ------------------------ | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | --------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------- |
| **Kubernetes KCA**       | 6/30–7/6                                                                                            | 7/7–7/13                                                           | 7/14–7/20                                                                                              | 7/21–7/27                                                                                                         | 7/28–8/3                                                                 | 8/4–8/10                                            | 8/11–8/17                                                                          | 8/18–8/24                                             |
| **KillaCoda Modules**    | ✅ Playground, ✅ Vim Setup, \~Apiserver Crash, Application Misconfigured 1, ConfigMap Access in Pods | Application Misconfigured 2, Multi Container Issue, Ingress Create | Apiserver Crash, Apiserver Misconfigured, Kubelet Misconfigured, Kube Controller Manager Misconfigured | RBAC ServiceAccount/User Permissions, NetworkPolicy Namespace Selector, Misconfigured, Pod Affinity/Anti-Affinity | Cluster Node Join, Static Pod Move, Cluster Certificate Management       | Cluster Setup, Cluster Upgrade                      | Revisit weak labs, YAML & RBAC, simulate full labs                                 | Final review + light lab refresh                      |
| **CKA Exam Preparation** | Intro to K8s (2h30m  )?PODS?, Stateless App Deploy (45m)                                                    | Stateful App Deploy (2h45m), K8s Concepts Quiz (20m)               | Administering Clusters (1h08m), Access Troubleshooting (30m), Node Failures (30m)                      | Component Failures (30m), App Failures (1h), Auth & RBAC (30m)                                                    | Network Policies (40m), Security Contexts (40m), ConfigMaps/Secrets (1h) | Cluster Mgmt: Create, Backup, Restore, Upgrade (3h) | Practice Exams: Storage, Troubleshooting, Workloads, Services, Architecture (\~5h) | CKA Challenge Lab (1h15m), CKA Final Exam Sim (1h30m) |

---
🥋 30-Day Kubernetes Daily Kata Calendar (6/30–7/29)

| Day | Date | Topic                       | Task                                                                  |Status|
| --- | ---- | --------------------------- | --------------------------------------------------------------------- |----|
| 1   | 6/30 | Pods & Labels               | Create, label, and inspect a basic Pod                                |  [ ]  |
| 2   | 7/1  | Namespaces                  | Create a namespace and deploy a Pod into it                           |  [ ]  |
| 3   | 7/2  | ReplicaSets                 | Create a ReplicaSet with 3 replicas and scale it                      |  [ ]  |
| 4   | 7/3  | Deployments                 | Convert ReplicaSet into Deployment and update it                      |  [ ]  |
| 5   | 7/4  | Services (ClusterIP)        | Expose a Deployment with a ClusterIP service                          |  [ ]  |
| 6   | 7/5  | NodePort                    | Expose your service externally using NodePort                         |  [ ]  |
| 7   | 7/6  | Environment Variables       | Inject env vars via YAML and command line                             |  [ ]  |
| 8   | 7/7  | ConfigMaps                  | Create a ConfigMap and mount as environment variables or volumes      |  [ ]  |
| 9   | 7/8  | Secrets                     | Securely inject Secrets via env or volumes                            |  [ ]  |
| 10  | 7/9  | Probes                      | Add liveness and readiness probes to Pods                             |  [ ]  |
| 11  | 7/10 | Volumes                     | Use `emptyDir` volume for Pod data sharing                            |  [ ]  |
| 12  | 7/11 | Persistent Volumes (PV/PVC) | Create a Persistent Volume and mount it in a Pod                      |  [ ]  |
| 13  | 7/12 | Init Containers             | Add an Init Container to prepare a volume or config                   |  [ ]  |
| 14  | 7/13 | Jobs                        | Create a short-lived Job and monitor its completion                   |  [ ]  |
| 15  | 7/14 | CronJobs                    | Schedule a CronJob to run every minute                                |  [ ]  |
| 16  | 7/15 | Resource Limits             | Set memory and CPU requests and limits                                |  [ ]  |
| 17  | 7/16 | Affinity/Anti-Affinity      | Control scheduling with pod affinity rules                            |  [ ]  |
| 18  | 7/17 | Taints & Tolerations        | Taint a node and allow Pods with toleration                           |  [ ]  |
| 19  | 7/18 | Node Selectors              | Use labels to target specific nodes for scheduling                    |  [ ]  |
| 20  | 7/19 | DaemonSets                  | Run one Pod on every node with a DaemonSet                            |  [ ]  |
| 21  | 7/20 | RBAC & ServiceAccounts      | Create Roles, RoleBindings, and SAs for Pod access                    |  [ ]  |
| 22  | 7/21 | Ingress Basics              | Setup Nginx Ingress Controller and basic rules                        |  [ ]  |
| 23  | 7/22 | Ingress Path Routing        | Define path-based routing for multiple services                       |  [ ]  |
| 24  | 7/23 | Network Policies            | Restrict Pod access using NetworkPolicies                             |  [ ]  |
| 25  | 7/24 | Horizontal Pod Autoscaler   | Scale a Deployment based on CPU usage                                 |  [ ]  |
| 26  | 7/25 | Custom Metrics + HPA        | Extend HPA to use mocked custom metrics                               |  [ ]  |
| 27  | 7/26 | Helm Basics                 | Install an application using a public Helm chart                      |  [ ]  |
| 28  | 7/27 | Helm Templating             | Create your own Helm chart for a basic Deployment                     |  [ ]  |
| 29  | 7/28 | StatefulSets                | Deploy a StatefulSet with unique IDs and stable storage               |  [ ]  |
| 30  | 7/29 | Final Challenge             | Deploy full app (Deployment + Service + Ingress + ConfigMap + Secret) |  [ ]  |
---
Killacoda | 20 Scenarios

| Day | Date    | Scenario Title                 | Completed (✅/❌) |
|-----|---------|-------------------------------|-------------------|
| 1   | 2025‑06‑30 | Scenario 1                     |       [ ]            |
| 2   | 2025‑07‑01 | Scenario 2                     |       [ ]            |
| 3   | 2025‑07‑02 | Scenario 3                     |       [ ]            |
| 4   | 2025‑07‑03 | Scenario 4                     |       [ ]            |
| 5   | 2025‑07‑04 | Scenario 5                     |       [ ]            |
| 6   | 2025‑07‑05 | Scenario 6                     |       [ ]            |
| 7   | 2025‑07‑06 | Scenario 7                     |       [ ]            |
| 8   | 2025‑07‑07 | Scenario 8                     |       [ ]            |
| 9   | 2025‑07‑08 | Scenario 9                     |       [ ]            |
| 10  | 2025‑07‑09 | Scenario 10                    |       [ ]            |
| 11  | 2025‑07‑10 | Scenario 11                    |       [ ]            |
| 12  | 2025‑07‑11 | Scenario 12                    |       [ ]            |
| 13  | 2025‑07‑12 | Scenario 13                    |       [ ]            |
| 14  | 2025‑07‑13 | Scenario 14                    |       [ ]            |
| 15  | 2025‑07‑14 | Scenario 15                    |       [ ]            |
| 16  | 2025‑07‑15 | Scenario 16                    |       [ ]            |
| 17  | 2025‑07‑16 | Scenario 17                    |       [ ]            |
| 18  | 2025‑07‑17 | Scenario 18                    |       [ ]            |
| 19  | 2025‑07‑18 | Scenario 19                    |       [ ]            |
| 20  | 2025‑07‑19 | Scenario 20                    |       [ ]            |

Killacoda | 30 Scenarios
| Day | Date       | Scenario Title              | Completed (✅/❌) |
|-----|------------|-----------------------------|------------------|
| 1   | 2025-06-30 |                             |        [ ]          |
| 2   | 2025-07-01 |                             |        [ ]          |
| 3   | 2025-07-02 |                             |        [ ]          |
| 4   | 2025-07-03 |                             |        [ ]          |
| 5   | 2025-07-04 |                             |        [ ]          |
| 6   | 2025-07-05 |                             |        [ ]          |
| 7   | 2025-07-06 |                             |        [ ]          |
| 8   | 2025-07-07 |                             |        [ ]          |
| 9   | 2025-07-08 |                             |        [ ]          |
| 10  | 2025-07-09 |                             |        [ ]          |
| 11  | 2025-07-10 |                             |        [ ]          |
| 12  | 2025-07-11 |                             |        [ ]          |
| 13  | 2025-07-12 |                             |        [ ]          |
| 14  | 2025-07-13 |                             |        [ ]          |
| 15  | 2025-07-14 |                             |        [ ]          |
| 16  | 2025-07-15 |                             |        [ ]          |
| 17  | 2025-07-16 |                             |        [ ]          |
| 18  | 2025-07-17 |                             |        [ ]          |
| 19  | 2025-07-18 |                             |        [ ]          |
| 20  | 2025-07-19 |                             |        [ ]          |
| 21  | 2025-07-20 |                             |        [ ]          |
| 22  | 2025-07-21 |                             |        [ ]          |
| 23  | 2025-07-22 |                             |        [ ]          |
| 24  | 2025-07-23 |                             |        [ ]          |
| 25  | 2025-07-24 |                             |        [ ]          |
| 26  | 2025-07-25 |                             |        [ ]          |
| 27  | 2025-07-26 |                             |        [ ]          |
| 28  | 2025-07-27 |                             |        [ ]          |
| 29  | 2025-07-28 |                             |        [ ]          |
| 30  | 2025-07-29 |                             |        [ ]          |
