from dbaccess.dbcontext import Base
from dbmodels.dictionaries.dictionary_base import DictionaryBase


class StopBit(DictionaryBase, Base):
    __tablename_ = "StopBit"
