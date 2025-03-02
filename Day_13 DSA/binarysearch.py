def BST(arr,target):
    left,right = 0,len(arr) - 1
    while left<= right:
        mid = left + (right - left)//2
        if arr[mid]==target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 9
result = BST(arr,target)
# print(result)
if result != -1:
    print(f"element found at index {result}")
else:
    print("element not found")