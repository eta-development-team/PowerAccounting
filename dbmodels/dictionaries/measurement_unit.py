from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.dictionaries.dictionary_base import DictionaryBase


class MeasurementUnit(DictionaryBase, Base):
    __tablename__ = "MeasurementUnit"

    physicalParameterId = Column(
        "PhysicalParameterId",
        Integer,
        ForeignKey("Dictionaries.PhysicalParameter.Id")
    )
    physicalParameter = relationship("PhysicalParameter", back_populates="measurementUnits")
