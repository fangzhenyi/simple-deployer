export DOCKER_COMPOSE_YML=docker-compose.yml.tpl.ubuntu14.04
export HOSTS_LAYOUT=hosts.layout.tpl.5
export HADOOP_VERSION=${HADOOP_VERSION:-"3.0.0"}
export CONTAINER_NAME=hadoop${HADOOP_VERSION}-
./cluster.sh provision
(cd playbooks; ansible-playbook -i hosts.layout hadoop_apache_federation_deploy.yml --extra-vars "HADOOP_VERSION=${HADOOP_VERSION}")
