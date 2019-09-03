from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase
from dbmodels.abstract.entity import Entity
from dbmodels.abstract.history_base import HistoryBase


class DeviceReader(Base, DictionaryBase, HistoryBase):
    __tablename__ = "DeviceReader"
    __table_args__ = {"schema": "Business"}

    maxThreadCount = Column("MaxThreadCount", Integer, default=50)
    updateConfigInterval = Column("UpdateConfigInterval", Integer, default=60)
    queuePollingInterval = Column("QueuePollingInterval", Integer, default=45)
    hoveringTaskRemoveTime = Column("HoveringTaskRemoveTime", Integer, default=5)
    signalRNetAddress = Column("SignalRNetAddress", String(16))
    signalRPort = Column("SignalRPort", Integer)
    signalRHub = Column("SignalRHub", String(64))
    serverCommunicatorNetAddress = Column("ServerCommunicatorNetAddress", String(128))
    serverCommunicatorController = Column("ServerCommunicatorController", String(64))
    serverCommunicatorReceiveAction = Column("ServerCommunicatorReceiveAction", String(64))

    deviceReaderTypeId = Column(
        "DeviceReaderTypeId",
        Integer,
        ForeignKey("Dictionaries.DeviceReaderType.Id")
    )
    userId = Column(
        "UserId",
        Integer,
        ForeignKey("Admin.User.Id")
    )

    deviceReaderType = relationship("DeviceReaderType", back_populates="deviceReaders")
    user = relationship("User", back_populates="deviceReaders")

    accessPoints = relationship("AccessPoint", back_populates="deviceReader")
