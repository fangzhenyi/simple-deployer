#!/usr/bin/env python
import sys
import commands
from jinja2 import Environment, PackageLoader

def hostname(ip):
    return 'hadoop' + ip[ip.rindex('.') + 1:]

def username():
    return commands.getoutput('./bin/container-name.sh')

def ip(hostname):
    return commands.getoutput('grep -m 1 ' + hostname + ' /etc/hosts | awk \'{print $1}\'')

if __name__ == "__main__":   
    env = Environment(loader=PackageLoader('templates', '.'))
    template = env.get_template(sys.argv[1])
    print template.render(HOSTNAME_1=username()+'01', HOSTNAME_2=username()+'02', HOSTNAME_3=username()+'03', HOSTNAME_4=username()+'04', HOSTNAME_5=username()+'05', HOSTIP_1=ip(username()+'01'), HOSTIP_2=ip(username()+'02'), HOSTIP_3=ip(username()+'03'), HOSTIP_4=ip(username()+'04'), HOSTIP_5=ip(username()+'05'))
