#!/usr/bin/python
# -*- coding: utf-8 -*-
import ConfigParser
import MySQLdb as mdb
import sys
import time
import logging
###################################################3
try:
	logging.basicConfig(filename='/home/ec2-user/error.log',filemode='a', format='%(asctime)s  %(levelname)s:  %(message)s', level=logging.DEBUG)

except:
  
    logging.exception("Error in logging configuration")
    sys.exit(1)
    
#######################################################
try:
    config = ConfigParser.ConfigParser()
    config.read("/home/ec2-user/sql.cnf")

    username = config.get('client', 'user')
    password = config.get('client', 'password')
    host = config.get('client', 'host')
    db_name = config.get('client', 'db_name')
    mysql_version  = config.get('client', 'mysql_version')

except IOError,e:
    
    logging.exception("Error %d: %s" % (e.args[0],e.args[1]))
    sys.exit(1)
    
##########################################################
try:
    con = mdb.connect( host, username, password, db_name)
	
    cur = con.cursor()
    cur.execute("SELECT VERSION()")
    ver = cur.fetchone()
    print "Database version : %s " % ver
    
    test = "SELECT DATABASE()"
    cur.execute(test)
    rows = cur.fetchall()
	
    for row in rows:
    
        if row[0] == db_name:
        	logging.info("database % s present",  db_name)
        else:
        	print "Database %s not present" % db_name
        	logging.error("Database %s not present",  db_name)
        	sys.exit(1)
    
#    cur.execute("SHOW GRANTS FOR 'fissionlabs'@'localhost'")
#    data = cur.fetchall()
#    print data
        
except mdb.Error, e:
  
    logging.exception("Error %d: %s" % (e.args[0],e.args[1]))
    sys.exit(1)
    

    

