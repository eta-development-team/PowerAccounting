from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class TransportType(DictionaryBase, Base):
    __tablename__ = "TransportType"

    accessPoints = relationship("AccessPoint", back_populates="transportType")
