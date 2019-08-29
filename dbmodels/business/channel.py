from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base


class Channel(Base):
    """Represents a Channel entity in a database"""

    __tablename__ = "Channel"
    __table_args__ = {"schema": "Business"}

    id = Column("Id", Integer, primary_key=True)
    description = Column("Description", String)
    measurementDeviceId = Column(
        "MeasurementDeviceId",
        Integer,
        ForeignKey("Business.MeasurementDevice.Id")
    )
    resourceSystemTypeId = Column(
        "ResourceSystemTypeId",
        Integer,
        ForeignKey("Dictionaries.ResourceSystemType.Id")
    )

    measurementDevice = relationship("MeasurementDevice", back_populates="channels")
    resourceSystemType = relationship("ResourceSystemType", back_populates="channels")

    def __str__(self):
        return self.description
