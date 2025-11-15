num1=[1,2,3]
num2=[4,5,6]
result=map(lambda x,y:x+y,num1,num2)
print("addition of two lists")
print(list(result))
print("enter  5 numbers")
num=[1,2,3,4,5]
def sq(n):
    return n*n
sq=list(map(sq,num))
print("numbers squares oin the list is")
print(sq)