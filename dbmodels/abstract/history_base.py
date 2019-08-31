from sqlalchemy import Column
from sqlalchemy import String, DateTime


class HistoryBase:
    createdBy = Column("CreatedBy", String)
    createdDate = Column("CreatedDate", DateTime)
    updatedBy = Column("UpdatedBy", String)
    updatedDate = Column("UpdatedDate", DateTime)
