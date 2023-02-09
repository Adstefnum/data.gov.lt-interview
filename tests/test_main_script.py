from src.modules.read_and_print_data_utils import read_data_into_printable_format
from src.modules.retrieve_data import get_data
from src.modules.read_and_print_data_utils import pretty_print_data
from prettytable import PrettyTable


def test_main_script():
    table_data = get_data()
    data = read_data_into_printable_format(table_data)
    table = pretty_print_data(data)
    assert table is not None
    assert isinstance(table, PrettyTable)

    assert table.rowcount == 11
    assert len(table.field_names) == 5