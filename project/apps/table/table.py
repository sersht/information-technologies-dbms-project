from copy import deepcopy
from json import dump, load
from pathlib import Path
from os import remove

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
            if not isinstance(value[i], self.types[i]):
                raise ValueError(
                    i + '-th field should be type ' + str(self.types[i]) + 
                    ' instead of ' + str(type(value[i])))

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
        tablePath = self.creatorDb.root + name + '.table'
        with open(tablePath, 'w') as file:
            dump(self.__dict__, file)

    def deleteFromStorage(self):
        tablePath = self.creatorDb.root + name + '.table'
        if Path(tablePath).is_file():
            remove(tablePath)
        else:
            raise Exception('Deleting non existing file')

    def update(self, recordIndex, fieldIndex, value):
        if not isinstance(value, self.types[fieldIndex]):
            raise ValueError(
                'New value type should be ' + str(self.types[fieldIndex]) +
                ' instead of ' + str(type(value)))
        
        self.records[recordIndex][fieldIndex] = value

