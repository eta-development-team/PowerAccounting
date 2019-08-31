from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class AgreementSystemParameter(DictionaryBase, Base):
    __tablename__ = "AgreementSystemParameter"
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
    physicalParameter = relationship("PhysicalParameter", back_populates="agreementSystemParameters")
    resourceSystemType = relationship("ResourceSystemType", back_populates="agreementSystemParameters")
