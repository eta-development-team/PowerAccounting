from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase, Column, String


class ResourceSystemType(DictionaryBase, Base):
    __tablename__ = "ResourceSystemType"

    shortName = Column("ShortName", String)
    channels = relationship("Channel", back_populates="resourceSystemType")
    parameters = relationship("Parameter", back_populates="resourceSystemType")
    agreementSystemParameters = relationship("AgreementSystemParameter", back_populates="resourceSystemType")


