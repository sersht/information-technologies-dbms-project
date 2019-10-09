import unittest
from tests.table.customtypes.image import TestImage
from tests.table.customtypes.segment import TestSegment

if __name__ == '__main__':
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner()

    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestImage))
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestSegment))

    runner.run(suite)
