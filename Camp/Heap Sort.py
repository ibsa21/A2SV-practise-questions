#User function Template for python3
class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        left = self.leftChild(arr, i)
        right = self.rightChild(arr, i)
        
        
        largest = i
        if left < n and  arr[i] <= arr[left]:
            largest = left
        if right < n and  arr[right] >= arr[largest]:
            largest = right
        
        if largest != i:
            self.swap(arr, largest, i)
            self.heapify(arr, n, largest)
            
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(n//2-1, -1, -1):
            self.heapify(arr, n, i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr, n)
        x = 1
        for i in range(n-1, -1, -1):
            self.swap(arr, 0, i)
            self.heapify(arr, n-x , 0)
            x += 1
    
    def rightChild(self, arr,  i):
        return 2*i + 2
        
    def leftChild(self, arr, i):
        return 2*i + 1
    
    def swap(self, arr, i1, i2):
        arr[i1], arr[i2] = arr[i2], arr[i1]
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends
