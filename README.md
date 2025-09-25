# Kubernetes_Study  
Kubernetes Study ✅

Main documents:

- [Documentation](https://kubernetes.io/docs)  
- [Blog](https://kubernetes.io/blog/)  
- [Helm Documentation](https://helm.sh/docs)  
- [CKA Gateway API](https://gateway-api.sigs.k8s.io/)  

---

## Combined 8-Week CKA Study Plan (Killer Shell Modules + Foundational Topics)

### 📅 CKA Study Calendar Overview

| Subject               | Week_01      | Week_02      | Week_03      | Week_04      | Week_05      | Week_06      | Week_07      | Week_08      |
|-----------------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|
| **Kubernetes KCA**    | 9/2–9/8      | 9/9–9/15     | 9/16–9/22    | 9/23–9/29    | 9/30–10/6    | 10/7–10/13   | 10/14–10/20  | 10/21–10/27  |
| **KillaCoda Modules** | ✅ Playground, ✅ Vim Setup, ~Apiserver Crash, Application Misconfigured 1, ConfigMap Access in Pods | Application Misconfigured 2, Multi Container Issue, Ingress Create | Apiserver Crash, Apiserver Misconfigured, Kubelet Misconfigured, Kube Controller Manager Misconfigured | RBAC ServiceAccount/User Permissions, NetworkPolicy Namespace Selector, Misconfigured, Pod Affinity/Anti-Affinity | Cluster Node Join, Static Pod Move, Cluster Certificate Management | Cluster Setup, Cluster Upgrade | Revisit weak labs, YAML & RBAC, simulate full labs | Final review + light lab refresh |
| **CKA Exam Prep**     | Intro to K8s (2h30m), Stateless App Deploy (45m) | Stateful App Deploy (2h45m), K8s Concepts Quiz (20m) | Administering Clusters (1h08m), Access Troubleshooting (30m), Node Failures (30m) | Component Failures (30m), App Failures (1h), Auth & RBAC (30m) | Network Policies (40m), Security Contexts (40m), ConfigMaps/Secrets (1h) | Cluster Mgmt: Create, Backup, Restore, Upgrade (3h) | Practice Exams: Storage, Troubleshooting, Workloads, Services, Architecture (~5h) | CKA Challenge Lab (1h15m), CKA Final Exam Sim (1h30m) |
| Udemy Kubernetes  | [] Section 1-2 |  [] Section 3-4   |  [] Section 5-6    | [] Section 7   |  [] Section 8-9  | [] Section 10-12   | [] Section 13-14   |   -   |
| Udemy Kubernetes  | [] Section 1-2 | [] Section 3-4 | [] Section 5-6 | [] Section 7 | [] Section 8-9 | [] Section 10-11 | [] Section 12-14 | [] Section 15-18 |

---

# Kubernetes_Study  
Kubernetes Study ✅

Main documents:

- [Documentation](https://kubernetes.io/docs)  
- [Blog](https://kubernetes.io/blog/)  
- [Helm Documentation](https://helm.sh/docs)  
- [CKA Gateway API](https://gateway-api.sigs.k8s.io/)  

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

#### 🥋 30-Day Kubernetes Daily Kata Calendar (9/2–10/1)

| Day | Date | Topic                       | Task                                                                  | Status |
| --- | ---- | --------------------------- | --------------------------------------------------------------------- | ------ |
| 1   | 9/2  | Pods & Labels               | Create, label, and inspect a basic Pod                                | [ ]   |
| 2   | 9/3  | Namespaces                  | Create a namespace and deploy a Pod into it                           | [ ]   |
| 3   | 9/4  | ReplicaSets                 | Create a ReplicaSet with 3 replicas and scale it                      | [ ]   |
| 4   | 9/5  | Deployments                 | Convert ReplicaSet into Deployment and update it                      | [ ]   |
| 5   | 9/6 **(WKND)** | Services (ClusterIP)        | Expose a Deployment with a ClusterIP service                          | [ ]   |
| 6   | 9/7 **(WKND)** | NodePort                    | Expose your service externally using NodePort                         | [ ]   |
| 7   | 9/8  | Environment Variables       | Inject env vars via YAML and command line                             | [ ]   |
| 8   | 9/9  | ConfigMaps                  | Create a ConfigMap and mount as env vars or volumes                   | [ ]   |
| 9   | 9/10 | Secrets                     | Securely inject Secrets via env or volumes                            | [ ]   |
| 10  | 9/11 | Probes                      | Add liveness and readiness probes to Pods                             | [ ]   |
| 11  | 9/12 | Volumes                     | Use `emptyDir` volume for Pod data sharing                            | [ ]   |
| 12  | 9/13 **(WKND)** | Persistent Volumes (PV/PVC) | Create a PV and mount it in a Pod                                     | [ ]   |
| 13  | 9/14 **(WKND)** | Init Containers             | Add an Init Container to prepare a volume or config                   | [ ]   |
| 14  | 9/15 | Jobs                        | Create a short-lived Job and monitor completion                       | [ ]   |
| 15  | 9/16 | CronJobs                    | Schedule a CronJob to run every minute                                | [ ]   |
| 16  | 9/17 | Resource Limits             | Set memory and CPU requests and limits                                | [ ]   |
| 17  | 9/18 | Affinity/Anti-Affinity      | Control scheduling with affinity rules                                | [ ]   |
| 18  | 9/19 | Taints & Tolerations        | Taint a node and allow Pods with toleration                           | [ ]   |
| 19  | 9/20 **(WKND)** | Node Selectors              | Use labels to target nodes for scheduling                             | [ ]   |
| 20  | 9/21 **(WKND)** | DaemonSets                  | Run one Pod on every node with a DaemonSet                            | [ ]   |
| 21  | 9/22 | RBAC & ServiceAccounts      | Create Roles, RoleBindings, and SAs for Pod access                    | [ ]   |
| 22  | 9/23 | Ingress Basics              | Setup Nginx Ingress and basic rules                                   | [ ]   |
| 23  | 9/24 | Ingress Path Routing        | Define path-based routing for multiple services                       | [ ]   |
| 24  | 9/25 | Network Policies            | Restrict Pod access using NetworkPolicies                             | [ ]   |
| 25  | 9/26 | Horizontal Pod Autoscaler   | Scale a Deployment based on CPU usage                                 | [ ]   |
| 26  | 9/27 **(WKND)** | Custom Metrics + HPA        | Extend HPA with mocked custom metrics                                 | [ ]   |
| 27  | 9/28 **(WKND)** | Helm Basics                 | Install an app using a public Helm chart                              | [ ]   |
| 28  | 9/29 | Helm Templating             | Create your own Helm chart for a Deployment                           | [ ]   |
| 29  | 9/30 | StatefulSets                | Deploy a StatefulSet with stable storage                              | [ ]   |
| 30  | 10/1 | Final Challenge             | Deploy app (Deployment + Service + Ingress + ConfigMap + Secret)      | [ ]   |

---

#### Killacoda | 20 Scenarios (9/2–9/21)

| Day | Date       | Scenario Title         | Completed (✅/❌) |
| --- | ---------- | ---------------------- | --------------- |
| 1   | 2025-09-02 | Scenario 1 - Vim Setup | [ ]            |
| 2   | 2025-09-03 | Scenario 2             | [ ]            |
| 3   | 2025-09-04 | Scenario 3             | [ ]            |
| 4   | 2025-09-05 | Scenario 4             | [ ]            |
| 5   | 2025-09-06 **(WKND)** | Scenario 5  | [ ]            |
| 6   | 2025-09-07 **(WKND)** | Scenario 6  | [ ]            |
| 7   | 2025-09-08 | Scenario 7             | [ ]            |
| 8   | 2025-09-09 | Scenario 8             | [ ]            |
| 9   | 2025-09-10 | Scenario 9             | [ ]            |
| 10  | 2025-09-11 | Scenario 10            | [ ]            |
| 11  | 2025-09-12 | Scenario 11            | [ ]            |
| 12  | 2025-09-13 **(WKND)** | Scenario 12 | [ ]            |
| 13  | 2025-09-14 **(WKND)** | Scenario 13 | [ ]            |
| 14  | 2025-09-15 | Scenario 14            | [ ]            |
| 15  | 2025-09-16 | Scenario 15            | [ ]            |
| 16  | 2025-09-17 | Scenario 16            | [ ]            |
| 17  | 2025-09-18 | Scenario 17            | [ ]            |
| 18  | 2025-09-19 | Scenario 18            | [ ]            |
| 19  | 2025-09-20 **(WKND)** | Scenario 19 | [ ]            |
| 20  | 2025-09-21 **(WKND)** | Scenario 20 | [ ]            |

---

#### Killacoda | 30 Scenarios (9/2–10/1)

| Day | Date       | Scenario Title                               | Completed (✅/❌) |
| --- | ---------- | -------------------------------------------- | --------------- |
| 1   | 2025-09-02 | Scenario 1 - Create a Gateway and HTTPRoute  | [ ]            |
| 2   | 2025-09-03 |                                              | [ ]            |
| 3   | 2025-09-04 |                                              | [ ]            |
| 4   | 2025-09-05 |                                              | [ ]            |
| 5   | 2025-09-06 **(WKND)** |                                   | [ ]            |
| 6   | 2025-09-07 **(WKND)** |                                   | [ ]            |
| 7   | 2025-09-08 |                                              | [ ]            |
| 8   | 2025-09-09 |                                              | [ ]            |
| 9   | 2025-09-10 |                                              | [ ]            |
| 10  | 2025-09-11 |                                              | [ ]            |
| 11  | 2025-09-12 |                                              | [ ]            |
| 12  | 2025-09-13 **(WKND)** |                                   | [ ]            |
| 13  | 2025-09-14 **(WKND)** |                                   | [ ]            |
| 14  | 2025-09-15 |                                              | [ ]            |
| 15  | 2025-09-16 |                                              | [ ]            |
| 16  | 2025-09-17 |                                              | [ ]            |
| 17  | 2025-09-18 |                                              | [ ]            |
| 18  | 2025-09-19 |                                              | [ ]            |
| 19  | 2025-09-20 **(WKND)** |                                   | [ ]            |
| 20  | 2025-09-21 **(WKND)** |                                   | [ ]            |
| 21  | 2025-09-22 |                                              | [ ]            |
| 22  | 2025-09-23 |                                              | [ ]            |
| 23  | 2025-09-24 |                                              | [ ]            |
| 24  | 2025-09-25 |                                              | [ ]            |
| 25  | 2025-09-26 |                                              | [ ]            |
| 26  | 2025-09-27 **(WKND)** |                                   | [ ]            |
| 27  | 2025-09-28 **(WKND)** |                                   | [ ]            |
| 28  | 2025-09-29 |                                              | [ ]            |
| 29  | 2025-09-30 |                                              | [ ]            |
| 30  | 2025-10-01 |                                              | [ ]            |

---

### 🎯 QA Training Path: Certified Kubernetes Administrator (CKA) Exam Preparation  
[Course Link](https://platform.qa.com/learning-paths/certified-kubernetes-administrator-exam-preparation-242/)  
**Goal:** Complete before **9/29/2025**  
**Total Duration:** ~23h 54m | 26 steps (Lessons, Labs, Exams)

---

#### 📅 4-Week Completion Plan

| Week (Target Dates) | Focus Area | Content Breakdown | Duration |
|---------------------|------------|------------------|----------|
| **Week 1**<br>9/2 – 9/8  | Foundations + Stateless/Stateful | • Course Resume / Overview (5m)<br>• Intro to Kubernetes (2h30m)<br>• Lab: Deploy Stateless App (45m)<br>• Lab: Deploy Stateful App (2h45m)<br>• Exam: Kubernetes Concepts (20m) | ~6h30m |
| **Week 2**<br>9/9 – 9/15 | Cluster Admin + Troubleshooting | • Lesson: Administering Clusters (1h08m)<br>• Labs: Cluster Access (30m), Node Failures (30m), Component Failures (30m), Application Failures (1h)<br>• Lab: Securing Clusters w/ RBAC (1h) | ~4h40m |
| **Week 3**<br>9/16 – 9/22 | Security + Cluster Lifecycle | • Labs: Network Policies (30m), Security Contexts (40m), ConfigMaps & Secrets (40m), Create/Manage Cluster (1h)<br>• Labs: Backup/Restore (40m), Upgrade Cluster (1h)<br>• Lesson: CKA Exam Guide (6m) | ~4h40m |
| **Week 4**<br>9/23 – 9/29 | Practice + Challenge | • Labs: Practice Exams (Storage, Troubleshooting, Workloads, Services, Architecture) (~5h total)<br>• Lab: Kubernetes Certification Challenge (1h15m)<br>• Exam: Final CKA Sim (1h30m) | ~7h45m |

---

#### ✅ Tracking Table (By Step with Dates)

| Step | Date       | Type   | Title                                        | Duration | Status |
|------|------------|--------|----------------------------------------------|----------|--------|
| 1    | 9/2        | Lesson | Course Resume / Overview                     | 5m       | [ ]    |
| 2    | 9/2        | Lesson | Intro to Kubernetes                          | 2h30m    | [ ]    |
| 3    | 9/3        | Lab    | Deploy a Stateless App                       | 45m      | [ ]    |
| 4    | 9/4        | Lab    | Deploy a Stateful App                        | 2h45m    | [ ]    |
| 5    | 9/5        | Exam   | Knowledge Check: Kubernetes Concepts         | 20m      | [ ]    |
| 6    | 9/6        | Lesson | Administering Kubernetes Clusters            | 1h08m    | [ ]    |
| 7    | 9/7        | Lab    | Troubleshooting: Cluster Access Issues       | 30m      | [ ]    |
| 8    | 9/8        | Lab    | Troubleshooting: Cluster Node Failures       | 30m      | [ ]    |
| 9    | 9/9        | Lab    | Troubleshooting: Component Failures          | 30m      | [ ]    |
| 10   | 9/10       | Lab    | Troubleshooting: Application Failures        | 1h       | [ ]    |
| 11   | 9/11       | Lab    | Securing Kubernetes (Auth & RBAC)            | 1h       | [ ]    |
| 12   | 9/12       | Lab    | Network Policies                             | 30m      | [ ]    |
| 13   | 9/13       | Lab    | Security Contexts                            | 40m      | [ ]    |
| 14   | 9/14       | Lab    | ConfigMaps & Secrets                         | 40m      | [ ]    |
| 15   | 9/15       | Lab    | Create & Manage Cluster from Scratch         | 1h       | [ ]    |
| 16   | 9/16       | Lab    | Backup & Restore Cluster                     | 40m      | [ ]    |
| 17   | 9/17       | Lab    | Upgrade Cluster w/ kubeadm                   | 1h       | [ ]    |
| 18   | 9/18       | Lesson | CKA Exam Guide                               | 6m       | [ ]    |
| 19   | 9/19       | Lab    | Practice Exam: Storage                       | 1h       | [ ]    |
| 20   | 9/20       | Lab    | Practice Exam: Troubleshooting               | 50m      | [ ]    |
| 21   | 9/21       | Lab    | Practice Exam: Workloads                     | 1h       | [ ]    |
| 22   | 9/22       | Lab    | Practice Exam: Services & Networking         | 1h       | [ ]    |
| 23   | 9/23       | Lab    | Practice Exam: Cluster Architecture          | 1h20m    | [ ]    |
| 24   | 9/24       | Lab    | Kubernetes Certification Challenge           | 1h15m    | [ ]    |
| 25   | 9/25       | Exam   | Final CKA Sim                                | 1h30m    | [ ]    |
| 26   | 9/29       | Completion | Earn Certificate of Completion          | —        | [ ]    |

---

### 🚀 AWS DevOps Engineer Role Training (Nexpro Technologies Inc)  
**Duration:** 9/2 – 9/29  
**Goal:** Align CKA + QA Kubernetes prep with AWS DevOps/SRE skill requirements

#### 📅 Weekly Study Focus

| Week | Dates       | Focus Areas | Reflected Training Links |
|------|-------------|-------------|--------------------------|
| **Week 1** | 9/2 – 9/8   | • Terraform fundamentals (IaC) <br>• AWS IAM & VPC basics <br>• CI/CD Git basics | • QA CKA Course Intro <br>• Kata: Pods, Namespaces, Services <br>• AWS Docs: [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html), [VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) |
| **Week 2** | 9/9 – 9/15  | • EKS deep dive <br>• Terraform AWS provider (IAM/VPC/EKS) <br>• CI/CD with GitLab runners | • QA Labs: Stateless/Stateful Apps <br>• Kata: ConfigMaps, Secrets, Probes <br>• AWS Workshop: [EKS Workshop](https://eksworkshop.com/) |
| **Week 3** | 9/16 – 9/22 | • ArgoCD on EKS <br>• Microservices on K8s <br>• Python scripting for automation | • QA Labs: Cluster Lifecycle (Backup/Restore, Upgrade) <br>• Kata: RBAC, Ingress, Network Policies <br>• ArgoCD Docs |
| **Week 4** | 9/23 – 9/29 | • SRE principles <br>• Observability: logs/metrics/alerts <br>• CloudFront, API Gateway | • QA Practice Exams + Final Sim <br>• Kata: StatefulSets + Final Challenge <br>• AWS Docs: CloudFront, API GW |

#### ✅ Skill Tracking Table

| Skill Area | Training Resource | Target Date | Status |
|------------|-------------------|-------------|--------|
| **Terraform IaC** | HashiCorp Learn – Terraform AWS provider | 9/2–9/8  | [ ] |
| **AWS IAM + VPC** | AWS Docs / Hands-on labs | 9/2–9/8  | [ ] |
| **AWS EKS** | AWS EKS Workshop | 9/9–9/15 | [ ] |
| **CI/CD – GitLab** | GitLab Docs + runner setup | 9/9–9/15 | [ ] |
| **ArgoCD** | ArgoCD Getting Started lab | 9/16–9/22 | [ ] |
| **Python Scripting** | Automate IAM/S3 with boto3 | 9/16–9/22 | [ ] |
| **SRE Concepts** | Google SRE Book (free) | 9/23–9/29 | [ ] |
| **CloudFront + API GW** | AWS Docs / free labs | 9/23–9/29 | [ ] |
| **Kubernetes Debugging** | QA CKA Troubleshooting labs | 9/23–9/29 | [ ] |

---

### 📅 Daily Integrated Training Plan (9/2 – 9/29)

| Date | Kata Task | QA CKA Prep | AWS DevOps Training |
|------|-----------|-------------|---------------------|
| **9/2** | Pods & Labels | Step 1: Course Resume (5m) + Step 2: Intro to K8s (2h30m) | Terraform basics: init & providers |
| **9/3** | Namespaces | Step 3: Lab – Deploy Stateless App (45m) | Terraform: AWS IAM resources (users, roles, policies) |
| **9/4** | ReplicaSets | Step 4: Lab – Deploy Stateful App (2h45m) | Terraform: AWS VPC basics (subnets, IGW, route tables) |
| **9/5** | Deployments | Step 5: Exam – Kubernetes Concepts (20m) | AWS IAM + VPC review (hands-on lab) |
| **9/6 (WKND)** | Services (ClusterIP) | Step 6: Lesson – Administering Clusters (1h08m) | AWS EKS: cluster creation walkthrough |
| **9/7 (WKND)** | NodePort | Step 7: Lab – Troubleshooting: Cluster Access Issues (30m) | AWS EKS: deploy worker nodes |
| **9/8** | Environment Variables | Step 8: Lab – Troubleshooting: Node Failures (30m) | GitLab CI basics: runners + pipelines |
| **9/9** | ConfigMaps | Step 9: Lab – Troubleshooting: Component Failures (30m) | GitLab CI: build & test pipeline for Python app |
| **9/10** | Secrets | Step 10: Lab – Troubleshooting: App Failures (1h) | AWS EKS: deploy sample app (kubectl apply) |
| **9/11** | Probes | Step 11: Lab – Securing K8s (RBAC) (1h) | ArgoCD: install on EKS cluster |
| **9/12** | Volumes | Step 12: Lab – Network Policies (30m) | ArgoCD: sync Git repo to EKS |
| **9/13 (WKND)** | PV & PVC | Step 13: Lab – Security Contexts (40m) | Terraform: S3 bucket + lifecycle |
| **9/14 (WKND)** | Init Containers | Step 14: Lab – ConfigMaps & Secrets (40m) | Python boto3: manage IAM users & groups |
| **9/15** | Jobs | Step 15: Lab – Create & Manage Cluster from Scratch (1h) | Terraform: EKS via module |
| **9/16** | CronJobs | Step 16: Lab – Backup & Restore Cluster (40m) | Python: automate EC2 with boto3 |
| **9/17** | Resource Limits | Step 17: Lab – Upgrade Cluster w/ kubeadm (1h) | GitLab CI + ArgoCD integration demo |
| **9/18** | Affinity/Anti-Affinity | Step 18: Lesson – CKA Exam Guide (6m) | AWS Lambda + API Gateway basics |
| **9/19** | Taints & Tolerations | Step 19: Practice Exam – Storage (1h) | CloudWatch metrics + logging |
| **9/20 (WKND)** | Node Selectors | Step 20: Practice Exam – Troubleshooting (50m) | SRE: SLIs, SLOs, SLAs |
| **9/21 (WKND)** | DaemonSets | Step 21: Practice Exam – Workloads (1h) | EKS monitoring with Prometheus |
| **9/22** | RBAC & ServiceAccounts | Step 22: Practice Exam – Services & Networking (1h) | ArgoCD: rolling deployments |
| **9/23** | Ingress Basics | Step 23: Practice Exam – Cluster Architecture (1h20m) | CloudFront setup (CDN) |
| **9/24** | Ingress Path Routing | Step 24: Lab – Kubernetes Certification Challenge (1h15m) | API Gateway + Lambda integration |
| **9/25** | Network Policies | Step 25: Exam – Final CKA Sim (1h30m) | EKS: troubleshoot pods & services |
| **9/26** | HPA (CPU scaling) | Review QA weak areas | Terraform: remote state + workspaces |
| **9/27 (WKND)** | Custom Metrics + HPA | Review QA weak areas | Python: CloudWatch automation (alarms) |
| **9/28 (WKND)** | Helm Basics | Revisit QA Labs: RBAC + Networking | GitLab CI: multi-stage pipelines |
| **9/29** | Helm Templating | Revisit QA Labs: StatefulSets | ArgoCD: blue/green + canary deployments |
