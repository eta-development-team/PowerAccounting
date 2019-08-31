from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class TechnologicAdjunctionType(DictionaryBase, Base):
    __tablename__ = "TechnologicAdjunctionType"
