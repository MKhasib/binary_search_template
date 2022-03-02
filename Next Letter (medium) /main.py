def feasible(value, key):
    return value > key
def search_next_letter(arr, key):
  left,right=0,len(arr)
  while left<right:

    middle=left+(right-left)//2
    if feasible(arr[middle],key):
      right=middle
    else:
      left=middle+1
  return arr[left] if left<len(arr) else arr[0]
def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()