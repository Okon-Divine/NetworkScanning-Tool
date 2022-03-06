#!/bin/bash

interface=$(cat _gateway/IF.txt)

path_arp="/usr/sbin/arp-scan"

[ -f "$path_arp" ] && echo -e "\e[32m\e[1m ..\e[0m" || sudo apt install arp-scan -y
sudo "$path_arp" --localnet -I "$interface" -x > result/arp-scan.txt
echo -e "\e[32m\e[1m Scanning... \e[0m"