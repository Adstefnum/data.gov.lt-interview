from .load_data_into_classes import load_data
from .tables_classes import Database, Column, Table
from prettytable import PrettyTable

def read_data_into_printable_format(table_data):

    data = []
    database_count, table_count= -1,0
    for row in table_data:
        database_name = row[0].strip()
        table_name = row[1].strip()
        column_name = row[2].strip()
        
        if database_name:
            database = Database(name=database_name, title='')
            fully_loaded_database = load_data(database, row)
            data.append([fully_loaded_database])
            database_count += 1
            table_count = 0
            
        elif table_name:
            table = Table(name=table_name, title='')
            fully_loaded_table = load_data(table, row)
            data[database_count].append([fully_loaded_table, []]) 
            table_count += 1

        elif column_name:
            column = Column(name=column_name, title='', dtype=None)
            fully_loaded_column = load_data(column, row)
            data[database_count][table_count][1].append(fully_loaded_column)
        
        else:
            continue

    return data

#[
# [DB, [table, [columns]], [table,[columns]]]
# [DB, [table, [columns]], [table,[columns]]]
# ]
def pretty_print_data(data):
    table = PrettyTable(["database", "table", "column", "type", "title"])
    table.align["database"] = "l"
    table.align["table"] = "l"
    table.align["column"] = "l"
    table.align["type"] = "l"
    table.align["title"] = "l"

    for data_entry in data:
        for data_entry_contents in data_entry:
            if type(data_entry_contents) == Database:
                table.add_row([data_entry_contents.name,"","","",data_entry_contents.title])
            elif type(data_entry_contents) == list:
                for entry in data_entry_contents:
                    if type(entry) == Table:
                        table.add_row(["",entry.name,"","",entry.title])
                    elif type(entry) == list:
                        for column in entry:
                            table.add_row(["","",column.name,column.dtype, column.title])
  
    return table