#!/usr/bin/env python3
#
# Code written by Daniel Linge 8/5/2016
#

import sys,os
sys.path.append(os.path.abspath('..'))
from boto_aws import getInstPL

import time
from datetime import datetime
import slackweb  #pip install slackweb https://github.com/satoshi03/slack-python-webhook/blob/master/README.md
import requests  #pip install requests
import boto.ec2

d = datetime.now()

#Slack incoming web hook
slack = slackweb.Slack(url="https://hooks.slack.com/services/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")



def site_up():
    "Function to monitor uptime, info gathered from aws"
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
                        print( client + " is up at " + str(d))
                        print(r.status_code)
                    else:
                        slack.notify(text=client + " Website is Down!", channel="#ec2-status", username="status-bot",icon_emoji=':warning:')
                        print( client+ " is down at " + str(d))
                        print(r.status_code)
                except requests.exceptions.ReadTimeout:
                    slack.notify(text=client + " Website is Down!", channel="#ec2-status", username="status-bot", icon_emoji=':warning:')


site_up()

