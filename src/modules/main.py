from load_data_into_classes import load_data
from retrieve_data import get_data
from tables_classes import Node, Database, Column, Table, Integer, String

def run(table_data):

    databases = []
    tables = []
    columns = []

    for row in table_data:
        if row[0].strip() and not row[1].strip() and not row[2].strip():
            databases.append(Database(name="DB", title=row[4].strip()))
        elif row[0].strip() and row[1].strip() and not row[2].strip():
            tables.append(Table(name="TBL", title=row[4].strip()))
        elif row[0].strip() and row[1].strip() and row[2].strip():
            column = Column(name=row[2].strip(), title=row[4].strip())
            load_data(column, row)
            columns.append(column)

    for database in databases:
        load_data(database, None)

    for table in tables:
        load_data(table, None)

    for column in columns:
        load_data(column, None)






if "__name__" == __main__:
    table_data = get_data()
    run(table_data)