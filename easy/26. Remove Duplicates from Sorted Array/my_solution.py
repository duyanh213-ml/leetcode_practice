class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        first_id = 0
        second_id = 1

        unique_len = len(set(nums))

        while second_id < unique_len:
            if nums[second_id] == nums[first_id]:
                nums.pop(second_id)
            else:
                first_id += 1
                second_id += 1 


        return unique_len
    

if __name__ == "__main__":
    
    test_case1 = [1, 1, 2, 4, 4, 5, 6]
    test_case2 = [1, 1, 2]

    solution = Solution()

    print(solution.removeDuplicates(test_case1))
    print(solution.removeDuplicates(test_case2))

    print(test_case1)
    print(test_case2)


