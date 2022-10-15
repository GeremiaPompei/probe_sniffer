#!/bin/bash

if [ $# -eq 0 ]
then
    echo "Should be supplied netwok name (e.g. en0, wlan0, ...)"
    echo "The list of net cards is the following:"
    ifconfig | expand | cut -c1-8 | sort | uniq -u | awk -F: ' {print $1;}'
else
    NET_INTERFACE_NAME=$1
    sudo ifconfig $NET_INTERFACE_NAME down                                                  # to switch-down wifi (to disassociate it from connected network)
    sudo ifconfig $NET_INTERFACE_NAME up                                                    # to switch-on wifi (to disassociate it from connected network)
    if [ $# -eq 1 ]
    then
        sudo tcpdump -Ini $NET_INTERFACE_NAME -e -s 256 type mgt subtype probe-req           # to sniff using tcpdump
    else
        sudo tcpdump -Ini $NET_INTERFACE_NAME -e -s 256 type mgt subtype probe-req -w $2     # to sniff using tcpdump
    fi
fi