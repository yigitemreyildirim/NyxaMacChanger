# you must be root
# python nyxa_mac_changer.py -i eth0 -m 00:22:33:55:11
import subprocess
import optparse

print("Nyxa Mac Changer Started")

parse_object = optparse.OptionParser()

parse_object.add_option("-i","--interface",dest="interface",default="eth0",help="Interface to change mac address")
parse_object.add_option("-m","--mac",dest="mac_address",default="00:11:22:33:33:55",help="new mac address")

(user_input,arguments) = parse_object.parse_args()

user_interface = user_input.interface
user_mac_address = user_input.mac_address

subprocess.call(["ifconfig",user_interface,"down"])
subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
subprocess.call(["ifconfig",user_interface,"up"])

subprocess.call(["clear"])

print("Mac Address Changed Successfully")
print(f"Interface of the changed MAC address: {user_interface}")
print(f"Changed mac address: {user_mac_address}")
