import urllib
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

from dbmodels.business import accesspoint, measurement_device, channel
from dbmodels.dictionaries import \
    baud, data_bit, stop_bit, parity, resource_system_type, \
    physical_parameter, \
    parameter, measurement_unit, device, agreement_system_parameter, \
    device_event_parameter, internal_device_event

from dbmodels.admin import role, user

# Dictionaries

Baud = baud.Baud
StopBit = stop_bit.StopBit
DataBit = data_bit.DataBit
Parity = parity.Parity
MeasurementUnit = measurement_unit.MeasurementUnit
ResourceSystemType = resource_system_type.ResourceSystemType
AgreementSystemParameter = agreement_system_parameter.AgreementSystemParameter
PhysicalParameter = physical_parameter.PhysicalParameter
Parameter = parameter.Parameter
Device = device.Device
DeviceEventParameter = device_event_parameter.DeviceEventParameter
InternalDeviceEvent = internal_device_event.InternalDeviceEvent

# Business
AccessPoint = accesspoint.AccessPoint
MeasurementDevice = measurement_device.MeasurementDevice
Channel = channel.Channel

# Admin
User = user.User
Role = role.Role


class DbContext:
    Session = sessionmaker()

    dns = ("DRIVER=SQL Server Native Client 11.0; \n"
           "SERVER=localhost\SQLSERVER2; \n"
           "DATABASE=EnergyTechAudit.PowerAccounting.Database; \n"
           "UID=sa;\n"
           "PWD=1D#4$Hm2")

    def __init__(self):
        params = urllib.parse.quote_plus(self.dns)
        engine = sa.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
        Base.metadata.bind = engine
        self.Session.configure(bind=engine)
