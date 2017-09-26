#!/usr/bin/env python
import sys
from jinja2 import Environment, PackageLoader

def parse_ip_range(ip_range):
    splits = ip_range.split('-')

    ip_prefix = splits[0][:splits[0].rindex('.')]
    start_index = int(splits[0][splits[0].rindex('.') + 1:])
    end_index = int(splits[1])

    for i in range(start_index, end_index + 1):
        ip = ip_prefix + '.' + str(i)
        ips.append((hostname(ip), ip))

def parse_ip_addrs(ip_addrs):
    splits = ip_addrs.split(',')
    
    for split in splits[:]:
        if split.find('-') != -1:
            parse_ip_range(split)
        else:
            ips.append((hostname(split), split))

def hostname(ip):
    return 'hadoop' + ip[ip.rindex('.') + 1:]

if __name__ == "__main__":
    ips = []
    
    parse_ip_addrs(sys.stdin.readlines()[0])

    env = Environment(loader=PackageLoader('templates', '.'))
    template = env.get_template(sys.argv[1])
    print template.render(HOSTNAME_1=ips[0][0], HOSTNAME_2=ips[1][0], HOSTNAME_3=ips[2][0], 
    HOSTIP_1=ips[0][1], HOSTIP_2=ips[1][1], HOSTIP_3=ips[2][1])
