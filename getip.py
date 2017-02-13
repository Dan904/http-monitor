#!/usr/bin/env python3


from requests import get

def getcity():
    atlip = '76.17.118.203'
    myip = str(get("https://api.ipify.org").text)
    if myip == atlip:
        city = "Atlanta"
        print(city)
        return city
    else:
        city = "Melbourne"
        print(city)
        return city




if __name__ == "__main__":
    getcity()

