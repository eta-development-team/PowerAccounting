from sqlalchemy import Column, Boolean

from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class NotificationType(DictionaryBase, Base):
    __tablename__ = "NotificationType"

    isActive = Column("IsActive", Boolean)
