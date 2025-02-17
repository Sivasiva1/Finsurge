
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

f = [j for i in matrix for j in i ]
print(f) 

t = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print(t) 

m = [[[i*j for j in range(1,5)]] for i in range(1,5)]
print(m) 

nes = [[[(j*3) for j in i] for i in matrix],
       [[(j*4) for j in i] for i in matrix],
       [[(j*3) for j in i] for i in matrix]] 
print(nes) 

numbers = [[1, 4, 5], [8, 9, 12], [15, 16, 20]]

even = [[col for col in row if col % 2==0 ]for row in numbers]
print(even) 

string = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

inti = [[int(col)for col in row] for row in string]
print(inti)
n = len(matrix) 
diagonal =  [[matrix[row][row], matrix[row][n - row - 1]] for row in range(n)]
print(diagonal) 