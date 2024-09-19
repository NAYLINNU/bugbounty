
#!/usr/bin/env python
import scapy.all as scapy
packet = scapy.ARP(op=2, pdst="192.168.223.72", hwdst="08:00:27:67:0c:a6", psrc="192.168.223.115")
print(packet.show())
print(packet.summary())