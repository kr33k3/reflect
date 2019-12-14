print("UserView Start")
from DataAccess.Views.Models.DB_Engine import session, SafeCommit, New_UUID, Error

from DataAccess.Views.Models.User import User, user_username_requestKey, user_password_requestKey

class user_access_template:
	username = None
	password = None

	def __init__(self, template_dict):
		self.username = template_dict[user_username_requestKey] if user_username_requestKey in template_dict else None
		self.password = template_dict[user_password_requestKey] if user_password_requestKey in template_dict else None

#Create User
#Creates a user
#_username, password - strings
def CreateUser(template):
	new_user = User(id = New_UUID(), username = template.username, password = template.password)
	session.add(new_user)
	return SafeCommit(new_user)

#Get user by their id
def GetUser(uuid):
	user = session.query(User).filter(User.id==uuid).first()
	return user if user != None else Error("User not found")

#Login
def Login(template):
	user = session.query(User).filter( \
		User.username==template.username, \
		User.password==template.password
		).first()
	toReturn = user if user is not None else Error("Username or password were incorrect")
	return toReturn

#Update a user's password
def UpdatePassword(template, new_password):
	user = Login(template)
	if type(user) is not User:
		return user
	user.password = new_password
	return SafeCommit(user)

print("UserView End")