from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class ProcessingStatus(DictionaryBase, Base):
    __tablename__ = "ProcessingStatus"
