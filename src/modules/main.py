from read_and_print_data_utils import read_data_into_printable_format, pretty_print_data
from retrieve_data import get_data

if __name__ == "__main__":
    table_data = get_data()
    data = read_data_into_printable_format(table_data)
    table = pretty_print_data(data)
    print(table)
   