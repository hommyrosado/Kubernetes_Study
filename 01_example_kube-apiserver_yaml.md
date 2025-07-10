| Color Code | Used For                                                |
| ---------- | ------------------------------------------------------- |
| 🟦         | YAML Structure (`apiVersion`, `kind`, `metadata`, etc.) |
| 🟩         | APIServer Container Command Flags                       |
| 🟨         | Certificate and TLS Settings                            |
| 🟧         | Probes (Liveness, Readiness, Startup)                   |
| 🟥         | Volumes and Mounts                                      |
| 🟪         | (Unused in this example, reserved for RBAC/advanced)    |
| ⬛          | Other/Infrastructure-Specific Settings                  |

---
```yaml

🟦 apiVersion: v1                               # Version of the Kubernetes API
🟦 kind: Pod                                     # Defines the resource type as a Pod
🟦 metadata:
  🟦 annotations:
    🟦 kubeadm.kubernetes.io/kube-apiserver.advertise-address.endpoint: 172.30.1.2:6443  # API server advertise address
  🟦 creationTimestamp: null
  🟦 labels:
    🟦 component: kube-apiserver                 # Label for component
    🟦 tier: control-plane                       # Label indicating control plane component
  🟦 name: kube-apiserver                        # Pod name
  🟦 namespace: kube-system                     # Namespace for system pods
🟦 spec:
  🟦 containers:
  - 🟦 command:
    - 🟩 kube-apiserver                          # Main command to run the API server
    - 🟩 --advertise-address=172.30.1.2          # IP address the API server advertises
    - 🟩 --allow-privileged=true                 # Allows privileged containers
    - 🟩 --authorization-mode=Node,RBAC          # Authorization modes used
    - 🟨 --client-ca-file=/etc/kubernetes/pki/ca.crt               # CA for client cert auth
    - 🟩 --enable-admission-plugins=NodeRestriction              # Admission plugins to enable
    - 🟩 --enable-bootstrap-token-auth=true                      # Allows bootstrap token auth
    - 🟨 --etcd-cafile=/etc/kubernetes/pki/etcd/ca.crt            # CA file to verify etcd
    - 🟨 --etcd-certfile=/etc/kubernetes/pki/apiserver-etcd-client.crt  # Cert for etcd client
    - 🟨 --etcd-keyfile=/etc/kubernetes/pki/apiserver-etcd-client.key   # Key for etcd client
    - 🟩 --etcd-servers=https://127.0.0.1:2379                     # etcd server URL
    - 🟨 --kubelet-client-certificate=/etc/kubernetes/pki/apiserver-kubelet-client.crt  # Cert for kubelet auth
    - 🟨 --kubelet-client-key=/etc/kubernetes/pki/apiserver-kubelet-client.key          # Key for kubelet auth
    - 🟩 --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname  # Order to access kubelets
    - 🟨 --proxy-client-cert-file=/etc/kubernetes/pki/front-proxy-client.crt            # Proxy client cert
    - 🟨 --proxy-client-key-file=/etc/kubernetes/pki/front-proxy-client.key             # Proxy client key
    - 🟩 --requestheader-allowed-names=front-proxy-client                               # Allowed request header names
    - 🟨 --requestheader-client-ca-file=/etc/kubernetes/pki/front-proxy-ca.crt          # Request header CA
    - 🟩 --requestheader-extra-headers-prefix=X-Remote-Extra-                          # Extra headers prefix
    - 🟩 --requestheader-group-headers=X-Remote-Group                                  # Group headers
    - 🟩 --requestheader-username-headers=X-Remote-User                                # Username headers
    - 🟩 --secure-port=6443                        # Secure port for API server
    - 🟩 --service-account-issuer=https://kubernetes.default.svc.cluster.local         # SA token issuer
    - 🟨 --service-account-key-file=/etc/kubernetes/pki/sa.pub                         # Public key for SA tokens
    - 🟨 --service-account-signing-key-file=/etc/kubernetes/pki/sa.key                 # Signing key for SA tokens
    - 🟩 --service-cluster-ip-range=10.96.0.0/12                                        # Cluster IP range for services
    - 🟨 --tls-cert-file=/etc/kubernetes/pki/apiserver.crt                             # TLS cert for API server
    - 🟨 --tls-private-key-file=/etc/kubernetes/pki/apiserver.key                      # TLS key for API server
    🟦 image: registry.k8s.io/kube-apiserver:v1.32.1      # Image for the API server
    🟦 imagePullPolicy: IfNotPresent                      # Pull image if not present
    🟧 livenessProbe:
      🟧 failureThreshold: 8
      🟧 httpGet:
        🟧 host: 172.30.1.2
        🟧 path: /livez
        🟧 port: 6443
        🟧 scheme: HTTPS
      🟧 initialDelaySeconds: 10
      🟧 periodSeconds: 10
      🟧 timeoutSeconds: 15
    🟦 name: kube-apiserver
    🟧 readinessProbe:
      🟧 failureThreshold: 3
      🟧 httpGet:
        🟧 host: 172.30.1.2
        🟧 path: /readyz
        🟧 port: 6443
        🟧 scheme: HTTPS
      🟧 periodSeconds: 1
      🟧 timeoutSeconds: 15
    🟦 resources:
      🟦 requests:
        🟦 cpu: 50m
    🟧 startupProbe:
      🟧 failureThreshold: 24
      🟧 httpGet:
        🟧 host: 172.30.1.2
        🟧 path: /livez
        🟧 port: 6443
        🟧 scheme: HTTPS
      🟧 initialDelaySeconds: 10
      🟧 periodSeconds: 10
      🟧 timeoutSeconds: 15
    🟥 volumeMounts:
    - 🟥 mountPath: /etc/ssl/certs
      🟥 name: ca-certs
      🟥 readOnly: true
    - 🟥 mountPath: /etc/ca-certificates
      🟥 name: etc-ca-certificates
      🟥 readOnly: true
    - 🟥 mountPath: /etc/kubernetes/pki
      🟥 name: k8s-certs
      🟥 readOnly: true
    - 🟥 mountPath: /usr/local/share/ca-certificates
      🟥 name: usr-local-share-ca-certificates
      🟥 readOnly: true
    - 🟥 mountPath: /usr/share/ca-certificates
      🟥 name: usr-share-ca-certificates
      🟥 readOnly: true
  ⬛ hostNetwork: true                             # Uses the node network namespace
  ⬛ priority: 2000001000                          # Scheduler priority
  ⬛ priorityClassName: system-node-critical       # High priority class
  ⬛ securityContext:
    ⬛ seccompProfile:
      ⬛ type: RuntimeDefault                      # Uses default seccomp profile
  🟥 volumes:
  - 🟥 hostPath:
      🟥 path: /etc/ssl/certs
      🟥 type: DirectoryOrCreate
    🟥 name: ca-certs
  - 🟥 hostPath:
      🟥 path: /etc/ca-certificates
      🟥 type: DirectoryOrCreate
    🟥 name: etc-ca-certificates
  - 🟥 hostPath:
      🟥 path: /etc/kubernetes/pki
      🟥 type: DirectoryOrCreate
    🟥 name: k8s-certs
  - 🟥 hostPath:
      🟥 path: /usr/local/share/ca-certificates
      🟥 type: DirectoryOrCreate
    🟥 name: usr-local-share-ca-certificates
  - 🟥 hostPath:
      🟥 path: /usr/share/ca-certificates
      🟥 type: DirectoryOrCreate
    🟥 name: usr-share-ca-certificates
🟦 status: {}

```
