from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class City(DictionaryBase, Base):
    __tablename__ = "City"
    latinCode = Column("LatinCode", String)
    minimalTemperature = Column("MinimalTemperature", Integer)
    districts = relationship("District", back_populates="city")