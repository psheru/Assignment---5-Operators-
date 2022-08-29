#6. Write a python script which takes a three digit number from the user and displays
#only its middle digit.

num=int(input('enter the three digit number:-'))
num=int(num/10)
answer=(num%10)
print('answer is:-',answer)
