# 📘 Understanding Kubernetes Logs  
_A Comprehensive Guide_  
👤 @Govardhana Miriyala Kannaiah

---

| **Log Type**           | **Log Path**                                      | **What It Means**                                                                 |
|------------------------|---------------------------------------------------|------------------------------------------------------------------------------------|
| **Container Logs**     | `/var/log/containers/*.log`                       | Container-specific details: exceptions, crashes, misconfigurations                |
| **Pod Logs**           | `/var/log/pods/*.log`                             | Container interactions within a pod, multi-container issues like network problems |
| **Kubelet Logs**       | `/var/log/kubelet.log`                            | Pod lifecycle, resources, communication, scheduling and execution issues          |

## 🔧 Control Plane Logs

| Component                   | Log Path                                          | What It Means                                                                     |
|----------------------------|---------------------------------------------------|------------------------------------------------------------------------------------|
| **API Server Logs**        | `/var/log/kube-apiserver.log`                     | API server operations and client interaction issues                               |
| **Controller Manager Logs**| `/var/log/kube-controller-manager.log`            | Issues with controllers like ReplicaSets or deployments                           |
| **Scheduler Logs**         | `/var/log/kube-scheduler.log`                     | Pod scheduling issues, like resource constraints or affinity rules                |
| **etcd Logs**              | Based on etcd deployment                          | Data consistency or leader election issues with the etcd cluster                  |

---

## 🖥️ Node Logs
| **Log Type**         | **Log Path**              | **What It Means**                                               |
|----------------------|---------------------------|------------------------------------------------------------------|
| **Syslog**           | Based on Linux distro     | Node-related issues, such as hardware failures or resource problems |

---

## 🧾 Application Logs
| **Log Path**         | **What It Means**                                         |
|----------------------|-----------------------------------------------------------|
| `/var/log/app.log`   | App-specific issues like logic errors or slow responses   |

---

## 🧩 Custom Logs
| **Log Path**                | **What It Means**                                      |
|-----------------------------|--------------------------------------------------------|
| `/var/log/custom-app.log`   | Critical use-case-specific issues or events            |
