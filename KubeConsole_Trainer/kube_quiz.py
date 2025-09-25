# kube_quiz.py
import random

# Question bank (Free-form answers) - ordered from easiest to hardest with supplemental scenario-based tasks
questions = [
    # === Easy: Basic kubectl commands ===
    {
        "question": "List all pods in ps output format",
        "answer": "kubectl get pods"
    },
    {
        "question": "List all pods in ps output format with more information (such as node name)",
        "answer": "kubectl get pods -o wide"
    },
    {
        "question": "List all Kubernetes services",
        "answer": "kubectl get services"
    },
    {
        "question": "List all deployments in JSON output format, in the 'v1' version of the 'apps' API group",
        "answer": "kubectl get deployments.v1.apps -o json"
    },
    {
        "question": "List the pods in the kube-system namespace with their IP addresses",
        "answer": "kubectl get pods -n kube-system -o wide"
    },

    # === Moderate: Logs, configs, debugging ===
    {
        "question": "View the logs for the API server",
        "answer": "kubectl logs -n kube-system <APISERVER_POD>"
    },
    {
        "question": "Describe a pod named 'nginx-pod' to view running containers",
        "answer": "kubectl describe pod nginx-pod"
    },
    {
        "question": "Describe a node named 'worker-node-1' to check memory, CPU, and health status",
        "answer": "kubectl describe node worker-node-1"
    },
    {
        "question": "Get the number of failed jobs across all namespaces",
        "answer": "kubectl get jobs --all-namespaces | grep \"failed\""
    },
    {
        "question": "Get the list of CronJobs across all namespaces",
        "answer": "kubectl get cronjobs --all-namespaces"
    },

    # === Advanced: Troubleshooting scenarios ===
    {
        "question": "Create a ConfigMap and mount it in a pod",
        "answer": "kubectl create configmap <NAME> --from-literal=key=value && kubectl run <POD> --image=nginx --dry-run=client -o yaml > pod.yaml"
    },
    {
        "question": "Check Kubelet service status on the node",
        "answer": "systemctl status kubelet"
    },
    {
        "question": "Join a node to the cluster using kubeadm",
        "answer": "kubeadm join <MASTER_IP>:6443 --token <TOKEN> --discovery-token-ca-cert-hash sha256:<HASH>"
    },
    {
        "question": "Backup etcd cluster manually",
        "answer": "ETCDCTL_API=3 etcdctl snapshot save snapshot.db --endpoints=https://127.0.0.1:2379 --cacert=<CA> --cert=<CERT> --key=<KEY>"
    },
    {
        "question": "Move a static pod to another node",
        "answer": "mv /etc/kubernetes/manifests/<POD>.yaml <NEW_NODE>:<PATH>"
    },

    # === Cluster Operations ===
    {
        "question": "Upgrade the control plane components with kubeadm",
        "answer": "kubeadm upgrade apply v1.27.0"
    },
    {
        "question": "Modify the cluster DNS IP settings",
        "answer": "Edit /etc/cni/net.d/* or kube-dns deployment and restart networking"
    },

    # === Scheduling ===
    {
        "question": "Apply a node affinity rule to a pod",
        "answer": "spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution"
    },
    {
        "question": "Apply a toleration to a pod YAML",
        "answer": "spec.tolerations"
    },

    # === Networking ===
    {
        "question": "Create a NetworkPolicy to allow traffic between two namespaces",
        "answer": "kubectl apply -f <networkpolicy>.yaml"
    },
    {
        "question": "Create an Ingress to route to an existing deployment",
        "answer": "kubectl apply -f ingress.yaml"
    },

    # === RBAC ===
    {
        "question": "Create a role and role binding to allow a user to list pods",
        "answer": "kubectl create role pod-reader --verb=get,list --resource=pods && kubectl create rolebinding read-pods --role=pod-reader --user=<USER>"
    },
    {
        "question": "Create a cluster role binding for a service account",
        "answer": "kubectl create clusterrolebinding sa-viewer --clusterrole=view --serviceaccount=default:my-sa"
    },

    # === Added: Full CKA 30 Questions with Solutions (Concise) ===
    { "question": "Deploy a pod 'nginxpod' on the controlplane node", "answer": "kubectl run nginxpod --image=nginx --dry-run=client -o yaml > pod.yaml && edit nodeName: controlplane && kubectl apply -f pod.yaml" },
    { "question": "Expose pod 'nginxpod' as ClusterIP service 'nginxsvc' on port 80", "answer": "kubectl expose pod nginxpod --name=nginxsvc --port=80" },
    { "question": "Expose pod 'nginxpod' as NodePort service 'nginxnodeportsvc' with NodePort 30200", "answer": "kubectl expose pod nginxpod --name=nginxnodeportsvc --port=80 --type=NodePort && kubectl edit svc nginxnodeportsvc" },
    { "question": "Create a Deployment 'nginx-deploy' with 3 replicas and scale to 5", "answer": "kubectl create deployment nginx-deploy --image=nginx --replicas=3 && kubectl scale deployment nginx-deploy --replicas=5" },
    { "question": "Create a DaemonSet running nginx on all nodes", "answer": "kubectl create daemonset nginx-ds --image=nginx -n kube-system" },
    { "question": "Create a static pod 'nginx-static'", "answer": "Place manifest in /etc/kubernetes/manifests/nginx-static.yaml" },
    { "question": "Create a ConfigMap 'app-config' with APP_MODE=prod", "answer": "kubectl create configmap app-config --from-literal=APP_MODE=prod" },
    { "question": "Create a Secret 'db-secret' with DB_PASS=admin123", "answer": "kubectl create secret generic db-secret --from-literal=DB_PASS=admin123" },
    { "question": "Create a PersistentVolume 'pv-demo' with 1Gi and /mnt/data", "answer": "kubectl apply -f pv.yaml && kubectl apply -f pvc.yaml" },
    { "question": "Use default StorageClass for a dynamic PVC", "answer": "kubectl apply -f pvc-dynamic.yaml" },
    { "question": "Label pod nginxpod tier=frontend and list it", "answer": "kubectl label pod nginxpod tier=frontend && kubectl get pods -l tier=frontend" },
    { "question": "Taint node01 with key=value:NoSchedule and run a tolerating pod", "answer": "kubectl taint node node01 key=value:NoSchedule && edit pod spec to add tolerations" },
    { "question": "Create a pod with nodeAffinity requiring disktype=ssd", "answer": "Add affinity.nodeAffinity in pod spec" },
    { "question": "Create pods with affinity and anti-affinity to role=frontend", "answer": "Add podAffinity and podAntiAffinity in pod spec" },
    { "question": "Deploy a pod with cpu=500m,mem=128Mi requests and cpu=1,mem=256Mi limits", "answer": "Add resources.requests and resources.limits in pod spec" },
    { "question": "Autoscale 'nginx-deploy' with CPU target 80%, min=1, max=5", "answer": "kubectl autoscale deployment nginx-deploy --cpu-percent=80 --min=1 --max=5" },
    { "question": "Create a NetworkPolicy to allow frontend → db only", "answer": "kubectl apply -f netpol.yaml" },
    { "question": "Create an Ingress with paths /app1 → svc1 and /app2 → svc2", "answer": "kubectl apply -f ingress.yaml" },
    { "question": "Verify DNS resolution of service 'nginxsvc'", "answer": "kubectl run test --image=busybox --rm -it -- nslookup nginxsvc" },
    { "question": "Deploy a pod with an initContainer and nginx main container", "answer": "Define initContainers and containers in pod spec" },
    { "question": "Create a ServiceAccount 'app-sa' and run a pod with it", "answer": "kubectl create serviceaccount app-sa && edit pod spec with serviceAccountName: app-sa" },
    { "question": "Create a Role allowing get/list pods in namespace dev and bind to app-sa", "answer": "kubectl apply -f role.yaml && kubectl apply -f rolebinding.yaml" },
    { "question": "Create a ClusterRole allowing list nodes and bind to app-sa", "answer": "kubectl apply -f clusterrole.yaml && kubectl apply -f clusterrolebinding.yaml" },
    { "question": "Enable NodeRestriction admission controller", "answer": "Edit /etc/kubernetes/manifests/kube-apiserver.yaml and add --enable-admission-plugins=NodeRestriction" },
    { "question": "Run a pod with runAsUser=1000 and NET_ADMIN capability", "answer": "Add securityContext with runAsUser and capabilities in pod spec" },
    { "question": "View logs of pod nginxpod (and sidecar if present)", "answer": "kubectl logs nginxpod && kubectl logs nginxpod -c sidecar" },
    { "question": "Debug nginxpod with describe and exec", "answer": "kubectl describe pod nginxpod && kubectl exec -it nginxpod -- curl localhost" },
    { "question": "Backup etcd to snapshot.db and restore it", "answer": "ETCDCTL_API=3 etcdctl snapshot save snapshot.db && ETCDCTL_API=3 etcdctl snapshot restore snapshot.db" },
    { "question": "Upgrade cluster to v1.27.0", "answer": "kubeadm upgrade plan && kubeadm upgrade apply v1.27.0" },
    { "question": "Locate and edit kube-apiserver manifest", "answer": "Edit /etc/kubernetes/manifests/kube-apiserver.yaml" }
]

def run_quiz():
    score = 0
    total = len(questions)
    passing_score = 0.7  # 70% required to pass
    wrong_answers = []
    random.shuffle(questions)

    print("\n📘 Kubernetes Command Quiz - Freeform Edition 📘")
    print("Type the exact kubectl command and press Enter. Answers must match exactly.")
    print("Type 'help' to reveal the correct answer and try again (no penalty).\n")
    print(f"📝 Total Questions: {total}")
    print(f"✅ Passing Score: {int(passing_score * 100)}% ({int(total * passing_score)} correct answers required)\n")

    for i, q in enumerate(questions, 1):
        while True:
            print(f"Q{i}: {q['question']}")
            user_answer = input("Your answer: ").strip()

            if user_answer.lower() == "help":
                print(f"💡 Correct command: {q['answer']}")
                continue  # Allow retry without penalty

            if user_answer == q['answer']:
                print("✅ Correct!")
                score += 1
            else:
                print("❌ Incorrect.")
                wrong_answers.append({
                    "question": q['question'],
                    "your_answer": user_answer,
                    "correct_answer": q['answer']
                })
            print(f"✔ Correct answer: {q['answer']}\n")
            break

    print("\n📊 Quiz Complete!")
    print(f"Your Score: {score} / {total} ({int((score/total)*100)}%)")

    if score / total >= passing_score:
        print("🎉 Result: PASSED")
    else:
        print("❌ Result: FAILED")

    if wrong_answers:
        print("\n❌ Questions you got wrong:")
        for idx, wrong in enumerate(wrong_answers, 1):
            print(f"\n{idx}. {wrong['question']}")
            print(f"   Your answer:    {wrong['your_answer']}")
            print(f"   Correct answer: {wrong['correct_answer']}")
    else:
        print("🎯 Perfect score! Well done!")

if __name__ == "__main__":
    run_quiz()
