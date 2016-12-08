#!/usr/bin/env python3


from urllib.request import urlopen

def getcity():
    atlip = b'76.17.118.203'
    myip = urlopen("http://myip.dnsdynamic.org/").read()
    if myip == atlip:
        city = "Atlanta"
        return city
    else:
        city = "Melbourne"
        return city




if __name__ == "__main__":
    getcity()

