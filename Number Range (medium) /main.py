def binary_search(arr,key,is_lower):
    def feasible(value,key,is_lower):
        if value>key:
            return True
        if value <key:
            return False
        if is_lower:
            return True
        return False
    left,right=0,len(arr)
    while left<right:
        middle=left+(right-left)//2
        if feasible(arr[middle],key,is_lower):
            right=middle
        else:
            left=middle+1
    if left<len(arr):
        if is_lower:
            if arr[left]==key:
                return left
        else:
            if arr[left-1]==key:
                return left-1
    return -1

def find_range(arr,key):
    return [binary_search(arr,key,True),binary_search(arr,key,False)]
def main():
  print(find_range([4, 6, 6, 6, 9], 6))
  print(find_range([1, 3, 8, 10, 15], 10))
  print(find_range([1, 3, 8, 10, 15], 12))
  print(find_range([1, 3, 8, 10, 15], 17))
  print(find_range([1, 3, 8, 10, 15], 0))



main()
