import numpy as np 
print("---------------------------1d array--------------------------------------")
#1D Array 
arr = np.array([1,2,3,4])
print(arr) 
print("--------------------------2d array----------------------------------------")
#2D Array 
arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr) 
print("---------------------------3d array---------------------------------------")
#3D Array 
arr = np.array([[[1,2,3],[4,5,6]]])
print(arr) 
print("------------------------nd array------------------------------------------")
#nd array 
arr = np.array([1,2,3] , ndmin=5)
print(arr) 
print("----------------------------size,ndmin----------------------------------------")
# size , dimension 
print(arr.size)
print(arr.ndim)
print("--------------------------------reshape---------------------------------------------")
#reshape 
arr = np.array([1, 2, 3, 4, 5, 6])
arr = arr.reshape(2, 3) #(row,col)
print(arr)
print("-----------------------------------Slicing-----------------------------------------")
#slicing 
arr = np.array([10, 20, 30, 40, 50])
print(arr[1:4]) 
print(arr[:3])
print(arr[2:]) 
print("-------------------------------------array operations------------------------------------")
#array operations 
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)
print(arr1//arr2)

print("------------------------------MATHEMATICAL OPERATIONS--------------------------------")
#mathematical operations 
arr = np.array([1, 2, 3, 4]) 
print(np.sin(arr))
print(np.cos(arr))
print(np.sum(arr))
print(np.log(arr))
print(np.exp(arr))
print(np.abs(arr))
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr)) 

print("---------------------------------array concat-------------------------------------------")
#array concatenation 
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Vertically stack arrays
print(np.vstack((arr1, arr2))) #row wise 

# Horizontally stack arrays
print(np.hstack((arr1, arr2))) #col wise 
print("--------------------------------generate random ----------------------------------------")
#Random Number Generation

print(np.random.rand(10)) #0 to 1 
print(np.random.randint(1, 100))
print("---------------------------------filter----------------------------------------------")
#filter 
arr = np.array([10, 20, 30, 40, 50])
print(arr[arr>20])
print("-----------------------------------Sort-----------------------------------------------------")
#sort 
arr = np.array([5, 2, 9, 1, 5, 6])
arr.sort()
print(arr)
print("---------------------------------unique elements--------------------------------------------")
#unique elements 
arr = np.array([1, 2, 2, 3, 4, 4, 5])
print(np.unique(arr)) 
print("------------------------------------transpose matrix-----------------------------------------")
#transpose the matrix 
arr = np.array([[1, 2], [3, 4]])
print(arr.T)
print("--------------------------------------flattening array---------------------------------------")
#Flattening Arrays
arr = np.array([[1,2,3],[4,5,6]])
print(arr.flatten())
print("-----------------------------------identity matrix------------------------------------------------")
#identity matrix (1's in diagonal)
print(np.eye(4))
print("-----------------------------------zeros and ones matrix------------------------------------------")
#zeros and one matrix 
print(np.zeros((3, 3)))
print(np.ones((3, 3)))
print("----------------------------------list to numpy array -------------------------------------------")
#convert list to array 
my_list = [1, 2, 3, 4]
arr = np.array(my_list)
print(arr)
print("-----------------------------------broadcasting--------------------------------------------------")
#broadcasting 
arr = np.array([[1, 2], [3, 4]])
print(arr + 10)


