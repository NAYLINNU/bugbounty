#!/usr/bin/env python
import subprocess
import optparse
#interface = "wlan0"
#new_mac = "00:11:22:33:44:88"                      #normal
#print("[+] Changing MAC address for " + interface + " to " + new_mac)
#subprocess.call("ifconfig " + interface + " down ", shell=True)
#subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
#subprocess.call("ifconfig " + interface + " up ", shell=True)

#interface = input("interface> ")                                 #python3
#new_mac = input("new_Mac> ")
#print("[+] Changing MAC address for " + interface + " to " + new_mac)
#subprocess.call("ifconfig " + interface + " down ", shell=True)
#subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
#subprocess.call("ifconfig " + interface + " up ", shell=True)

#interface = raw_input("interface> ")                                 #python2
#new_mac = raw_input("new_Mac> ")
#print("[+] Changing MAC address for " + interface + " to " + new_mac)
#subprocess.call("ifconfig " + interface + " down ", shell=True)
#subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
#subprocess.call("ifconfig " + interface + " up ", shell=True)


parser = optparse.OptionParser()                            #pthon2
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.parse_args()
interface = raw_input("interface> ")
new_mac = raw_input("new_Mac> ")
print("[+] Changing MAC address for " + interface + " to " + new_mac)
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])