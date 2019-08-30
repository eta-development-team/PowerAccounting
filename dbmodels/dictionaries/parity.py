from dbaccess.dbcontext import Base
from dbmodels.dictionaries.dictionary_base import DictionaryBase


class Parity(DictionaryBase, Base):
    __tablename_ = "Parity"
