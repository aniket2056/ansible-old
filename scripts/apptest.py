#!/usr/bin/python
import urllib
import difflib
import logging
import requests
import sys
import ConfigParser
 ########################################################
logging.basicConfig(filename='/home/ec2-user/error.log',filemode='a', format='%(asctime)s  %(levelname)s:  %(message)s', level=logging.DEBUG)

###########################################################
try:
    config = ConfigParser.ConfigParser()
    config.read("/home/ec2-user/sql.cnf")
    host = config.get('client', 'host')
    app_name = config.get('client', 'app_name')
    port = config.get('client', 'tomcat_port')
    
except IOError,e:
    
    logging.exception("Error %d: %s" % (e.args[0],e.args[1]))
    sys.exit()

#################################################################    
try: 
	r = requests.get("http://%s:%s/%s"% (host, port, app_name))
	if r.status_code == 200:
		logging.info ("App is running")
#    else:
#		raise Exception("App not running")
except :
	logging.exception(" webpage down")
##########################################################################

try:
    f = urllib.urlopen("http://%s:%s/%s"% (host, port, app_name))
    data = f.read()
    file = open("/home/ec2-user/webpage.txt",'w')
    file.write(data)
    file.close()
    file1 = open("/home/ec2-user/webpage.txt")
    file2 = open("/home/ec2-user/reference.txt")
    
    result = difflib.SequenceMatcher(None, file1.read(), file2.read())
    if result.ratio() < 0.6:
        logging.exception(" unexpected webpage ")
        sys.exit()
        
except IOError,e:
    logging.exception("Error %s: %s" % (e.args[0],e.args[1]))
    sys.exit(1)


