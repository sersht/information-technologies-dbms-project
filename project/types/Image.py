import base64
from pathlib import Path

class Image:
    def __init__(self, imagePath, imageName='default-image', imageType='jpg'):
        if not Path(imagePath).is_file():
            raise ValueError('Given path is not a file')
        
        self._imageName = imageName
        self._imageType = imageType

        with open(imagePath, 'rb') as file:
            self._imageBytesBase64 = base64.b64encode(file.read())
    
    def save(self, directoryPath):
        if not Path(directoryPath).is_dir():
            raise ValueError('Given path does not exist or is not a directory')

        fullImagePath = directoryPath + self._imageName + '.' + self._imageType
    
        with open(fullImagePath, 'xb') as file:
            file.write(base64.b64decode(self._imageBytesBase64))
           
#img = Image('C:\\Projects\\information-technologies-dbms-project\\project\\t.txt', imageType='jpg')
# with open('C:\\Projects\\information-technologies-dbms-project\\project\\t.txt', 'r') as file:
#     a = file.read()
#     with open('C:\\Projects\\information-technologies-dbms-project\\project\\q.jpg', 'xb') as img:
#         img.write(base64.b64decode(a))
