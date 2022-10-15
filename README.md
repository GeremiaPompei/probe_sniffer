# Probe request sniffing

*REMEMBER*: disassociate connected wifi before running test with monitor mode.

## Shell

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
./sniff.sh
```
to list local interface that can be used to sniff
```
./sniff.sh NET_INTERFACE_NAME
```
to sniff in monitor mode filtering only the probe requests
```
./sniff.sh NET_INTERFACE_NAME FILENAME.pcapng
```
to sniff in monitor mode filtering only the probe requests and save results in FILENAME.pcapng

## Python script
To install packages
```
pip install -r requirements.txt
```
Commands could be:
```
python sniff.py
```
to list local interface that can be used to sniff
```
sudo python sniff.py NET_INTERFACE_NAME
```
to sniff in promiscuous mode
```
sudo python sniff.py NET_INTERFACE_NAME monitor
```
to sniff in monitor mode
```
sudo python sniff.py NET_INTERFACE_NAME probe
```
to sniff in monitor mode filtering only the probe requests.