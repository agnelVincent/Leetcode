class Solution:
    def capitalizeTitle(self, title: str) -> str:
        arr = title.split()
        i = 0
        while i < len(arr):
            temp = arr[i]
            if len(temp) <= 2:
                arr[i] = temp.lower()
                i += 1
                continue
            temp = temp.lower()
            temp = temp.capitalize()
            arr[i] = temp
            i += 1
        return ' '.join(arr)