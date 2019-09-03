from datetime import datetime

from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, DateTime, Float, Boolean
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.entity import Entity
from dbmodels.abstract.history_base import HistoryBase


class AccessPoint(Base, Entity, HistoryBase):
    __tablename__ = "AccessPoint"
    __table_args__ = {"schema": "Business"}

    description = Column("Description", String(64))
    identifier = Column("Identifier", String(128))
    netAddress = Column("NetAddress", String(16), default="10.135.64.1")
    port = Column("Port", Integer, default=5010)
    netPhone = Column("NetPhone", String(16))
    lastConnectionTime = Column("LastConnectionTime", DateTime, default=datetime.fromisoformat("1900-01-01"))
    lastStatusConnectionId = Column("LastStatusConnectionId", Integer, default=1)
    successConnectionPercent = Column("SuccessConnectionPercent", Float, default=0.0)
    ControllerAddress = Column("ControllerAddress", Integer, default=255)
    IsNeedToReconfigure = Column("IsNeedToReconfigure", Boolean, default=False)

    transportTypeId = Column(
        "TransportTypeId",
        Integer,
        ForeignKey("Dictionaries.TransportType.Id"), default=3
    )
    transportServerModelId = Column(
        "TransportServerModelId",
        Integer,
        ForeignKey("Dictionaries.TransportServerModel.Id"), default=3
    )
    deviceReaderId = Column(
        "DeviceReaderId",
        Integer,
        ForeignKey("Business.DeviceReader.Id")
    )

    transportType = relationship("TransportType", back_populates="accessPoints")
    transportServerModel = relationship("TransportServerModel", back_populates="accessPoints")
    deviceReader = relationship("DeviceReader", back_populates="accessPoints")

    measurementDevices = relationship("MeasurementDevice", back_populates="accessPoint")
