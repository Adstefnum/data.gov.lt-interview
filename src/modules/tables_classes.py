from dataclasses import dataclass

@dataclass
class Node:
     name:str
     title:str

@dataclass
class Database(Node):
     pass

@dataclass
class Table(Node):
     pass

@dataclass
class DataType:
     name:str

@dataclass
class Column(Node):
     dtype: DataType

class Integer(DataType):
     pass

class String(DataType):
     pass