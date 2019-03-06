nums=[1,2,3,4,5,6,7,8,9,10]

my_list=[n*n for n in nums]

print(my_list)

my_list=[]

for n in nums:
    my_list.append(n*n)

print(my_list)

# alternative for lambda

my_lambda_list=[]
my_lambda_list=list(map(lambda x:x*x,nums))

print(my_lambda_list)

# complex functions

my_list=[n for n in nums if n%2==0]

print(my_list)

my_lambda_list=list(filter(lambda _:_%2==0,nums))

print(my_lambda_list)


my_list=[]
for letter in 'abcd':
    for t in range(4):
        my_list.append((letter,t))

print(my_list)

my_list=[(letter,num) for letter in 'abcd' for num in range(4) ]

print(my_list)

names=['Bruce','Clark']
heros=['Batman','Superman']

print(list(zip(names,heros)))

my_dict={}

for n,h in zip(names,heros):
    my_dict[n]=h

print(my_dict)

my_dict={n:h for n,h in zip(names,heros)}

print(my_dict)

#set comprehension
nums=[1,1,2,2,3,3,4,6,5]

my_set=set()
for n in nums:
    my_set.add(n)

print(my_set)

my_set={n for n in nums}

print(my_set)

#generator

#nums=[1,2,3,4,5,6]

def ge_func(nums):
    for n in nums:
        yield n*n

my_gen=ge_func(nums)

for i in my_gen:
    print(i)

my_gen= (n*n for n in nums)

print(list(my_gen))