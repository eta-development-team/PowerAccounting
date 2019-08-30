from dbaccess.dbcontext import Base
from dbmodels.dictionaries.dictionary_base import DictionaryBase


class BinaryContentType(DictionaryBase, Base):
    __tablename__ = "BinaryContentType"
