from multipledispatch import dispatch
from tables_classes import Node, Database, Column, Table, Integer, String

@dispatch(Node, list)
def load_data(class_instance, row):
    title = row[4].strip()
    class_instance.title = title


@dispatch(Database, list)
def load_data(class_instance, row):
    load_data(class_instance,row)

@dispatch(Table, list)
def load_data(class_instance, row):
    load_data(class_instance,row)

@dispatch(Column, list)
def load_data(class_instance, row):
    load_data(class_instance,row)
    dtype_title = row[3].strip()
    if dtype_title == 'integer':
        class_instance.dtype = Integer()
    elif dtype_title == 'string':
        class_instance.dtype = String()