from sqlalchemy import Numeric, String, Column

from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class Dimension(DictionaryBase, Base):
    __tablename__ = "Dimension"
    Prefix = Column("prefix", String)
    Value = Column("value", Numeric(20, 7))
