import pytest
from src.modules.tables_classes import Database, Table, Column, Integer, String
from src.modules.load_data_into_classes import load_data, load_node_data

def test_load_node_data():
    pass

def test_load_data_for_database():
    row = ['DB', '', '', '', 'DB 1']
    database = Database(name=row[1],title='')
    database = load_data(database, row)
    assert database.title == 'DB 1'

   
def test_load_data_for_table():
    row = ['', 'TBL', '', '', 'TBL 1']
    table = Table(name=row[2],title='')
    table = load_data(table, row)
    assert table.title == 'TBL 1'

def test_load_data_for_column_with_integer_datatype():
    row = ['', '', 'COL1', 'int', 'Column 1']
    column = Column(name=row[3],title='',dtype=None)
    column = load_data(column, row)
    assert column.title == 'Column 1'
    assert isinstance(column.dtype, Integer)

def test_load_data_for_column_with_string_datatype():
    row = ['', '', 'COL1', 'string', 'Column 2']
    column = Column(name=row[3],title='',dtype=None)
    column = load_data(column, row)
    assert column.title == 'Column 2'
    assert isinstance(column.dtype, String)
