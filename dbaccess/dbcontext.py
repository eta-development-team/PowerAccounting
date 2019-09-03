import urllib
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

from dbmodels.business import accesspoint, \
    measurement_device, mnemoscheme, \
    channel_template, channel, device_reader, \
    organization, building, user_additional_info

from dbmodels.dictionaries import \
    baud, data_bit, stop_bit, parity, \
    resource_system_type, resource_subsystem_type, \
    transport_type, transport_server_model, physical_parameter, \
    parameter, measurement_unit, device_parameter, device, agreement_system_parameter, \
    device_event_parameter, internal_device_event, device_reader_type, \
    status_connection, com_port, port_type, mnemoscheme_type, \
    organization_type, building_purpose, district, gender, city

from dbmodels.admin import role, user


# Admin
User = user.User
Role = role.Role

# Dictionaries
Baud = baud.Baud
StopBit = stop_bit.StopBit
DataBit = data_bit.DataBit
Parity = parity.Parity
MeasurementUnit = measurement_unit.MeasurementUnit
ResourceSystemType = resource_system_type.ResourceSystemType
ResourceSubsystemType = resource_subsystem_type.ResourceSubsystemType
AgreementSystemParameter = agreement_system_parameter.AgreementSystemParameter
PhysicalParameter = physical_parameter.PhysicalParameter
Parameter = parameter.Parameter
TransportType = transport_type.TransportType
TransportServerModel = transport_server_model.TransportServerModel
DeviceParameter = device_parameter.DeviceParameter
Device = device.Device
deviceReaderType = device_reader_type.DeviceReaderType
DeviceEventParameter = device_event_parameter.DeviceEventParameter
InternalDeviceEvent = internal_device_event.InternalDeviceEvent
StatusConnection = status_connection.StatusConnection

# Business
DeviceReader = device_reader.DeviceReader
AccessPoint = accesspoint.AccessPoint
MeasurementDevice = measurement_device.MeasurementDevice
ChannelTemplate = channel_template.ChannelTemplate
Channel = channel.Channel


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
