"""This is the Controller where all the action takes place :D """
from db import *
from flask import request

#Login controller, validate and return UserObject
def login(username,password):
	auth = Authenticate(usrename,password)
	if auth != None:
		return auth
	else:
		return "Access Denied. Username/Password Incorrect or does not exist"



#Signup Controller to welcome new members	
def signup(email_id):
	if SignUp(email_id) !=None:
		try:
			password = GeneratePassword()
			SetPassword(email_id,password)
			return password
		except Exception, error:
			print "Signup failed because ", error
			return "Signup Failed"		
	else:
		return "The Email id Already exists."

#Storing contact information 	
def store(request,email):
	if request.method == 'POST' or request.method == 'PUT':
		contacts = request.POST['contacts']
		for contact in contacts:
			StoreContacts(email, contact)


		
