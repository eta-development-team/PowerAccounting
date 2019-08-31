from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class StatusConnection(DictionaryBase, Base):
    __tablename__ = "StatusConnection"
