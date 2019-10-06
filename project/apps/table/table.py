import json
import os
from copy import deepcopy
from pathlib import Path
from customtypes.TypesMap import TYPE_BY_CODE 

# Temporary storing all records in table as two-dimensional list (array)
# Maybe later will switch on dictionaries or objects if needed
# Consequences are as follows: 
# 1) can only "append" and "pop" (insert/delete in/from the back of table) in O(1) time-complexity
# 2) arbitrary insertion/deletion using O(len(records)) time-complexity

class Table:

    def __init__(self, name, columnNames, columnTypes, databaseRoot):
        if len(columnNames) != len(columnTypes):
            raise ValueError(
                'Unequal length of column-type and column-name lists')

        self.creatorDbRoot = databaseRoot
        self.name = name
        self.columns = columnNames
        self.types = columnTypes
        self.records = []

    def _checkTypesOf(self, values):
        for i in range(len(values)):
            neededType = TYPE_BY_CODE[self.types[i]]
            if not isinstance(values[i], neededType):
                raise ValueError(
                    i + '-th field should be type ' + str(neededType) + 
                    ' instead of ' + str(type(values[i])))

    def _checkLengthOf(self, values):
        if len(values) != len(self.columns):
            raise ValueError(
                ('Add' if len(values) < len(self.columns) else 'Remove') +
                ' some fiels to create record for ' + self.name + ' table')

    # TODO: values should be list
    # TODO: not sure, maybe replace with just .insert() - need to read docs
    # TODO: think about better index management
    def insert(self, values, index=None):
        self._checkLengthOf(values)
        self._checkTypesOf(values)
    
        if index is None:
            self.records.append(deepcopy(values))
        else:
            self.records.insert(index, deepcopy(values))

    # TODO: think about better index management
    def delete(self, index=None):
        if not self.records:
            raise Exception("Can't remove record from empty table")
        
        if index is None:
            self.records.pop()
        else:
            self.records.pop(index)

    def saveOnStorage(self):
        tablePath = self.creatorDbRoot + self.name + '.table'
        with open(tablePath, 'w') as file:
            json.dump(self.__dict__, file)

    def deleteFromStorage(self):
        tablePath = self.creatorDbRoot + self.name + '.table'
        if Path(tablePath).is_file():
            os.remove(tablePath)
        else:
            raise Exception('Deleting non existing file')

    def update(self, recordIndex, fieldIndex, value):
        neededType = TYPE_BY_CODE[self.types[fieldIndex]]
        if not isinstance(value, neededType):
            raise ValueError(
                'New value type should be ' + str(neededType) +
                ' instead of ' + str(type(value)))
        
        self.records[recordIndex][fieldIndex] = value
