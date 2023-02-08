import pytest
from src.modules.tables_classes import Database, Table, Column, Integer, String
from src.modules.load_data_into_classes import load_data, load_node_data

def test_load_node_data_for_database():
    row = ['DB', '', '', '', 'DB 1']
    database = Database(name=row[0],title='')
    result = load_node_data(database,row)

    assert isinstance(result, Database)
    assert result == database
    assert result.title == row[4].strip()

def test_load_node_data_for_table():
    row = ['DB', '', '', '', 'DB 1']
    table = Table(name=row[1],title='')
    result = load_node_data(table,row)

    assert result == table
    assert isinstance(result, Table)
    assert result.title == row[4].strip()

def test_load_node_data_for_column_with_integer_datatype():
    row = ['', '', 'COL1', 'int', 'Column 1']
    column = Column(name=row[2],title='',dtype=None)
    result = load_node_data(column, row)
    assert result == column
    assert isinstance(result, Column)
    assert result.title == row[4].strip()

   
def test_load_data_for_database():
    row = ['DB', '', '', '', 'DB 1']
    database = Database(name=row[0],title='')
    database = load_data(database, row)
    assert database.title == 'DB 1'



   
def test_load_data_for_table():
    row = ['', 'TBL', '', '', 'TBL 1']
    table = Table(name=row[1],title='')
    table = load_data(table, row)
    assert table.title == 'TBL 1'

def test_load_data_for_column_with_integer_datatype():
    row = ['', '', 'COL1', 'int', 'Column 1']
    column = Column(name=row[2],title='',dtype=None)
    column = load_data(column, row)
    assert column.title == 'Column 1'
    assert isinstance(column.dtype, Integer)

def test_load_data_for_column_with_string_datatype():
    row = ['', '', 'COL1', 'string', 'Column 2']
    column = Column(name=row[2],title='',dtype=None)
    column = load_data(column, row)
    assert column.title == 'Column 2'
    assert isinstance(column.dtype, String)
