import numpy as np
# emp=np.full((3,4),2)
# print(emp)
mat=np.arange(1,11).reshape(2,5)
# print(mat)

# revv=np.flip(mat)
# print(revv)

# trans=np.transpose(mat)
# print(trans)

sample=np.array([1,2,3,4,5,6,7,8,9,10])
# print(np.min(sample))
# print(np.max(sample))
# print(np.mean(sample))
# print(np.median(sample))
# print(np.std(sample))

# res=np.where(sample>0,"+",sample)
# print(res)

evenn=sample[sample%2==0]
print(evenn)