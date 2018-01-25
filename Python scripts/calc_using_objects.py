#this is just an example of oops concepts
class calc :
    add=None
    mul=None
    def _init_(self):
        print("class is constructed")
    def addi(self,a,b):
        self.add=a+b
        return(self.add)
    def mult(self,a,b) :
        self.mul=a*b
        return(self.mul)
    def _del_(self) :
        print("deleated")
x=calc()
a=input("Enter first no : ")
b=input("Enter second no : ")
try :
    a=int(a)
    b=int(b)
except :
    a=None
    b=None
    print("Enter a valid no")
if a is None or b is None :
    print("Operation cant perform ")
else :
    print("Addition is : ",x.addi(a,b),"Multiplication is : ",x.mult(a,b))