from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base


class User(Base):
    __tablename__ = 'User'
    __table_args__ = {"schema": "Admin"}

    id = Column("Id", Integer, primary_key = True)
    userName = Column("UserName", String)
    roleId = Column("RoleId", Integer, ForeignKey('Admin.Role.Id'))
    role = relationship("Role", back_populates = "users")