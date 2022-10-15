import os
import sys
import socket

def main():
    if len(sys.argv) <= 1:
        addrs = socket.if_nameindex()
        print(f'{len(addrs)} nets')
        for k, v in addrs:
            print(f' > {k}: {v}')
    else:
        dev = sys.argv[1]
        print(f' > net: {dev}')
        save_wireshark = '-w wireshark.pcapng'
        os.system(f'sudo ifconfig {dev} down')
        os.system(f'sudo ifconfig {dev} up;')
        cmd = f'sudo tcpdump -v -i {dev} {save_wireshark}'
        if len(sys.argv) > 2:
            mode = sys.argv[2]
            if 'monitor' == mode:
                print(f' > mode: MONITOR')
                cmd = f'sudo tcpdump -v -Ini {dev} {save_wireshark}'
            if 'probe' == mode:
                print(f' > mode: PROBE')
                cmd = f'sudo tcpdump -v -Ini {dev} -e -s 256 type mgt subtype probe-req {save_wireshark}'
        print(f' > cmd: {cmd}')
        os.system(cmd)
                    
if __name__ == "__main__":
    main()