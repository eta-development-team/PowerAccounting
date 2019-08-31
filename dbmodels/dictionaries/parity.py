from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class Parity(DictionaryBase, Base):
    __tablename__ = "Parity"
    devices = relationship("Device", back_populates="parity")
