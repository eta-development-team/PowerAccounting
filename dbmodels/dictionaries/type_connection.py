from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class TypeConnection(DictionaryBase, Base):
    __tablename__ = "TypeConnection"
