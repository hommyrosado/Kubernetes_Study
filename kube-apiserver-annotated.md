# Annotated `kube-apiserver.yaml.ori`

### 🔎 Legend of Annotations:

| Symbol | Category Description                                   |
| ------ | ------------------------------------------------------ |
| 🟥     | Control Plane configuration and static Pod metadata    |
| 🟩     | Networking and IP address/port configuration           |
| 🟨     | Authentication and Authorization mechanisms            |
| 🟧     | TLS and certificate-related settings                   |
| 🟪     | Probes: liveness, readiness, and startup health checks |
| ⚙️     | Runtime and OS-level configurations                    |
| 📦     | Volumes and mounted file paths                         |

```yaml
apiVersion: v1
kind: Pod # 🟥 Control Plane - This is a static Pod
metadata:
  annotations:
    kubeadm.kubernetes.io/kube-apiserver.advertise-address.endpoint: 172.30.1.2:6443 # 🟩 Networking - Advertise address
  creationTimestamp: null
  labels:
    component: kube-apiserver # 🟥 Control Plane
    tier: control-plane # 🟥 Control Plane
  name: kube-apiserver # 🟥 Control Plane
  namespace: kube-system # 🟥 Control Plane
spec:
  containers:
    - command:
        - kube-apiserver # 🟥 Control Plane
        - --advertise-address=172.30.1.2 # 🟩 Networking - Cluster IP communication
        - --allow-privileged=true # ⚙️ Runtime - Allow privileged containers
        - --authorization-mode=Node,RBAC # 🟨 AuthN/AuthZ - Node and RBAC authorization
        - --client-ca-file=/etc/kubernetes/pki/ca.crt # 🟨 AuthN/AuthZ - Client cert auth
        - --enable-admission-plugins=NodeRestriction # 🟨 AuthN/AuthZ - Restricts node capabilities
        - --enable-bootstrap-token-auth=true # 🟨 AuthN/AuthZ - Bootstrap tokens for node join
        - --etcd-cafile=/etc/kubernetes/pki/etcd/ca.crt # 🟧 TLS - etcd CA cert
        - --etcd-certfile=/etc/kubernetes/pki/apiserver-etcd-client.crt # 🟧 TLS - etcd client cert
        - --etcd-keyfile=/etc/kubernetes/pki/apiserver-etcd-client.key # 🟧 TLS - etcd client key
        - --etcd-servers=https://127.0.0.1:2379 # 🟩 Networking - Local etcd endpoint
        - --kubelet-client-certificate=/etc/kubernetes/pki/apiserver-kubelet-client.crt # 🟧 TLS - kubelet client cert
        - --kubelet-client-key=/etc/kubernetes/pki/apiserver-kubelet-client.key # 🟧 TLS - kubelet client key
        - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname # 🟩 Networking
        - --proxy-client-cert-file=/etc/kubernetes/pki/front-proxy-client.crt # 🟧 TLS - Aggregator proxy cert
        - --proxy-client-key-file=/etc/kubernetes/pki/front-proxy-client.key # 🟧 TLS - Aggregator proxy key
        - --requestheader-allowed-names=front-proxy-client # 🟨 AuthN/AuthZ - Front proxy access
        - --requestheader-client-ca-file=/etc/kubernetes/pki/front-proxy-ca.crt # 🟧 TLS - CA for proxy
        - --requestheader-extra-headers-prefix=X-Remote-Extra- # 🟨 AuthN/AuthZ
        - --requestheader-group-headers=X-Remote-Group # 🟨 AuthN/AuthZ
        - --requestheader-username-headers=X-Remote-User # 🟨 AuthN/AuthZ
        - --secure-port=6443 # 🟩 Networking - HTTPS port
        - --service-account-issuer=https://kubernetes.default.svc.cluster.local # 🟨 AuthN/AuthZ - Token issuer
        - --service-account-key-file=/etc/kubernetes/pki/sa.pub # 🟧 TLS - Service account public key
        - --service-account-signing-key-file=/etc/kubernetes/pki/sa.key # 🟧 TLS - Signing key
        - --service-cluster-ip-range=10.96.0.0/12 # 🟩 Networking - Service IP range
        - --tls-cert-file=/etc/kubernetes/pki/apiserver.crt # 🟧 TLS - HTTPS cert
        - --tls-private-key-file=/etc/kubernetes/pki/apiserver.key # 🟧 TLS - HTTPS key
      image: registry.k8s.io/kube-apiserver:v1.32.1 # 🟥 Control Plane - API server image
      imagePullPolicy: IfNotPresent # ⚙️ Runtime - Pull only if not present

      livenessProbe: # 🟪 Probes - Check if alive
        failureThreshold: 8
        httpGet:
          host: 172.30.1.2
          path: /livez
          port: 6443
          scheme: HTTPS
        initialDelaySeconds: 10
        periodSeconds: 10
        timeoutSeconds: 15

      name: kube-apiserver # 🟥 Control Plane

      readinessProbe: # 🟪 Probes - Ready for traffic
        failureThreshold: 3
        httpGet:
          host: 172.30.1.2
          path: /readyz
          port: 6443
          scheme: HTTPS
        periodSeconds: 1
        timeoutSeconds: 15

      resources: # ⚙️ Runtime - Resource reservation
        requests:
          cpu: 50m

      startupProbe: # 🟪 Probes - Startup check
        failureThreshold: 24
        httpGet:
          host: 172.30.1.2
          path: /livez
          port: 6443
          scheme: HTTPS
        initialDelaySeconds: 10
        periodSeconds: 10
        timeoutSeconds: 15

      volumeMounts: # 📦 Volumes - Mount certs into container
        - mountPath: /etc/ssl/certs
          name: ca-certs
          readOnly: true
        - mountPath: /etc/ca-certificates
          name: etc-ca-certificates
          readOnly: true
        - mountPath: /etc/kubernetes/pki
          name: k8s-certs
          readOnly: true
        - mountPath: /usr/local/share/ca-certificates
          name: usr-local-share-ca-certificates
          readOnly: true
        - mountPath: /usr/share/ca-certificates
          name: usr-share-ca-certificates
          readOnly: true

  hostNetwork: true # 🟩 Networking - Use host network
  priority: 2000001000 # ⚙️ Runtime - Very high priority
  priorityClassName: system-node-critical # ⚙️ Runtime - Must run
  securityContext: # ⚙️ Runtime - Seccomp settings
    seccompProfile:
      type: RuntimeDefault

  volumes: # 📦 Volumes - Host directories
    - hostPath:
        path: /etc/ssl/certs
        type: DirectoryOrCreate
      name: ca-certs
    - hostPath:
        path: /etc/ca-certificates
        type: DirectoryOrCreate
      name: etc-ca-certificates
    - hostPath:
        path: /etc/kubernetes/pki
        type: DirectoryOrCreate
      name: k8s-certs
    - hostPath:
        path: /usr/local/share/ca-certificates
        type: DirectoryOrCreate
      name: usr-local-share-ca-certificates
    - hostPath:
        path: /usr/share/ca-certificates
        type: DirectoryOrCreate
      name: usr-share-ca-certificates

status: {} # 🟥 Control Plane - Static Pod placeholder
```

---

### 🔎 Legend of Annotations:

| Symbol | Category Description                                   |
| ------ | ------------------------------------------------------ |
| 🟥     | Control Plane configuration and static Pod metadata    |
| 🟩     | Networking and IP address/port configuration           |
| 🟨     | Authentication and Authorization mechanisms            |
| 🟧     | TLS and certificate-related settings                   |
| 🟪     | Probes: liveness, readiness, and startup health checks |
| ⚙️     | Runtime and OS-level configurations                    |
| 📦     | Volumes and mounted file paths                         |
