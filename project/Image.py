from pathlib import Path

class Image:
    def __init__(self, imagePath, imageName='default-image', imageType='jpg'):
        if not Path(imagePath).is_file():
            raise ValueError('Given path is not a file')
        
        self._imageName = imageName
        self._imageType = imageType

        with open(imagePath, 'rb') as file:
            self._imageBytes = file.read().decode('latin_1')
    
    def save(self, directoryPath):
        if not Path(directoryPath).is_dir():
            raise ValueError('Given path does not exist or is not a directory')

        fullImagePath = directoryPath + self._imageName + '.' + self._imageType
    
        with open(fullImagePath, 'xb') as file:
            file.write(self._imageBytes.encode('latin_1'))
            
#img = Image('C:\\Projects\\information-technologies-dbms-project\\project\\t.jpg', imageType='txt')
#img.save('C:\\Projects\\information-technologies-dbms-project\\project\\')
