class Solution:
    def romanToInt(self, s: str) -> int:
        list_roma = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        int_roma = 0
        prev_value = 0  

        for symbol in s[::-1]: 
            print('symbol',symbol)
            value = list_roma[symbol]
            if value < prev_value:
                int_roma -= value
            else:
                int_roma += value
            prev_value = value

        print(int_roma)
        return int_roma

case_1 = Solution()
case_1.romanToInt('XIX')