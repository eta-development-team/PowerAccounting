from dbaccess.dbcontext import Base
from dbmodels.dictionaries.dictionary_base import DictionaryBase


class DataBit(DictionaryBase, Base):
    __tablename_ = "DataBit"
