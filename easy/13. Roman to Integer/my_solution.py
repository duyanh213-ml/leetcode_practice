class Solution:
    def romanToInt(self, s: str) -> int:

        roman_dic = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        num_list_convert = [roman_dic[s[0]]]
        j = 0

        for i in range(1, len(s)):
            if roman_dic[s[i]] > num_list_convert[j]:
                num_list_convert[j] = roman_dic[s[i]] - num_list_convert[j]
            else:
                num_list_convert.append(roman_dic[s[i]])
                j += 1
        
        return sum(num_list_convert)
                
