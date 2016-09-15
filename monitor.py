#!/usr/bin/env python
#
# Code written by Daniel Linge 8/5/2016
#
# based off of http://www.craigaddyman.com/python-script-to-monitor-site-up-time/


import time
from datetime import datetime
import slackweb  #pip install slackweb https://github.com/satoshi03/slack-python-webhook/blob/master/README.md
import requests  #pip install requests

i = datetime.now()

#Slack incoming web hook
slack = slackweb.Slack(url="https://hooks.slack.com/services/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")

# List of Clients
clients = {

        'Mothers Touch':'http://motouchmovers.com',
        'Addy Rose':'http://addyrosehair.com',
        'Advanced Surgical':'http://advancedsurgical.md',
        'Andrea Young':'http://andrea2016.com',
        'Artistic Closet':'http://artisticcloset.com',
        'Atlantis Vision':'http://atlantisvisioncenter.com',
        'Aware Ortho':'http://awareorthopaedics.com',
        'Blue Sky Plumbing':'http://blueskyplumbingsolutions.com',
        'Brenner Architect':'http://brennerarchitect.com',
        'Brevard Mediation':'http://brevardmediationservices.com',
        'Brevard Shutter':'http://brevardshutter.com',
        'Burton Homes':'http://burtonhomes.com',
        'Cassels Garage':'http://casselsgarage.com',
        'Certified Roofing':'http://certifiedroofingllc.com',
        'Champion Brevard':'http://www.championbrevard.com',
        'Coulter Designs':'http://coulterdesigns.com',
        'Discovery Aviation':'http://discovery-aviation.com',
        'Dr. Go':'http://drgomd.com',
        'Florida Breeze':'http://floridabreeze.com',
        'Florida Moving Systems':'http://flmove.com',
        'Fountain of You':'http://fountainofyou.md',
        'Glenn Painter':'http://gapainter.com',
        'Houston Family':'http://houstonfamilymagazine.com',
        'Indialantic Medical':'http://drstember.com',
        'ICC':'http://injurycareclinic.com',
        'Inspirations Design':'http://inspirationsdesigncenter.com',
        'ITTBAPA':'http://itstimetobeaparentagain.com',
        'Math Doctor':'http://mathdoctorbrevard.com',
        'MMS':'http://downtownmelbourne.com',
        'Mermaid Bride':'http://mermaidbride.com',
        'Nance':'http://nancelaw.com',
        'NC Repower':'http://northcourtenayrepowercenter.com',
        'Traxx':'http://offthetraxx.com',
        'Political Food for Thought':'http://politicalfoodforthought.com',
        'Real Estate Ink':'http://realestateinksolutions.com',
        'Solar Solutions':'http://solarsolutionsvero.com',
        'Steel Group':'http://steelegroupllc.com',
        'Sun Plumbing':'http://sunplumbing.com',
        'Ted Seymour':'http://tedseymour.org',
        'The Car People':'http://thecarpeople.com',
        'TLP':'https://www.tightlineproductions.com',
        'Tripod Aluminum':'http://tripodaluminum.com',
        'Danlinge':'http://danlinge.xyz'
}



def site_up():
        "Function to monitor uptime"
        print("Running check at " + str(i))
        for client, site in clients.items():
            try:
                r = requests.get(site, verify=False, timeout =10)
                if r.status_code == 200:    # 200 = up! 
                    time.sleep(1)           # 1 second between checks
                    #print( str(client) + "is up at" + str(i)) 
                    #print(r.status_code)
                else:
                    slack.notify(text=client + " Website is Down!", channel="#ec2-status", username="status-bot",icon_emoji=':warning:')
                    print( str(client) + " is down at " + str(i))
                    print(r.status_code)
            except requests.exceptions.ReadTimeout:
                slack.notify(text=client + " Website is Down!", channel="#ec2-status", username="status-bot", icon_emoji=':warning:') 
            except:
                pass

#            except requests.exceptions.ConnectionError:
#                slack.notify(text=client + " Website is Down!", channel="#ec2-status", username="status-bot", icon_emoji=':warning:')
#                print( str(client) + " is down at " + str(i))
#                print(r.status_code)
#            except requests.exceptions.ReadTimeout:
#                slack.notify(text=client + " Website is Down!", channel="#ec2-status", username="status-bot", icon_emoji=':warning:')
#                print( str(client) + " is down at " + str(i))
#                print(r.status_code)
#            except requests.exceptions.SSLError:
#                pass
#


site_up()

