class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        index = 0
        length = len(s)

        while index < length:
            current_value = roman_values[s[index]]

            # Check if a subtractive pair exists
            if index + 1 < length:
                next_value = roman_values[s[index + 1]]
                if current_value < next_value:
                    total += next_value - current_value
                    index += 2
                    continue

            # Normal case (add current symbol)
            total += current_value
            index += 1

        return total
        
    
example = Solution()
# print(example.romanToInt('III'))
print(example.romanToInt('MCMXCIV'))