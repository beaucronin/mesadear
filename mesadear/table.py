

class Table(object):
    from .base import Base
    def __init__(self, base: Base, table_name: str):
        self.base = base
        self.table_name = table_name
    
    def get_record(self, rec_id: str):
        from .record import Record
        return Record(self, rec_id)
        