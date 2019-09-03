from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class DeviceReaderType(DictionaryBase, Base):
    __tablename__ = "DeviceReaderType"

    deviceReaders = relationship("DeviceReader", back_populates="deviceReaderType")
