# Kubernetes_Study
Kubernetes Study
✅ 
| Subject   | Week_01 | Week_02 | Week_03 | Week_04 | Week_05 | Week_06 | Week_07 | Week_08 |
|-----------|---------|---------|---------|---------|---------|---------|---------|---------|
| Kubernetes KCA  |  6/1-7   |  6/8-14  |  6/15-21  | 6/22-28   |  6/29-7/5   |   7/13-19   |   7/20-26   |   7/27-30   |
| KillaCoda Modules  |  x   |  x  |  x  | x   |  x   |   x   |   x   |   x   |
| CKA Exam Preparation |  x   |  x  |  x  | x   |  x   |   x   |   x   |   x   |

## 8-Week CKA Study Plan (Killer Shell Modules + Foundational Topics)

### WEEK 1: Foundational Concepts + Pod Lifecycle

Goal: Master cluster architecture and working with Pods.

[ ] Day 1–2:[ ] Module: Kubernetes Basics

Learn architecture: node types, control plane, etcd, kubelet

Practice: kubectl cluster-info, kubectl get nodes

[ ] Day 3–4:[ ] Module: Working with Pods

Create and manage Pods

Practice: kubectl run, kubectl describe pod

[ ] Day 5:[ ] Module: Multi-Container Pods

Understand sidecars and init containers

Practice: YAML for multiple containers

[ ] Day 6:[ ] Module: Namespaces & Contexts

Practice switching contexts and using namespaces

Commands: kubectl config use-context, kubectl get pods -n kube-system

[ ] Day 7:[ ] Review & Lab Practice (1st 4 modules)

Use Killer Coda playgrounds for hands-on repetition

Killer Shell Module: Playground, Vim Setup, Application Misconfigured 1, ConfigMap Access in Pods

---


### WEEK 2: Configuration & Networking

Goal: Understand ConfigMaps, Secrets, Services, and DNS

[ ] Day 8–9:[ ] Module: ConfigMaps & Secrets

Practice creating ConfigMaps & Secrets

Environment variables in pods

[ ] Day 10–11:[ ] Module: Service Networking (ClusterIP, NodePort)

Understand service types

Practice exposing deployments via kubectl expose

[ ] Day 12:[ ] Module: DNS & Environment Injection

Practice accessing services via DNS

Use ConfigMaps in environment

[ ] Day 13:[ ] Module: Port Forwarding & Probes

Practice: kubectl port-forward, liveness/readiness probes

[ ] Day 14:[ ] Review & Labs

Killer Shell Modules: Application Misconfigured 2, Application Multi Container Issue, Ingress Create  

---

### WEEK 3: Controllers, Scheduling & Logs

Goal: Manage Deployments, Jobs, and troubleshoot applications

[ ] Day 15–16:[ ] Module: Deployments & ReplicaSets

Rolling updates, scaling, undoing changes

Commands: kubectl rollout, kubectl scale

[ ] Day 17–18:[ ] Module: Jobs & CronJobs

Create & schedule jobs

Clean up pods

[ ] Day 19–20:[ ] Module: Taints, Tolerations, NodeSelectors

Practice scheduling rules

[ ] Day 21:[ ] Module: Logs & Debugging

Practice: kubectl logs, kubectl exec, kubectl describe

Killer Shell Modules: Apiserver Crash, Apiserver Misconfigured, Kubelet Misconfigured, Kube Controller Manager Misconfigured

---


### WEEK 4: RBAC, NetworkPolicy, Review

Goal: Master RBAC, NetworkPolicies; reinforce weak areas

[ ] Day 22–23:[ ] Review & Practice Killer Shell Labs:

RBAC ServiceAccount Permissions, RBAC User Permissions

[ ] Day 24–25:[ ] NetworkPolicy:

Practice: NetworkPolicy Namespace Selector, NetworkPolicy Misconfigured

[ ] Day 26–27:[ ] Scheduling Review

Killer Shell Modules: Scheduling Priority, Pod Affinity, Pod Anti Affinity

[ ] Day 28–29:[ ] YAML speed drills, exam technique

Review: resource limits, probes, jobs, services

[ ] Day 30:[ ] Mock Exam 1

Simulate full exam experience

---


### WEEK 5: Cluster Operations

Goal: Understand node management, static pods, and kubeadm tasks

[ ] Day 31–33:[ ] Cluster Operations

Killer Shell Modules: Cluster Node Join, Static Pod move

[ ] Day 34–36:[ ] Certificates and Cluster Setup

Killer Shell Modules: Cluster Certificate Management, Cluster Setup

[ ] Day 37–38:[ ] Cluster Upgrade

Killer Shell Module: Cluster Upgrade

---


### WEEK 6: Full Lab Practice + Weak Areas

Goal: Address all weak areas and build exam confidence

[ ] Day 39–41:[ ] Deep Dive on Weak Topics (based on Week 1–5 performance)

[ ] Day 42–43:[ ] Full Practice: YAML creation, imperative commands, cert troubleshooting

---


### WEEK 7: Mock Exams & Recovery

Goal: Test readiness and optimize timing/strategy

[ ] Day 44–46:[ ] Killer.sh Practice Exam 2 (timed)

Post-exam review of incorrect answers

[ ] Day 47–48:[ ] Focused labs: Misconfigurations, RBAC, Taints, Static Pods

---


### WEEK 8: Final Review

Goal: Light review and rest

[ ] Day 49–50:[ ] YAML & Cheat Sheet Refresher

Flashcards, resource types, config syntax

[ ] Day 51–52:[ ] Light Lab Practice (optional)

[ ] Day 53–54:✅ Rest and mental prep for exam


### Optional Resources

Kubernetes Official Docs: https://kubernetes.io/docs

Killer.sh CKA Cheatsheet: https://killer.sh/cka/cheatsheet/