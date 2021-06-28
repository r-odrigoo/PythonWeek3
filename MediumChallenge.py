name = input ("Enter your name: ")

if name.isupper() == True:
    print(f'{name} is shouting')

elif name.islower() == True:
    print(f'{name} is whispering')

else: 
    print(f'{name} is speaking normally')


