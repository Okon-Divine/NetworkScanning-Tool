#!/bin/python3


import pandas as pd
import numpy as np
import sys


def read_data(path):
    df = pd.read_csv(path)
    return df


def get_mac_vals(df):
    mac_value = df["BSSID"][2:]
    return mac_value


def get_channel(df):

    key = []
    values = []
    array_val = []
    bssid = np.array(df["BSSID"])
    channel = np.array(df[" channel"])
    df_bc = dict(zip(bssid, channel))
    for l, n in df_bc.items():
        key.append(l)
        values.append(n)
    for j in key:
        if j == "Station MAC":
            break
        array_val.append(j)
    return array_val


def values_addr(df):
    values = []
    array_vals = []
    bssid = np.array(df["BSSID"])
    channel = np.array(df[" channel"])
    df_bc = dict(zip(bssid, channel))
    for l, n in df_bc.items():
        values.append(n)
    for j in values:
        if j == " Power":
            break
        array_vals.append(j)
    return array_vals


def program_t(array_val, array_vals):
    with open("_gateway/BSSID.txt", "r") as f1:
        f_1 = f1.read().strip()
    file = open("store/txt/file.txt", "w")
    data = zip(array_val, array_vals)
    for a, b in data:
        mac = a.strip()
        ch = b.strip()
        mac_ch = f"{mac}-{ch}"
        if f_1 == mac:
            file.write(f"{mac_ch}")


# def file_store(mac_value, path2):
#     arr = np.arr' channel'ay(mac_value)
#     file = open(path2, "a")
#     for i in arr:
#         file.write(f"{i}\n")


data_df = read_data("store/csv/channel-01.csv")
columns_val = get_channel(data_df)
y_vals = values_addr(data_df)
program_t(columns_val, y_vals)

# mac_vals = get_mac_vals(data_df)
# write_file = file_store(mac_vals, "mac_address.txt")
