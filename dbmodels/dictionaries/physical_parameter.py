from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Column

from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class PhysicalParameter(DictionaryBase, Base):
    __tablename__ = "PhysicalParameter"

    order = Column("Order", Integer)

    parameters = relationship("Parameter", back_populates="physicalParameter")
    measurementUnits = relationship("MeasurementUnit", back_populates="physicalParameter")
    agreementSystemParameters = relationship("AgreementSystemParameter", back_populates="physicalParameter")

