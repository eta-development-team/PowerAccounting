from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.entity import Entity
from dbmodels.abstract.history_base import HistoryBase


class User(Base, HistoryBase, Entity):
    __tablename__ = 'User'
    __table_args__ = {"schema": "Admin"}

    userName = Column("UserName", String)
    roleId = Column("RoleId", Integer, ForeignKey('Admin.Role.Id'))
    role = relationship("Role", back_populates="users")
