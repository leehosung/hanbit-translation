#!/usr/bin/python

import re
from subprocess import Popen, PIPE
from setting import *
from sendsms import sendSMS

p = Popen([URLWATCH, "--urls", URL, "--hooks", HOOK], stdout=PIPE, stderr=PIPE)
(stdout, stderr) = p.communicate()
if stdout != None:
    sites = re.findall("CHANGED:.*", stdout)
    for site in sites:
        msg = site
        sendSMS(user=SMS_USER, passwd=SMS_PASSWD, callback=CALLBACK, callno=CALLNO, msg=msg)
