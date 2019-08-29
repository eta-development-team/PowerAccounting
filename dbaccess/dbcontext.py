import urllib
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

from dbmodels.business import accesspoint, user, measurementdevice, role, channel

AccessPoint = accesspoint.AccessPoint;
MeasurementDevice = measurementdevice.MeasurementDevice
Channel = channel.Channel
User = user.User
Role = role.Role


class DbContext:
    Session = sessionmaker()

    dns = """DRIVER=SQL Server Native Client 11.0; 
            SERVER=localhost\SQLSERVER2; 
            DATABASE=EnergyTechAudit.PowerAccounting.Database; 
            UID=sa;
            PWD=1D#4$Hm2"""

    def __init__(self):
        params = urllib.parse.quote_plus(self.dns)
        engine = sa.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
        Base.metadata.bind = engine
        self.Session.configure(bind=engine)
