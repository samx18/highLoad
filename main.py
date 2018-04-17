# Copyright 2018 Sam Palani under MIT License https://opensource.org/licenses/MIT

from urllib2 import  Request, urlopen, URLError, HTTPError
import subprocess
import os

# Set slack integration

SLACK_CHANNEL = 'bot-testing'
URL="https://hooks.slack.com/services/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"

# Set trigger threshold

trigger=6.00

# Get hostname from system

process = subprocess.Popen(['hostname'], stdout=subprocess.PIPE)
out, err = process.communicate()
host=out.split('\n')[0]

#host=call(["hostname"]) Used for debugging on mac


# Read load averages

f=open("/proc/loadavg","r")
#print f.read()
data=f.readlines()
f.close()

# Read the first line of the data list

datastr=data[0]

# Split the line into a string list delimted by space and extract the first element

load=datastr.split(' ')[0]

# Using a curl command since legacy version of python on Emtek

# Post to the AWS bot API via curl

cmd="curl -s -X POST -H 'Content-type: application/json' --data '{\"text\": \":rotating_light: There is a high load on server ` %s ` , current load is ` %s ` \", \"channel\": \"#notifications\"}' https://hooks.slack.com/services/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 -k" % (host,load)

# Post to slack if threshold is breached 

if float(load) > trigger: os.system(cmd)