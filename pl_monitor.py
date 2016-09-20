#!/usr/bin/env python3
#
# monitor plutonium clients

import sys,os
sys.path.append(os.path.abspath('..'))
from boto_aws import getInstPL

import time
from datetime import datetime
import slackweb  #pip install slackweb https://github.com/satoshi03/slack-python-webhook/blob/master/README.md
import requests  #pip install requests
import boto.ec2


#Slack incoming web hook



def pl_site_up():
    "Function to monitor uptime, info gathered from aws"
    d = datetime.now()
    plSlack = slackweb.Slack(url="https://hooks.slack.com/services/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")
    print("Running Check at " + str(d))
    for i in getInstPL():
        tags = i.tags
        client = list(tags.values())[list(tags.keys()).index('Client')]
        site = list(tags.values())[list(tags.keys()).index('URL')]
        for tag,value in tags.items():
            if tag == 'Process' and value == 'Live':
                try:
                    r = requests.get(site, verify=False, timeout=10)
                    if r.status_code == 200:
                        time.sleep(1)
                        d = datetime.now()
                        print( client + " is up at " + str(d))
                        print(r.status_code)
                    else:
                        plSlack.notify(text=client + " Website is Down!", channel="#ec2-status", username="status-bot",icon_emoji=':warning:')
                        print( client+ " is down at " + str(d))
                        print(r.status_code)
                except requests.exceptions.ReadTimeout:
                    plSlack.notify(text=client + " Website is Down!", channel="#ec2-status", username="status-bot", icon_emoji=':warning:')

if __name__ == "__main__":
    pl_site_up()


