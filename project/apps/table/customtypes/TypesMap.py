from .Image import Image
from .Segment import Segment

TYPE_BY_CODE = {
    'int': int,
    'str': str,
    'float': float,
    'image': Image,
    'segment': Segment,
}
