# slackmon

using boto, slackmon grabs tabs from aws and tests each site to make sure it's up. 

if not, a message is sent to slack. 

required tags:

Client = client name

Process = live (if not live, the site will not be tracked)

URL = www.example.com


