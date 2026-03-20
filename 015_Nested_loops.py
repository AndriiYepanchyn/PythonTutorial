smile = '\U0001f611'

# Simple way
for i in range(11): 
    print(smile * i) 

# Using nested loops
for i in range(11): 
    count = 0
    emoticons = ''
    while count < i:
        emoticons +=smile
        count +=1
    print (emoticons)    
