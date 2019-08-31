from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.entity import Entity
from dbmodels.abstract.history_base import HistoryBase


class MeasurementDevice(Base, HistoryBase, Entity):
    """Represents a MeasurementDevice entity in a database."""

    __tablename__ = "MeasurementDevice"
    __table_args__ = {"schema": "Business"}

    description = Column("Description", String)
    accessPointId = Column("AccessPointId", Integer, ForeignKey("Business.AccessPoint.Id"))

    accessPoint = relationship("AccessPoint", back_populates="measurementDevices")
    channels = relationship("Channel", back_populates="measurementDevice")

    def __str__(self):
        return self.description
