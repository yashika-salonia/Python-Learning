# print(type('1 2 3 4 6'))
name='Michael Jackson'
# print(name[2])
# print(name[-11]) #start form last

str='nothing is impossible'
# len(str)
# print(str[::3]) #print elm at index 1,3,5...
# print(str[0:5:1]) #get every 1st elem from index 0 to 4 (5 is excluded)
# print(str[0:5:2]) #get every 2nd elem from index 0 to 4 (5 is excluded)

name=name+' is \n the best dancer' #new line through \n - escape character
# print(name)

#both will convert the string in raw form and it will be printed as it is 
# print('hello \\n world')
# print(r'hello \n world')

#upper case
# print(name.upper())

#lower case
# print(name.lower())

#replace michael with Janice
# print(name.replace('Michael','Janice'))

#to find the substring in the string
print(name.find('el'))

print(name.find('jack'))