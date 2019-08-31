from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class PlacementPurpose(DictionaryBase, Base):
    __tablename__ = "PlacementPurpose"
