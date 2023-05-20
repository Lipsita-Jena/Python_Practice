# 1.by using f

msg = 'Hi'
msg2 = ',\nI am Lipsita'

print(f'{msg}{msg2}')

#2. Using + operator

print(msg+msg2)

#3. join operator - It is a built in function in string 

print("".join([msg,msg2]))

#4 Using % 

print('Good Morning %s %s'%(msg ,msg2))

#5.Using comma

print('google',msg,msg2)