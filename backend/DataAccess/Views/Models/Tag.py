print("Tag Start")

import sqlalchemy as db
from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from DataAccess.Views.Models.DB_Engine import engine, Base
from DataAccess.Views.Models.linkingTables import memory_tag_table


tag_id_requestKey = "id"
tag_title_requestKey = "title"
tag_memories_requestKey = "memories"

class Tag(Base):
    __tablename__ = 'tag'
    id = Column(String, primary_key=True)
    title = Column(String, unique=True)
    memories = relationship("Memory", secondary=memory_tag_table)
    
    def to_dict(self):
        return {
            tag_id_requestKey:self.id,
            tag_title_requestKey:self.title
        }


print("Tag End")
