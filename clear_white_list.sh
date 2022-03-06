#!/bin/bash

echo "" > "white_list/list.txt"
echo "" > "result/arp-scan.txt"
sudo rm -rfv store/csv/* && sudo rm -rfv _gateway/* && sudo rm -rfv store/txt/* 