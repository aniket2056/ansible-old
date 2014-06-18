#!/usr/bin/python
import os
import logging
import sys
import ConfigParser
###########################################

logging.basicConfig(filename='/home/ec2-user/error.log',filemode='a', format='%(asctime)s  %(levelname)s:  %(message)s', level=logging.DEBUG)
#############################################
try:
    config = ConfigParser.ConfigParser()
    config.read("/home/ec2-user/sql.cnf")
    app_name = config.get('client', 'app_name')
    
except IOError,e:
    
    logging.exception("Error %d: %s" % (e.args[0],e.args[1]))
    sys.exit()
#########################################################

if os.path.isfile("/var/lib/tomcat7/webapps/"+app_name+".war"):
	 logging.info("war file transfer successful")

else:
	raise Exception( "war file not present")
	sys.exit()
