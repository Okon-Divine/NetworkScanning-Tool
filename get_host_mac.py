#!/bin/python3

import pandas as pd
import numpy as np


def read_data(path):
    df = pd.read_csv(path)
    return df


def get_mac_vals(df):
    file = open("store/txt/current.txt", "a")
    with open("white_list/list.txt", "r") as valid_mac:
        read_vm = valid_mac.read().strip().split("\n")
    mac_value = np.array(df["BSSID"][2:])
    for mac in mac_value:
        lmac = mac.lower()
        if lmac not in read_vm:
            file.write(f"{mac}\n")


data = read_data("store/csv/mac-01.csv")
get_mac_vals(data)
