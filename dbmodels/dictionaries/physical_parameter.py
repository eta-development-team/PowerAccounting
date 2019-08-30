from sqlalchemy import ForeignKey

from dbmodels.dictionaries.dictionary_base import DictionaryBase, Integer, Column
from dbaccess.dbcontext import Base


class PhysicalParameter(DictionaryBase, Base):
    __tablename__ = "PhysicalParameter"

    order = Column("Order", Integer)


class Parameter(DictionaryBase, Base):
    __tablename__ = "Parameter"
    physicalParameterId = Column(
        "PhysicalParameterId",
        Integer,
        ForeignKey("Dictionaries.PhysicalParameter.Id")
    )
    resourceSystemTypeId = Column(
        "ResourceSystemTypeId",
        Integer,
        ForeignKey("Dictionaries.ResourceSystemType.Id")
    )

