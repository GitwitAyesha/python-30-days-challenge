# leetcode problem number 703
import heapq

class KthLargest:
    
    def __init__(self, k: int, nums: list[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

k = 3
nums = [4, 5, 8, 2]
kthLargest = KthLargest(k, nums)

print(kthLargest.add(3))  
print(kthLargest.add(5))  
print(kthLargest.add(10)) 
print(kthLargest.add(9))  
print(kthLargest.add(4))  