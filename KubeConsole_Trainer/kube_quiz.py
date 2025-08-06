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
{
        "question": "Display all nodes in the cluster",
        "answer": "kubectl get nodes"
    },
    {
        "question": "Write logs of container nginx in deployment 'collect-data' in namespace 'management' to /root/logs.log",
        "answer": "kubectl logs -n management deploy/collect-data -c nginx >> /root/logs.log"
    },
    {
        "question": "Write logs of container httpd in deployment 'collect-data' in namespace 'management' to /root/logs.log",
        "answer": "kubectl logs -n management deploy/collect-data -c httpd >> /root/logs.log"
    },
    {
        "question": "Create a pod manifest using dry-run and save to 1.yaml",
        "answer": "kubectl run nginxpod --image=nginx --dry-run=client -o yaml >1.yaml"
    },
    {
        "question": "Create a pod from the manifest file 1.yaml",
        "answer": "kubectl apply -f 1.yaml"
    },
    {
        "question": "Schedule pod defined in 1.yaml to controlplane node",
        "answer": "Edit 1.yaml to add: nodeName: controlplane, then apply with kubectl apply -f 1.yaml"
    },
    {
        "question": "Expose pod 'nginxpod' as service 'nginxsvc' on port 80",
        "answer": "kubectl expose pod nginxpod --name=nginxsvc --port=80"
    },
    {
        "question": "Expose pod 'nginxpod' as a NodePort service named 'nginxnodeportsvc' on port 80",
        "answer": "kubectl expose pod nginxpod --name=nginxnodeportsvc --port=80 --type=NodePort"
    },
    {
        "question": "Edit NodePort of service 'nginxnodeportsvc' to use 30200",
        "answer": "kubectl edit svc nginxnodeportsvc"
    },
    {
        "question": "Scale deployment 'frontend' in 'production' namespace to 2 replicas",
        "answer": "kubectl scale deploy frontend --replicas=2 -n production"
    },
    {
        "question": "Change image of deployment 'frontend' in 'production' namespace to nginx:1.25",
        "answer": "kubectl set image deploy frontend nginx=nginx:1.25 -n production"
    },
    {
        "question": "Autoscale deployment 'frontend' in 'production' namespace from 3 to 5 pods at 80%% CPU",
        "answer": "kubectl -n production autoscale deploy frontend --min=3 --max=5 --cpu-percentage=80"
    },
    {
        "question": "Expose deployment 'frontend' in 'production' namespace as a NodePort service named 'frontendsvc'",
        "answer": "kubectl -n production expose deploy frontend --name=frontendsvc --port=80 --type=NodePort"
    },
    {
        "question": "Create a PersistentVolume with 10Gi and path /mnt/data",
        "answer": "kubectl apply -f pv-volume.yaml"
    }
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
