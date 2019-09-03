from geoalchemy2 import Geography
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.entity import Entity
from dbmodels.abstract.history_base import HistoryBase


class Organization(Base, Entity, HistoryBase):
    __tablename__ = "Organization"
    __table_args__ = {"schema": "Business"}

    description = Column("Description", String(256))
    fullAddress = Column("FullAddress", String(256))
    location = Column("Location", Geography(geometry_type='POINT', srid=4326))

    organizationTypeId = Column(
        "OrganizationTypeId",
        Integer,
        ForeignKey("Dictionaries.OrganizationType.Id")
    )

    organizationType = relationship("OrganizationType", back_populates="organizations")
    buildings = relationship("Building", back_populates="organization")
    channels = relationship("Channel", back_populates="organization")
