l1=[0,1,2,3,4,5]
# a= lambda x: [i*10 for i in x]
# print(a(l1))

# b=lambda x: [i  for i in x if i%2==0]
# print(b(l1))

# c=lambda a,b: a**b
# print(c(2,3))

# d=filter(lambda x:x%2==0,l1)
# print(list(d))

e=map(lambda x:x**2,l1)
print(list(e))