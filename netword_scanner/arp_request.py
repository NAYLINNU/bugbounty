#!/usr/bin/env python
#import scapy.all as scapy
#def scan(ip):
#    arp_request = scapy.ARP()
#    arp_request.pdst=ip
#    print(arp_request.summary())
#    scapy.ls(scapy.ARP())
#scan("192.168.30.172/24")

import scapy.all as scapy
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    print(arp_request.summary())
scan("192.168.30.172/24")
