import unittest
from unittest.mock import patch
from project.apps.table.table import Table


class TestTableCreate(unittest.TestCase):

    def test_create_non_unique_columns(self):
        with self.assertRaises(ValueError):
            table = Table.create('', ['123', '123'], [], '')

    def test_create_unequal_params_length(self):
        with self.assertRaises(ValueError):
            table = Table.create('', ['123', ], ['int', 'str'], '')

    def test_create_unsupported_type(self):
        with self.assertRaises(ValueError):
            table = Table.create('', ['123'], ['unsupportedtype'], '')

    @patch('project.apps.table.table.Table.saveOnStorage')
    def test_create(self, saveOnStorage):
        table = Table.create('', [], [], '')

        self.assertEqual(table.creatorDbRoot, '')
        self.assertEqual(table.name, '')
        self.assertEqual(table.columns, [])
        self.assertEqual(table.types, [])
        self.assertEqual(table.records, [])
        self.assertEqual(saveOnStorage.call_count, 1)

class TestTableInsert(unittest.TestCase):

    @patch('project.apps.table.table.Table.saveOnStorage')
    def setUp(self, saveOnStorage):
        self.table = Table.create(
            name='name', 
            columnNames=['int', 'float', 'str', 'segment', 'image'], 
            columnTypes=['int', 'float', 'str', 'segment', 'image'],
            databaseRoot=''
        )

class TestTableRestore(unittest.TestCase):

    def test_restore_from_non_existing_file(self):
        with self.assertRaises(Exception):
            table = Table.restore('nonexisting.file')
