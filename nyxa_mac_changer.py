# you must be root
import subprocess
import optparse

def getUserInput():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", default="eth0",help="Interface to change mac address")
    parse_object.add_option("-m", "--mac", dest="mac_address", default="00:11:22:33:33:55", help="new mac address")
    return parse_object.parse_args()

def changeMacAddress(user_interface,user_mac_address):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
    subprocess.call(["ifconfig",user_interface,"up"])
    subprocess.call(["clear"])

print("Nyxa Mac Changer Started")

(user_input,arguments) = getUserInput()
changeMacAddress(user_input.interface,user_input.mac_address)

print("Mac Address Changed Successfully")
print(f"Interface of the changed MAC address: ")
print(f"Changed mac address: ")




