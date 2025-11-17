from enum import Enum


class DataType(Enum):
    """
    Types of data
    """
    
    String = "String"
    StringList = "StringList"
    Numeric = "Numeric"
    Integer = "Integer"
    Boolean = "Boolean"
    Enumeration = "Enumeration"
    Binary = "Binary"
    Guid = "Guid"