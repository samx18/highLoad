from urllib2 import  Request, urlopen, URLError, HTTPError
from subprocess import call
ENCRYPTED_HOOK_URL = 'AQECAHgT/MsA4/sL3S5flIV8eLI13GPSUwLOdlMiunWVHtJm/QAAAKcwgaQGCSqGSIb3DQEHBqCewqjkhhdsaNcvpwhgalpPcG/zOdFIdFOunHYCARCAYMZU9PoYrTUEAkey+GCXqLTTmNpECB2Sh6CY0hwh1b2gV3+0GxRMwtvZiNYltvSXjR2pY2qoxxmXfxH54jzsOBUNOtICPzj4onrmbmd6d4nfMiLtuGUwT1rwctPIHifCKQ=='
import simplejson as json
SLACK_CHANNEL = 'bot-testing'

call(["ls", "-l"])
