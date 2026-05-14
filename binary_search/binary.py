# Implement:
class BinarySearch:
    def __init__(self):
        pass

    
# binary search (on a sorted array of integers)
    def search(self,arr,target):
        left,right = 0 , len(arr) - 1

        while left<=right:
            mid = (left+right) // 2
        
            if arr[mid] < target:
                left = mid + 1
            
            elif arr[mid] > target:
                right = mid - 1
            
            else:
                return mid

        return -1


# binary search using recursion
