# Bubble Sort implementation
def bubbleSort(arr): 
    array_length = len(arr) 
  
    # Traverse through all array elements 
    for i in range(array_length): 
        # Last i elements are already in place 
        for j in range(0, array_length-i-1): 
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  
# random test array
arr = [69, 420, 25, 12, 22, 11, 90] 
  
bubbleSort(arr) 
  
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i])