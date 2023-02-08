from multipledispatch import dispatch
from tables_classes import Database, Column, Table, Integer, String

def load_node_data(class_instance, row):
    title = row[4].strip()
    class_instance.title = title
    return class_instance


@dispatch(Database, list)
def load_data(class_instance, row):
    return load_node_data(class_instance,row)

@dispatch(Table, list)
def load_data(class_instance, row):
   return load_node_data(class_instance,row)

@dispatch(Column, list)
def load_data(class_instance, row):
    dtype_name = row[3].strip()
    if dtype_name == 'int':
        class_instance.dtype = Integer('integer')
    elif dtype_name == 'string':
        class_instance.dtype = String('string')
    return load_node_data(class_instance,row)