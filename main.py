#!/bin/python3
import pandas as pd
import subprocess
import numpy as np
from rich import print


def get_host():
    subprocess.call("./scanner.sh", shell=True)


def print_result(path):
    res = pd.read_table(path, delimiter="\t", header=None, names=["IP", "MAC", "NAME"])
    return res


def save_valid_mac():
    with open("white_list/list.txt", "r") as f1:
        stored_mac = f1.read().strip().split()
    file = open("white_list/list.txt", "a")
    res = print_result("result/arp-scan.txt")
    valid_mac = np.array(res["MAC"].unique())
    if len(valid_mac) == 0:
        print("[red bold]Pls run the scan command[/red bold]")
    else:
        for val in valid_mac:
            if val not in stored_mac:
                file.write(f"{val}\n")


def compare_mac():
    subprocess.call("./check-scanner.sh", shell=True)
    invalid_mac = []
    s_in = open("store/txt/file.txt", "a")
    with open("white_list/list.txt", "r") as f1:
        f2 = f1.read().strip().split()
    res = print_result("result/arp-scan.txt")
    mac = np.array(res["MAC"].unique())
    for i in mac:
        if i not in f2:
            invalid_mac.append(i)
            s_in.write(f"{i}\n")
    return len(invalid_mac)


def deauth():
    subprocess.call("./deauth.sh", shell=True)
