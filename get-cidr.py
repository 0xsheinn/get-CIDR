#!/usr/bin/python3
#author: shanekhant

import sys
import requests

if len(sys.argv) != 2:
        print(f"[+] Usage: python3 {sys.argv[0]} paypal")
        exit(1)

org_name = sys.argv[1]
url = f"http://asnlookup.com/api/lookup?org={org_name}"
req = requests.get(url)
cidr_range = req.json()
if str(cidr_range) == "[]":
        txt = f"""
Sorry! {sys.argv[1]} doesn't have a registered ASN.
For smaller organizations the ASN will usually be that of their ISP whereas the hostname might not.
One example of this is 207.97.227.245, a GitHub IP address. The ASN is AS27357 (Rackspace Hosting),
but the hostname is pages.github.com.
        """
        print(txt)
else:
        for cidr in cidr_range:
                with open(f"CIDR_Range_for_{sys.argv[1]}.lst","a") as ips:
                        ips.write(cidr + "\n")
                        print(cidr)