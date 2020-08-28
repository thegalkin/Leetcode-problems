class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0
        maxstr = ""
        for i in s: #ord order 
            a = s[s.find(i):len(s)+1] #saving string to check it
            for j in a: # checking the string
                if not a.count(j) < 2:
                    a = ""
                    break
            if a == "":
                pass
            if len(a) > maximum:
                maximum = len(a)
                maxstr = a
        s = s[::-1]
        for i in s: #rev order
            a = s[s.find(i):len(s)+1] #saving string to check it
            for j in a: # checking the string
                if not a.count(j) < 2:
                    a = ""
                    break
            if a == "":
                pass
            if len(a) > maximum:
                maximum = len(a)
                maxstr = reversed(a)
        return maximum
sol = Solution
sol.lengthOfLongestSubstring("abcdee")