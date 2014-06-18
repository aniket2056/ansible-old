#!/usr/bin/python

import subprocess
import sys
import logging
import commands

logging.basicConfig(filename='/home/ec2-user/error.log',filemode='a', format='%(asctime)s  %(levelname)s:  %(message)s', level=logging.DEBUG)

 
out =  commands.getoutput(' netstat -anp |grep 8080')
str = 'LISTEN'
if out.find(str) != -1:
    logging.info(" Port 8080 is listening (Tomcat running)")
else:
    logging.exception(" port 8080 is not listening..tomcat not running")

