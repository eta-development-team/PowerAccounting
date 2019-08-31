from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class ComPort(DictionaryBase, Base):
    __tablename_ = "ComPort"
