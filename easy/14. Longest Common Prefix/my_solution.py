class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        n = len(strs[0])
        
        for i in range(n):
                flag = True
                for k in range(1, len(strs)):
                    if strs[0][0:(n - i)] not in strs[k][0:(n - i)]:
                        flag = False
                        break
                
                if flag:
                    return strs[0][0:(n - i)]
        return ""