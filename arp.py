import socket
import uuid

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Does not actually establish a connection; used to find the routing interface
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = "127.0.0.1"
    finally:
        s.close()
    return local_ip

def get_mac():
    mac_num = uuid.getnode()

    mac_address = ':'.join(['{:02x}'.format((mac_num >> i) & 0xff) for i in range(0, 8*6, 8)][::-1])

    return mac_address

def arp_reply(ip, mac, target_ip, target_mac):
    # first the Eth header which is Dest Mac + Src Mac + 0x0806 for arp protocol
    eth = bytes.fromhex(target_mac) + bytes.fromhex(mac) + bytes.fromhex("08 06")

    # next we need the actual payload which is:
    # hardware type 0x0001 for ethernet 1
    # protocol type ipv4 0x0800
    # Hardware Length 06
    # Protocol Length 04
    # Src Mac + Src Ip + Target Mac + Target Ip
    arp = (
        bytes.fromhex("00 01") +
        bytes.fromhex("08 00") +
        bytes.fromhex("06 04") +
        bytes.fromhex(mac) +
        bytes.fromhex(ip) +
        bytes.fromhex(target_mac) +
        bytes.fromhex(target_ip)
    )

    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)