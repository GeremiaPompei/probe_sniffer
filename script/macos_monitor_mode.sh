#!/bin/bash

NET_INTERFACE_NAME=$1

airport='/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport'

$airport -z                              # to disconnect from current wifi connections
$airport $NET_INTERFACE_NAME sniff 11    # to enable the monitor mode