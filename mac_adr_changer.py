#!/usr/bin/env python

import subprocess
import optparse

#08:00:27:5b:b1:a6
# interface = "eth0"
# new_mac = "02:a0:04:d3:00:11"

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="The new MAC address")
(options, arguments) = parser.parse_args()

# interface = input("Enter the interface to change:")
# new_mac = input("Enter the new mac address:")

interface = options.interface
new_mac = options.new_mac

print("[+] Changing mac address for " + interface + " to " + new_mac)
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

