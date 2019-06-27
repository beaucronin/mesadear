from typing import Iterable, List, Optional
from .util import create_connection

class Base(object):

    
    def __init__(self, app_id, apikey: Optional[str]=None):
        self.conn = create_connection(app_id, apikey)
    
    def tables(self) -> List[str]:
        pass
    
    def get_table(self, table_name: str):
        from .table import Table
        return Table(self, table_name)
    
