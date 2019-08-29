from sqlalchemy import Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base


class Role(Base):
    __tablename__ = "Role"
    __table_args__ = {"schema": "Admin"}

    id = Column("Id", Integer, primary_key = True)
    code = Column("Code", String)
    users = relationship("User", back_populates = "role")

    def __repr__(self):
        return "<Role(id='%s')>" % self.id
