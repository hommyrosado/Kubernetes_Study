# 03 Apiserverver Crash

**Part 01: Configure a wrong argument**

The idea here is to misconfigure the Apiserver in different ways, then check possible log locations for errors.

You should be very comfortable with situations where the Apiserver is not coming back up.

Configure the Apiserver manifest with a new argument `--this-is-very-wrong`.

Check if the _Pod_ comes back up and what logs this causes.

Fix the Apiserver again.

Log Locations:

Log locations to check:

- `/var/log/pods`
- `/var/log/containers`
- crictl ps + crictl logs
- docker ps + docker logs (in case when Docker is used)
- kubelet logs: `/var/logs/syslog` or `journalctl`

**Solution**

# always make a backup !

`cp /etc/kubernetes/manifests/kub-apiserver.yaml ~/kube-apiserver.yaml.ori`

# make the change

`vim /etc/kubernetes/manifest/kube-apiserver.yaml`

# wait till container restarts

`watch crictl ps`

# check for apiserver pod

`k -n kubesystem get pod`

**Apiserver is not coming back, we messed up!**

# check pod logs

`cat /var/log/pods/kube-system_kube-apiserver-controlplane_a3a455d471f833137588e71658e739da > 2022-01-26T10:41:12.401641185Z stderr F Error: unknown flag: --this-is-very-wrong`

Now undo the change and continue

# smart people use a backup

`cp ~/kube-apiserver.yaml.ori /etc/kubernetes/manifests/kube-apiserver.yaml`

**Part 02: Misconfigure ETCD connection**

Change the existing Apiserver manifest argument to: `--etcd-servers=this-is-very-wrong` .

Check what the logs say, without using anything in `/var `.

Fix the Apiserver again.

Log Locations:

Log locations to check:

- `/var/log/pods`
- `/var/log/containers`
- crictl ps + crictl logs
- docker ps + docker logs (in case when Docker is used)
- kubelet logs: `/var/logs/syslog` or `journalctl`

# always make a backup !

cp /etc/kubernetes/manifests/kube-apiserver.yaml ~/kube-apiserver.yaml.ori

# make the change

vim /etc/kubernetes/manifests/kube-apiserver.yaml

# wait till container restarts

watch crictl ps

# check for apiserver pod

k -n kube-system get pod
