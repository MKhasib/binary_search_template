def feasible(value, key, IS_ACENDING):
  if IS_ACENDING:
    return value >= key
  return value <= key
def binary_search(arr, key):

  left,right=0,len(arr)
  if len(arr)!=1:
    IS_ACENDING=arr[0]<arr[1]
  else:
    IS_ACENDING =True
  while left<right:

    middle=left+(right-left)//2
    if feasible(arr[middle],key,IS_ACENDING):
      right=middle
    else:
      left=middle+1
  return left if arr[left]==key else -1




def main():
  print(binary_search([4, 6, 10], 10))
  print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
  print(binary_search([10, 6, 4], 10))
  print(binary_search([10, 6, 4], 4))
  print(binary_search([10], 4))


main()