from dbaccess.dbcontext import Base
from dbmodels.dictionaries.dictionary_base import DictionaryBase


class SubsystemType(DictionaryBase, Base):
    __tablename__ = "SubsystemType"
