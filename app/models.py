from sqlalchemy import Column, Integer, String, Text, DateTime
from . import Base
from datetime import datetime

# TODO: Review 모델 클래스를 만드세요 (Base 상속)

class Review(Base):
    __tablename__ = "reviews"
# TODO: id, title, content, rating 컬럼을 정의하세요
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    rating = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


    def __repr__(self):
        return f"<Review id={self.id} title='{self.title}'>\ncontent : {self.content}\nrating: {self.rating}"
    

