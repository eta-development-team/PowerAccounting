from sqlalchemy import Column, ForeignKey, Boolean
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.entity import Entity
from dbmodels.abstract.history_base import HistoryBase


class Channel(Base, Entity, HistoryBase):
    """Represents a Channel entity in a database"""

    __tablename__ = "Channel"
    __table_args__ = {"schema": "Business"}

    description = Column("Description", String(64))
    activated = Column("Activated", Boolean, default=True)
    order = Column("Order", Integer)

    channelTemplateId = Column(
        "ChannelTemplateId",
        Integer,
        ForeignKey("Business.ChannelTemplate.Id")
    )
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
    mnemoschemeId = Column(
        "MnemoschemeId",
        Integer,
        ForeignKey("Business.Mnemoscheme.Id")
    )
    organizationId = Column(
        "OrganizationId",
        Integer,
        ForeignKey("Business.Organization.Id")
    )
    measurementDevice = relationship("MeasurementDevice", back_populates="channels")
    resourceSystemType = relationship("ResourceSystemType", back_populates="channels")
    channelTemplate = relationship("ChannelTemplate", back_populates="channels")
    mnemoscheme = relationship("Mnemoscheme", back_populates="channels")
    organization = relationship("Organization", back_populates="channels")

    def __str__(self):
        return self.description
