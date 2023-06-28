'''
Solved date: 06-28-23

Link on leetcode:
https://leetcode.com/problems/queue-reconstruction-by-height/

Level: Medium

@author: Anh-ND
'''
import ast
import time


PATH_FILE = r'C:\Users\Admin\VS_Workspace\study\leetcode\medium\406 Queue Reconstruction By Height\testcase.txt'



class Solution:

    def __createKList(self, people: list[list[int]]):
        k_list = []

        for person in people:
            k_list.append(person[1])

        return sorted(list(set(k_list)))

    def __createHDict(self, k_list: list[int], people: list[list[int]]):
        h_dict = {}

        for k in k_list:
            h_dict[k] = []

        for person in people:
            h_dict[person[1]].append(person[0])

        for key in h_dict.keys():
            h_dict[key] = sorted(h_dict[key], reverse=True)

        return h_dict

    def __findNearestOf(self, num, arr):

        if num == 0:
            return 0

        for i in range(1, len(arr)):
            if arr[i] > num:
                return arr[i - 1]

        return arr[-1]

    def __isHasKItemGreaterOrEquals(self, k, arr: list[list[int]], num):
        if len(arr) == 0:
            return True

        count = 0

        for item in arr:
            if item[0] >= num:
                count += 1

        return k == count

    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        results = []

        # Create k-list
        k_list = self.__createKList(people=people)

        # Create h-dict
        h_dict = self.__createHDict(k_list=k_list, people=people)

        result_id = 0

        while result_id < len(people):
            temp_id = self.__findNearestOf(result_id, k_list)

            while temp_id >= 0:
                if self.__isHasKItemGreaterOrEquals(temp_id, results, h_dict[temp_id][-1]):
                    results.append([h_dict[temp_id][-1], temp_id])
                    h_dict[temp_id].pop()

                    if len(h_dict[temp_id]) == 0:
                        k_list.remove(temp_id)
                        h_dict.pop(temp_id)

                    result_id += 1
                    break
                else:
                    temp_id = k_list[k_list.index(temp_id) - 1]

        return results


if __name__ == "__main__":
    solution = Solution()

    people_test1 = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    people_test2 = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]

    with open(PATH_FILE, 'r') as file:
        file_contents = file.read()

    people_test3 = ast.literal_eval(file_contents)

    print(type(people_test3))


    start = time.time()

    print(solution.reconstructQueue(people=people_test1))
    print(solution.reconstructQueue(people=people_test2))
    print(solution.reconstructQueue(people=people_test3))

    stop = time.time()

    print(f"\n\nIt spends {stop - start} seconds to run all test cases")
