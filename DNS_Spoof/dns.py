#!/usr/bin/env python 
#iptables -I FORWARD -j NFQUEUE --queue-num 1
#iptables -I INPUT -d 192.168.0.0/24 -j NFQUEUE --queue-num 1
#iptables --flush   -F [chain]          Delete all rules in  chain or all chains
#iptables -I INPUT -j NFQUEUE --queue-num 1
#iptables -I OUTPUT -J NFQUEUE --queue-num 1
#pip install netfilterqueue
import netfilterqueue

def process_packet(packet):
    print(packet)
    packet.accept()	#drop = is not load web

queue = netfilterqueue.NetfilterQueue()
queue.bind(1, process_packet)
try:
    queue.run()
except KeyboardInterrupt:

    print('exiting .....')

queue.run()