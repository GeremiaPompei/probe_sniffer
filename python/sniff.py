import os
from pathlib import Path
from sys import argv
from scapy.all import *
from datetime import datetime

def printer(time, rssi, src_mac, ap_mac):
    print(f'time: {time}', f'rssi: {rssi:2}dBm', f'src: {src_mac}', f'ap: {ap_mac}', sep='\t')

def file_writer(fp):
    def callback(time, rssi, src_mac, ap_mac):
        fp.write(f'{time},{rssi},{src_mac},{ap_mac}\n')
        fp.flush()
    return callback

def prn(callbacks=[]):
    def handler(p):
        if not (p.haslayer(Dot11ProbeReq)):
            return
        time = datetime.fromtimestamp(p.time)
        rssi = p[RadioTap].dBm_AntSignal
        src_mac = p[Dot11].addr2
        ap_mac = p[Dot11].addr2
        for callback in callbacks:
            callback(time, rssi, src_mac, ap_mac)
    return handler

def main():
    if len(argv) <= 1:
        addrs = socket.if_nameindex()
        print(f'{len(addrs)} nets')
        for k, v in addrs:
            print(f' > {k}: {v}')
    else:
        iface = argv[1]
        now = datetime.now().strftime('%Y%m%d_%H%M%S')
        dir = Path('scan')
        if not dir.exists():
            dir.mkdir()
        with open(dir / f'probereq_{now}.csv', 'w') as fp:
            fp.write('time,rssi,src,ap\n')
            sniff(iface=iface, prn=prn(callbacks=[
                printer,
                file_writer(fp=fp)
            ]), monitor=True)

if __name__ == "__main__":
    main()