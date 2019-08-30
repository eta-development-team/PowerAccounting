from dbaccess.dbcontext import Base
from dbmodels.dictionaries.dictionary_base import DictionaryBase


class SeasonType(DictionaryBase, Base):
    __tablename__ = "SeasonType"
