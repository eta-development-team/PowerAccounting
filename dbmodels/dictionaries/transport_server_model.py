from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class TransportServerModel(DictionaryBase, Base):
    __tablename__ = "TransportServerModel"

    accessPoints = relationship("AccessPoint", back_populates="transportServerModel")
