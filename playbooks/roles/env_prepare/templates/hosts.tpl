127.0.0.1   localhost
{% for host in groups['all'] %}
{{ hostvars[host]['ansible_ssh_host'] }}    {{ hostvars[host]['inventory_hostname'] }}
{% endfor %}
