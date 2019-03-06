s='char'
b=True

print(type(s))
print(type(b))

##String Manipulations
message='Charan\'s life'
print(message)

message="""Your world
is amazing"""
print(message)

#Print Length of Message
print(len(message))

message="Hello World"

#Cutting/Slicing a string
print(message[10])
print(message[0:5])
print(message[:5])
print(message[6:])

#String Methods

print(message.lower())
print(message.upper())
print(message.count('l'))
print(message.find('l'))
print(message.replace('Hello','Bye'))
print(message+' & Universe')
print('{}, {}. {}!'.format('Good','Morning','Charan'))
print(dir(message))
print(help(str))

#Int,Float

i=5
j=6
f=1.5
print(type(i))
print(type(f))

#Operations
print(6//5) #Floor Division
print(3**3) #Exponent
print(5%3)
print(abs(-2))
print(round(1.7,1))
print(i>4)
print(i==4)

li=[1,2,3,4]
tu=(1,2,3,4)
di={'key':'value','key2':[1,2,3,4]}
se={1,2,3,4}

print(type(li))
print(type(tu))
print(type(di))
print(type(se))