# Kubernetes_Study  
Kubernetes Study ✅

Main documents:

- [Documentation](https://kubernetes.io/docs)  
- [Blog](https://kubernetes.io/blog/)  
- [Helm Documentation](https://helm.sh/docs)  
- [CKA Gateway API](https://gateway-api.sigs.k8s.io/)  

---

## Combined 6-Week CKA Study Plan (Killer Shell Modules + Foundational Topics)

### 📅 CKA Study Calendar Overview (Start: **9/22/2025**, End: **10/31/2025**)

| Subject               | Week_01      | Week_02      | Week_03      | Week_04      | Week_05      | Week_06      |
|-----------------------|--------------|--------------|--------------|--------------|--------------|--------------|
| **Kubernetes KCA**    | 9/22–9/28    | 9/29–10/5    | 10/6–10/12   | 10/13–10/19  | 10/20–10/26  | 10/27–10/31  |
| **KillaCoda Modules** | ✅ Playground, ✅ Vim Setup, ~Apiserver Crash, Application Misconfigured 1, ConfigMap Access in Pods | Application Misconfigured 2, Multi Container Issue, Ingress Create | Apiserver Crash, Apiserver Misconfigured, Kubelet Misconfigured, Kube Controller Manager Misconfigured | RBAC ServiceAccount/User Permissions, NetworkPolicy Namespace Selector, Pod Affinity/Anti-Affinity | Cluster Node Join, Static Pod Move, Cluster Certificate Mgmt | Revisit weak labs, YAML & RBAC, simulate full labs + Final review |
| **CKA Exam Prep**     | Intro to K8s (2h30m), Stateless App Deploy (45m) | Stateful App Deploy (2h45m), K8s Concepts Quiz (20m) | Administering Clusters (1h08m), Access Troubleshooting (30m), Node Failures (30m) | Component Failures (30m), App Failures (1h), Auth & RBAC (30m) | Network Policies (40m), Security Contexts (40m), ConfigMaps/Secrets (1h) | Practice Exams + Final CKA Sim (~6h30m) |
| Udemy Kubernetes  | [] Section 1-2 | [] Section 3-4 | [] Section 5-6 | [] Section 7 | [] Section 8-9 | [] Section 10-11 | [] Section 12-14 | [] Section 15-18 |   -   |

---
---

# 📅 Dual-Course CKA Timeline (9/22 → 10/31)

This schedule blends **Course 1 (platform.qa)** — *Certified Kubernetes Administrator (CKA) Exam Preparation (~24h, 26 steps)* — with **Course 2 (Udemy)** — *CKA with Practice Tests* — to reinforce each topic. Platform.qa provides structure and labs; Udemy provides primers, deeper dives, and mocks.

---

## Week 1 — Foundations & Core Workloads (Mon 9/22 – Sun 9/28)
- **Mon 9/22**
  - platform.qa: ✅ Course intro (5m12s, done), *Introduction to Kubernetes* (2h30m)
  - Udemy: Cluster Architecture, Pods + YAML, Deployments (≈40–60m)
- **Tue 9/23**
  - platform.qa: Lab – Deploy Stateless App (45m)
  - Udemy: Services (ClusterIP/LoadBalancer), Namespaces (≈35–45m)
- **Wed 9/24**
  - platform.qa: Lab – Deploy Stateful App (2h45m)
  - Udemy (optional): Storage intro (PV/PVC basics) (≈20–30m)
- **Thu 9/25**
  - platform.qa: Exam – Knowledge Check: Concepts (20m)
  - Udemy: Imperative vs Declarative + kubectl tips (≈25–35m)
- **Fri 9/26**
  - platform.qa: Buffer/notes tidy (≤30m)
  - Udemy (optional): Review lab solutions (≤20m)
- **Sat 9/27** — Udemy: Pods/ReplicaSets/Deployments recap (≤45m)
- **Sun 9/28** — Rest / catch-up

---

## Week 2 — Admin & Troubleshooting I (Mon 9/29 – Sun 10/5)
- **Mon 9/29**
  - platform.qa: Lesson – Administering Clusters (1h08m)
  - Udemy: Scheduling intro, Manual Scheduling, Labels/Selectors (≈25–35m)
- **Tue 9/30**
  - platform.qa: Lab – Troubleshooting: Cluster Access (30m)
  - Udemy: Taints/Tolerations, Node Selectors, Node Affinity (≈25–35m)
- **Wed 10/1**
  - platform.qa: Lab – Troubleshooting: Node Failures (30m)
  - Udemy: Resource Limits, editing pods/deployments (≈20–25m)
- **Thu 10/2**
  - platform.qa: Lab – Troubleshooting: Component Failures (30m)
  - Udemy: DaemonSets, Static Pods, Priority Classes (≈25–35m)
- **Fri 10/3**
  - platform.qa: Lab – Troubleshooting: Application Failures (1h)
  - Udemy (optional): Multiple schedulers + profiles (≈15–20m)
- **Sat 10/4** — Udemy: Admission Controllers (≈20–25m)
- **Sun 10/5** — Buffer/catch-up (≤30m)

---

## Week 3 — Security & Cluster Lifecycle (Mon 10/6 – Sun 10/12)
- **Mon 10/6**
  - platform.qa: Lab – Securing Clusters (Auth & RBAC) (1h)
  - Udemy: Security primitives, Authn, RBAC basics (≈25–35m)
- **Tue 10/7**
  - platform.qa: Lab – Network Policies (30m)
  - Udemy: NetPol + patterns (≈20–30m)
- **Wed 10/8**
  - platform.qa: Lab – Security Contexts (40m)
  - Udemy: Image security; Security Contexts (≈20–30m)
- **Thu 10/9**
  - platform.qa: Lab – ConfigMaps & Secrets (40m)
  - Udemy: Env vars, ConfigMaps, Secrets (≈25–35m)
- **Fri 10/10**
  - platform.qa: Lab – Create & Manage Cluster from Scratch (1h)
  - Udemy: Kubeadm deploy overview (≈20–30m)
- **Sat 10/11**
  - platform.qa: Lab – Backup & Restore Cluster (40m)
  - Udemy: etcd basics, snapshot/restore; ETCDCTL (≈20–30m)
- **Sun 10/12**
  - platform.qa: Lab – Upgrade Cluster (1h)
  - platform.qa: Lesson – CKA Exam Guide (6m35s)

---

## Week 4 — Networking + Practice Exams (Mon 10/13 – Sun 10/19)
- **Mon 10/13**
  - platform.qa: Practice Exam – Storage (1h)
  - Udemy: Storage recap (PV/PVC/SC) (≈20–25m)
- **Tue 10/14**
  - platform.qa: Practice Exam – Troubleshooting (50m)
  - Udemy: Troubleshooting intro + app failure (≈20–30m)
- **Wed 10/15**
  - platform.qa: Practice Exam – Workloads & Scheduling (1h)
  - Udemy: Networking prereqs (routing, DNS, CoreDNS) (≈25–35m)
- **Thu 10/16**
  - platform.qa: Practice Exam – Services & Networking (1h)
  - Udemy: CNI overview, Service networking (≈20–30m)
- **Fri 10/17**
  - platform.qa: Practice Exam – Cluster Arch/Install/Config (1h20m)
  - Udemy: Ingress + Gateway API (≈25–35m)
- **Sat 10/18**
  - platform.qa: Kubernetes Certification Challenge (1h15m)
  - Udemy (optional): Ingress labs solutions (≤20m)
- **Sun 10/19** — Light review (≤30m)

---

## Week 5 — Harden & Deepen (Mon 10/20 – Sun 10/26)
- **Mon 10/20**
  - platform.qa: CKA Challenge (1h15m)
  - Udemy: TLS in Kubernetes; Certificates API (≈25–35m)
- **Tue 10/21** — Udemy: Service Accounts; Kubeconfig; Authorization (≈25–35m)
- **Wed 10/22** — Udemy: Helm basics; Upgrading a chart; Kustomize intro (≈30–40m)
- **Thu 10/23** — Udemy: Network troubleshooting practice; logs/monitoring (≈25–35m)
- **Fri 10/24** — Udemy: Storage labs recap (PVC/SC) (≈20–30m)
- **Sat 10/25** *(optional)* — Udemy: Lightning Lab / Mock Exam 1 (≈30–45m)
- **Sun 10/26** *(optional)* — Udemy: Lightning Lab / Mock Exam 2 (≈30–45m)

---

## Week 6 — Final Sim & Taper (Mon 10/27 – Fri 10/31)
- **Mon 10/27** — Udemy: RBAC YAML reps; kubectl one-liners (30–45m)
- **Tue 10/28** — Udemy: Troubleshooting drills (pods/nodes/events/logs) (30–45m)
- **Wed 10/29** — Udemy: Timed dry-run, 6–8 tasks (30–45m)
- **Thu 10/30** — Rest/reset (15–20m skim notes)
- **Fri 10/31** — platform.qa: Final CKA Simulation Exam (1h30m)

---

✅ **Coverage Checklist**
- **platform.qa:** All 26 steps, 20 labs, 4 lessons, 2 exams — completed by 10/31.
- **Udemy:** Aligned sections (Core Concepts → Workloads → Security → Networking → Storage → Helm/Kustomize → Troubleshooting → Mocks).

This ensures mastery from both courses without overload, finishing strong by **10/31**.



---

#### 🥋 40-Day Kubernetes Daily Kata Calendar (**9/22–10/31**)

| Day | Date | Topic                       | Task                                                                  | Status |
| --- | ---- | --------------------------- | --------------------------------------------------------------------- | ------ |
| 1   | 9/22 | Pods & Labels               | Create, label, and inspect a basic Pod                                | [ ]   |
| 2   | 9/23 | Namespaces                  | Create a namespace and deploy a Pod into it                           | [ ]   |
| 3   | 9/24 | ReplicaSets                 | Create a ReplicaSet with 3 replicas and scale it                      | [ ]   |
| 4   | 9/25 | Deployments                 | Convert ReplicaSet into Deployment and update it                      | [ ]   |
| 5   | 9/26 | Services (ClusterIP)        | Expose a Deployment with a ClusterIP service                          | [ ]   |
| 6   | 9/27 **(WKND)** | NodePort          | Expose your service externally using NodePort                         | [ ]   |
| 7   | 9/28 **(WKND)** | Environment Variables | Inject env vars via YAML and command line                          | [ ]   |
| 8   | 9/29 | ConfigMaps                  | Create a ConfigMap and mount as env vars or volumes                   | [ ]   |
| 9   | 9/30 | Secrets                     | Securely inject Secrets via env or volumes                            | [ ]   |
| 10  | 10/1 | Probes                      | Add liveness and readiness probes to Pods                             | [ ]   |
| 11  | 10/2 | Volumes                     | Use `emptyDir` volume for Pod data sharing                            | [ ]   |
| 12  | 10/3 | Persistent Volumes (PV/PVC) | Create a PV and mount it in a Pod                                     | [ ]   |
| 13  | 10/4 **(WKND)** | Init Containers   | Add an Init Container to prepare a volume or config                   | [ ]   |
| 14  | 10/5 **(WKND)** | Jobs              | Create a short-lived Job and monitor completion                       | [ ]   |
| 15  | 10/6 | CronJobs                    | Schedule a CronJob to run every minute                                | [ ]   |
| 16  | 10/7 | Resource Limits             | Set memory and CPU requests and limits                                | [ ]   |
| 17  | 10/8 | Affinity/Anti-Affinity      | Control scheduling with affinity rules                                | [ ]   |
| 18  | 10/9 | Taints & Tolerations        | Taint a node and allow Pods with toleration                           | [ ]   |
| 19  | 10/10 | Node Selectors             | Use labels to target nodes for scheduling                              | [ ]   |
| 20  | 10/11 **(WKND)** | DaemonSets       | Run one Pod on every node with a DaemonSet                            | [ ]   |
| 21  | 10/12 **(WKND)** | RBAC & ServiceAccounts | Create Roles, RoleBindings, and SAs for Pod access               | [ ]   |
| 22  | 10/13 | Ingress Basics             | Setup Nginx Ingress and basic rules                                   | [ ]   |
| 23  | 10/14 | Ingress Path Routing       | Define path-based routing for multiple services                       | [ ]   |
| 24  | 10/15 | Network Policies           | Restrict Pod access using NetworkPolicies                             | [ ]   |
| 25  | 10/16 | Horizontal Pod Autoscaler  | Scale a Deployment based on CPU usage                                 | [ ]   |
| 26  | 10/17 **(WKND)** | Custom Metrics + HPA | Extend HPA with mocked custom metrics                            | [ ]   |
| 27  | 10/18 **(WKND)** | Helm Basics      | Install an app using a public Helm chart                              | [ ]   |
| 28  | 10/19 **(WKND)** | Helm Templating  | Create your own Helm chart for a Deployment                           | [ ]   |
| 29  | 10/20 | StatefulSets               | Deploy a StatefulSet with stable storage                              | [ ]   |
| 30  | 10/21 | Final Challenge            | Deploy app (Deployment + Service + Ingress + ConfigMap + Secret)      | [ ]   |
| 31  | 10/22 | Advanced RBAC              | Create ClusterRoles, ClusterRoleBindings with namespaces              | [ ]   |
| 32  | 10/23 | Advanced Networking        | Implement complex NetworkPolicies across namespaces                   | [ ]   |
| 33  | 10/24 | ETCD Backup/Restore        | Backup and restore etcd manually                                      | [ ]   |
| 34  | 10/25 **(WKND)** | TLS & Certificates | Manage TLS secrets, rotate certs in cluster                        | [ ]   |
| 35  | 10/26 **(WKND)** | Pod Security Policies | Apply PodSecurity admission (baseline, restricted)                 | [ ]   |
| 36  | 10/27 | Cluster Upgrades           | Simulate kubeadm upgrade process                                      | [ ]   |
| 37  | 10/28 | Debugging                  | Use `kubectl debug`, node/pod troubleshooting                        | [ ]   |
| 38  | 10/29 | Disaster Recovery          | Simulate region/node failure and recovery                             | [ ]   |
| 39  | 10/30 | Full Exam Simulation       | Timed mock of full CKA labs                                           | [ ]   |
| 40  | 10/31 | Wrap-Up + Review           | Review weak areas, YAML speed, command fluency                        | [ ]   |

---

#### Killacoda | 30 Scenarios (**9/22–10/31**)

| Day | Date       | Scenario Title                  | Completed (✅/❌) |
| --- | ---------- | ------------------------------- | --------------- |
| 1   | 2025-09-22 | Scenario 1 - Vim Setup          | [ ]            |
| 2   | 2025-09-23 | Scenario 2 - Pods Basics        | [ ]            |
| 3   | 2025-09-24 | Scenario 3 - Deployments        | [ ]            |
| 4   | 2025-09-25 | Scenario 4 - Services           | [ ]            |
| 5   | 2025-09-26 | Scenario 5 - Namespaces         | [ ]            |
| 6   | 2025-09-27 | Scenario 6 - RBAC               | [ ]            |
| 7   | 2025-09-28 | Scenario 7 - ConfigMaps/Secrets | [ ]            |
| 8   | 2025-09-29 | Scenario 8 - Ingress            | [ ]            |
| 9   | 2025-09-30 | Scenario 9 - NetworkPolicies    | [ ]            |
| 10  | 2025-10-01 | Scenario 10 - StatefulSets      | [ ]            |
| 11  | 2025-10-02 | Scenario 11 - Helm Basics       | [ ]            |
| 12  | 2025-10-03 | Scenario 12 - Helm Advanced     | [ ]            |
| 13  | 2025-10-04 | Scenario 13 - DaemonSets        | [ ]            |
| 14  | 2025-10-05 | Scenario 14 - Jobs/CronJobs     | [ ]            |
| 15  | 2025-10-06 | Scenario 15 - Debugging         | [ ]            |
| 16  | 2025-10-07 | Scenario 16 - Troubleshooting   | [ ]            |
| 17  | 2025-10-08 | Scenario 17 - etcd Recovery     | [ ]            |
| 18  | 2025-10-09 | Scenario 18 - Cluster Upgrade   | [ ]            |
| 19  | 2025-10-10 | Scenario 19 - Disaster Recovery | [ ]            |
| 20  | 2025-10-11 | Scenario 20 - Advanced RBAC     | [ ]            |
| 21  | 2025-10-12 | Scenario 21 - Pod Security      | [ ]            |
| 22  | 2025-10-13 | Scenario 22 - Logging/Monitoring| [ ]            |
| 23  | 2025-10-14 | Scenario 23 - Advanced Ingress  | [ ]            |
| 24  | 2025-10-15 | Scenario 24 - Scaling Apps      | [ ]            |
| 25  | 2025-10-16 | Scenario 25 - Multi-Cluster     | [ ]            |
| 26  | 2025-10-17 | Scenario 26 - Cert Mgmt         | [ ]            |
| 27  | 2025-10-18 | Scenario 27 - Final Lab I       | [ ]            |
| 28  | 2025-10-19 | Scenario 28 - Final Lab II      | [ ]            |
| 29  | 2025-10-30 | Scenario 29 - Mock Exam I       | [ ]            |
| 30  | 2025-10-31 | Scenario 30 - Mock Exam II      | [ ]            |

---

### 🎯 QA Training Path: Certified Kubernetes Administrator (CKA) Exam Preparation  
[Course Link](https://platform.qa.com/learning-paths/certified-kubernetes-administrator-exam-preparation-242/)  
**Goal:** Complete before **10/31/2025**  
**Total Duration:** ~23h 54m | 26 steps (Lessons, Labs, Exams)

---

#### 📅 4-Week Completion Plan (Start: **9/22/2025**, End: **10/19/2025**, buffer until **10/31/2025**)

| Week (Target Dates) | Focus Area | Content Breakdown | Duration |
|---------------------|------------|------------------|----------|
| **Week 1**<br>9/22 – 9/28  | Foundations + Stateless/Stateful | • Course Resume / Overview (5m)<br>• Intro to Kubernetes (2h30m)<br>• Lab: Deploy Stateless App (45m)<br>• Lab: Deploy Stateful App (2h45m)<br>• Exam: Kubernetes Concepts (20m) | ~6h30m |
| **Week 2**<br>9/29 – 10/5 | Cluster Admin + Troubleshooting | • Lesson: Administering Clusters (1h08m)<br>• Labs: Cluster Access (30m), Node Failures (30m), Component Failures (30m), Application Failures (1h)<br>• Lab: Securing Clusters w/ RBAC (1h) | ~4h40m |
| **Week 3**<br>10/6 – 10/12 | Security + Cluster Lifecycle | • Labs: Network Policies (30m), Security Contexts (40m), ConfigMaps & Secrets (40m), Create/Manage Cluster (1h)<br>• Labs: Backup/Restore (40m), Upgrade Cluster (1h)<br>• Lesson: CKA Exam Guide (6m) | ~4h40m |
| **Week 4**<br>10/13 – 10/19 | Practice + Challenge | • Labs: Practice Exams (Storage, Troubleshooting, Workloads, Services, Architecture) (~5h total)<br>• Lab: Kubernetes Certification Challenge (1h15m)<br>• Exam: Final CKA Sim (1h30m) | ~7h45m |

---

### 🚀 AWS DevOps Engineer Role Training (Nexpro Technologies Inc)  
**Duration:** **9/22 – 10/31**  
**Goal:** Align CKA + QA Kubernetes prep with AWS DevOps/SRE skill requirements

---

### 📅 Daily Integrated Training Plan (**9/22 – 10/31**)

| Date | Kata Task | QA CKA Prep | AWS DevOps Training |
|------|-----------|-------------|---------------------|
| **9/22** | Pods & Labels | Step 1: Course Resume (5m) + Step 2: Intro to K8s (2h30m) | Terraform basics: init & providers |
| **9/23** | Namespaces | Step 3: Lab – Deploy Stateless App (45m) | Terraform: AWS IAM resources (users, roles, policies) |
| **9/24** | ReplicaSets | Step 4: Lab – Deploy Stateful App (2h45m) | Terraform: AWS VPC basics (subnets, IGW, route tables) |
| **9/25** | Deployments | Step 5: Exam – Kubernetes Concepts (20m) | AWS IAM + VPC review (hands-on lab) |
| **9/26** | Services (ClusterIP) | Step 6: Lesson – Administering Clusters (1h08m) | AWS EKS: cluster creation walkthrough |
| **9/27** | NodePort | Step 7: Lab – Troubleshooting: Cluster Access Issues (30m) | AWS EKS: deploy worker nodes |
| **9/28** | Environment Variables | Step 8: Lab – Troubleshooting: Node Failures (30m) | GitLab CI basics: runners + pipelines |
| **9/29** | ConfigMaps | Step 9: Lab – Troubleshooting: Component Failures (30m) | GitLab CI: build & test pipeline for Python app |
| **9/30** | Secrets | Step 10: Lab – Troubleshooting: App Failures (1h) | AWS EKS: deploy sample app (kubectl apply) |
| **10/1** | Probes | Step 11: Lab – Securing K8s (RBAC) (1h) | ArgoCD: install on EKS cluster |
| **10/2** | Volumes | Step 12: Lab – Network Policies (30m) | ArgoCD: sync Git repo to EKS |
| **10/3** | PV & PVC | Step 13: Lab – Security Contexts (40m) | Terraform: S3 bucket + lifecycle |
| **10/4** | Init Containers | Step 14: Lab – ConfigMaps & Secrets (40m) | Python boto3: manage IAM users & groups |
| **10/5** | Jobs | Step 15: Lab – Create & Manage Cluster from Scratch (1h) | Terraform: EKS via module |