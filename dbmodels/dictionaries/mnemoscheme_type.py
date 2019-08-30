from dbaccess.dbcontext import Base
from dbmodels.dictionaries.dictionary_base import DictionaryBase


class MnemoschemeType(DictionaryBase, Base):
    __tablename__ = "MnemoschemeType"
