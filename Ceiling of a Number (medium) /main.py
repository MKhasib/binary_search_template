def feasible(value, key):
    return value >= key
def search_ceiling_of_a_number(arr, key):

  left,right=0,len(arr)
  while left<right:

    middle=left+(right-left)//2
    if feasible(arr[middle],key):
      right=middle
    else:
      left=middle+1
  return left if left<len(arr) else -1
def main():
  print(search_ceiling_of_a_number([4, 6, 10], 6))
  print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
  print(search_ceiling_of_a_number([4, 6, 10], 17))
  print(search_ceiling_of_a_number([4, 6, 10], -1))


main()