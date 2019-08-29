from sqlalchemy.orm import relationship
from dbmodels.dictionaries.dictionarybase import DictionaryBase
from dbaccess.dbcontext import Base


class ResourceSystemType(DictionaryBase, Base):
    __tablename__ = "ResourceSystemType"

    channels = relationship("Channel", back_populates="resourceSystemType")

    def __str__(self):
        return self.description
