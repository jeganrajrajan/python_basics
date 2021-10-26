import numpy as np
print(np.array([1,2,3,5,6]))

# array_dimensions
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# fromiter() array
iterable = (a * a for a in range(8))

arr = np.fromiter(iterable, float)

print("fromiter() array :", arr)






# Access Array Elements
# 1D
arr = np.array([1, 2, 3, 4])
print(arr[1])
# 2D
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st dim: ', arr[0, 1])
# 3D
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])

# Slicing
# 1D
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

# negative slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])
# 2D
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])
# copy&view
# Make a copy, change the original array, and display both arrays
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)
# view
# Make a view, change the both original and view array, and display both arrays
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)

# shape
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)
# reshape
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
# 1D to 3D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)

# iterating
arr = np.array([1, 2, 3])

for x in arr:
  print(x)

# 2D
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)
# 3d
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)

# split
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

# split array
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])


# sort
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))