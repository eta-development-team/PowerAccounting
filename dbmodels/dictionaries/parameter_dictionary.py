from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class ParameterDictionary(DictionaryBase, Base):
    __tablename__ = "ParameterDictionary"
