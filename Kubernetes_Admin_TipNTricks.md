# 🚀 Kubernetes Administration Tips and Tricks  
📍 Source: [techopsexamples.com](https://techopsexamples.com)

---

## 🧰 Kubectl Aliases
- Automate frequent checks with aliases.
- Use `--field-selector` and `-o jsonpath` to drill down quickly.

## 🔒 Avoid cluster-admin in prod
- Replace `cluster-admin` with scoped Role and RoleBinding.
- Periodically audit all bindings for over-permissioned accounts.

## 📏 Always define resource limits
- Add CPU and memory limits to every pod spec to avoid noisy neighbors.
- Reject unbounded pods using `LimitRanges` and `ResourceQuotas`.

## 🧹 Drain nodes before maintenance
- Use `kubectl cordon` and `kubectl drain` before rebooting nodes.
- Add PDBs to critical workloads to avoid full eviction.

## 🧭 Use namespaces per env.
- Use dev, staging, and prod namespaces, not folders or tags.
- Apply `NetworkPolicies` and limit cross-namespace communication.

## 🏷️ Tag nodes with labels for scheduling
- Use `app`, `tier`, `env` labels for all Kubernetes objects.
- Query resources and build selectors using consistent labels.

## ❤️‍🩹 Use readiness and liveness probes
- Don’t expose broken apps. Configure probes so only healthy pods receive traffic.

## 🌀 Rollback deployments safely
- Use `kubectl rollout undo` if a new version fails.
- Always monitor rollout status before declaring success.

## 🚫 Avoid :latest image tags
- Pin image versions instead of relying on `:latest`.
- Ensures consistent rollouts and prevents unexpected changes.

## 🔐 Use ConfigMaps and Secrets as readonly
- Mount as volumes or inject via environment variables.
- Mark Secrets as `readOnly: true` and enable encryption at rest.

## 🔒 Restrict inter-pod traffic
- Define `NetworkPolicies` to block all by default.
- Whitelist only required ports and pod selectors.

## ⚖️ Use taints and tolerations wisely
- Taint special nodes and allow only required pods to tolerate.
- Prevent general workloads from scheduling on reserved nodes.

## 🔁 Rotate Secrets and tokens
- Set short TTLs for tokens and automate secret regeneration.
- Avoid static credentials embedded in container images.

## 🧍‍♂️ Run containers as non-root
- Use `runAsNonRoot` and drop Linux capabilities in specs.
- Set `readOnlyRootFilesystem: true` for better hardening.

## 👤 Use ServiceAccounts per workload
- Create dedicated `ServiceAccounts` with scoped permissions.
- Avoid using the default `ServiceAccount` in any namespace.

## 📂 Centralize logs for all pods
- Use a lightweight log shipper to send logs to a searchable backend.
- Index by namespace, pod, and container for easy debugging.

## 🛑 PodDisruptionBudgets for HA
- Set `minAvailable` or `maxUnavailable` in PDB specs.
- Protect critical pods during voluntary evictions and upgrades.

## 💾 Back up etcd regularly
- Schedule `etcdctl snapshot save` and sync to object storage.
- Validate snapshot integrity before cluster upgrades.

## 🧹 Regularly clean up unused resources
- Delete old ReplicaSets, Jobs, and failed pods using lifecycle policies.
- Use tools like `kubeclean` to keep the cluster tidy.

## 🔐 Use session-based access over SSH
- Enable agent-based or API-driven session tools for platform.
- Disable SSH on nodes and eliminate static credential management entirely.
