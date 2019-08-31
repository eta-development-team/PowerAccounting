from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class Gender(DictionaryBase, Base):
    __tablename__ = "Gender"