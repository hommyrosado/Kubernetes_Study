
# How to Learn Kubernetes

// This guide breaks down Kubernetes concepts into focused learning areas for better understanding and mastery.

## Core Objects
// Core Kubernetes resources used to define workloads and their configuration.

- Pods                       // Smallest deployable unit in Kubernetes; wraps one or more containers
- ReplicaSets               // Ensures a specified number of pod replicas are running at all times
- Deployments               // Declarative updates for ReplicaSets and Pods
- StatefulSets              // Manages stateful applications with stable IDs and storage
- Services                  // Exposes a set of pods as a network service
- Ingress                   // Manages external access to services (usually HTTP/S)
- ConfigMaps                // External configuration storage for application settings
- Secrets                   // Stores sensitive data like passwords and API keys
- PersistentVolume Claims (PVCs)  // Requests storage resources from PersistentVolumes
- Jobs                      // Creates one-off batch tasks
- DaemonSets                // Ensures a copy of a pod runs on all (or selected) nodes

## Architecture Components
// Core components that make up the Kubernetes control plane and node agents.

- API Server                // Frontend of the Kubernetes control plane; handles REST operations
- etcd                      // Distributed key-value store for all cluster data
- Scheduler                 // Assigns newly created pods to suitable nodes
- Controller Manager        // Runs controller loops to ensure the desired state
- Kubelet                   // Node agent that runs on each worker node
- Kube Proxy                // Maintains network rules and load balancing on each node
- Cloud Controller Manager  // Integrates with cloud provider APIs

## Controllers
// Control loops that reconcile desired state with current cluster state.

- Deployment Controller     // Manages Deployments and ensures desired ReplicaSets
- ReplicaSet Controller     // Ensures the desired number of replicas for a pod
- StatefulSet Controller    // Ensures ordering and uniqueness for stateful pods
- HPA (Horizontal Pod Autoscaler)  // Automatically scales pods based on CPU/memory usage
- CronJob Controller        // Manages time-based job scheduling
- DaemonSet Controller      // Ensures DaemonSets are running on all necessary nodes
- VPA (Vertical Pod Autoscaler)  // Automatically adjusts pod resource requests/limits

## Extensibility
// Tools and resources to customize and extend Kubernetes.

- CRDs (Custom Resource Definitions) // Define your own resource types
- Operators                 // Automate complex, stateful application management
- Helm Charts              // Package manager for Kubernetes applications
- Kustomize                // Customizes raw YAML without templates
- Admission Controllers    // Intercept requests to validate or mutate Kubernetes objects

## Webhooks
// Dynamic admission controllers that can validate or mutate Kubernetes requests.

- Mutating Webhooks        // Modify incoming requests before storing them
- Validating Webhooks      // Validate requests before they are persisted
- OPA (Open Policy Agent)  // Policy engine for fine-grained control
- Dynamic Admission Controllers // Enable real-time decisions at admission time

## Runtime
// Container runtimes that Kubernetes can interface with to run workloads.

- docker                   // Classic container runtime (being phased out in favor of others)
- containerd               // Lightweight container runtime used by many distributions
- CRI-O                    // Kubernetes-native container runtime for OpenShift and others
- Mirantis Container Runtime (MCR) // Commercial Docker runtime offering from Mirantis

## Security & Policy
// Tools and objects for securing and enforcing policies in your cluster.

- RBAC                     // Role-Based Access Control for API permissions
- Network Policies         // Control traffic flow between pods
- Security Contexts        // Define privilege and access settings for pods/containers
- Service Accounts         // Provide identity to pods for API access
- Pod Security Standards (PSS) // Enforce security controls on pods
- Secrets Encryption       // Encrypt Kubernetes secrets at rest

## Observability
// Tools for monitoring, logging, and metrics collection in Kubernetes.

- Metrics Server           // Exposes CPU and memory usage for pods and nodes
- Liveness & Readiness Probes // Health checks for containers
- Startup Probes           // Specialized probe for slow-starting containers
- Prometheus               // Metrics collection and alerting system
- Grafana                  // Dashboard tool for visualizing metrics
- OpenTelemetry            // Standard for collecting traces, metrics, and logs


![How to Learn Kubernetes](/images/How_to_Learn_Kubernetes.gif)