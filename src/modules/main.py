from load_data_into_classes import load_data
from retrieve_data import get_data
from tables_classes import Node, Database, Column, Table, Integer, String

def run(table_data):

#[
# [DB, [table, [columns]], [table,[columns]]]
# [DB, [table, [columns]], [table,[columns]]]
# ]
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
        



    print(data)

        

if __name__ == "__main__":
    table_data = get_data()
    run(table_data)