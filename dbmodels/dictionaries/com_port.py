from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class ComPort(DictionaryBase, Base):
    __tablename__ = "ComPort"

    measurementDevices = relationship("MeasurementDevice", back_populates="comPort")
