""" Going to add all db functions in this File ONLY
	these functions are not tested yet.""" 
from pymongo import *
import logging  # logging for debug purposes
import os

# Host and Port settings for Mongo Server connection
connSettings = { 'host':'127.0.0.1',
				'port': 27017}

# The DB connection needs to be opened/closed for each query thus Connect() and Disconnect()
def Connect(host=connSettings['host'], port=connSettings['port']):
	conn = MongoClient(host, port)
	db = conn.airbook
	collection = db.collection
	return collection

def Disconnect(host=connSettings['host'], port=connSettings['port']):
	conn = Disconnect(host, port)	
	


# Authenticate function to confirm wether the values exist in DB and allow login
def Authenticate(email,password):
	db = Connect()
	try:
		userObject = db.find_one({"_id":email,
				 "password":password})
		return userObject 
	except Exception, error:
		logging.warning('Did not authenticate user with email %s and password %s because %s'%(email, password, error))
		return None
	Disconnect()			

# Signup To allow people to sign up for the APP. Should be able to accept all the vital information .i.e. email_id 
def SignUp(*args):
	db = Connect()
	for email in args:
		try:
			userObject = {'_id':email}
			print userObject
			db.insert(userObject)
			logging.info('User created successfully')
			return 1
		except Exception, error:
			logging.warning('Signup for the user %s unsuccessful because %s'%(email, error)) 
			return None
	Disconnect()


# StoreContacts does what the name suggests add contacts to userObjects 
def StoreContacts(email, **kwargs):
	db = Connect()
	for key, value in kwargs.items:
		try:		
			db.update({'_id':email},
					{
					'contacts':{"$push":{key:value}}
					})
			logging.info('Contacts Added')			
			return 1
		except Exception, error:
			logging.warning('Contact Update Unsuccessful because %s'%error)
			return None 
	Disconnect()

# This will Help reset password of an User
def SetPassword(_id,password):
	db = Connect()
	try:
		db.update({'_id':_id},{'password':password})
		return 1
		logging.info('password set')
	except Exception, error:
		logging.warning('Unable to set password because %s'%error)
		return None
	Disconnect()

# this will generate  a password using the OS random byte generator
def GeneratePassword():
	password = os.urandom(8).encode('hex')
	return password
	
			
"""Gonna Leave it here, Sleepy ZzzZZZzzZZ"""			 
def  RetrieveContacts():
	pass		
		
	
			
 
