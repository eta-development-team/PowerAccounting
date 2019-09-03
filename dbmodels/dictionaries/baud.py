from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class Baud(DictionaryBase, Base):
    __tablename__ = "Baud"

    devices = relationship("Device", back_populates="baud")
    measurementDevices = relationship("MeasurementDevice", back_populates="baud")

