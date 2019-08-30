from dbaccess.dbcontext import Base
from dbmodels.dictionaries.dictionary_base import DictionaryBase


class Baud(DictionaryBase, Base):
    __tablename_ = "Baud"
