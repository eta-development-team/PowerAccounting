from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class PeriodType(DictionaryBase, Base):
    __tablename__ = "PeriodType"
