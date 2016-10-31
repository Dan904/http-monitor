#!/usr/bin/env python
#
# Media Temple Clients

import time
from datetime import datetime
import slackweb  #pip install slackweb https://github.com/satoshi03/slack-python-webhook/blob/master/README.md
import requests  #pip install requests


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


if __name__ == '__main__':
    mt_site_up()


