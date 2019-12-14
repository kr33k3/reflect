print("Models Start")

from .DB_Engine import Base, engine
#import the tables to build their model classes
import DataAccess.Views.Models.User
import DataAccess.Views.Models.Memory
import DataAccess.Views.Models.Tag

#Create the table in the db
Base.metadata.create_all(engine)

print("Models End")
