import os
import unittest
from ..Image import Image


IMAGE_PATH = os.sep.join([os.path.dirname(__file__), 'image.jpg'])


class TestImage(unittest.TestCase):
    
    def test_create_from_existing_image(self):
        image = Image(IMAGE_PATH)
        
        self.assertTrue(hasattr(image, '_imageBytesBase64'))
        self.assertGreater(len(image._imageBytesBase64), 0)
    
    def test_create_from_non_existing_image(self):
        with self.assertRaises(ValueError):
            image = Image(os.path.join(os.path.dirname(__file__), 'nonexisting.file'))

    def test_create_from_base64_string(self):
        fileImage = Image(IMAGE_PATH)
        processedBase64ImageString = str(fileImage._imageBytesBase64)[2:-1]
        base64Image = Image(processedBase64ImageString, False)
        
        self.assertIsInstance(fileImage._imageBytesBase64, bytes)
        self.assertIsInstance(base64Image._imageBytesBase64, str)
        self.assertEqual(processedBase64ImageString, base64Image._imageBytesBase64)
        self.assertEqual(fileImage.data, base64Image.data)

    def test_save_image(self):
        currentDirectory = os.path.dirname(__file__)
        fullCopyPath = os.path.join(currentDirectory, 'copy.jpg')
        image = Image(IMAGE_PATH)

        with self.assertRaises(ValueError):
            image.saveOnStorage(os.path.join(currentDirectory, 'nonexisting'), 'image', 'jpg')

        image.saveOnStorage(currentDirectory, 'copy', 'jpg')

        self.assertTrue(os.path.exists(fullCopyPath))

        os.remove(fullCopyPath)
