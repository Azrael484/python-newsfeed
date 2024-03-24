from datetime import datetime
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property

class Post(Base):
	__tablename__ = 'posts'
	id = Column(Integer, primary_key=True)
	title = Column(String(100), nullable=False)
	post_url = Column(String(100), nullable=False)
	user_id = Column(Integer, ForeignKey('users.id'))
	created_at = Column(DateTime, default=datetime.now)
	updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
	vote_count = column_property(
		select(func.count(Vote.id)).select_from(Vote).where(Vote.post_id == id)
	)
	# dynamic properties generated when a query for a given post is made

	user = relationship('User')
	comments = relationship('Comment', cascade='all,delete') # if the post is deleted, delete all of the associated comments
	votes = relationship('Vote', cascade='all,delete')

