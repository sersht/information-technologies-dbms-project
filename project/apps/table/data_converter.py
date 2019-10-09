from project.apps.table.customtypes.image import Image
from project.apps.table.customtypes.segment import Segment


class DataConverter:

    @staticmethod
    def serialize(data):
        if isinstance(data, (int, float, str)):
            return str(data)

        if isinstance(data, Image):
            return data.data

        if isinstance(data, Segment):
            return [data.left, data.right]

    @staticmethod
    def deserialize(data, Type):
        if Type is int or Type is float or Type is str:
            return Type(data)

        if Type is Image:
            return Image.restore(data)

        if Type is Segment:
            return Segment(data[0], data[1])
