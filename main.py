ffrom urllib2 import  Request, urlopen, URLError, HTTPError
import subprocess
import os

# Set slack integration

SLACK_CHANNEL = 'bot-testing'
URL="https://hooks.slack.com/services/Txxxxxxxxxxxxxx"

# Set trigger threshold

trigger=6.00

# Get hostname from system

process = subprocess.Popen(['hostname'], stdout=subprocess.PIPE)
out, err = process.communicate()
host=out.split('\n')[0]
#host=out.split(' ')[0].split('\n')

#host=call(["hostname"])

print host

# Read load averages

f=open("/proc/loadavg","r")
data=f.readlines()
f.close()

# Read the first line of the data list

datastr=data[0]

# Split the line into a sting list delimted by space and extract the first element

load=datastr.split(' ')[0]

cmd="curl -X POST -H 'Content-type: application/json' --data '{\"text\": \":rotating_light: There is a high load on server:` %s ` . Current Load: ` %s ` .\", \"channel\": \"#bot-testing\"}' https://hooks.slack.com/services/Txxxxxxxxxxxxxx -k" % (host,load)

if float(load) < trigger: os.system(cmd)