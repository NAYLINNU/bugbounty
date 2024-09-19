#!usr/bin/env python
import subprocess
import optparse
parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac",  dest="new_mac", help="New MAC address")
(options, arguments) = parser.parse_args()
interface = options.interface
new_mac = options.new_mac
#run command =python mac_changer_with_argument.py --interface wlan0 --mac 00:11:22:33:44:45
print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
