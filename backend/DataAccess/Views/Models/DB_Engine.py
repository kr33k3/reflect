print("DB_Engine Start")

from uuid import uuid4
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#The engine
engine = db.create_engine('sqlite:///Reflect.db',connect_args={'check_same_thread': False})
#The base class for the models
Base = declarative_base(engine)

#The session, for performing CRUD operations
SessionBase = sessionmaker(bind=engine, autoflush=False)
session = SessionBase() 

#SafeCommit
#If an error occurs on commit, rolls back the changes and returns the eroor
#Otherwise, returns the provided returnValue
printErrors = False
def SafeCommit(returnValue):
	try:
		session.commit()
	except Exception as exception:
		session.rollback()
		ex_str = exception.__str__()
		if printErrors:
			print("\nError: " + ex_str + "\n\n")
		return Error(ex_str)
	else:
		return returnValue if returnValue is not None else "Success"

def New_UUID():
	return str(uuid4())

def Error(message):
	return {"Error": message}

def Success(message):
	return {"Success": message}

print("DB_Engine End")
