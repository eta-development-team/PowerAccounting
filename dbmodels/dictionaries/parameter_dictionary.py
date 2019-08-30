from dbaccess.dbcontext import Base
from dbmodels.dictionaries.dictionary_base import DictionaryBase


class ParameterDictionary(DictionaryBase, Base):
    __tablename__ = "ParameterDictionary"
