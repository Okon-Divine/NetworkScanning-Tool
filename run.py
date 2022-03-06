#!/bin/python3

from rich import print
from main import get_host, print_result, save_valid_mac, compare_mac, deauth
import sys
import os
import subprocess


msg = """
    [[red]![/red]] input [bold red]scan[/bold red] to discover connected devices on your network
    [[red]![/red]] input [bold red]hosts[/bold red] to view connected devices
    [[red]![/red]] input [bold red]save[/bold red] to whitelist the current devices
    [[red]![/red]] restart the program i.e input [bold red]exit[/bold red]/[bold red]quit[/bold red] then input [bold red]./run.sh[/bold red]
    [[red]![/red]] input [bold red]scan[/bold red] to discover connected devices on your network
    [[red]![/red]] input [bold red]check[/bold red] to validate current devices
    [[red]![/red]] input [bold red]deauth[/bold red] to deauthenticate invalid devices
"""

print(f"[bold green]{msg}[/bold green]")

while True:
    ci = input("[!] ")
    fci = ci.strip().lower()
    if fci == "scan":
        get_host()
        print_result("result/arp-scan.txt")
        print("[blue]No of host found ↓[/blue]")
        os.system("wc -l result/arp-scan.txt | cut -d ' ' -f1")
        print("[bold purple]-[/bold purple]" * 50)
    elif fci == "hosts":
        hosts = print_result("result/arp-scan.txt")
        print(f"[bold cyan]{hosts}[/bold cyan]")
    elif fci == "save":
        save_valid_mac()
        print("[bold green] saved [/bold green]")
    elif fci == "check":
        res = compare_mac()
        print(f"[bold red]{res} invalid host[/bold red]")
    elif fci == "deauth":
        deauth()
    elif fci == "clear":
        sys.stderr.write("\x1b[2J\x1b[H")
    elif fci == "exit" or fci == "quit":
        subprocess.call("./clear.sh", shell=True)
        sys.exit()
    elif fci == "exit -w" or fci == "quit -w":
        subprocess.call("./clear_white_list.sh", shell=True)
        sys.exit()
    else:
        print("[underline red]Invalid input[/underline red]")
