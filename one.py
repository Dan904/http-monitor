#!/usr/bin/env python3


import boto.ec2
import time
from datetime import datetime
import slackweb  #pip install slackweb https://github.com/satoshi03/slack-python-webhook/blob/master/README.md
import requests  #pip install requests
from requests import get

def getInstPL():
    inc = "pluto"
    conn = boto.ec2.connect_to_region("us-west-2",profile_name='pluto')
    reservations = conn.get_all_instances()
    instances = [i for r in reservations for i in r.instances]
    return instances

def getInst():
    inc = "tlp"
    conn = boto.ec2.connect_to_region("us-west-2")
    reservations = conn.get_all_instances()
    instances = [i for r in reservations for i in r.instances]
    return instances


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


def slackMessage(client,city,url,error,company):
    """ Slack message with 5 variables in paragraph format"""
    attachments = []
    attachment = {
            "fallback":client+" Down in " +city,
            "pretext": "*WEBSITE DOWN in "+city+"*",
            "title": client,
            "title_link": url,
            "text":"Error = "+error,
            "color": "#ff0000",
            "mrkdwn_in": ["text","pretext"]
            }
    attachments.append(attachment)
    plSlack = slackweb.Slack(url="https://hooks.slack.com/services/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")
    tlpSlack = slackweb.Slack(url="https://hooks.slack.com/services/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")
    if company == "tlp":
        tlpSlack.notify(attachments=attachments, channel="#ec2-status", username="status-bot",icon_emoji=':warning:')
    else:
        plSlack.notify(attachments=attachments, channel="#ec2-status", username="status-bot",icon_emoji=':warning:')


def site_up():
    """Tests each instance on aws using tags if the site is up"""
    d = datetime.now()
    headers = {'User-Agent': 'Plutonium Slack Monitor Script'}
    print("Running Check at " + str(d))
    city = getcity()
    for i in getInst() + getInstPL():
        try:
            tags = i.tags
            key = i.key_name
            if key == "Pluto":
                inc = "pluto"
            else:
                inc = "tlp"
            client = list(tags.values())[list(tags.keys()).index('Client')]
            site = list(tags.values())[list(tags.keys()).index('URL')]
            for tag,value in tags.items():
                if tag == 'Process' and value == 'Live':
                    try:
                        r = requests.get(site, verify=False, timeout=10, headers=headers)
                        if r.status_code == 200:
                            time.sleep(1)
                            d = datetime.now()
                            print(' ')
                            print( client + " is up at " + str(d))
                            print(r.status_code)
                        else:
                            slackMessage(client,city,site,str(r.status_code),inc)
                            print(' ')
                            print( client+ " is down at " + str(d))
                            print(r.status_code)
                    except requests.exceptions.ReadTimeout:
                        slackMessage(client,city,site,"Timeout",inc)
                        print(' ')
                        print( client + " is down at " + str(d))
                        print("error = timeout")
                    except requests.exceptions.ConnectionError:
                        slackMessage(client,city,site,"Connection Refused",inc)
                        print(' ')
                        print( client + " is down at " + str(d))
                        print("error = connection refused")
                    except:
                        pass
        except ValueError:
            slackMessage(client,city,site,"URL Tag in AWS is Broken",inc)
            pass

site_up()

# Media Temple Clients

#Slack incoming web hook

# List of Clients
clients = {

        'Mothers Touch':'http://motouchmovers.com',
        'Addy Rose':'http://addyrosehair.com',
        'Aware Ortho':'http://awareorthopaedics.com',
        'Brenner Architect':'http://brennerarchitect.com',
        'Discovery Aviation':'http://discovery-aviation.com',
        'Dr. Go':'http://drgomd.com',
        'Florida Moving Systems':'http://flmove.com',
        'Indialantic Medical':'http://drstember.com',
        'Traxx':'http://offthetraxx.com',
        'Political Food for Thought':'http://politicalfoodforthought.com',
        'Sun Plumbing':'http://sunplumbing.com',
        'Dr. Stember':'http://drstember.com',
        'Florida Ultra Running Club':'http://furtinc.com',
        'dlxyz':'http://danlinge.xyz'
}



def mt_site_up():
        "Function to monitor uptime"
        tlpSlack = slackweb.Slack(url="https://hooks.slack.com/services/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")
        d = datetime.now()
        print("Running check at " + str(d))
        for client, site in clients.items():
            try:
                r = requests.get(site, verify=False, timeout =10)
                if r.status_code == 200:    # 200 = up! 
                    time.sleep(1)           # 1 second between checks
                    d = datetime.now()
                    print(' ')
                    print( str(client) + " is up at " + str(d))
                    print(r.status_code)
                else:
                    tlpSlack.notify(text=client + " Website is Down!", channel="#ec2-status", username="status-bot",icon_emoji=':warning:')
                    d = datetime.now()
                    print( str(client) + " is down at " + str(d))
                    print(r.status_code)
            except requests.exceptions.ReadTimeout:
                tlpSlack.notify(text=client + " Website is Down!", channel="#ec2-status", username="status-bot", icon_emoji=':warning:')
            except:
                pass


def tlp_print():
    print(' ')
    print('-'*50)
    print(' ')
    print("Checking Tight Line Production Clients")
    print(' ')
    print('-'*50)
    print(' ')

def pl_print():
    print(' ')
    print('-'*50)
    print(' ')
    print("Checking Plutonium Production Clients")
    print(' ')
    print('-'*50)
    print(' ')

def mt_print():
    print(' ')
    print('-'*50)
    print(' ')
    print("Checking Media Temple TLP Clients")
    print(' ')
    print('-'*50)
    print(' ')


def main():
    pl_print()
    pl_site_up()
#    mt_print()
#    mt_site_up()
    tlp_print()
    tlp_site_up()

#if __name__ == "__main__":
#    test()


