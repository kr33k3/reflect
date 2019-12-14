print("Memory Start")

import sqlalchemy as db
from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from DataAccess.Views.Models.DB_Engine import engine, Base
from DataAccess.Views.Models.linkingTables import memory_tag_table


memory_id_requestKey = "id"
memory_title_requestKey = "title"
memory_content_requestKey = "content"
memory_user_id_requestKey = "user_id"
memory_user_requestKey = "user"
memory_tags_requestKey = "tags"

class Memory(Base):
	__tablename__ = 'memory'
	id = Column(String, primary_key=True)
	title = Column(String)
	content = Column(String)
	user_id = Column(String, ForeignKey('user.id')) 
	#user - see User.memories backref
	tags = relationship("Tag", secondary=memory_tag_table)
	#TODO add source
	#TODO add page range
	
	def to_dict(self, include_user=False):
		toReturn = {
			memory_id_requestKey:self.id,
			memory_title_requestKey:self.title,
			memory_content_requestKey:self.content
		}
		toReturn[memory_tags_requestKey] = []
		for tag in self.tags:
			toReturn[memory_tags_requestKey].append(tag.to_dict())
		if include_user:
			toReturn[memory_user_requestKey] = self.user.to_dict() if self.user is not None else "None"
		return toReturn


print("Memory End")
