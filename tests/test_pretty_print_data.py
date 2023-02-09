from src.modules.read_and_print_data_utils import pretty_print_data
from src.modules.tables_classes import Database, Integer, Table, Column, String
from prettytable import PrettyTable

# Test 1: Check if the function returns a PrettyTable object
def test_pretty_print_data_output_type():
    data = [
        [Database("db1", "Database 1"), [Table("tb1", "Table 1"), [Column("col1", "int", "Column 1")]]]
    ]
    result = pretty_print_data(data)
    assert isinstance(result, PrettyTable), f"Expected type 'PrettyTable', but got {type(result)}"

# Test 2: Check if the function correctly displays the database name, table name, and column name, type, and title
def test_pretty_print_data_output_content():
    data = [
        [Database("db1", "Database 1"), [Table("tb1", "Table 1"), [Column("col1", "Column 1", Integer(name='integer'))]]],
        [Database("db2", "Database 2"), [Table("tb2", "Table 2"), [Column("col2", "Column 2", Integer(name='integer')), Column("col3", "Column 3",String(name='string'))]]],
    ]
    result = pretty_print_data(data)
    expected_output = PrettyTable(["database", "table", "column", "type", "title"])
    expected_output.align["database"] = "l"
    expected_output.align["table"] = "l"
    expected_output.align["column"] = "l"
    expected_output.align["type"] = "l"
    expected_output.align["title"] = "l"
    expected_output.add_row(["db1","","","","Database 1"])
    expected_output.add_row(["","tb1","","","Table 1"])
    expected_output.add_row(["","","col1", Integer(name='integer'),"Column 1"])
    expected_output.add_row(["db2","","","","Database 2"])
    expected_output.add_row(["","tb2","","","Table 2"])
    expected_output.add_row(["","","col2", Integer(name='integer'),"Column 2"])
    expected_output.add_row(["","","col3",String(name='string'),"Column 3"])

    assert str(result) == str(expected_output), f"Expected output:\n{expected_output}\n\nGot:\n{str(result)}"

# Test 3: Check if the function handles an empty input
def test_pretty_print_data_empty_input():
    data = []
    result = pretty_print_data(data)
 
    expected_output = PrettyTable(["database", "table", "column", "type", "title"])

    assert str(result) == str(expected_output), f"Expected output:\n{expected_output}\n\nGot:\n{str(result)}"
