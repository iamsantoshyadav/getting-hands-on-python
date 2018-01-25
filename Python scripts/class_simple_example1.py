#%%
#This program is just an example of learning basic concept about oops concept
class even_odd : #"even_odd is our class name or for understand it we can assume that it is just a templete "
    even=0 #this data usder tha class are atributes of tha class
    odd=0
    def no_even(self,string):  #when we decdeare any function in any class is calle method
        for words in string :
            if words in ("a","e","i","o","u","A","E","I","O","U"):
                self.even=self.even+1
        print("No of even words in given data : ",self.even)
    def no_odd(self,string) :
        for words in string :
            if words not in ("a","e","i","o","u","A","E","I","O","U"):
                self.odd=self.odd+1
        print("No of odd cherecter is : ",self.odd)                
var=even_odd() #here var is class even_odd type
data=input("Enter any type of data : ")
var.no_even(data)# herewe can undertand with this followig expression too even_odd.no_even(data) whre var=even_odd()
var.no_odd(data)
#folowing syntex just tell about types of class and also direction of class type veriable
print(type(var))
print(dir(var))
