import os
import unittest
from project.apps.table.customtypes.segment import Segment


class TestSegment(unittest.TestCase):

    def setUp(self):
        self.segment = Segment()

    def test_assignment(self):
        with self.assertRaises(TypeError):
            self.segment.left = '123'

        with self.assertRaises(TypeError):
            self.segment.right = '123'

        self.segment.left = 123.4
        self.segment.right = 123.9

        self.assertEqual(self.segment.left, 123.4)
        self.assertEqual(self.segment.right, 123.9)

    def test_contains(self):
        self.segment.left = 0
        self.segment.right = 1

        with self.assertRaises(TypeError):
            self.segment.contains('123')

        self.assertTrue(self.segment.contains(0))
        self.assertTrue(self.segment.contains(1))
        self.assertTrue(self.segment.contains(0.5))
        self.assertTrue(self.segment.contains(0.00000000001))
        self.assertTrue(self.segment.contains(0.99999999999))

        self.assertFalse(self.segment.contains(-0.000000001))
        self.assertFalse(self.segment.contains(1.000000001))
