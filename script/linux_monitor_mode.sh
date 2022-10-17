#!/bin/bash

NET_INTERFACE_NAME=$1

sudo ifconfig $NET_INTERFACE_NAME down          # to switch-down wifi (to disassociate it from connected network)
sudo iwconfig $NET_INTERFACE_NAME mode monitor  # to switch net card in monitor mode
sudo ifconfig $NET_INTERFACE_NAME up            # to switch-on wifi (to disassociate it from connected network)