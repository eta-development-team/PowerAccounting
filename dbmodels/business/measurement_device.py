from datetime import datetime

from sqlalchemy import Column, ForeignKey, Float, DateTime, BigInteger, Boolean
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.entity import Entity
from dbmodels.abstract.history_base import HistoryBase


class MeasurementDevice(Base, HistoryBase, Entity):
    """Represents a MeasurementDevice entity in a database."""

    __tablename__ = "MeasurementDevice"
    __table_args__ = {"schema": "Business"}

    description = Column("Description", String(64))
    subModel = Column("SubModel",  String(16))
    autoDefTimeoutAnswer = Column("AutoDefTimeoutAnswer", Integer, default=5000)
    amountAttempt = Column("AmountAttempt", Integer, default=3)
    networkAddress = Column("NetworkAddress", Integer, default=1)
    priority = Column("Priority", Integer, default=0)
    successConnectionPercent = Column("SuccessConnectionPercent", Float, default=0.0)
    lastConnectionTime = Column("LastConnectionTime", DateTime, default=datetime.fromisoformat("1900-01-01"))
    pollingInterval = Column("PollingInterval", Integer, default=60)
    startReadArchiveDate = Column("StartReadArchiveDate", DateTime, default=datetime.fromisoformat("1900-01-01"))
    currentAccreditationDate = Column("CurrentAccreditationDate", DateTime, default=datetime.fromisoformat("1900-01-01"))
    nextAccreditationDate = Column("NextAccreditationDate", DateTime, default=datetime.fromisoformat("1900-01-01"))
    manufacturingDate = Column("ManufacturingDate", DateTime, default=datetime.fromisoformat("1900-01-01"))
    factoryNumber = Column("FactoryNumber", BigInteger)
    firmware = Column("Firmware", String(16))
    turnOn = Column("TurnOn", Boolean, default=True)
    giveCurrData = Column("GiveCurrData", Boolean, default=True)
    giveHArcData = Column("GiveHArcData", Boolean, default=True)
    giveDArcData = Column("GiveDArcData", Boolean, default=True)
    giveMArcData = Column("GiveMArcData", Boolean, default=True)

    deviceId = Column(
        "DeviceId",
        Integer,
        ForeignKey("Dictionaries.Device.Id")
    )
    accessPointId = Column(
        "AccessPointId",
        Integer,
        ForeignKey("Business.AccessPoint.Id")
    )
    comPortId = Column(
        "ComPortId",
        Integer,
        ForeignKey("Dictionaries.ComPort.Id")
    )
    dataBitId = Column(
        "DataBitId",
        Integer,
        ForeignKey("Dictionaries.DataBit.Id")
    )
    stopBitId = Column(
        "StopBitId",
        Integer,
        ForeignKey("Dictionaries.StopBit.Id")
    )
    parityId = Column(
        "ParityId",
        Integer,
        ForeignKey("Dictionaries.Parity.Id")
    )
    portTypeId = Column(
        "PortTypeId",
        Integer,
        ForeignKey("Dictionaries.PortType.Id")
    )
    baudId = Column(
        "BaudId",
        Integer,
        ForeignKey("Dictionaries.Baud.Id")
    )

    accessPoint = relationship("AccessPoint", back_populates="measurementDevices")
    device = relationship("Device", back_populates="measurementDevices")
    comPort = relationship("ComPort", back_populates="measurementDevices")
    baud = relationship("Baud", back_populates="measurementDevices")
    dataBit = relationship("DataBit", back_populates="measurementDevices")
    stopBit = relationship("StopBit", back_populates="measurementDevices")
    parity = relationship("Parity", back_populates="measurementDevices")
    portType = relationship("PortType", back_populates="measurementDevices")

    channels = relationship("Channel", back_populates="measurementDevice")

    def __str__(self):
        return self.description
