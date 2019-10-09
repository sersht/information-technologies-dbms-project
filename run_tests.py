import unittest
from tests.table.customtypes.image import TestImage
from tests.table.customtypes.segment import TestSegment
from tests.table.table import TestTableCreate, TestTableRestore

if __name__ == '__main__':
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner()

    suite.addTest(
        unittest.defaultTestLoader.loadTestsFromTestCase(TestImage))

    suite.addTest(
        unittest.defaultTestLoader.loadTestsFromTestCase(TestSegment))

    suite.addTest(
        unittest.defaultTestLoader.loadTestsFromTestCase(TestTableCreate))
    suite.addTest(
        unittest.defaultTestLoader.loadTestsFromTestCase(TestTableRestore))

    runner.run(suite)
