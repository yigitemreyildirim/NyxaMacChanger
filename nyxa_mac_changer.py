# you must be root
import subprocess

print("Nyxa Mac Changer is starting")

interface = "eth0"
mac_address = "00:11:22:33:44:55"


subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",mac_address])
subprocess.call(["ifconfig",interface,"up"])

subprocess.call(["ifconfig",interface])


print("Mac Address Changed Successfully")

