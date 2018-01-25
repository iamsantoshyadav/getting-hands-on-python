#this is just an example of object oriented program which is made for just getting hands on oops concepts
class demo :
    data="santosh"
    def demofunction(self):
        self.data=self.data+"yadav"
        print(self.data)
        return(self.data)
x=demo()
x.demofunction()