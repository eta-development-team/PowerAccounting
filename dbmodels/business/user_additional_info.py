from datetime import datetime

from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.entity import Entity
from dbmodels.abstract.history_base import HistoryBase


class UserAdditionalInfo(Base, Entity, HistoryBase):
    __tablename__ = "UserAdditionalInfo"
    __table_args__ = {"schema": "Business"}

    description = Column("Description", String(64))
    firstName = Column("FirstName", String(32))
    lastName = Column("LastName", String(32))
    patronimic = Column("Patronimic", String(32))
    birthDay = Column("BirthDay", DateTime, default=datetime.fromisoformat("1900-01-01"))
    phone = Column("Phone", String(16))
    email = Column("Email", String(128))
    genderId = Column(
        "GenderId",
        Integer,
        ForeignKey("Dictionaries.Gender.Id")
    )
    gender = relationship("Gender", back_populates="userAdditionalInfos")
    buildings = relationship("Building", back_populates="userAdditionalInfo")
