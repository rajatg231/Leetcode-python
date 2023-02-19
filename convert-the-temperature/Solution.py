// https://leetcode.com/problems/convert-the-temperature

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        K= celsius + 273.15
        F= (celsius*1.8)+32.00
        return [K,F]