from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base


class ResourceSystemType(Base):
    __tablename__ = "ResourceSystemType"
    __table_args__ = {"schema": "Dictionaries"}
    id = Column("Id", Integer, primary_key=True)
    code = Column("Code", String)
    description = Column("Description", String)

    channels = relationship("Channel", back_populates="resourceSystemType")

    def __str__(self):
        return self.description
