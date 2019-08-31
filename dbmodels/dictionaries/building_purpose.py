from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class BuildingPurpose(DictionaryBase, Base):
    __tablename__ = "BuildingPurpose"
