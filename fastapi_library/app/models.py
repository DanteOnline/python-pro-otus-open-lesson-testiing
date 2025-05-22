from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import declarative_base


Base = declarative_base(cls=AsyncAttrs)


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(32), nullable=False)
    birthday_year = Column(Integer, nullable=False)

    def __str__(self):
        return f"{self.name}: {self.birthday_year}"
