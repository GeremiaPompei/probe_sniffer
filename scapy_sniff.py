from sys import argv
from scapy.all import *

def handler(p):
    if not (p.haslayer(Dot11ProbeReq)):
        return
    rssi = p[RadioTap].dBm_AntSignal
    src_mac = p[Dot11].addr2
    ap_mac = p[Dot11].addr2
    info = f"rssi={rssi:2}dBm, src={src_mac}, ap={ap_mac}"
    if p.haslayer(Dot11ProbeReq):
        print(f"[ProbReq ] {info}")

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        addrs = socket.if_nameindex()
        print(f'{len(addrs)} nets')
        for k, v in addrs:
            print(f' > {k}: {v}')
    else:
        sniff(iface=argv[1], prn=handler, monitor=True)