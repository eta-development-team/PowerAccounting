from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base


class MeasurementDevice(Base):
    """Represents a MeasurementDevice entity in a database."""

    __tablename__ = "MeasurementDevice"
    __table_args__ = {"schema": "Business"}

    id = Column("Id", Integer, primary_key=True)
    description = Column("Description", String)
    accessPointId = Column("AccessPointId", Integer, ForeignKey("Business.AccessPoint.Id"))

    accessPoint = relationship("AccessPoint", back_populates="measurementDevices")
    channels = relationship("Channel", back_populates="measurementDevice")

    def __str__(self):
        return self.description
