"""This is where I plan to have url mapping and app configuration"""

from flask import Flask
from views import *
from db import *




app = Flask(__name__)
app.config.from_object(__name__)

"""The email should be permanently stored for a logqed in User and automatically be used."""

@app.route('/login/<email_id>/<password>', methods=['GET','PUT','POST'])
def auth(email_id,password):	

	auth = Authenticate(email_id,passowrd)
	if auth != None:
		return "Login successful"
	else:
		return "Access Denied. Username/Password Incorrect or does not exist"

@app.route('/signup/<email_id>/', methods=['GET','POST','PUT'])
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


@app.route('/store_contacts/<email_id>', methods=['POST','PUT'])
def store(request,email):
	if request.method == 'POST' or request.method == 'PUT':
		contacts = request.POST['contacts']
		for contact in contacts:
			StoreContacts(email, contact)


if __name__ == "__main__":
	app.run(debug=True)
