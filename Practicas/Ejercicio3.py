import numpy as np
h = np.array([[1, 2], [3, 4]])
i = np.array([[1, 2], [3, 4]])
print(h + i)
print(h - i)
print(h * i)
print(h / i)

j = np.array([1, 2, 3, 4])
print(j.sum())
k= np.array([[1,1],[2,2]])
print(k.sum(axis=0))
print(k.sum(axis=1))
print(k.sum())