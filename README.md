# Probe request sniffing

*REMEMBER*: disassociate connected wifi before running test with monitor mode:
- macOS
```
airport -z                              # to disconnect from current wifi connections
airport $NET_INTERFACE_NAME sniff 11    # to enable the monitor mode
```
- linux (*script/linux_monitor_mode.sh*)
```
sudo ifconfig $NET_INTERFACE_NAME down          # switch-off net card
sudo iwconfig $NET_INTERFACE_NAME mode monitor  # switch net card in monitor mode
sudo ifconfig $NET_INTERFACE_NAME up            # switch-on net card
```

## tcpdump

Using terminal tool called **tcpdump** in *sudo* mode.
```
sudo ifconfig $NET_INTERFACE_NAME down     # to switch-down wifi (to disassociate it from connected network)
sudo ifconfig $NET_INTERFACE_NAME up       # to switch-on wifi (to disassociate it from connected network)
sudo tcpdump -Ini $NET_INTERFACE_NAME -e -s 256 type mgt subtype probe-req     # to sniff using tcpdump
```
To save the analysis in a file with wireshark format launch the command with **-w** and the name of the file .pcapng
```
sudo tcpdump -Ini {NET_INTERFACE_NAME} -e -s 256 type mgt subtype probe-req -w {filename}.pcapng
```
There is a script to do this that can be run using the commands:
```
./tcpdump_sniff.sh
```
to list local interface that can be used to sniff
```
./tcpdump_sniff.sh NET_INTERFACE_NAME
```
to sniff in monitor mode filtering only the probe requests
```
./tcpdump_sniff.sh NET_INTERFACE_NAME FILENAME.pcapng
```
to sniff in monitor mode filtering only the probe requests and save results in FILENAME.pcapng

## scapy
Scapy is a library used to debug networks. This provides many ways to analyse packages from inside and outside a target network. Here is implemented a script in python to filter packages related to probe requests.

To install packages
```
sudo pip install -r requirements.txt
```
Commands are:
```
sudo python sniff.py
```
to list local interface that can be used to sniff
``` 
sudo python sniff.py NET_INTERFACE_NAME
```
to sniff probe requests. Remember to enable the monitor mode on selected NET_INTERFACE_NAME.