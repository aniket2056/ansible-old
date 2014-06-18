#!/usr/bin/python

import subprocess
import sys
import logging
import commands

logging.basicConfig(filename='/home/ec2-user/error.log',filemode='a',format='%(asctime)s  %(levelname)s:  %(message)s', level=logging.DEBUG)

 

out =  commands.getoutput(' netstat -anp |grep 8080')
str = 'TIME_WAIT'
if out.find(str) != -1:
    logging.info(" Port 8080 is NOT listening...tomcat successfully stopped for deployment")
else:
    logging.exception(" 8080 port is listening...tomcat stopping process is unsuccessfull..aborting deployment ")
    sys.exit()

    



