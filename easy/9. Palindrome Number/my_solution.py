class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)

        length_str = len(string)
        stop_index = length_str // 2
        length_str -= 1

        for i in range(stop_index):
            if string[i] != string[length_str - i]:
                return False

        return True