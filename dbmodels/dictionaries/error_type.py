from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class ErrorType(DictionaryBase, Base):
    __tablename__ = "ErrorType"
