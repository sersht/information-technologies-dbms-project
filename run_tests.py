import unittest
from tests.customtypes.image import TestImage
from tests.customtypes.segment import TestSegment

if __name__ == '__main__':
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner()

    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestImage))
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestSegment))

    runner.run(suite)
