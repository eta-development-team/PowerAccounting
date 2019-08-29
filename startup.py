from dbaccess.dbcontext import DbContext
from dbaccess.dbcontext import MeasurementDevice

dbContext = DbContext()

measurementDevices = dbContext.Session()\
    .query(MeasurementDevice)\
    .limit(10)

for md in measurementDevices:
    print(md)
    for c in md.channels:
        print("\t", c, c.measurementDevice.id, c.resourceSystemType)


