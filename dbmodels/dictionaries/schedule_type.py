from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class ScheduleType(DictionaryBase, Base):
    __tablename__ = "SeasonType"
