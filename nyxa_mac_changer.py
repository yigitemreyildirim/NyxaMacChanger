# you must be root
import subprocess
import optparse

print("Nyxa Mac Changer Started")

parse_object = optparse.OptionParser()

parse_object.add_option("-i","--interface",dest="interface",default="eth0",help="Interface to change mac address")
parse_object.add_option("-m","--mac",dest="mac_address",default="eth0",help="new mac address")

(user_input,arguments) = parse_object.parse_args()

user_interface = user_input.interface
user_mac_address = user_input.mac_address

interface = "eth0"
mac_address = "00:11:22:33:44:55"

subprocess.call(["ifconfig",user_interface,"down"])
subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
subprocess.call(["ifconfig",user_interface,"up"])

subprocess.call(["clear"])
print(user_interface)
print(user_mac_address)


print("Mac Address Changed Successfully")

