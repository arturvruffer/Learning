import numpy as np



a = np.array([1,2,3], dtype="int64")
print(a)

b = np.array([[1.4, 2.0, 3.], [4.,5.,6.]])
print(b)

c = np.array([[[1,2,3],[4,5,6]],[[7,8,9], [10,11,12]]])


#Anzahl der Dimensionen
print(a.ndim)
print(b.ndim)
print(c.ndim)

#Format des Arrays
print(a.shape)
print(b.shape)
print(c.shape)

print(a.dtype)
print(b.nbytes)

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[1, 4])

d = np.array([[1, 2, 3, 4, 5, 6, 7], [9, 10, 11, 12, 13, 14]])
print(d)
print(d[0])
print(d.ndim)
print(d[0, 0])
print(d[1, 6])


