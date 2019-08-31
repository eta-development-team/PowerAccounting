from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class TemperatureProfile(DictionaryBase, Base):
    __tablename__ = "TemperatureProfile"
