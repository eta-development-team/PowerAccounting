from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class TransportServerModel(DictionaryBase, Base):
    __tablename__ = "TransportServerModel"
