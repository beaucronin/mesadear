# from .base import Base
# from .table import Table
# from .record import Record
from mesadear import Base, Table, Record

APP_ID = 'app0hvWRfvw4zG1u8'

base = Base(APP_ID, apikey='keymQOHiFteAFDHEG')
table = base.get_table('Problem')
record = table.get_record('rechOp2DvbgGzmMHg')

print(record.Description)
print(record.Name)