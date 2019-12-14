print("User Start")

import sqlalchemy as db
from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from DataAccess.Views.Models.DB_Engine import engine, Base

user_id_requestKey = "id"
user_username_requestKey = "username"
user_password_requestKey = "password"
user_memories_requestKey = "memories"

class User(Base):
	__tablename__ = 'user'
	id = Column(String, primary_key=True)
	username = Column(String, unique=True)
	password = Column(String)
	memories = relationship("Memory", backref="user")
	
	def to_dict(self, includePassword=False):
		user_dict = {
			user_id_requestKey:self.id,
			user_username_requestKey:self.username,	
		}
		if includePassword:
			user_dict[user_password_requestKey] = self.password
		return user_dict

print("User End")
