from dbaccess.dbcontext import Base
from dbmodels.dictionaries.dictionary_base import DictionaryBase


class PortType(DictionaryBase, Base):
    __tablename_ = "PortType"
