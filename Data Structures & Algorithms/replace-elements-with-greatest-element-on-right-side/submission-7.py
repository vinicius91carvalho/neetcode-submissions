class Solution:
    # def replaceElements(self, arr: List[int]) -> List[int]:
    #     for i in range(len(arr) - 1):
    #         right_great_elem = arr[i + 1]
    #         for j in range(i + 1, len(arr) - 1):
    #             if right_great_elem < arr[j + 1]:
    #                 right_great_elem = arr[j + 1]
    #         arr[i] = right_great_elem
    #     arr[len(arr) - 1] = -1
    #     return arr
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_value = -1  
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = max_value
            if temp > max_value:
                max_value = temp
           
        return arr