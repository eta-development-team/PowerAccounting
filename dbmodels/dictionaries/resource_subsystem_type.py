from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class ResourceSubsystemType(DictionaryBase, Base):
    __tablename__ = "ResourceSubsystemType"
