from src.modules.read_and_print_data_utils import read_data_into_printable_format
from src.modules.tables_classes import Database, Table, Column, Integer
import pytest




@pytest.mark.parametrize("get_data", ["small"], indirect=True)
def test_read_data_into_printable_format_with_small_data(get_data):
    data = read_data_into_printable_format(get_data)

    # Assert that there is only one database
    assert len(data) == 1

    # Assert that the database has a name and a title
    database = data[0][0]
    assert isinstance(database, Database)
    assert database.name == 'DB'
    assert database.title == 'DB 1'

    # Assert that the database has only one table
    tables = data[0][1:]
    assert len(tables) == 1

    # Assert that the table has a name and a title
    table = tables[0][0]
    assert isinstance(table, Table)
    assert table.name == 'TBL'
    assert table.title == 'TBL 1'

    # Assert that the table has only one column
    columns = tables[0][1]
    assert len(columns) == 1

    # Assert that the column has a name, a title, and a dtype
    column = columns[0]
    assert isinstance(column, Column)
    assert column.name == 'COL1'
    assert column.title == 'Column 1'
    assert isinstance(column.dtype, Integer)


@pytest.mark.parametrize("get_data", ["large"], indirect=True)
def test_read_data_into_printable_format_with_large_data(get_data):
    data = read_data_into_printable_format(get_data)

    # Assert that the first database has a name and a title
    database1 = data[0][0]
    assert isinstance(database1, Database)
    assert database1.name == 'DB'
    assert database1.title == 'DB 1'

    # Assert that the first table has a name and a title
    tables1 = data[0][1:]
    table1 = tables1[0][0]
    assert isinstance(table1, Table)
    assert table1.name == 'TBL'
    assert table1.title == 'TBL 1'

    # Assert that the first column has a name, a title, and a dtype
    columns1 = tables1[0][1]
    column1 = columns1[0]
    assert isinstance(column1, Column)
    assert column1.name == 'COL1'
    assert column1.title == 'Column 1'
    assert isinstance(column1.dtype, Integer)

    database2 = data[1][0]
    assert isinstance(database2, Database)
    assert database2.name == 'DB'
    assert database2.title == 'DB 2'

    tables2 = data[1][1:]
    # Assert that the first and second tables has a name and a title
    table1 = tables2[0][0]
    assert isinstance(table1, Table)
    assert table1.name == 'TBL'
    assert table1.title == 'TBL 2'

    table2 = tables2[1][0]
    assert isinstance(table2, Table)
    assert table2.name == 'TBL'
    assert table2.title == 'TBL 3'


def test_read_data_into_printable_format_continue_statement():
    table_data = [
        ["db 1", "", "", "","Database 1"],
        ["", "", "", "",""]
    ]

    result = read_data_into_printable_format(table_data)

    # Verify that the continue statement was executed
    assert result == [
        [Database("db 1","Database 1")]


    ]


@pytest.mark.parametrize('get_data', ['small', 'large'], indirect=True)
def test_read_data_into_printable_format_output(get_data):
    data = read_data_into_printable_format(get_data)
    assert isinstance(data, list)


@pytest.mark.parametrize('get_data', ['small', 'large'], indirect=True)
def test_read_data_into_printable_format_database_count(get_data):
    data = read_data_into_printable_format(get_data)
    if get_data == 'small':
        assert len(data) == 1
    elif get_data == 'large':
        assert len(data) == 2


@pytest.mark.parametrize('get_data', ['small', 'large'], indirect=True)
def test_read_data_into_printable_format_table_count(get_data):
    data = read_data_into_printable_format(get_data)
    if get_data == 'small':
        assert len(data[0]) == 2
    elif get_data == 'large':
        assert len(data[0]) == 2
        assert len(data[1]) == 3


@pytest.mark.parametrize('get_data', ['small', 'large'], indirect=True)
def test_read_data_into_printable_format_column_count(get_data):
    data = read_data_into_printable_format(get_data)
    if get_data == 'small':
        assert len(data[0][1][1]) == 1
    elif get_data == 'large':
        assert len(data[0][1][1]) == 1
        assert len(data[0][2][1]) == 2
        assert len(data[1][1][1]) == 2
        assert len(data[1][2][1]) == 2
        assert len(data[1][3][1]) == 1
