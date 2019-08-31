from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class StopBit(DictionaryBase, Base):
    __tablename__ = "StopBit"
    devices = relationship("Device", back_populates="stopBit")
