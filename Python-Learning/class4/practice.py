# # # # x:list=['a','b','c','d']
# # # # # too_expensive='d'
# # # # # x.remove(too_expensive)
# # # # # print(f'A {too_expensive} is too expensive')
# # # # # print(f'A {too_expensive} is too expensive')
# # # # print(x.__len__())
# # # y:list=['a', 'b', 'c', 'd']
# # # for x in y:
# # #     print(f'Hi my friend {x.title()}')


# # x = list(range(10))
# # # print(x)
# # for y in range(10):
# #  print(y)
# # for a in x:
# #     print(f'Your numbers are out of 10; {a}')

# # to get even numbs list by range function
# x=list(range(2, 11, 2))
# print(x)
# # to get odd numbs
# y=list(range(1, 12, 2))
# print(y)
# # to get square of all numbs of list
x:list=[]
for a in range(10):
    b=a**2
    x.append(b)
print(x)
# my logic
d = [x**2 for x in range(2, 10, 2)]
print(d)
e=list(range(2, 10, 2))
c = [x**2 for x in e] 
print(c)
# special function practice
print(min(c))
print(max(c))
print(sum(c))
print(min(d))
print(max(d))
print(sum(d))