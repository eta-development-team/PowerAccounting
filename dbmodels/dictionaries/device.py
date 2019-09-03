from sqlalchemy import Column, Integer, Boolean, Binary, ForeignKey
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class Device(DictionaryBase, Base):
    __tablename__ = "Device"

    archiveDepthHour = Column("ArchiveDepthHour", Integer)
    archiveDepthDay = Column("ArchiveDepthDay", Integer)
    archiveDepthMonth = Column("ArchiveDepthMonth", Integer)
    shortName = Column("ShortName", Integer)
    image = Column("Image", Binary("MAX"))
    hasDigitalInterface = Column("HasDigitalInterface", Boolean)
    calibrationInterval = Column("CalibrationInterval", Integer)
    channelsCount = Column("ChannelsCount", Integer)
    isIntegralArchiveValue = Column("IsIntegralArchiveValue", Boolean)
    baudId = Column(
        "BaudId",
        Integer,
        ForeignKey("Dictionaries.Baud.Id")
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
    baud = relationship("Baud", back_populates="devices")
    dataBit = relationship("DataBit", back_populates="devices")
    stopBit = relationship("StopBit", back_populates="devices")
    parity = relationship("Parity", back_populates="devices")

    deviceEventParameters = relationship("DeviceEventParameter", back_populates="device")
    internalDeviceEvents = relationship("InternalDeviceEvent", back_populates="device")
    deviceParameters = relationship("DeviceParameter", back_populates="device")
    channelTemplates = relationship("ChannelTemplate", back_populates="device")
