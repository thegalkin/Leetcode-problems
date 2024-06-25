class Solution:
    numbers = {"I": 1, "V": 5,"X": 10,"L": 50, "C": 100,"D": 500,"M": 1000}
            
    def romanToInt(self, s: str) -> int:
        sum = 0
        length = len(s)
        i = 0
        while i < length-1:
            letter = s[i]
            if self.numbers[letter] < self.numbers[s[i+1]]:
                sum -= self.numbers[letter]
            else:
                sum += self.numbers[letter]           
            i += 1 
        return sum + self.numbers[s[length-1]]
    


c = Solution()
print(c.romanToInt("III"))
assert c.romanToInt("III") == 3