import numpy as np

X = np.array([[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19]])
print(X[:-1])
z=X[:, -1]
print(z.shape)
print(X[:-1])
print(X)
print(X.shape)
y=X[:, :-1]
print(X[:, :-1])
print(y.shape)
print(X[:,1:])
#print(X[:,:])
c=X[:,0]
print(c,c.shape)