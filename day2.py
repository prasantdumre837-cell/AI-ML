import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(arr * 2)

b=np.arange(1,20,2)
print(b)
print(b.size)
print(b.reshape(2,5))
print(b)
print(b.shape)
print(b.ndim)

# for 3d 
c = np.arange(1, 25) 
c = c.reshape(2, 3, 4)
print(c)
print(c.size)

x=np.array([1,2,3,4])
y=np.array([5,6,7,8])
print(x+y)

print(x[x>2])
print(y[y>5])
print(x+y)

print("Mean", x.mean())
print("Standard Deviation", x.std())
print("Median", np.median(x))

