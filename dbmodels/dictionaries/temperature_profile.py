from dbaccess.dbcontext import Base
from dbmodels.dictionaries.dictionary_base import DictionaryBase


class TemperatureProfile(DictionaryBase, Base):
    __tablename_ = "TemperatureProfile"
