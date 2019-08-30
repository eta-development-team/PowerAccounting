from dbaccess.dbcontext import Base
from dbmodels.dictionaries.dictionary_base import DictionaryBase


class ProtocolSubType(DictionaryBase, Base):
    __tablename__ = "ProtocolSubType"
