import json
import os
from copy import deepcopy
from pathlib import Path
from project.apps.table.data_converter import DataConverter
from project.apps.table.customtypes.types_map import TYPE_BY_CODE


# Temporary storing all records in table as two-dimensional list (array)
# Maybe later will switch on dictionaries or objects if needed
# Consequences are as follows:
# 1) can only "append" and "pop" (insert/delete in/from the back of table) in O(1) time-complexity
# 2) arbitrary insertion/deletion using O(len(records)) time-complexity


class Table:

    @staticmethod
    def create(name, columnNames, columnTypes):

        if len(columnNames) != len(columnTypes):
            raise ValueError('Unequal length of column-type and column-name lists!')

        if len(set(columnNames)) != len(columnNames):
            raise ValueError('Column names should be unique!')

        if any(typeCode not in TYPE_BY_CODE.keys() for typeCode in columnTypes):
            raise ValueError('Unsupported type!')

        table = Table()
        table.name = name
        table.columns = columnNames
        table.types = columnTypes
        table.records = []

        table.saveOnDatabase()

        return table

    @staticmethod
    def restore(configPath):
        if not Path(configPath).is_file():
            raise Exception('Restoring table from non existing file')

        table = Table()

        with open(configPath, 'r') as file:
            deserializedDict = json.load(file)

        for i in range(len(deserializedDict['records'])):
            for j in range(len(deserializedDict['records'][i])):
                Type = TYPE_BY_CODE[deserializedDict['types'][j]]
                deserializedDict['records'][i][j] = DataConverter.deserialize(deserializedDict['records'][i][j], Type)

        table.__dict__ = deserializedDict

        return table

    def _checkIfisLegalToInsert(self, values):
        if len(values) < len(self.columns):
            raise ValueError('Add some fiels to create a record for ' + self.name + ' table')

        if len(values) > len(self.columns):
            raise ValueError('Remove some fiels to create a record for ' + self.name + ' table')

        for i in range(len(values)):
            neededType = TYPE_BY_CODE[self.types[i]]

            if not isinstance(values[i], neededType):
                presentedType = type(values[i])
                raise ValueError(str(i) + '-th field should be type ' + str(neededType) +
                                 ' instead of ' + str(presentedType))

    # TODO: values should be list
    # TODO: not sure, maybe replace with just .insert() - need to read docs
    # TODO: think about better index management
    def insert(self, values, index=None):
        self._checkIfisLegalToInsert(values)

        if index is None:
            self.records.append(deepcopy(values))
        else:
            self.records.insert(index, deepcopy(values))

    # TODO: think about better index management
    def update(self, recordIndex, fieldName, value):
        # TODO: add check if is legal to update
        # TODO: replace with smth better complexity
        fieldIndex = self.columns.index(fieldName)
        neededType = TYPE_BY_CODE[self.types[fieldIndex]]

        if not isinstance(value, neededType):
            raise ValueError(
                'New value type should be ' + str(neededType) +
                ' instead of ' + str(type(value)))

        self.records[recordIndex][fieldIndex] = value

    # TODO: think about better index management
    def delete(self, index=None):
        if not self.records:
            raise Exception("Can't remove record from empty table")

        if index is None:
            self.records.pop()
        else:
            self.records.pop(index)

    def saveOnDatabase(self):
        tablePath = os.sep.join([self.creatorDbRoot, self.name + '.table'])
        serializedDict = deepcopy(self.__dict__)

        for i in range(len(serializedDict['records'])):
            for j in range(len(serializedDict['records'][i])):
                serializedDict['records'][i][j] = DataConverter.serialize(serializedDict['records'][i][j])

        with open(tablePath, 'w') as file:
            json.dump(serializedDict, file)

    def deleteFromStorage(self):
        tablePath = os.sep.join([self.creatorDbRoot, self.name + '.table'])
        if not Path(tablePath).is_file():
            raise Exception('Deleting non existing file')
        os.remove(tablePath)
