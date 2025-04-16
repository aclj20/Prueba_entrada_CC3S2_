from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text
import json

Base = declarative_base()

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(Text, nullable=False)
    options = Column(Text, nullable=False) 
    correct_answer = Column(Text, nullable=False)
    nivel = Column(String, nullable=False)

    def __init__(self, **kwargs):
        if isinstance(kwargs.get("options"), list):
            kwargs["options"] = json.dumps(kwargs["options"])
        super().__init__(**kwargs)


