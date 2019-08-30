from dbaccess.dbcontext import Base
from dbmodels.dictionaries.dictionary_base import DictionaryBase


class TransportType(DictionaryBase, Base):
    __tablename_ = "TransportType"
