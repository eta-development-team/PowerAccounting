from sqlalchemy import Column
from sqlalchemy import String

from dbmodels.abstract.entity import Entity


class DictionaryBase(Entity):
    __table_args__ = {"schema": "Dictionaries"}

    code = Column("Code", String)
    description = Column("Description", String)

    def __str__(self):
        return self.description
