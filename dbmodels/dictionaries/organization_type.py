from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class OrganizationType(DictionaryBase, Base):
    __tablename__ = "OrganizationType"
