#!/usr/bin/env python

import os
import argparse
import shutil


def read_current_hosts_file():
    file = open("/etc/hosts", "r")
    print(file.read())

def get_script_location():
    file_location = os.path.dirname(os.path.realpath(__file__))
    return file_location


def back_up_hosts_file():
    working_dir = get_script_location()
    print("Copying /etc/hosts to {0}/hosts_backup/hosts".format(working_dir))
    shutil.copy("/etc/hosts", "{0}/hosts_backup/hosts".format(working_dir))


def append_to_hosts(ip_addr, hosts_array):
    hosts = ' '.join(hosts_array)
    line = "{0} {1}".format(ip_addr, hosts)
    print("Appending to /etc/hosts: {0}".format(line))


parser = argparse.ArgumentParser(description="Add to /etc/hosts")

parser.add_argument("-r", "--read", action="store_true", help="Read current /etc/hosts file")
parser.add_argument("-b", "--backup", action="store_true", help="Backup the current /etc/hosts file")
parser.add_argument("ip_addr", default="no_op", nargs="?", help="ip address to add")
parser.add_argument("hosts", default="no_op", nargs="*", help="Host(s) to bind to ip address")

args = parser.parse_args()

print(args)

if args.backup:
    back_up_hosts_file()

if args.read:
    read_current_hosts_file()

if args.ip_addr != "no_op" and args.hosts != "no_op":
    append_to_hosts(args.ip_addr, args.hosts)
