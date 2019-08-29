from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base


class AccessPoint(Base):
    __tablename__ = "AccessPoint"
    __table_args__ = {"schema": "Business"}

    id = Column("Id", Integer, primary_key=True)
    description = Column("Description", String)
    measurementDevices = relationship(
        "MeasurementDevice",
        back_populates="accessPoint"
    )
