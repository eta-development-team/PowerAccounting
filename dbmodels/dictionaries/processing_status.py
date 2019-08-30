from dbaccess.dbcontext import Base
from dbmodels.dictionaries.dictionary_base import DictionaryBase


class ProcessingStatus(DictionaryBase, Base):
    __tablename_ = "ProcessingStatus"
