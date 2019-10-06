from numbers import Number

class Segment:
    def __init__(self, leftEnd=float('-inf'), rightEnd=float('inf')):
        self._left = leftEnd
        self._right = rightEnd
    
    @property
    def left(self):
        return self._left
    
    @left.setter
    def left(self, value):
        if isinstance(value, Number):
            self._left = value
        raise TypeError('Left end of a segment should be a number')

    @property
    def right(self):
        return self._right
    
    @left.setter
    def right(self, value):
        if isinstance(value, Number):
            self._right = value
        raise TypeError('Right end of a segment should be a number')

    def contains(self, value):
        if isinstance(value, Number):
            return self._left <= value <= self._right
        raise TypeError('Can\'t compare non-numeric')

    # Assume that none of the segment is empty
    def __lt__(self, other):
        if self._left == other._left:
            return self._right < other._right
        return self._left < other._left
        