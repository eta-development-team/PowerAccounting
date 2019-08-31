from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class DeviceParameter(DictionaryBase, Base):
    __tablename__ = "DeviceParameter"
    deviceId = Column("DeviceId", Integer, ForeignKey("Dictionaries.Device.Id"))
    device = relationship("Device", back_populates="deviceParameters")