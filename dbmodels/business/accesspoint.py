from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.entity import Entity
from dbmodels.abstract.history_base import HistoryBase


class AccessPoint(Base, Entity, HistoryBase):
    __tablename__ = "AccessPoint"
    __table_args__ = {"schema": "Business"}

    description = Column("Description", String)
    measurementDevices = relationship(
        "MeasurementDevice",
        back_populates="accessPoint"
    )
