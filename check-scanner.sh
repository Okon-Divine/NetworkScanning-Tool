#/bin/bash

interface=$(cat _gateway/IF.txt)

sudo arp-scan --localnet -I "$interface" -x > result/arp-scan.txt