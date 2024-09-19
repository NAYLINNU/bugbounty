#!usr/bin/env python
import subprocess
import optparse
#run command=python3 mac_changer_using_condition.py -i wlan0 -m 00:11:11:11:11:11
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
        # erro comand = python3 mac_changer_using_condition.py -m 00:11:22:33:44:44
    elif not options.new_mac:
        parser.error("[-] Please specify new mac, use --help for more info")
        # erro comand = python3 mac_changer_using_condition.py -i wlan0 (or) etho
    return options
def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
options = get_arguments()
change_mac(options.interface, options.new_mac)