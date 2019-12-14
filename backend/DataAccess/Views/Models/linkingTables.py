import sqlalchemy as db
from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from DataAccess.Views.Models.DB_Engine import engine, Base

memory_tag_table = Table('memory_tag', Base.metadata,
	Column('memory_id', String, ForeignKey('memory.id')),
	Column('tag_id', String, ForeignKey('tag.id'))
	)
