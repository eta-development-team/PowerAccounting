from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class OrganizationType(Base, DictionaryBase):
    __tablename__ = "OrganizationType"

    organizations = relationship("Organization", back_populates="organizationType")
