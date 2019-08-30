from sqlalchemy import Column, Integer, Binary


from dbaccess.dbcontext import Base
from dbmodels.dictionaries.dictionary_base import DictionaryBase


class Device(DictionaryBase, Base):
    __tablename__ = "Device"

    archiveDepthHour = Column("ArchiveDepthHour", Integer)
    archiveDepthDay = Column("ArchiveDepthDay", Integer)
    archiveDepthMonth = Column("ArchiveDepthMonth", Integer)
    shortName = Column("ShortName", Integer)
    image = Column("Image", Binary("MAX"))

