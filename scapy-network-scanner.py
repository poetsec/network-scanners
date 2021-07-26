#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

scan("# add IP and/or range here")
