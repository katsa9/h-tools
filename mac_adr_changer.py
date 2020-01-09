#!/usr/bin/env python

import subprocess

#08:00:27:5b:b1:a6
# interface = "eth0"
# new_mac = "02:a0:04:d3:00:11"

interface = input("Enter the interface to change:")
new_mac = input("Enter the new mac address:")

print("[+] Changing mac address for " + interface + " to " + new_mac)
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

