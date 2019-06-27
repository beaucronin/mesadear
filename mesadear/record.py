from typing import Any, Dict
from .table import Table


class Record(object):
    
    def __init__(self, table: Table, record_id: str):
        self.table = table
        self.record_id = record_id
        self.is_fetched = False
        self.data: Dict[str, Any]
    
    def _maybe_fetch(self):
        if not self.is_fetched:
            self._fetch()
    
    def _fetch(self):
        conn: Connection = self.table.base.conn
        self.data = conn.retrieve_record(self.table.table_name, self.record_id)
        self.is_fetched = True

    def fetched(func):
        # @wraps(func)
        def wrapper(self, *args, **kwargs):
            self._maybe_fetch()
            return func(self, *args, **kwargs)
        
        return wrapper
    
    # @fetched
    def __getattr__(self, field_name):
        self._maybe_fetch()
        return self.data['fields'].get(field_name, None)
    
    fetched = staticmethod(fetched)
