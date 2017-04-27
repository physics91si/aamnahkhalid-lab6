import numpy as np
import matplotlib.pyplot as plt
arr = np.zeros((9,9))
arrOfOnes = np.ones(9)
arr[:,0]= 1
arr[:,1]= 1
arr[:,2]= 1
arr[8,:]=1
arr[(4,7,1),(5,7,8)]=1
print(arr)
plt.spy(arr)
plt.savefig('matrix.png')
