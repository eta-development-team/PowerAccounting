from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class Parameter(DictionaryBase, Base):
    __tablename__ = "Parameter"

    shortDescription = Column("ShortDescription", String)
    integrableValue = Column("IntegrableValue", Boolean)
    physicalParameterId = Column(
        "PhysicalParameterId",
        Integer,
        ForeignKey("Dictionaries.PhysicalParameter.Id")
    )
    resourceSystemTypeId = Column(
        "ResourceSystemTypeId",
        Integer,
        ForeignKey("Dictionaries.ResourceSystemType.Id")
    )

    physicalParameter = relationship("PhysicalParameter", back_populates="parameters")
    resourceSystemType = relationship("ResourceSystemType", back_populates="parameters")
