from sqlalchemy import Column, Numeric, Integer, ForeignKey
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class ParameterDictionaryValue(DictionaryBase, Base):
    value = Column("Value", Numeric(19, 7))
    deviceId = Column(
        "DeviceId",
        Integer,
        ForeignKey("Dictionaries.Device.Id")
    )
    parameterDictionaryId = Column(
        "ParameterDictionaryId",
        Integer,
        ForeignKey("Dictionaries.ParameterDictionary.Id")
    )
    device = relationship("Device", back_populates="parameterDictionaryValue")
    parameterDictionary = relationship("ParameterDictionary", back_populates="parameterDictionaryValue")
