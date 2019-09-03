from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class StatusConnection(DictionaryBase, Base):
    __tablename__ = "StatusConnection"

    accessPoints = relationship("AccessPoint", back_populates="lastStatusConnection")

