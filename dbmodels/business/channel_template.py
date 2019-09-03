from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.entity import Entity
from dbmodels.abstract.history_base import HistoryBase


class ChannelTemplate(Base, Entity, HistoryBase):
    __tablename__ = "ChannelTemplate"
    __table_args__ = {"schema": "Business"}

    description = Column("Description", String)
    comment = Column("Comment", String)
    resourceSystemTypeId = Column(
        "ResourceSystemTypeId",
        Integer,
        ForeignKey("Dictionaries.ResourceSystemType.Id")
    )
    resourceSubsystemTypeId = Column(
        "ResourceSubsystemTypeId",
        Integer,
        ForeignKey("Dictionaries.ResourceSubsystemType.Id")
    )
    mnemoschemeId = Column(
        "MnemoschemeId",
        Integer,
        ForeignKey("Business.Mnemoscheme.Id")
    )
    deviceId = Column(
        "DeviceId",
        Integer,
        ForeignKey("Dictionaries.Device.Id")
    )

    device = relationship("Device", back_populates="channelTemplates")
    resourceSystemType = relationship("ResourceSystemType", back_populates="channelTemplates")
    resourceSubsystemType = relationship("ResourceSubsystemType", back_populates="channelTemplates")

    channels = relationship("Channel", back_populates="channelTemplate")
