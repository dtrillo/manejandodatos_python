# coding: utf-8
__author__ = 'dtrillo'

import sys;
import pymysql; #mysql library (you will need to install this on the system)

#MySQL Singleton Class with pymysql
class MySQLConnector(object):
    #	http://famousphil.com/blog/2012/01/mysql-singleton-classes-in-php-and-python/
	_connection = None;
	_instance = None;

	def __init__(self, host="localhost", user="root", passwd="forever", database="", debug=False):	# Versión 1.0.1
		try:
			if MySQLConnector._instance == None:
				MySQLConnector._instance = self;
				self.dbhost = host
				self.dbuser = user
				self.dbpassword = passwd
				self.dbname = database
				MySQLConnector._instance.connect(debug);	# Versión 1.0.1
		except Exception, e:
			print "MySQL Error "+str(e);

	def instance(self):
		return MySQLConnector._instance;

	def get_connection(self):
		return MySQLConnector._connection;

	def connect(self, debug=False):
		try:
			MySQLConnector._connection = pymysql.connect(self.dbhost, self.dbuser, self.dbpassword, self.dbname);
			if debug:
					print "INFO: Database connection successfully established";
		except Exception, e:
			print "ERROR: MySQL Connection Couldn't be created... Fatal Error! "+str(e);
			sys.exit();

	def disconnect(self):
		try:
			MySQLConnector._connection.close();
		except:
			pass;#connection not open

	#returns escaped data for insertion into mysql
	#def esc(self, esc):
	#	return MySQLdb.escape_string(str(esc));

	#query with no result returned
	def query(self, sql):
		cur = MySQLConnector._connection.cursor();
		return cur.execute(sql);

	def tryquery(self, sql):
		try:
			cur = MySQLConnector._connection.cursor();
			return cur.execute(sql);
		except:
			return False;

	#inserts and returns the inserted row id (last row id in PHP version)
	def insert(self, sql):
		cur = MySQLConnector._connection.cursor();
		cur.execute(sql);
		return self._connection.insert_id();

	def tryinsert(self, sql):
		try:
			cur = MySQLConnector._connection.cursor();
			cur.execute(sql);
			return self._connection.insert_id();
		except:
			return -1;

	#returns the first item of data
	def queryrow(self, sql):
		cur = MySQLConnector._connection.cursor();
		cur.execute(sql);
		return cur.fetchone();

	#returns a list of data (array)
	def queryrows(self, sql):
		cur = MySQLConnector._connection.cursor();
		cur.execute(sql);
		return cur.fetchmany();
