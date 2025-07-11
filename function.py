def add(a=10): #by default value 10
    b=a+1
    print(a,'If u add one ',b)
    return(a)

def sub(a):
    b=a-1
    print(a,' If u subtract one ',b)
    return(a)

def sub(a):
    b=a-1
    print(a,' If u subtract one ',b)
    return(a)

def mul(a,b):
    print(a,'*',b, '=',a*b)
    # return(a)

def div(a):
    b=a/2
    print(a,' If u divide by 2 ',b)
    return(a)

def mulString(str,no):
    print(str*no)

# mulString('hello \n',10)
# mulString(10,'hello \n')
add()
# sub(8)
# mul(3,4)
# div(8)

def type_of_album(artist,album,year_relesed):
    print(artist, album, year_relesed)
    if(year_relesed>1988):
        return "Modern"
    else:
        return "Old"
    
# x=type_of_album('Heena', 'Thriller', 1978)
# print(x)

# y=type_of_album('Blacky', 'Fiction & Fantasy', 1990)
# print(y)

#print list
def printList(list):
    for elm in list:
        print(elm)

printList(['1',1,'sun','moon'])