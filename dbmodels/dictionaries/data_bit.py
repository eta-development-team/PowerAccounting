from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class DataBit(DictionaryBase, Base):
    __tablename__ = "DataBit"
    devices = relationship("Device", back_populates="dataBit")
