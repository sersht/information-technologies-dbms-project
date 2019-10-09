import os
import base64
from pathlib import Path


class Image:
    def __init__(self, inputData, isFilePath=True):
        if isFilePath:
            self._createFromImageFile(inputData)
        else:
            self._createFromBase64Code(inputData)

    def _createFromImageFile(self, imagePath):
        if not Path(imagePath).is_file():
            raise ValueError('Given path is not a file')

        # Assume that image path file is actually an image
        with open(imagePath, 'rb') as file:
            self._imageBytesBase64 = base64.b64encode(file.read())

    def _createFromBase64Code(self, data):
        self._imageBytesBase64 = data

    # Returns base64 encoded image file in string format
    @property
    def data(self):
        if type(self._imageBytesBase64) is str:
            return self._imageBytesBase64
        else:
            # Bytes representation is always in form of b'...'
            # so should store it without b-character and quotes
            bytesLiteralRepresentation = str(self._imageBytesBase64)
            return bytesLiteralRepresentation[2:-1]

    # TODO: maybe add name, type validation
    def saveOnStorage(self, directoryPath, name, type):
        if not Path(directoryPath).is_dir():
            raise ValueError('Given path does not exist or is not a directory')
        
        fullFileName = name + '.' + type
        fullImagePath = os.path.join(directoryPath, fullFileName)

        with open(fullImagePath, 'wb') as file:
            file.write(base64.b64decode(self._imageBytesBase64))
