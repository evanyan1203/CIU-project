from binary import BinarySearch

bs = BinarySearch()

nums = [1, 3, 5, 7, 9]

print(bs.search(nums, 5))  
#  2

print(bs.search(nums, 6))  
#  -1

print(bs.search_recursion(nums, 7, 0, len(nums)-1))  
#  3