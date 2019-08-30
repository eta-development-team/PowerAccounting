from dbaccess.dbcontext import Base
from dbmodels.dictionaries.dictionary_base import DictionaryBase


class TypeConnection(DictionaryBase, Base):
    __tablename_ = "TypeConnection"
