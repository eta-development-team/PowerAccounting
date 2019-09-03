from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class District(DictionaryBase, Base):
    __tablename__ = "District"

    cityId = Column("CityId", Integer, ForeignKey("Dictionaries.City.Id"))

    city = relationship("City", back_populates="districts")
    buildings = relationship("Building", back_populates="district")
