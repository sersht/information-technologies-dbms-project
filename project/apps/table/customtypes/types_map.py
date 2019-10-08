from project.apps.table.customtypes.image import Image
from project.apps.table.customtypes.segment import Segment

TYPE_BY_CODE = {
    'int': int,
    'str': str,
    'float': float,
    'image': Image,
    'segment': Segment,
}
