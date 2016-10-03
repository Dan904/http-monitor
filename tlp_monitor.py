#!/usr/bin/env python3
#
# monitor tlp clients

from awsboto import getInst

import time
from datetime import datetime
import slackweb  #pip install slackweb https://github.com/satoshi03/slack-python-webhook/blob/master/README.md
import requests  #pip install requests
import boto.ec2


#Slack incoming web hook



def tlp_site_up():
    "Function to monitor uptime, info gathered from aws"
    d = datetime.now()
    tlpSlack = slackweb.Slack(url="https://hooks.slack.com/services/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")
    print("Running Check at " + str(d))
    for i in getInst():
        try:
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
                            print(' ')
                            print( client + " is up at " + str(d))
                            print(r.status_code)
                        else:
                            tlpSlack.notify(text=client + " Website is Down!", channel="#ec2-status", username="status-bot",icon_emoji=':warning:')
                            print(' ')
                            print( client+ " is down at " + str(d))
                            print(r.status_code)
                    except requests.exceptions.ReadTimeout:
                        tlpSlack.notify(text=client + " Website is Down!", channel="#ec2-status", username="status-bot", icon_emoji=':warning:')
                    except:
                        pass
        except ValueError:
            tlpSlack.notify(text=client+"'s URL Tag is broken. Site not monitored till it's fixed.", channel='#ec2-status', username="status-bot", icon_emoji=':warning:')
            pass

if __name__ == "__main__":
    tlp_site_up()


