arr = [1,4,7,9]
target = 11 

left = 0 
right = len(arr)-1 

while left < right:
    value = arr[left] + arr[right]
    if value == target:
        print(left,right) 
        break 
    if value < target:
        left+=1 
    else:
        right-=1 