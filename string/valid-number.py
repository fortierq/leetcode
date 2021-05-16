import re

class Solution:
    def isNumber(self, s: str) -> bool:
        return re.fullmatch("([+-]?(((\d+\.\d*)|(\.\d+))|(\d+))([eE][+-]?\d+)?)", s) is not None
