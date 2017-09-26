./cluster.sh provision
(cd playbooks; ansible-playbook -i hosts.layout hadoop_apache_HA_deploy.yml)
