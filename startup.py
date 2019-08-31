from dbaccess.dbcontext import DbContext
from dbaccess.dbcontext import MeasurementDevice

dbContext = DbContext()

query = dbContext.Session()\
    .query(MeasurementDevice)

measurementDevices = query.limit(10)

for md in measurementDevices:
    print(md.id, md)
    for c in md.channels:
        print("\t", c, c.measurementDevice.id, c.resourceSystemType, c.createdBy)


