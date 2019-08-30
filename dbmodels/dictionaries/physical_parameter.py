from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.dictionaries.dictionary_base import DictionaryBase, Integer, Column


class PhysicalParameter(DictionaryBase, Base):
    __tablename__ = "PhysicalParameter"

    order = Column("Order", Integer)

    parameters = relationship("Parameter", back_populates="physicalParameter")
    measurementUnits = relationship("MeasurementUnit", back_populates="physicalParameter")
