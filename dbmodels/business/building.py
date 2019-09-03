from geoalchemy2 import Geography
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.entity import Entity
from dbmodels.abstract.history_base import HistoryBase


class Building(Base, Entity, HistoryBase):
    __tablename__ = "Building"
    __table_args__ = {"schema": "Business"}

    description = Column("Description", String(64))
    fullAddress = Column("FullAddress", String(256))
    square = Column("Square", Float, default=0.0)
    countFlats = Column("CountFlats", Integer, default=0)
    location = Column("Location", Geography(geometry_type='POINT', srid=4326))

    buildingPurposeId = Column(
        "BuildingPurposeId",
        Integer,
        ForeignKey("Dictionaries.BuildingPurpose.Id")
    )
    districtId = Column(
        "DistrictId",
        Integer,
        ForeignKey("Dictionaries.District.Id")
    )
    organizationId = Column(
        "OrganizationId",
        Integer,
        ForeignKey("Business.Organization.Id")
    )

    buildingPurpose = relationship("BuildingPurpose", back_populates="buildings")
    district = relationship("District", back_populates="buildings")
    organization = relationship("Organization", back_populates="buildings")
    userAdditionalInfo = relationship("UserAdditionalInfo", back_populates="buildings")


