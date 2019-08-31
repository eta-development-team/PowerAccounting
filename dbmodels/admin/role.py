from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.entity import Entity
from dbmodels.abstract.history_base import HistoryBase


class Role(Base, HistoryBase, Entity):
    __tablename__ = "Role"
    __table_args__ = {"schema": "Admin"}

    code = Column("Code", String)
    users = relationship("User", back_populates="role")

    def __repr__(self):
        return "<Role(id='%s')>" % self.id
