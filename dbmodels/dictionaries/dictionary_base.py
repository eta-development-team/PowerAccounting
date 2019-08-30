from sqlalchemy import Column
from sqlalchemy import Integer, String


class DictionaryBase:
    __table_args__ = {"schema": "Dictionaries"}
    id = Column("Id", Integer, primary_key=True)
    code = Column("Code", String)
    description = Column("Description", String)

    def __str__(self):
        return self.description
